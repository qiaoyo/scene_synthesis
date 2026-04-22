"""Delete an asset instance from the scene."""
from __future__ import annotations

from typing import Any, Dict

from .base import BaseTool, ToolResult


class DeleteAssetTool(BaseTool):
    name = "delete_asset"
    description = "从场景中删除一个资产实例"

    parameters_schema = {
        "instance_id": {
            "type": "str",
            "required": True,
            "description": "要删除的资产实例 ID，如 'Conveyor_1'",
        },
    }

    def execute(self, params: Dict[str, Any], **ctx: Any) -> ToolResult:
        scene = ctx.get("scene")
        if scene is None:
            return ToolResult(ok=False, error="scene 未提供")

        instance_id = params.get("instance_id", "")
        if not instance_id:
            return ToolResult(ok=False, error="instance_id 为必填参数")

        asset = scene.get_asset(instance_id)
        if asset is None:
            return ToolResult(ok=False, error=f"未找到资产: {instance_id}")

        removed = scene.remove_asset(instance_id)
        return ToolResult(ok=True, result={
            "deleted_id": removed.instance_id,
            "asset_id": removed.asset_id,
            "position": list(removed.position),
        })
