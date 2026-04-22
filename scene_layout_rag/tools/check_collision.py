"""AABB collision detection tool."""
from __future__ import annotations

from typing import Any, Dict

from .base import BaseTool, ToolResult


def _aabb_overlap(pos_a: tuple, bbox_a: tuple, pos_b: tuple, bbox_b: tuple) -> float:
    """Compute overlap volume between two axis-aligned bounding boxes.

    Each box is centred at *pos* with half-extents *bbox/2*.
    Returns 0.0 if the boxes do not overlap.
    """
    overlap = 1.0
    for i in range(3):
        a_min = pos_a[i] - bbox_a[i] / 2.0
        a_max = pos_a[i] + bbox_a[i] / 2.0
        b_min = pos_b[i] - bbox_b[i] / 2.0
        b_max = pos_b[i] + bbox_b[i] / 2.0
        lo = max(a_min, b_min)
        hi = min(a_max, b_max)
        if lo >= hi:
            return 0.0
        overlap *= hi - lo
    return overlap


class CheckCollisionTool(BaseTool):
    name = "check_collision"
    description = "检测场景中的碰撞（AABB 包围盒检测）"

    parameters_schema = {
        "instance_id": {
            "type": "str",
            "required": False,
            "description": "检查特定资产的碰撞；省略则检查全部",
        },
    }

    @property
    def modifies_scene(self) -> bool:
        return False

    def execute(self, params: Dict[str, Any], **ctx: Any) -> ToolResult:
        scene = ctx.get("scene")
        if scene is None:
            return ToolResult(ok=False, error="scene 未提供")

        target_id = params.get("instance_id")
        assets = list(scene.assets.values())
        collisions = []

        for i, a in enumerate(assets):
            if target_id and a.instance_id != target_id:
                continue
            for b in assets[i + 1:] if not target_id else assets:
                if a.instance_id == b.instance_id:
                    continue
                vol = _aabb_overlap(a.position, a.bbox, b.position, b.bbox)
                if vol > 0:
                    collisions.append({
                        "a": a.instance_id,
                        "b": b.instance_id,
                        "overlap_volume": round(vol, 4),
                    })

        return ToolResult(ok=True, result={
            "collision_count": len(collisions),
            "collisions": collisions,
        })
