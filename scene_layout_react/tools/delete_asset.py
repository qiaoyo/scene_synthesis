"""delete_asset — 从场景里删除一个实例。"""
from __future__ import annotations
from typing import Any
from .base import Tool, ToolContext, ToolResult, register_tool

@register_tool
class DeleteAssetTool(Tool):
    schema = {
        "type": "function",
        "function": {
            "name": "delete_asset",
            "description": (
                "Delete an existing scene instance. "
                "Child instances supported by this instance will be detached "
                "instead of being deleted."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "instance_id": {
                        "type": "string",
                        "description": (
                            "Target scene instance ID to delete."
                        ),
                    },
                },
                "required": ["instance_id"],
                "additionalProperties": False,
            },
        },
    }

    def run(self, context: ToolContext, instance_id: str, **kwargs: Any) -> ToolResult:
        # 先记录被解绑的 children
        unparented = list(context.scene.state.support_children.get(instance_id, []))
        context.scene.delete(instance_id)
        return ToolResult(ok=True, data={
            "deleted_instance_id": instance_id,
            "unparented_children": unparented,
        })