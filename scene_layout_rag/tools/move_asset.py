"""Move an existing asset to a new position."""
from __future__ import annotations

from typing import Any, Dict

from .base import BaseTool, ToolResult


class MoveAssetTool(BaseTool):
    name = "move_asset"
    description = "移动已有资产到新位置（也可用于调整Z轴高度）"

    parameters_schema = {
        "instance_id": {
            "type": "str",
            "required": True,
            "description": "资产实例 ID，如 'Conveyor_1'",
        },
        "new_position": {
            "type": "list[float]",
            "required": True,
            "description": "新的世界坐标 [x, y, z]，单位米",
        },
    }

    def execute(self, params: Dict[str, Any], **ctx: Any) -> ToolResult:
        scene = ctx.get("scene")
        if scene is None:
            return ToolResult(ok=False, error="scene 未提供")

        instance_id = params.get("instance_id", "")
        new_position = params.get("new_position")
        if not instance_id or new_position is None:
            return ToolResult(ok=False, error="instance_id 和 new_position 为必填参数")

        asset = scene.get_asset(instance_id)
        if asset is None:
            return ToolResult(ok=False, error=f"未找到资产: {instance_id}")

        old_position = list(asset.position)
        new_pos = tuple(float(v) for v in new_position)
        scene.move_asset(instance_id, new_pos)

        return ToolResult(ok=True, result={
            "instance_id": instance_id,
            "old_position": old_position,
            "new_position": list(new_pos),
        })
