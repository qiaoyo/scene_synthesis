"""move_asset — 平移已有实例。"""
from __future__ import annotations
from .base import Tool, ToolContext, ToolResult, register_tool

@register_tool
class MoveAssetTool(Tool):
    schema = {
        "type": "function",
        "function": {
            "name": "move_asset",
            "description": "Move an existing scene instance to a new world position.",
            "parameters": {
                "type": "object",
                "properties": {
                    "instance_id": {
                        "type": "string",
                        "description": (
                            "Target scene instance ID."
                        ),
                    },
                    "new_position": {
                        "type": "array",
                        "items": {
                            "type": "number",
                        },
                        "minItems": 3,
                        "maxItems": 3,
                        "description": (
                            "Target world position [x, y, z] in meters."
                        ),
                    },
                },
                "required": [
                    "instance_id",
                    "new_position",
                ],
                "additionalProperties": False,
            },
        },
    }

    def run(self,context: ToolContext,instance_id: str,new_position: list[float],) -> ToolResult:
        if len(new_position) != 3:
            return ToolResult(
                ok=False,
                error="new_position must contain exactly 3 values",
            )
        try:
            new_position = [float(v) for v in new_position]
        except (TypeError, ValueError):
            return ToolResult(
                ok=False,
                error="new_position must contain numeric values",
            )
        inst = context.scene.get(instance_id)
        if inst is None:
            return ToolResult(
                ok=False,
                error=f"instance not found: {instance_id}",
            )
        old_position = list(inst.position)
        context.scene.move(instance_id,new_position,)
        return ToolResult(
            ok=True,
            data={
                "instance_id": instance_id,
                "old_position": old_position,
                "new_position": new_position,
            },
        )