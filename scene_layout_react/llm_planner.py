# llm_planner.py
from __future__ import annotations

import json
from typing import Any, Dict, List, Optional

from .config import ProjectConfig
ToolDecision = Dict[str, Any]
# =========================================================
# Planner
# =========================================================
class LLMPlanner:
    def __init__(
        self,
        config: ProjectConfig,
    ):
        self.config = config
        try:
            from openai import OpenAI
        except ModuleNotFoundError as exc:
            raise RuntimeError(
                "LLMPlanner requires the `openai` package. "
                "Install the LLM dependencies before constructing LLMPlanner."
            ) from exc

        self._client = OpenAI(
            base_url=config.llm_api_base_url,
            api_key=config.llm_api_key,
            timeout=float(getattr(config, "llm_timeout_sec", 60.0)),
            max_retries=int(getattr(config, "llm_max_retries", 2)),
        )

    # =====================================================
    # Plan Action
    # =====================================================
    def plan_action(
        self,
        command: str,
        scene_summary: Dict[str, Any],
        latest_observation: Optional[Dict[str, Any]],
        recent_actions: List[Dict[str, Any]],
        tool_specs: List[Dict[str, Any]],
        step: int,
        max_steps: int,
    ) -> ToolDecision:
        plan_system = """
            You are a reactive planning agent. Follow user instructions and invoke proper tools to complete tasks until the scene becomes fully compliant. You must follow the rules below to complete the task.
            Global Rules:
            - Bulk asset retrieval and placement are supported.
            - Retrieve all required assets in the retrieval phase and place all objects in the placement phase.
            - The workflow proceeds sequentially: asset retrieval, object placement, collision/support detection and adjustment to eliminate collisions.
            - retrieve_assets: Extract ALL required assets from the user command and retrieve them in ONE batch call using retrieve_asset. Do not proceed until all assets are retrieved.
            - place_core_objects: Place ALL retrieved core objects in ONE batch using multiple place_instance calls.
            - If there is a direct supporting relation between objects, use the setsupport tool to establish the relation after placing both objects.
            -Save the scene once all required assets are positioned and the observation result is valid.
        """
        user_prompt = f"""
            User Command:{command}
            Current Step:{step + 1} / {max_steps}
            Current Scene Summary:{json.dumps(scene_summary, ensure_ascii=False, indent=2)}
            Latest Observation:{json.dumps(latest_observation, ensure_ascii=False, indent=2)}
            Recent Actions:{json.dumps(recent_actions, ensure_ascii=False, indent=2)}
            Select the best tool calls for exactly one workflow step.
            Use tool calls directly.
        """
        try:
            response = self._client.chat.completions.create(
                model=self.config.model,
                messages=[
                    {"role": "system", "content": plan_system},
                    {"role": "user", "content": user_prompt},
                ],
                tools=tool_specs,
                tool_choice="auto",
                temperature=self.config.temperature,
                extra_body={
                    "chat_template_kwargs": {
                        "enable_thinking": self.config.llm_enable_thinking,
                    }
                },
            )
        except Exception as exc:
            return {
                "type": "planner_error",
                "stage": "tool_chat",
                "error": str(exc),
                "error_class": exc.__class__.__name__,
            }
        message = response.choices[0].message
        if message.tool_calls:
            calls = []
            for tool_call in message.tool_calls:
                raw_args = tool_call.function.arguments or "{}"
                try:
                    args = json.loads(raw_args)
                except Exception as exc:
                    return {
                        "type": "tool_chat_error",
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

        return {
            "type": "final",
            "content": message.content or "",
    }
