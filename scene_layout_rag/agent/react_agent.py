"""ReAct agent -- the core Think → Act → Observe → Reflect loop."""
from __future__ import annotations

import json
import re
from typing import Any, Dict, List, Optional, Tuple

from ..data_models import ActionRecord, AgentTrace, Lesson
from ..observer import SceneObserver
from ..prompts.templates import (
    SYSTEM_PROMPT,
    format_step_prompt,
    format_reflect_prompt,
    format_strategy_prompt,
)
from ..scene_state import SceneState
from ..tools.base import ToolRegistry


class ReActAgent:
    """Orchestrates the ReAct loop for iterative scene layout."""

    def __init__(
        self,
        llm: Any,                      # LLMPlanner instance (with react_call method)
        tool_registry: ToolRegistry,
        observer: SceneObserver,
        vector_store: Any,              # LocalVectorStore
        embedder: Any,                  # EmbeddingBackend
        max_steps: int = 20,
        reflection_enabled: bool = True,
        max_lessons: int = 10,
        max_working_memory: int = 15,
    ):
        self.llm = llm
        self.tools = tool_registry
        self.observer = observer
        self.vector_store = vector_store
        self.embedder = embedder
        self.max_steps = max_steps
        self.reflection_enabled = reflection_enabled
        self.max_lessons = max_lessons
        self.max_working_memory = max_working_memory

        self.lessons_learned: List[Lesson] = []
        self.retrieved_assets: List[Dict[str, Any]] = []
        self.history: List[ActionRecord] = []

    def run(
        self,
        command: str,
        catalog_summary: Dict[str, Any],
    ) -> Tuple[SceneState, AgentTrace]:
        """Execute the ReAct loop. Returns final scene state and execution trace."""
        scene = SceneState()
        last_observation: Dict[str, Any] = {
            "validation": {"ok": True, "collisions": [], "out_of_bounds": []},
            "suggestions": [],
        }
        strategy: Optional[str] = None

        # Build system prompt once
        system_prompt = SYSTEM_PROMPT.format(
            tools_description=self.tools.generate_tools_prompt(),
            catalog_summary=json.dumps(catalog_summary, ensure_ascii=False),
        )

        for step in range(self.max_steps):
            # ── Step 1: Think ──
            step_prompt = format_step_prompt(
                command=command,
                scene_state=scene.to_dict(),
                last_observation=last_observation,
                retrieved_assets=self.retrieved_assets[-self.max_working_memory:],
                lessons_learned=[
                    {"mistake": l.mistake, "correction": l.correction}
                    for l in self.lessons_learned[-5:]
                ],
                strategy=strategy,
            )

            raw_output = self.llm.react_call(system_prompt, step_prompt)
            parsed = self._parse_llm_output(raw_output)

            thought = parsed.get("thought", raw_output[:200])
            action = parsed.get("action", "")
            action_input = parsed.get("action_input", {})

            print(f"[ReAct Step {step}] Think: {thought[:80]}...")
            print(f"[ReAct Step {step}] Act: {action}({json.dumps(action_input, ensure_ascii=False)[:120]})")

            # ── Finish check ──
            if action == "finish":
                self.history.append(ActionRecord(
                    step=step, thought=thought, action="finish",
                    action_input={}, result_ok=True, observation_ok=True,
                ))
                break

            # ── Step 2: Act ──
            if not action or action not in self.tools.list_names():
                print(f"[ReAct Step {step}] 无效工具: {action}，跳过")
                self.history.append(ActionRecord(
                    step=step, thought=thought, action=action,
                    action_input=action_input, result_ok=False, observation_ok=True,
                ))
                last_observation = {
                    "validation": {"ok": True, "collisions": [], "out_of_bounds": []},
                    "suggestions": [f"工具 '{action}' 不存在，可用工具: {self.tools.list_names()}"],
                }
                continue

            result = self.tools.execute(
                action, action_input,
                scene=scene,
                vector_store=self.vector_store,
                embedder=self.embedder,
                llm=self.llm,
            )

            # Update working memory for retrieval results
            if action == "retrieve_assets" and result.ok:
                self._update_working_memory(result.result)

            # ── Step 3: Observe ──
            if self.tools.is_scene_modifier(action):
                observation = self.observer.observe(scene)
            else:
                observation = self.observer.observe_retrieval(
                    result.result if result.ok else {}
                )
            last_observation = observation

            obs_ok = observation.get("validation", {}).get("ok", True)
            print(f"[ReAct Step {step}] Obs: ok={obs_ok}, result_ok={result.ok}")

            # ── Step 4: Reflect (on failure) ──
            if (
                self.reflection_enabled
                and self.tools.is_scene_modifier(action)
                and not obs_ok
            ):
                self._do_reflection(
                    step, thought, action, action_input,
                    observation, command, system_prompt, strategy,
                )

            # Record
            self.history.append(ActionRecord(
                step=step, thought=thought, action=action,
                action_input=action_input, result_ok=result.ok,
                observation_ok=obs_ok,
            ))

        # Build trace
        trace = AgentTrace(
            command=command,
            steps=list(self.history),
            lessons=list(self.lessons_learned),
            final_scene_dict=scene.to_dict(),
            total_steps=len(self.history),
            success=any(s.action == "finish" for s in self.history),
        )

        return scene, trace

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _parse_llm_output(self, text: str) -> Dict[str, Any]:
        """Extract ``{thought, action, action_input}`` from LLM output."""
        # Try to find JSON block (possibly inside ```json ... ```)
        json_match = re.search(r"```json\s*(\{[\s\S]*?\})\s*```", text)
        if not json_match:
            json_match = re.search(r"(\{[\s\S]*\"action\"[\s\S]*?\})", text)
        if json_match:
            try:
                return json.loads(json_match.group(1))
            except json.JSONDecodeError:
                pass

        # Fallback: try the entire text as JSON
        try:
            data = json.loads(text.strip())
            if isinstance(data, dict) and "action" in data:
                return data
        except json.JSONDecodeError:
            pass

        return {"thought": text[:300], "action": "", "action_input": {}}

    def _update_working_memory(self, retrieval_result: Dict[str, Any]) -> None:
        existing_ids = {a.get("doc_id") for a in self.retrieved_assets}
        for asset in retrieval_result.get("assets", []):
            doc_id = asset.get("doc_id", "")
            if doc_id and doc_id not in existing_ids:
                self.retrieved_assets.append(asset)
                existing_ids.add(doc_id)
        # Trim to max
        if len(self.retrieved_assets) > self.max_working_memory * 2:
            self.retrieved_assets = self.retrieved_assets[-self.max_working_memory:]

    def _do_reflection(
        self,
        step: int,
        thought: str,
        action: str,
        action_input: Dict[str, Any],
        observation: Dict[str, Any],
        command: str,
        system_prompt: str,
        strategy: Optional[str],
    ) -> None:
        reflect_prompt = format_reflect_prompt(
            thought=thought,
            action=action,
            action_input=action_input,
            observation=observation,
        )
        raw_reflection = self.llm.react_call(system_prompt, reflect_prompt)
        parsed = self._parse_llm_output(raw_reflection)

        lesson = Lesson(
            step=step,
            situation=f"{action}({json.dumps(action_input, ensure_ascii=False)[:100]})",
            mistake=parsed.get("mistake", raw_reflection[:200]),
            correction=parsed.get("correction", ""),
        )
        self.lessons_learned.append(lesson)
        if len(self.lessons_learned) > self.max_lessons:
            self.lessons_learned = self.lessons_learned[-self.max_lessons:]

        print(f"[ReAct Step {step}] Reflect: {lesson.mistake[:80]}")

        # Strategy adjustment on consecutive failures
        if self._needs_strategy_change():
            strat_prompt = format_strategy_prompt(
                command=command,
                lessons=[
                    {"mistake": l.mistake, "correction": l.correction}
                    for l in self.lessons_learned[-3:]
                ],
                observation=observation,
            )
            strategy_text = self.llm.react_call(system_prompt, strat_prompt)
            print(f"[ReAct] Strategy adjustment: {strategy_text[:100]}")

    def _needs_strategy_change(self) -> bool:
        recent = self.history[-3:]
        if len(recent) < 2:
            return False
        fail_count = sum(1 for h in recent if not h.observation_ok)
        return fail_count >= 2


__all__ = ["ReActAgent"]
