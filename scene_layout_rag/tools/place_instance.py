"""Place a new asset instance into the scene."""
from __future__ import annotations

from typing import Any, Dict

from .base import BaseTool, ToolResult


class PlaceInstanceTool(BaseTool):
    name = "place_instance"
    description = "在场景中放置一个新的资产实例"

    parameters_schema = {
        "asset_id": {
            "type": "str",
            "required": True,
            "description": "资产类别 ID，如 'Conveyor'",
        },
        "usd_path": {
            "type": "str",
            "required": True,
            "description": "USD 模型文件路径",
        },
        "position": {
            "type": "list[float]",
            "required": True,
            "description": "世界坐标 [x, y, z]，单位米",
        },
        "rotation": {
            "type": "list[float]",
            "required": False,
            "description": "欧拉角 [rx, ry, rz]，单位度，默认 [0,0,0]",
        },
        "bbox": {
            "type": "list[float]",
            "required": False,
            "description": "包围盒 [宽, 长, 高]，单位米",
        },
        "description": {
            "type": "str",
            "required": False,
            "description": "语义描述（外观/用途）",
        },
    }

    def execute(self, params: Dict[str, Any], **ctx: Any) -> ToolResult:
        scene = ctx.get("scene")
        if scene is None:
            return ToolResult(ok=False, error="scene 未提供")

        asset_id = params.get("asset_id", "")
        usd_path = params.get("usd_path", "")
        position = params.get("position")
        if not asset_id or position is None:
            return ToolResult(ok=False, error="asset_id 和 position 为必填参数")

        position = tuple(float(v) for v in position)
        rotation = tuple(float(v) for v in params.get("rotation", [0, 0, 0]))
        raw_bbox = params.get("bbox")
        if raw_bbox and isinstance(raw_bbox, (list, tuple)) and len(raw_bbox) == 3:
            bbox = tuple(float(v) for v in raw_bbox)
        elif isinstance(raw_bbox, dict) and "size" in raw_bbox:
            bbox = tuple(float(v) for v in raw_bbox["size"])
        else:
            bbox = (1.0, 1.0, 1.0)
        description = params.get("description", "")

        from ..scene_state import AssetInstance
        instance_id = scene.generate_instance_id(asset_id)
        instance = AssetInstance(
            instance_id=instance_id,
            asset_id=asset_id,
            usd_path=usd_path,
            position=position,
            rotation=rotation,
            bbox=bbox,
            description=description,
        )
        scene.add_asset(instance)

        return ToolResult(ok=True, result={
            "instance_id": instance_id,
            "position": list(position),
            "bbox": list(bbox),
        })
