from __future__ import annotations
from typing import Any
from ..data_models import Instance
from ..validators import check_support_geometry
from .base import Tool, ToolContext, ToolResult, register_tool

@register_tool
class SetSupportTool(Tool):
    schema = {
        "type": "function",
        "function": {
            "name": "set_support",
            "description": ("""Register that a child instance is supported by a parent instance. This updates only the logical support relationship and also returns geometric validation results."""
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "child_id": {
                        "type": "string",
                        "description": (
                            "Child scene instance ID."
                        ),
                    },
                    "parent_id": {
                        "type": "string",
                        "description": (
                            "Parent scene instance ID."
                        ),
                    },
                },
                "required": [
                    "child_id",
                    "parent_id",
                ],
                "additionalProperties": False,
            },
        },
    }

    def run(self, context: ToolContext, child_id:str, parent_id:str) -> ToolResult:
        context.scene.set_support(child_id, parent_id) 
        return ToolResult(
            ok=True, 
            data={
            "child": child_id,
            "parent": parent_id
        })
