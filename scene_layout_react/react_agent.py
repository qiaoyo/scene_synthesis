# react_agent.py
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple
from .config import ProjectConfig
from .llm_planner import LLMPlanner,ToolDecision
from .observer import Observation, Observer
from .rag import AssetRAG
from .scene_state import SceneStateManager
from .tools.base import (
    TOOL_REGISTRY,
    ToolContext,
    ToolResult,
)
from .observe_backends import observe_scene_with_isaac
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
    _make_action_record,
    _recent_action_records,
)
#========================================================
# Runtime State
#========================================================
@dataclass
class AgentStep:
    step: int
    strategy: Optional[Dict[str, Any]] = None
    tool_decision: Optional[ToolDecision] = None
    tool_results: List[ToolResult] = field(default_factory=list)
    action_records: List[Dict[str, Any]] = field(default_factory=list)
    observation: Optional[Observation] = None

# =========================================================
# ReAct Agent
# =========================================================
class ReActAgent:
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
        self.tool_specs = [tool.schema for tool in TOOL_REGISTRY.values()]

    def _planner_context(self, history: List[AgentStep]) -> Dict[str, Any]:
        latest_observation = None
        if history and history[-1].observation is not None:
            latest_observation = history[-1].observation.to_dict()

        return {
            "scene_summary": self.scene.to_dict(),
            "latest_observation": latest_observation,
            "recent_actions": _recent_action_records(history, limit=3),
        }

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

        action_record = _make_action_record(
            step_idx=step_idx,
            tool_name=tool_name,
            tool_args=jsonable(tool_args),
            result=result,
        )
        tool_record = ToolRecord(
            name=tool_name,
            arguments=jsonable(tool_args),
            ok=result.ok,
            elapsed_ms=perf_ms(tool_start),
            result=result.to_dict(),
        )
        return result, action_record, tool_record

    def _move_calls_from_suggested_final_positions(
        self,
        observation: Observation,
    ) -> List[Dict[str, Any]]:
        validation = observation.validation or {}
        suggested_final_positions = validation.get("suggested_final_positions") or {}

        if not suggested_final_positions:
            suggested_move = validation.get("suggested_move") or {}
            if isinstance(suggested_move, dict):
                suggested_final_positions = suggested_move.get("final_positions") or {}

        if not isinstance(suggested_final_positions, dict):
            return []

        calls: List[Dict[str, Any]] = []
        seen: set[str] = set()

        for fallback_id, entry in suggested_final_positions.items():
            instance_id = str(fallback_id)
            final_position = None

            if isinstance(entry, dict):
                instance_id = str(entry.get("instance_id") or fallback_id)
                final_position = entry.get("final_position") or entry.get("new_position")
            elif isinstance(entry, (list, tuple)):
                final_position = entry

            if instance_id in seen or instance_id not in self.scene.state.instances:
                continue
            if not isinstance(final_position, (list, tuple)) or len(final_position) != 3:
                continue

            try:
                new_position = [float(value) for value in final_position]
            except (TypeError, ValueError):
                continue

            seen.add(instance_id)
            calls.append({
                "name": "move_asset",
                "arguments": {
                    "instance_id": instance_id,
                    "new_position": new_position,
                },
            })

        return calls

    def _apply_suggested_final_positions(
        self,
        observation: Observation,
        *,
        step_idx: int,
        step_record: StepRecord,
        recorder: RunRecorder,
        runtime: AgentStep,
        tool_results: List[ToolResult],
    ) -> int:
        move_calls = self._move_calls_from_suggested_final_positions(observation)
        if not move_calls:
            return 0

        for call in move_calls:
            tool_index = len(step_record.tools)
            result, action_record, tool_record = self._run_tool_call(call, step_idx)
            tool_results.append(result)
            runtime.action_records.append(action_record)
            step_record.tools.append(tool_record)
            recorder.save_step_tool(
                step=step_idx,
                tool_index=tool_index,
                tool_record=tool_record,
                action_record=action_record,
            )
            recorder.event("tool_finished", {"step": step_idx, "tool": tool_record})

        recorder.event(
            "auto_move_from_suggested_final_positions",
            {
                "step": step_idx,
                "move_count": len(move_calls),
                "calls": jsonable(move_calls),
            },
        )
        return len(move_calls)

    def _move_calls_from_support_suggestions(
        self,
        observation: Observation,
    ) -> List[Dict[str, Any]]:
        support_state = observation.support_state or {}
        invalid_relations = support_state.get("invalid_relations") or []
        if not isinstance(invalid_relations, list):
            return []

        calls: List[Dict[str, Any]] = []
        seen: set[str] = set()

        for relation in invalid_relations:
            if not isinstance(relation, dict):
                continue

            suggested_move = relation.get("suggested_move") or {}
            if not isinstance(suggested_move, dict):
                continue

            instance_id = (
                suggested_move.get("instance_id")
                or suggested_move.get("child_id")
                or relation.get("child")
            )
            if not isinstance(instance_id, str):
                continue
            if instance_id in seen or instance_id not in self.scene.state.instances:
                continue

            new_position = suggested_move.get("new_position")
            if not isinstance(new_position, (list, tuple)) or len(new_position) != 3:
                continue

            try:
                target_position = [float(value) for value in new_position]
            except (TypeError, ValueError):
                continue

            current_position = self.scene.state.instances[instance_id].position
            if all(
                abs(float(current_position[axis]) - target_position[axis]) < 1e-9
                for axis in range(3)
            ):
                continue

            seen.add(instance_id)
            calls.append({
                "name": "move_asset",
                "arguments": {
                    "instance_id": instance_id,
                    "new_position": target_position,
                },
            })

        return calls

    def _apply_support_suggested_moves(
        self,
        observation: Observation,
        *,
        step_idx: int,
        step_record: StepRecord,
        recorder: RunRecorder,
        runtime: AgentStep,
        tool_results: List[ToolResult],
    ) -> int:
        move_calls = self._move_calls_from_support_suggestions(observation)
        if not move_calls:
            return 0

        for call in move_calls:
            tool_index = len(step_record.tools)
            result, action_record, tool_record = self._run_tool_call(call, step_idx)
            tool_results.append(result)
            runtime.action_records.append(action_record)
            step_record.tools.append(tool_record)
            recorder.save_step_tool(
                step=step_idx,
                tool_index=tool_index,
                tool_record=tool_record,
                action_record=action_record,
            )
            recorder.event("tool_finished", {"step": step_idx, "tool": tool_record})

        recorder.event(
            "auto_move_from_support_suggestions",
            {
                "step": step_idx,
                "move_count": len(move_calls),
                "calls": jsonable(move_calls),
            },
        )
        return len(move_calls)

    def _finish_step(
        self,
        recorder: RunRecorder,
        record: RunRecord,
        step_record: StepRecord,
        step_start: float,
        save: bool = True,
    ) -> None:
        step_record.elapsed_ms = perf_ms(step_start)
        record.steps.append(step_record)
        recorder.event("step_finished", step_record.to_dict())
        if save:
            recorder.save_record(record)

    def _finish_run(
        self,
        recorder: RunRecorder,
        record: RunRecord,
        run_start: float,
        ok: bool,
        event_type: str = "run_finished",
        response: Optional[str] = None,
        error: Optional[str] = None,
    ) -> Dict[str, Any]:
        record.ok = ok
        record.response = response
        record.error = error
        record.elapsed_ms = perf_ms(run_start)
        recorder.event(event_type, record.to_dict())
        recorder.save_record(record)
        return record.to_dict()

    def _successful_save_usd(self, step_record: StepRecord) -> bool:
        return any(
            tool.name == "save_scene_usd" and tool.ok
            for tool in step_record.tools
        )

    # =====================================================
    # Main Loop
    # =====================================================
    def run(self, command: str, max_steps: int = 10) -> Dict[str, Any]:
        run_start = time.perf_counter()
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

        history: List[AgentStep] = []
        recorder.event("run_started", record.to_dict())

        for step_idx in range(max_steps):
            step_start = time.perf_counter()
            runtime = AgentStep(step=step_idx)
            step_record = StepRecord(step=step_idx, started_at=now_iso())
            recorder.event("step_started", {"step": step_idx})
            planner_context = self._planner_context(history)

            decision = self.planner.plan_action(
                command=command,
                scene_summary=planner_context["scene_summary"],
                latest_observation=planner_context["latest_observation"],
                recent_actions=planner_context["recent_actions"],
                tool_specs=self.tool_specs,
                step=step_idx,
                max_steps=max_steps,
            )

            runtime.tool_decision = decision
            step_record.decision = jsonable(decision)
            recorder.event("decision", {"step": step_idx, "decision": decision})

            if decision.get("type") in {"planner_error", "tool_chat_error"}:
                self._finish_step(recorder, record, step_record, step_start, save=False)
                return self._finish_run(
                    recorder,
                    record,
                    run_start,
                    ok=False,
                    event_type="run_failed",
                    error=decision.get("error"),
                )

            if decision.get("type") == "final":
                self._finish_step(recorder, record, step_record, step_start, save=False)
                return self._finish_run(
                    recorder,
                    record,
                    run_start,
                    ok=True,
                    response=decision.get("content", ""),
                )

            tool_results: List[ToolResult] = []
            tool_calls = decision.get("calls") if decision.get("type") == "tool_calls" else []

            if not isinstance(tool_calls, list):
                tool_calls = []
                tool_results.append(ToolResult(ok=False, error="planner returned invalid tool calls"))

            if decision.get("type") in {"planner_error", "tool_chat_error"}:
                tool_results.append(
                    ToolResult(
                        ok=False,
                        data={"planner_decision": decision},
                        error=decision.get("error", "planner decision failed"),
                    )
                )

            for tool_index, call in enumerate(tool_calls):
                result, action_record, tool_record = self._run_tool_call(call, step_idx)
                tool_results.append(result)
                runtime.action_records.append(action_record)
                step_record.tools.append(tool_record)
                recorder.save_step_tool(
                    step=step_idx,
                    tool_index=tool_index,
                    tool_record=tool_record,
                    action_record=action_record,
                )
                recorder.event("tool_finished", {"step": step_idx, "tool": tool_record})

            runtime.tool_results = tool_results

            observation = self.observer.observe()
            auto_move_count = self._apply_suggested_final_positions(
                observation,
                step_idx=step_idx,
                step_record=step_record,
                recorder=recorder,
                runtime=runtime,
                tool_results=tool_results,
            )
            if auto_move_count:
                recorder.event(
                    "auto_move_source_observation",
                    {"step": step_idx, "observation": observation.to_dict()},
                )
                observation = self.observer.observe()

            support_auto_move_count = self._apply_support_suggested_moves(
                observation,
                step_idx=step_idx,
                step_record=step_record,
                recorder=recorder,
                runtime=runtime,
                tool_results=tool_results,
            )
            if support_auto_move_count:
                recorder.event(
                    "auto_move_support_source_observation",
                    {"step": step_idx, "observation": observation.to_dict()},
                )
                observation = self.observer.observe()

            runtime.observation = observation
            step_record.observation = observation.to_dict()
            step_record.scene_snapshot_path = recorder.save_scene(step_idx, self.scene.to_dict())
            recorder.event("observation", {"step": step_idx, "observation": observation.to_dict()})

            history.append(runtime)
            saved_usd = self._successful_save_usd(step_record)
            if saved_usd and observation.ok:
                self._finish_step(recorder, record, step_record, step_start, save=False)
                return self._finish_run(
                    recorder,
                    record,
                    run_start,
                    ok=True,
                    response="scene saved and latest observation is valid",
                )

            self._finish_step(recorder, record, step_record, step_start)

        return self._finish_run(
            recorder,
            record,
            run_start,
            ok=False,
            error="max steps exceeded",
        )
