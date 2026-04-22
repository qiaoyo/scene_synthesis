"""Query the current scene state."""
from __future__ import annotations

from typing import Any, Dict

from .base import BaseTool, ToolResult


class QuerySceneTool(BaseTool):
    name = "query_scene"
    description = "查询当前场景状态，获取资产列表、统计信息或单个资产详情"

    parameters_schema = {
        "instance_id": {
            "type": "str",
            "required": False,
            "description": "查询特定资产的详情，如 'Conveyor_1'",
        },
        "asset_type": {
            "type": "str",
            "required": False,
            "description": "按类型过滤资产列表，如 'Conveyor'",
        },
        "summary": {
            "type": "bool",
            "required": False,
            "description": "设为 true 返回统计摘要而非完整列表",
        },
    }

    @property
    def modifies_scene(self) -> bool:
        return False

    def execute(self, params: Dict[str, Any], **ctx: Any) -> ToolResult:
        scene = ctx.get("scene")
        if scene is None:
            return ToolResult(ok=False, error="scene 未提供")

        instance_id = params.get("instance_id")
        asset_type = params.get("asset_type")
        summary = params.get("summary", False)

        # Single asset query
        if instance_id:
            asset = scene.get_asset(instance_id)
            if asset is None:
                return ToolResult(ok=False, error=f"未找到资产: {instance_id}")
            return ToolResult(ok=True, result={
                "instance_id": asset.instance_id,
                "asset_id": asset.asset_id,
                "usd_path": asset.usd_path,
                "position": list(asset.position),
                "rotation": list(asset.rotation),
                "bbox": list(asset.bbox),
                "description": asset.description,
                "support_parent": asset.support_parent,
                "support_children": asset.support_children,
            })

        # List / filter
        assets = scene.list_assets(asset_type=asset_type)

        if summary:
            type_counts: Dict[str, int] = {}
            for a in assets:
                type_counts[a.asset_id] = type_counts.get(a.asset_id, 0) + 1
            return ToolResult(ok=True, result={
                "total_assets": len(assets),
                "bounds": list(scene.bounds),
                "type_counts": type_counts,
            })

        return ToolResult(ok=True, result={
            "total_assets": len(assets),
            "assets": [
                {
                    "instance_id": a.instance_id,
                    "asset_id": a.asset_id,
                    "position": list(a.position),
                    "bbox": list(a.bbox),
                }
                for a in assets
            ],
        })
