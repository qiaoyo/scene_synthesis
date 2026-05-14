from __future__ import annotations
from typing import Any, Dict, List
from .base import Tool, ToolContext, ToolResult, register_tool

@register_tool
class QuerySceneTool(Tool):
    schema = {
        "type": "function",
        "function": {
            "name": "query_scene",
            "description": "Return the precise current scene state for reasoning and planning, including instance transforms, bounding boxes, support relations, and semantic metadata.",
            "parameters": {
                "type": "object",
                "properties": {
                    "instance_id": {
                        "type": "string",
                        "description": (
                            "If specified, return only this instance."
                        ),
                    },
                    "asset_type": {
                        "type": "string",
                        "description": (
                            "If specified, return only instances of this asset type."
                        ),
                    },
                },
                "additionalProperties": False,
            },
        },
    }
    def run(self, context: ToolContext, instance_id: str | None = None, asset_type: str | None = None,) -> ToolResult:
        instances: List[Dict[str, Any]] = []
        for inst in context.scene.state.instances.values():
            if instance_id and inst.instance_id != instance_id:
                continue
            if asset_type and inst.asset_type != asset_type:
                continue
            bbox_min, bbox_max = inst.aabb()
            instances.append({
                "instance_id": inst.instance_id,
                "asset_type": inst.asset_type,
                "asset_doc_id": inst.asset_doc_id,
                "position": inst.position,
                "rotation_deg": inst.rotation_deg,
                "bbox_size": inst.bbox_size,
                "bbox_min": bbox_min,
                "bbox_max": bbox_max,
                "parent_instance_id": inst.parent_instance_id,
            })
        if instance_id and not instances:
            return ToolResult(ok=False, error=f"未找到实例: {instance_id}")
        return ToolResult(ok=True, data={
            "instances": instances,
            "support_children": dict(context.scene.state.support_children),
            "instance_count": len(context.scene.state.instances),
        })
