# react_agent.py
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple
from .config import ProjectConfig
from .observer import Observer
from .rag import AssetRAG
from .scene_state import SceneStateManager
from .tools.base import (
    TOOL_REGISTRY,
    ToolContext,
    ToolResult,
)
from .observe_backends import observe_scene_with_isaac
import json
import time
from .run_records import (
    RunRecord,
    RunRecorder,
    StepRecord,
    ToolRecord,
    config_snapshot,
    jsonable,
    new_run_id,
    now_iso,
    perf_ms,
    runtime_version,
)
# =========================================================
# ReAct Agent
# =========================================================
class ReActAgent:
    # =====================================================
    # Init
    # =====================================================
    def __init__(self,config: ProjectConfig,rag: AssetRAG, scene: Optional[SceneStateManager] = None,):
        self.config = config
        self.rag = rag
        self.scene = scene if scene is not None else SceneStateManager()
        scene_observer = None
        if self.config.physics_enabled:
            scene_observer = lambda state: observe_scene_with_isaac(self.config, state)

        self.observer = Observer(
            self.scene,
            scene_observer=scene_observer,
            physics_required=self.config.physics_enabled,
        )

        self.tool_context = ToolContext(
            scene=self.scene,
            rag=self.rag,
            config=self.config,
            physics_enabled=self.config.physics_enabled,
            extras={}
        )
        
        self.tool_specs = [
            tool.schema 
            for tool in TOOL_REGISTRY.values()
            ]
                
        try:
            from openai import OpenAI
        except ModuleNotFoundError as exc:
            raise RuntimeError(
                "openai package is required"
            ) from exc
        self._llm = OpenAI(
            base_url=config.llm_api_base_url,
            api_key=config.llm_api_key,
            timeout=float(
                getattr(config, "llm_timeout_sec", 60.0)
            ),
            max_retries=int(
                getattr(config, "llm_max_retries", 2)
            ),
        )
        
    def _build_planner_prompt(
        self, 
        command: str,
        step_idx: int,
        max_steps: int,
        observation: Dict[str, Any],
        recent_tools: List[ToolRecord],
    ) -> str:
        """
        构造 Planner 输入
        """
        tool_history = []
        for tool in recent_tools[-10:]:
            tool_history.append({
                    "name": tool.name,
                    "arguments": tool.arguments,
                    "ok": tool.ok,
                    "result": tool.result,
                })
        
        tool_names = [
            tool.schema["function"]["name"]
            for tool in TOOL_REGISTRY.values()
        ]
        
        state_packet = {
            "user_command": command,
            "current_step": step_idx + 1,
            "max_steps": max_steps,
            "latest_observation": observation,
            "recent_tools": tool_history,
            "available_tools": tool_names,
        }

        return f"""
            Decide the next tool action for one workflow step.

            State Packet:
            {json.dumps(state_packet, ensure_ascii=False, indent=2)}

            Use this packet as the complete context:
            - user_command is the scene request.
            - latest_observation shows current objects, support relations, and validation
            status.
            - recent_tools shows previous tool calls and results.
            - available_tools lists callable tools.

            Decision guidance:
            - If assets are missing, retrieve them.
            - If required objects are not placed, place them.
            - If support relations are missing, set them.
            - Use support_type="surface" for on top of, on surface, or supported by
            relations.
            - Use support_type="container_inner" only when a child is inside an
            open Box and resting on the Box inner bottom surface.
            - If validation is missing or stale, run check_collision/check_support.
            - If check tools returned movement suggestions, use move_asset when reasonable.
            - If repeated movement fails, use replace_instance.
            - Delete only unnecessary or unrecoverable objects.
            - If the scene is complete, valid, stable, and unsaved, call save_scene_usd.
            - If save_scene_usd already succeeded, return final response.

            Return tool call(s) for this single step, or final response if the task is done.
            """.strip()

    def _planner_system_prompt(self) -> str:
        return """
            You are a robotic scene construction agent.
            Use the available tools to build the requested scene, make it physically valid,
            save the USD scene, and then stop.

            Follow the learned three-phase workflow:
            1. Build: retrieve assets, place objects, and register support relations.
            2. Validate and Adapt: check collision/support/stability, move objects using
            tool suggestions, replace difficult assets when needed, and delete only
            unnecessary or unrecoverable objects.
            3. Save: save the USD only after the scene is complete and valid.

            Hard rules:
            - Execute exactly one workflow step per round.
            - Treat latest_observation as the authoritative scene state.
            - Movement suggestions must come from check_collision or check_support results,
            not from observation alone.
            - For support relations, call set_support with support_type="surface"
            for ordinary top-surface support. Call support_type="container_inner"
            only for a child inside an open Box/bin/container, supported by the
            inner bottom surface.
            - Prefer move_asset before replace_instance, and replace_instance before
            delete_asset.
            - Never save an incomplete, colliding, unsupported, or unstable scene.
            - After save_scene_usd succeeds, return a final response and call no more tools.
            """.strip()

    def _build_planner_messages(
        self,
        user_prompt: str,
    ) -> List[Dict[str, str]]:
        return [
                {
                    "role": "system",
                    "content": self._planner_system_prompt(),
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ]

    def _plan_action(
        self,
        api_messages: List[Dict[str, str]],
    ) -> Dict[str, Any]:
        """
        Accept the full message list sent to the planner and return a
        tool-call or final-response decision.
        """
        try:
            response = self._llm.chat.completions.create(
                model=self.config.model,
                messages=api_messages,
                tools=self.tool_specs,
                tool_choice="auto",
                temperature=self.config.temperature,
                extra_body={
                    "chat_template_kwargs": {
                        "enable_thinking":
                            self.config.llm_enable_thinking,
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
                calls.append(
                    {
                        "id": tool_call.id,
                        "name": tool_call.function.name,
                        "arguments": args,
                    }
                )
            return {
                "type": "tool_calls",
                "calls": calls,
            }
        return {
            "type": "final",
            "content": message.content or "",
        }
    # =====================================================
    # Tool Execution
    # =====================================================
    def _run_tool_call(
        self,
        call: Any,
    ) -> Tuple[ToolResult, ToolRecord]:
        
        tool_start = time.perf_counter()

        if not isinstance(call, dict):
            tool_name = "<invalid>"
            tool_args: Dict[str, Any] = {}
            result = ToolResult(ok=False, error="tool call must be a dict")
        else:
            raw_tool_name = call.get("name")
            raw_tool_args = call.get("arguments", {})
            tool_name = str(raw_tool_name)

            if not isinstance(raw_tool_args, dict):
                tool_args = {"raw_arguments": jsonable(raw_tool_args)}
                result = ToolResult(ok=False, error=f"tool arguments for {tool_name} must be a dict")
            else:
                tool_args = raw_tool_args
                tool = TOOL_REGISTRY.get(raw_tool_name) if isinstance(raw_tool_name, str) else None
                
                if tool is None:
                    result = ToolResult(ok=False, error=f"unknown tool: {tool_name}")
                else:
                    result = tool(self.tool_context, **tool_args)
        tool_record = ToolRecord(
            name=tool_name,
            arguments=jsonable(tool_args),
            ok=result.ok,
            elapsed_ms=perf_ms(tool_start),
            result=result.to_dict(),
        )
        return result, tool_record

    # =====================================================
    # Main Loop
    # =====================================================
    
    def run(self, command: str, max_steps: int = 10) -> Dict[str, Any]:
        
        run_start = time.perf_counter()
        
        # =================================================
        # Runtime Setup
        # =================================================
        
        run_id = new_run_id()
        recorder = RunRecorder(self.config.output_dir, run_id)
        recent_tool_records: List[ToolRecord] = []
        self.tool_context.extras.update({
            "run_id": run_id,
            "run_dir": str(recorder.run_dir),
        })
        record = RunRecord(
            run_id=run_id,
            command=command,
            started_at=now_iso(),
            version=runtime_version(),
            config=config_snapshot(self.config),
        )
        # =================================================
        # Message History (multi-turn tool context)
        # =================================================
        initial_observation = self.observer.observe()
        obs_dict = initial_observation.to_dict()
    
        # =================================================
        # Main ReAct Loop
        # =================================================
        for step_idx in range(max_steps):
            step_start = time.perf_counter()
            step_record = StepRecord(step=step_idx, started_at=now_iso())

            # =============================================
            # Append step context to messages
            # =============================================
            user_prompt = self._build_planner_prompt(
                command=command,
                step_idx=step_idx,
                max_steps=max_steps,
                observation=obs_dict,
                recent_tools=recent_tool_records,
            )

            planner_messages = self._build_planner_messages(user_prompt)
            decision = self._plan_action(planner_messages)
            step_record.decision = jsonable(decision)
            recorder.save_planner_step(
                step=step_idx,
                command=command,
                messages=planner_messages,
                decision=jsonable(decision),
            )
            # =============================================
            # Planner Error
            # =============================================
            if decision.get("type") in {"planner_error", "tool_chat_error"}:
                step_record.elapsed_ms = perf_ms(step_start)
                record.steps.append(step_record)
                record.ok = False
                record.error = decision.get("error")
                record.elapsed_ms = perf_ms(run_start)
                recorder.save_record(record)
                return record.to_dict()
            # =============================================
            # Final Response
            # =============================================
            if decision.get("type") == "final":
                step_record.elapsed_ms = perf_ms(step_start)
                record.steps.append(step_record)
                record.ok = True
                record.response = decision.get("content", "")
                record.elapsed_ms = perf_ms(run_start)
                recorder.save_record(record)
                return record.to_dict()

            # =============================================
            # Tool Calls
            # =============================================
            tool_results: List[ToolResult] = []
            tool_calls = (
                        decision.get("calls")
                        if decision.get("type") == "tool_calls"
                        else []
                        )
            # =============================================
            # Execute Tools
            # =============================================
            for tool_index, call in enumerate(tool_calls):
                result, tool_record = self._run_tool_call(call)
                tool_results.append(result)
                step_record.tools.append(tool_record)
                recent_tool_records.append(tool_record)
                if len(recent_tool_records) > 20:
                    recent_tool_records = recent_tool_records[-20:]
                print(
                        f"[Step {step_idx}] "
                        f"{tool_record.name} "
                        f"ok={tool_record.ok}"
                    )
                recorder.save_step_tool(
                    step=step_idx,
                    tool_index=tool_index,
                    tool_record=tool_record,
                )
            # =============================================
            # Observation
            # =============================================
            observation = self.observer.observe()
            obs_dict = observation.to_dict()
            step_record.observation = obs_dict
            step_record.scene_snapshot_path = recorder.save_scene(step_idx, self.scene.to_dict())

            # =============================================
            # Step Finish
            # =============================================
            step_record.elapsed_ms = perf_ms(step_start)
            record.steps.append(step_record)
            recorder.save_record(record)
        
        record.ok = False
        record.error = "max steps exceeded"
        record.elapsed_ms = perf_ms(run_start)
        recorder.save_record(record)
        return record.to_dict()
