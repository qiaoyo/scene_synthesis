from __future__ import annotations

from typing import Any, Dict

from ..physics.isaac_bridge import IsaacBridgeError, run_isaac_operation
from .base import Tool, ToolContext, ToolResult, register_tool


@register_tool
class CheckSupportTool(Tool):
    schema = {
        "type": "function",
        "function": {
            "name": "check_support",
            "description": "Run Isaac Sim support validation for a child instance on a parent instance. Returns whether the relation is physically supported, diagnostic details such as z_gap and xy_coverage, issue messages, contacts, and a suggested_move when the relation is invalid.",
            "parameters": {
                "type": "object",
                "properties": {
                    "child_id": {
                        "type": "string",
                        "description": "Child scene instance ID.",
                    },
                    "parent_id": {
                        "type": "string",
                        "description": "Parent scene instance ID.",
                    },
                },
                "required": ["child_id", "parent_id"],
                "additionalProperties": False,
            },
        },
    }

    def run(self, context: ToolContext, child_id: str, parent_id: str) -> ToolResult:
        for instance_id in (child_id, parent_id):
            if instance_id not in context.scene.state.instances:
                return ToolResult(ok=False, error=f"instance not found: {instance_id}")

        try:
            payload = run_isaac_operation(
                config=context.config,
                operation="check_support",
                scene=context.scene.state,
                options={"child_id": child_id, "parent_id": parent_id,"include_suggestions": True,},
            )
        except IsaacBridgeError as exc:
            return ToolResult(ok=False, error=str(exc))

        if not payload.get("ok", False):
            return ToolResult(
                ok=False,
                data=payload,
                error=payload.get("error") or "; ".join(payload.get("errors", [])),
            )
        
        support = payload.get("support",{}) or {}

        data: Dict[str, Any] = {
            "backend": payload.get("backend", "isaacsim"),
            "supported": support.get("supported", False),
            "child": support.get("child", child_id),
            "parent": support.get("parent", parent_id),
            "contacts": support.get("contacts", []),
            "issues": support.get("issues", []),
            "warnings": payload.get("warnings", []),
            "suggested_move": support.get("suggested_move"),
        }
        return ToolResult(ok=True, data=data)
