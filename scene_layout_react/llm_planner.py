# llm_planner.py
from __future__ import annotations
import json
from typing import Any, Dict, List, Optional
from openai import OpenAI
from .config import ProjectConfig
from .tools.base import ToolResult
# =========================================================
# Types
# =========================================================
ToolDecision = Dict[str, Any]
ReflectionResult = Dict[str, Any]
StrategyResult = Dict[str, Any]
# =========================================================
# Planner
# =========================================================
class LLMPlanner:
    def __init__(
        self,
        config: ProjectConfig,
    ):
        self.config = config
        self._client = OpenAI(
            base_url=config.llm_api_base_url,
            api_key=config.llm_api_key,
        )
    # =====================================================
    # JSON Chat
    # =====================================================
    def _json_chat(self, system: str, user: str,) -> Dict[str, Any]:
        response = self._client.chat.completions.create(
            model=self.config.model,
            messages=[{"role": "system","content": system,},
                {"role": "user","content": user,}],
            response_format={"type": "json_object"},
            temperature=self.config.temperature,
        )
        text = (response.choices[0].message.content or "{}")
        try:
            return json.loads(text)
        except Exception as exc:
            return {
                "type": "json_error",
                "error": str(exc),
                "raw": text[:500],
            }
    # =====================================================
    # Tool Chat
    # =====================================================
    def _tool_chat(self, system: str, user: str, tools: List[Dict[str, Any]],) -> ToolDecision:
        response = self._client.chat.completions.create(
            model=self.config.model,
            messages=[{"role": "system", "content": system,},
                {"role": "user", "content": user,},],
            tools=tools,
            tool_choice="auto",
            temperature=self.config.temperature,
            extra_body={
                "chat_template_kwargs": {
                    "enable_thinking": True,
                }
            },
        )
        message = response.choices[0].message
        # -------------------------------------------------
        # Tool Calls
        # -------------------------------------------------
        if message.tool_calls:
            calls = []
            for tool_call in message.tool_calls:
                raw_args = (tool_call.function.arguments or "{}")
                try:
                    args = json.loads(raw_args)
                except Exception as exc:
                    return {
                        "type": "tool_error",
                        "error": str(exc),
                        "raw": raw_args[:500],
                    }
                calls.append({
                    "id": tool_call.id,
                    "name": tool_call.function.name,
                    "arguments": args,
                })
            return {
                "type": "tool_calls",
                "calls": calls,
            }
        # -------------------------------------------------
        # Final
        # -------------------------------------------------
        return {
            "type": "final",
            "content": (
                message.content
                or ""
            ),
        }
    # =====================================================
    # Reasoning
    # =====================================================
    def reason(
        self,
        command: str,
        scene_summary: Dict[str, Any],
        recent_observations: List[Dict[str, Any]],
        recent_reflections: List[Dict[str, Any]],
        tool_results: List[ToolResult],
        lessons: List[Dict[str, Any]],
        strategy: Optional[str],
        step: int,
        max_steps: int,
    ) -> StrategyResult:      
        REASON_SYSTEM = """
                You are a scene layout planning agent.
                Your job is to:
                - understand the user layout goal
                - analyze the current scene state
                - decide the next high-level layout strategy
                You DO NOT call tools.
                You ONLY produce structured reasoning.
                Focus on:
                - spatial arrangement
                - object relationships
                - scene completeness
                - support hierarchy
                - accessibility
                - realism
                - task progress
                Return a JSON object.
                  """
        user_prompt = f"""
                User Command:{command}
                Current Step:{step + 1} / {max_steps}
                Current Scene Summary:{json.dumps(scene_summary, ensure_ascii=False, indent=2)}
                Last Strategy:{strategy}
                Recent Observations:{json.dumps([o for o in recent_observations[-3:]], ensure_ascii=False, indent=2)}
                Recent Reflections:{json.dumps(recent_reflections[-3:], ensure_ascii=False, indent=2)}
                ToolResult:{json.dumps(tool_results, ensure_ascii=False, indent=2)}
                Lessons:{json.dumps(lessons[-5:], ensure_ascii=False, indent=2)}
                Analyze the current layout progress.
                Decide:
                - what is missing
                - what should happen next
                - whether the task is complete
                Return JSON:
                {{
                "goal": "...",
                "analysis": "...",
                "next_strategy": "...",
                "done": false
                }}
                """
        return self._json_chat(
            REASON_SYSTEM,
            user_prompt,
        )
    # =====================================================
    # Decide Action
    # =====================================================
    def decide_action(
        self,
        command: str,
        strategy: Dict[str, Any],
        scene_summary: Dict[str, Any],
        tool_specs: List[Dict[str, Any]],
        step: int,
        max_steps: int,
        tool_results: List[ToolResult],
    ) -> ToolDecision:
        ACTION_SYSTEM = """
                You are a scene construction agent.
                Your job is to select the correct tools
                to execute the current layout strategy.
                Guidelines:
                - use as few tools as possible
                - avoid invalid placements
                - respect support relationships
                - maintain realistic scale and positioning
                - prefer stable layouts
                - avoid overlapping objects
                - do not explain reasoning
                If the scene task is already complete,
                respond normally without tool calls.
                """
        user_prompt = f"""
                    User Command:{command}
                    Current Step:{step + 1} / {max_steps}
                    Current Scene:{json.dumps(scene_summary, ensure_ascii=False, indent=2)}
                    Current Strategy:{json.dumps(strategy, ensure_ascii=False, indent=2)}
                    Tool Result{json.dumps(tool_results, ensure_ascii=False, indent=2)}
                    Select the best tool calls to execute the strategy.
                    Use tool calls directly.
            """
        return self._tool_chat(
            ACTION_SYSTEM,
            user_prompt,
            tool_specs,
        )

    # =====================================================
    # Reflection
    # =====================================================
    def reflect(
        self,
        command: str,
        strategy: Dict[str, Any],
        tool_calls: List[Dict[str, Any]],
        observation: Dict[str, Any],
        tool_results: Dict[str, Any],
    ) -> ReflectionResult:
        REFLECT_SYSTEM = """
                    You are a scene layout critic.
                    Your job is to evaluate:
                    - whether the last actions improved the scene
                    - whether placement is physically plausible
                    - whether the scene satisfies the user goal
                    - whether layout quality improved
                    Identify:
                    - mistakes
                    - missing objects
                    - bad spatial relations
                    - unrealistic configurations
                    Generate:
                    - lessons
                    - suggestions
                    - next-step improvements
                    Return JSON only.
                    """
        user_prompt =  f"""
            User Command:{command}
            Strategy:{json.dumps(strategy, ensure_ascii=False, indent=2)}
            Executed Tool Calls"{json.dumps(tool_calls, ensure_ascii=False, indent=2)}
            Observation{json.dumps(observation, ensure_ascii=False, indent=2)}
            Tool Result{json.dumps(tool_results, ensure_ascii=False, indent=2)}
            Evaluate the latest scene modification.
            Return JSON:
            {{
            "success": true,
            "analysis": "...",
            "problems": [
                ...
            ],
            "lesson": "...",
            "next_strategy": "..."
            }}
            """
        return self._json_chat(
            REFLECT_SYSTEM,
            user_prompt,
        )