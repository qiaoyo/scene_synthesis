"""ReAct agent：思考 → 行动 → 观察 → 反思 → 策略调整。

对齐 ``方案/优化.md`` 中的「优化后的 ReAct 循环」。每一步都把 thought / action /
observation / reflection 持久化到 ``RunRecord``，运行结束后可以一并落盘。
"""
from __future__ import annotations

import json
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from ..config import ProjectConfig
from ..data_models import Action, Lesson, Observation, Reflection, SceneState
from ..llm_planner import LLMPlanner
from ..observer import Observer
from ..rag import AssetRAG
from ..scene_state import SceneStateManager
from ..template_parser import extract_template_instances
from ..tools.base import TOOL_REGISTRY, ToolContext, ToolResult, list_tool_specs


@dataclass
class StepRecord:
    step: int
    thought: str
    action: Dict[str, Any]
    observation: Dict[str, Any]
    reflection: Optional[Dict[str, Any]] = None


@dataclass
class RunRecord:
    command: str
    steps: List[StepRecord] = field(default_factory=list)
    lessons: List[Dict[str, Any]] = field(default_factory=list)
    strategy: Optional[str] = None
    final_scene: Optional[Dict[str, Any]] = None
    finish_reason: str = "max_steps"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "command": self.command,
            "steps": [
                {
                    "step": s.step,
                    "thought": s.thought,
                    "action": s.action,
                    "observation": s.observation,
                    "reflection": s.reflection,
                }
                for s in self.steps
            ],
            "lessons": list(self.lessons),
            "strategy": self.strategy,
            "final_scene": self.final_scene,
            "finish_reason": self.finish_reason,
        }


class ReActAgent:
    """主循环。"""

    def __init__(
        self,
        config: ProjectConfig,
        rag: AssetRAG,
        scene: Optional[SceneStateManager] = None,
        planner: Optional[LLMPlanner] = None,
        observer: Optional[Observer] = None,
    ):
        self.config = config
        self.rag = rag
        self.scene = scene or SceneStateManager()
        self.planner = planner or LLMPlanner(config)
        self.observer = observer or Observer(self.scene)

        # ToolContext 持有 scene + rag，9 个工具都通过它读写
        self.tool_ctx = ToolContext(
            scene=self.scene,
            rag=self.rag,
            physics_enabled=self.config.agent.physics_enabled,
            extras={},
        )
        self.tool_specs = list_tool_specs()
        self.working_memory: Dict[str, Any] = {
            "scene_type": None,
            "required_asset_types": [],
            "retrieved_scene_priors": [],
            "retrieved_scene_templates": [],
            "template_instances": [],
            "retrieved_assets": {},
        }
        self._last_retrieval_signature: Optional[tuple] = None

    # -- 核心循环 --

    def run(self, command: str) -> RunRecord:
        cfg_agent = self.config.agent
        record = RunRecord(command=command)
        last_observation: Optional[Observation] = None
        consecutive_failures = 0

        for step in range(cfg_agent.max_steps):
            # 1. 推理
            scene_summary = self._scene_summary()
            think_resp = self.planner.think_and_decide(
                command=command,
                scene_summary=scene_summary,
                last_observation=last_observation.to_dict() if last_observation else None,
                tool_specs=self.tool_specs,
                lessons=record.lessons,
                strategy=record.strategy,
                step=step,
                max_steps=cfg_agent.max_steps,
            )
            decision = think_resp.parsed
            thought = str(decision.get("thought", ""))
            action_name = str(decision.get("action", "") or "")
            action_input = decision.get("action_input") or {}
            if not isinstance(action_input, dict):
                action_input = {"_invalid": action_input}

            # 2. 终止条件
            if action_name == "finish":
                record.finish_reason = "finish"
                record.steps.append(StepRecord(
                    step=step,
                    thought=thought,
                    action={"tool": action_name, "tool_input": action_input},
                    observation={"ok": True, "tool_result": {"ok": True, "data": action_input}},
                ))
                break

            # 3. 行动
            tool = TOOL_REGISTRY.get(action_name)
            if tool is None:
                tool_result = self._unknown_tool_result(action_name, decision)
            elif self._is_repeated_retrieval(action_name, action_input):
                tool_result = ToolResult(
                    ok=False,
                    error=(
                        f"重复检索已阻止: {action_name} 已经成功返回过相关结果，"
                        "请根据 working_memory 进入下一阶段。"
                    ),
                )
            else:
                tool_result = tool(self.tool_ctx, **action_input)
                self._update_working_memory(action_name, action_input, tool_result)

            # 4. 观察
            observation = self.observer.observe(action_name, tool_result)
            last_observation = observation

            step_record = StepRecord(
                step=step,
                thought=thought,
                action={"tool": action_name, "tool_input": action_input},
                observation=observation.to_dict(),
            )

            # 5. 反思（只在异常或不稳定时触发）
            if cfg_agent.reflection_enabled and not observation.ok:
                reflect_resp = self.planner.reflect(
                    thought=thought,
                    action=action_name,
                    action_input=action_input,
                    observation=observation.to_dict(),
                    command=command,
                )
                reflection_dict = reflect_resp.parsed
                step_record.reflection = reflection_dict
                lesson = _reflection_to_lesson(action_name, reflection_dict)
                if lesson is not None:
                    record.lessons.append(lesson.to_dict())
                    if len(record.lessons) > cfg_agent.max_lessons:
                        record.lessons = record.lessons[-cfg_agent.max_lessons:]
                consecutive_failures += 1

                # 6. 策略调整
                if (
                    cfg_agent.strategy_adjust_enabled
                    and consecutive_failures >= 2
                ):
                    strat_resp = self.planner.adjust_strategy(
                        command=command,
                        recent_observations=[s.observation for s in record.steps[-3:]],
                        recent_reflections=[
                            s.reflection for s in record.steps[-3:] if s.reflection
                        ],
                    )
                    new_strategy = strat_resp.parsed.get("strategy")
                    if isinstance(new_strategy, str) and new_strategy.strip():
                        record.strategy = new_strategy.strip()
                        consecutive_failures = 0
            else:
                consecutive_failures = 0

            record.steps.append(step_record)

        record.final_scene = self.scene.to_dict()
        return record

    # -- 持久化 --

    def save(self, record: RunRecord, output_dir: Optional[Path] = None) -> Path:
        out_dir = output_dir or self.config.output_dir
        out_dir.mkdir(parents=True, exist_ok=True)
        ts = time.strftime("%Y%m%d-%H%M%S")
        out_path = out_dir / f"run_{ts}.json"
        out_path.write_text(json.dumps(record.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
        return out_path

    # -- 工具 --

    def _scene_summary(self) -> Dict[str, Any]:
        state: SceneState = self.scene.state
        return {
            "instance_count": len(state.instances),
            "instances": [
                {
                    "instance_id": iid,
                    "asset_type": inst.asset_type,
                    "position": inst.position,
                    "bbox_size": inst.bbox_size,
                    "parent_instance_id": inst.parent_instance_id,
                }
                for iid, inst in state.instances.items()
            ],
            "support_children": dict(state.support_children),
            "working_memory": self.working_memory,
        }

    # -- 工作记忆 --

    def _is_repeated_retrieval(self, action_name: str, action_input: Dict[str, Any]) -> bool:
        if action_name not in {"retrieve_scene_prior", "retrieve_scene_template", "retrieve_assets"}:
            self._last_retrieval_signature = None
            return False
        if action_name == "retrieve_scene_prior" and self._memory_has_results_for(action_name, action_input):
            return True
        signature = (action_name, json.dumps(action_input, sort_keys=True, ensure_ascii=False))
        repeated = signature == self._last_retrieval_signature
        if repeated and self._memory_has_results_for(action_name, action_input):
            return True
        return False

    def _update_working_memory(
        self,
        action_name: str,
        action_input: Dict[str, Any],
        tool_result: ToolResult,
    ) -> None:
        if action_name not in {"retrieve_scene_prior", "retrieve_scene_template", "retrieve_assets"}:
            self._last_retrieval_signature = None
            return

        signature = (action_name, json.dumps(action_input, sort_keys=True, ensure_ascii=False))
        if not tool_result.ok:
            self._last_retrieval_signature = signature
            return

        hits = tool_result.data.get("hits", [])
        if not hits:
            self._last_retrieval_signature = signature
            return

        if action_name == "retrieve_scene_prior":
            self._remember_scene_prior(hits)
        elif action_name == "retrieve_scene_template":
            self.working_memory["retrieved_scene_templates"] = _merge_hits(
                self.working_memory["retrieved_scene_templates"], hits
            )
            self.working_memory["template_instances"] = _merge_hits(
                self.working_memory["template_instances"],
                extract_template_instances(hits),
                limit=32,
            )
        elif action_name == "retrieve_assets":
            asset_type = action_input.get("asset_type") or "_any"
            if isinstance(asset_type, list):
                asset_type = ",".join(str(v) for v in asset_type)
            key = str(asset_type)
            current = self.working_memory["retrieved_assets"].get(key, [])
            self.working_memory["retrieved_assets"][key] = _merge_hits(current, hits)

        self._last_retrieval_signature = signature

    def _remember_scene_prior(self, hits: List[Dict[str, Any]]) -> None:
        self.working_memory["retrieved_scene_priors"] = _merge_hits(
            self.working_memory["retrieved_scene_priors"], hits
        )
        first = hits[0]
        scene_id = first.get("scene_id")
        if scene_id:
            self.working_memory["scene_type"] = scene_id
        required = list(self.working_memory.get("required_asset_types") or [])
        seen = set(required)
        for hit in hits:
            if self.working_memory.get("scene_type") and hit.get("scene_id") != self.working_memory["scene_type"]:
                continue
            for asset_type in hit.get("core_asset_types") or []:
                if asset_type not in seen:
                    required.append(asset_type)
                    seen.add(asset_type)
        self.working_memory["required_asset_types"] = required

    def _memory_has_results_for(self, action_name: str, action_input: Dict[str, Any]) -> bool:
        if action_name == "retrieve_scene_prior":
            return bool(self.working_memory.get("scene_type") and self.working_memory.get("required_asset_types"))
        if action_name == "retrieve_scene_template":
            return bool(self.working_memory.get("retrieved_scene_templates"))
        if action_name == "retrieve_assets":
            asset_type = action_input.get("asset_type") or "_any"
            if isinstance(asset_type, list):
                asset_type = ",".join(str(v) for v in asset_type)
            return bool(self.working_memory.get("retrieved_assets", {}).get(str(asset_type)))
        return False

    @staticmethod
    def _unknown_tool_result(action_name: str, decision: Dict[str, Any]):
        from ..tools.base import ToolResult  # local import to avoid cycle
        if "_parse_error" in decision:
            return ToolResult(ok=False, error=f"LLM 输出无法解析: {decision['_parse_error']}")
        return ToolResult(ok=False, error=f"未知工具: {action_name!r}")


def _reflection_to_lesson(action: str, reflection: Dict[str, Any]) -> Optional[Lesson]:
    summary = str(reflection.get("summary", "")).strip()
    cause = str(reflection.get("cause", "")).strip()
    next_strategy = str(reflection.get("next_strategy", "")).strip()
    if not (summary or cause or next_strategy):
        return None
    return Lesson(
        situation=f"action={action}: {summary}" if summary else f"action={action}",
        mistake=cause or "(unknown)",
        correction=next_strategy or "(no strategy provided)",
    )


def _merge_hits(existing: List[Dict[str, Any]], hits: List[Dict[str, Any]], limit: int = 8) -> List[Dict[str, Any]]:
    merged = list(existing)
    seen = {_hit_key(item) for item in merged}
    for hit in hits:
        key = _hit_key(hit)
        if key in seen:
            continue
        merged.append(hit)
        seen.add(key)
        if len(merged) >= limit:
            break
    return merged


def _hit_key(item: Dict[str, Any]) -> Any:
    return item.get("doc_id") or item.get("template_path") or item.get("template_name")


__all__ = ["ReActAgent", "RunRecord", "StepRecord"]
