from __future__ import annotations

from typing import Any, Dict, List

from ..physics.isaac_bridge import IsaacBridgeError, run_isaac_operation
from .base import Tool, ToolContext, ToolResult, register_tool

@register_tool
class CheckCollisionTool(Tool):
    schema = {
        "type": "function",
        "function": {
            "name": "check_collision",
            "description": "Run Isaac Sim collision checking for the current scene or a specific pair of instances.",
            "parameters": {
                "type": "object",
                "properties": {
                    "instance_id_a": {
                        "type": "string",
                        "description": "Optional first instance ID in a pair to check.",
                    },
                    "instance_id_b": {
                        "type": "string",
                        "description": "Optional second instance ID in a pair to check.",
                    },
                },
                "additionalProperties": False,
            },
        },
    }

    def run(
        self,
        context: ToolContext,
        instance_id_a: str | None = None,
        instance_id_b: str | None = None,
    ) -> ToolResult:
        
        pair: List[str] | None = None
        if instance_id_a or instance_id_b:
            if not instance_id_a or not instance_id_b:
                return ToolResult(
                    ok=False,
                    error="instance_id_a and instance_id_b must be provided together",
                )
            for instance_id in (instance_id_a, instance_id_b):
                if instance_id not in context.scene.state.instances:
                    return ToolResult(
                        ok=False,
                        error=f"instance not found: {instance_id}",
                    )
            pair = [instance_id_a, instance_id_b]

        try:
            payload = run_isaac_operation(
                config=context.config,
                operation="check_collision",
                scene=context.scene.state,
                options={"pair": pair} if pair else {},
            )
        except IsaacBridgeError as exc:
            return ToolResult(ok=False, error=str(exc))

        if not payload.get("ok", False):
            return ToolResult(
                ok=False,
                data=payload,
                error=payload.get("error") or "; ".join(payload.get("errors", [])),
            )

        data: Dict[str, Any] = {
            "backend": payload.get("backend", "isaacsim"),
            "collision_free": payload.get("collision_free", True),
            "collisions": payload.get("collisions", []),
            "warnings": payload.get("warnings", []),
        }
        return ToolResult(ok=True, data=data)

