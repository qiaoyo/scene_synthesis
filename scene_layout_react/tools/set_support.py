from __future__ import annotations
from .base import Tool, ToolContext, ToolResult, register_tool

@register_tool
class SetSupportTool(Tool):
    schema = {
        "type": "function",
        "function": {
            "name": "set_support",
            "description": ("""Register that a child instance is logically supported by a parent instance. This only updates the scene support relationship. It does not perform geometric or Isaac Sim validation. Use check_support or observe the scene to validate the relation."""
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
                "required": [ "child_id","parent_id",],
                "additionalProperties": False,
            },
        },
    }

    def run(self, context: ToolContext, child_id:str, parent_id:str) -> ToolResult:
        
        if child_id not in context.scene.state.instances:
            return ToolResult(
                ok=False,
                error=f"child instance not found: {child_id}",
            )

        if parent_id not in context.scene.state.instances:
            return ToolResult(
                ok=False,
                error=f"parent instance not found: {parent_id}",
            )

        if child_id == parent_id:
            return ToolResult(
                ok=False,
                error="child and parent cannot be the same instance",
            )

        if _would_create_support_cycle(context, child_id, parent_id):
            return ToolResult(
                ok=False,
                error=f"support relation would create a cycle: {child_id} -> {parent_id}",
            )

        old_parent_id = context.scene.state.instances[child_id].parent_instance_id

        context.scene.set_support(child_id, parent_id) 
        return ToolResult(
            ok=True,
            data={
                "child": child_id,
                "parent": parent_id,
                "old_parent": old_parent_id,
                "registered": True,
                "validation_performed": False,
            },
        )
        
def _would_create_support_cycle(
    context: ToolContext,
    child_id: str,
    parent_id: str,
) -> bool:
    current_id = parent_id
    visited: set[str] = set()

    while current_id:
        if current_id == child_id:
            return True

        if current_id in visited:
            return True

        visited.add(current_id)

        inst = context.scene.state.instances.get(current_id)
        if inst is None:
            return False

        current_id = inst.parent_instance_id

    return False
