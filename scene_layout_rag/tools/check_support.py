"""Check support relationships for an asset."""
from __future__ import annotations

from typing import Any, Dict, List

from .base import BaseTool, ToolResult


def _xy_overlap_ratio(child_pos, child_bbox, parent_pos, parent_bbox) -> float:
    """Return the fraction of the child's bottom area that overlaps the parent's top area."""
    c_xmin = child_pos[0] - child_bbox[0] / 2.0
    c_xmax = child_pos[0] + child_bbox[0] / 2.0
    c_ymin = child_pos[1] - child_bbox[1] / 2.0
    c_ymax = child_pos[1] + child_bbox[1] / 2.0

    p_xmin = parent_pos[0] - parent_bbox[0] / 2.0
    p_xmax = parent_pos[0] + parent_bbox[0] / 2.0
    p_ymin = parent_pos[1] - parent_bbox[1] / 2.0
    p_ymax = parent_pos[1] + parent_bbox[1] / 2.0

    ox = max(0.0, min(c_xmax, p_xmax) - max(c_xmin, p_xmin))
    oy = max(0.0, min(c_ymax, p_ymax) - max(c_ymin, p_ymin))
    child_area = child_bbox[0] * child_bbox[1]
    if child_area <= 0:
        return 0.0
    return (ox * oy) / child_area


def find_support_candidates(instance_id: str, scene: Any) -> List[Dict[str, Any]]:
    """Find assets that could geometrically support *instance_id*."""
    child = scene.get_asset(instance_id)
    if child is None:
        return []

    child_bottom_z = child.position[2] - child.bbox[2] / 2.0
    candidates = []

    for a in scene.assets.values():
        if a.instance_id == instance_id:
            continue
        parent_top_z = a.position[2] + a.bbox[2] / 2.0
        z_gap = abs(child_bottom_z - parent_top_z)
        if z_gap > 0.2:
            continue
        ratio = _xy_overlap_ratio(child.position, child.bbox, a.position, a.bbox)
        if ratio > 0.05:
            candidates.append({
                "instance_id": a.instance_id,
                "asset_id": a.asset_id,
                "top_z": round(parent_top_z, 3),
                "z_gap": round(z_gap, 3),
                "xy_overlap_ratio": round(ratio, 3),
            })

    candidates.sort(key=lambda c: (-c["xy_overlap_ratio"], c["z_gap"]))
    return candidates


class CheckSupportTool(BaseTool):
    name = "check_support"
    description = "检查一个资产的支撑关系（哪些物体可以支撑它）"

    parameters_schema = {
        "instance_id": {
            "type": "str",
            "required": True,
            "description": "要检查支撑关系的资产实例 ID",
        },
    }

    @property
    def modifies_scene(self) -> bool:
        return False

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

        candidates = find_support_candidates(instance_id, scene)
        current_parent = asset.support_parent

        return ToolResult(ok=True, result={
            "instance_id": instance_id,
            "current_parent": current_parent,
            "candidates": candidates,
        })
