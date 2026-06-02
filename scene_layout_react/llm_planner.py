# llm_planner.py
from __future__ import annotations
import json
from typing import Any, Dict, List, Optional
from .config import ProjectConfig
# =========================================================
# Planner
# =========================================================
class LLMPlanner:
    # =====================================================
    # Init
    # =====================================================
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
        messages: List[Dict[str, Any]],
        tool_specs: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """
        Accept the full multi-turn message list built by ReActAgent
        and return a tool-call or final-response decision.
        """
        plan_system = """
            You are a reactive planning agent for robotic scene construction.
            Follow user instructions and invoke proper tools to complete tasks
            until the scene becomes fully compliant.
            
            Workflow:
            - The workflow proceeds sequentially: 
            - Retrieve_assets: Extract ALL required assets from the user
              command and retrieve them in ONE batch call. Do not proceed
              until all assets are retrieved. Tool:retrieve_asset.
            - Place_core_objects: Place ALL retrieved core objects in ONE
              batch using multiple place_instance calls. Tool:place_instance.
            - Set support: After placing core objects, set support relations between them based on the scene context. Tool:set_support.
            - Check and Adjust: Run collision and support checks after core object placement. Adjust positions iteratively for invalid layouts. If adjustments fail, delete the asset and re-place the instance. Tools: check_collision, check_support, move_asset, simulate_step, delete_asset, place_instance
            - Save Scene: Once all core objects are placed and the scene is valid, save the scene. Tool:save_scene_usd.    
        """
        api_messages = [{"role": "system", "content": plan_system}] + list(messages)

        try:
            response = self._client.chat.completions.create(
                model=self.config.model,
                messages=api_messages,
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

        # =============================================
        # Tool Calls
        # =============================================
        if message.tool_calls:
            calls: List[Dict[str, Any]] = []
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

        # =============================================
        # Final Response
        # =============================================
        return {
            "type": "final",
            "content": message.content or "",
        }
