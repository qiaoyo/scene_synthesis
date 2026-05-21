from __future__ import annotations

from typing import Any, Dict

from ..physics.isaac_bridge import IsaacBridgeError, run_isaac_operation
from .base import Tool, ToolContext, ToolResult, register_tool


@register_tool
class SimulateStepTool(Tool):
    schema = {
        "type": "function",
        "function": {
            "name": "simulate_step",
            "description": "Run an Isaac Sim physics simulation step for the current scene and report stability feedback.",
            "parameters": {
                "type": "object",
                "properties": {
                    "duration": {
                        "type": "number",
                        "minimum": 0.0,
                        "description": "Simulation duration in seconds.",
                    },
                    "dt": {
                        "type": "number",
                        "exclusiveMinimum": 0.0,
                        "description": "Physics timestep in seconds.",
                    },
                    "write_back": {
                        "type": "boolean",
                        "description": "If true, update SceneState positions from Isaac final positions.",
                    },
                },
                "additionalProperties": False,
            },
        },
    }

    def run(
        self,
        context: ToolContext,
        duration: float | None = None,
        dt: float | None = None,
        write_back: bool = False,
    ) -> ToolResult:
        if duration is None:
            duration = float(getattr(context.config, "physics_sim_duration", 2.0))
        options: Dict[str, Any] = {"duration": float(duration)}
        if dt is not None:
            options["dt"] = float(dt)

        try:
            payload = run_isaac_operation(
                config=context.config,
                operation="simulate_step",
                scene=context.scene.state,
                options=options,
            )
        except IsaacBridgeError as exc:
            return ToolResult(ok=False, error=str(exc))

        if not payload.get("ok", False):
            return ToolResult(
                ok=False,
                data=payload,
                error=payload.get("error") or "; ".join(payload.get("errors", [])),
            )

        final_positions = payload.get("final_positions", {}) or {}
        if write_back:
            for instance_id, position in final_positions.items():
                if instance_id not in context.scene.state.instances:
                    continue
                context.scene.move(instance_id, [float(v) for v in position])

        data: Dict[str, Any] = {
            "backend": payload.get("backend", "isaacsim"),
            "stable": payload.get("stable", False),
            "fallen_assets": payload.get("fallen_assets", []),
            "contacts": payload.get("contacts", []),
            "final_positions": final_positions,
            "warnings": payload.get("warnings", []),
            "write_back": bool(write_back),
        }
        return ToolResult(ok=True, data=data)
