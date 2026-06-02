# react_agent.py
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple
from .config import ProjectConfig
from .llm_planner import LLMPlanner
from .observer import Observation, Observer
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
    def __init__(self,config: ProjectConfig,rag: AssetRAG,):
        self.config = config
        self.rag = rag
        self.scene = SceneStateManager()
        self.planner = LLMPlanner(config)
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
    
    # =====================================================
    # Tool Execution
    # =====================================================
    def _run_tool_call(
        self,
        call: Any,
        step_idx: int,
    ) -> Tuple[ToolResult, Dict[str, Any], ToolRecord]:
        
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

        last_observation: Optional[Observation] = None

        # =================================================
        # Message History (multi-turn tool context)
        # =================================================
        messages: List[Dict[str, Any]] = [
            {"role": "user", "content": f"User Command: {command}"},
        ]

        # =================================================
        # Main ReAct Loop
        # =================================================
        for step_idx in range(max_steps):
            step_start = time.perf_counter()
            step_record = StepRecord(step=step_idx, started_at=now_iso())

            # =============================================
            # Append step context to messages
            # =============================================
            obs_dict = (
                last_observation.to_dict()
                if last_observation is not None
                else None
            )
            step_context = (
                f"Current Step: {step_idx + 1} / {max_steps}\n"
                #f"Current Scene Summary:\n"
                #f"{json.dumps(self.scene.to_dict(), ensure_ascii=False, indent=2)}\n"
                f"Latest Observation:\n"
                f"{json.dumps(obs_dict, ensure_ascii=False, indent=2)}\n"
                f"Select the best tool calls for exactly one workflow step."
            )
            messages.append({"role": "user", "content": step_context})

            decision = self.planner.plan_action(
                messages=messages,
                tool_specs=self.tool_specs,
            )
            step_record.decision = jsonable(decision)
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
                result, tool_record = self._run_tool_call(call, step_idx)
                tool_results.append(result)
                step_record.tools.append(tool_record)

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
            # Append tool calls & results to message history
            # =============================================
            if tool_calls:
                assistant_tc = [
                    {
                        "id": call.get("id", f"call_{i}"),
                        "type": "function",
                        "function": {
                            "name": call.get("name", ""),
                            "arguments": json.dumps(
                                call.get("arguments", {}),
                                ensure_ascii=False,
                            ),
                        },
                    }
                    for i, call in enumerate(tool_calls)
                ]
                messages.append({
                    "role": "assistant",
                    "tool_calls": assistant_tc,
                })
                for call, result in zip(tool_calls, tool_results):
                    messages.append({
                        "role": "tool",
                        "tool_call_id": call.get("id", ""),
                        "content": json.dumps(
                            result.to_dict(),
                            ensure_ascii=False,
                        ),
                    })

            # =============================================
            # Observation
            # =============================================
            observation = self.observer.observe()
            last_observation = observation
            step_record.observation = observation.to_dict()
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