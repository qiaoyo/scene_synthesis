"""Set a support relationship between two assets -- with optional LLM decision."""
from __future__ import annotations

import json
from typing import Any, Dict, List

from .base import BaseTool, ToolResult
from .check_support import _xy_overlap_ratio, find_support_candidates


_MIN_OVERLAP = 0.3
_MAX_Z_GAP = 0.1


def _validate_support(child_id: str, parent_id: str, scene: Any) -> Dict[str, Any]:
    """Geometric validation of a support relationship."""
    child = scene.get_asset(child_id)
    parent = scene.get_asset(parent_id)
    if child is None or parent is None:
        return {"ok": False, "reason": "资产不存在", "issues": ["资产不存在"]}

    child_bottom_z = child.position[2] - child.bbox[2] / 2.0
    parent_top_z = parent.position[2] + parent.bbox[2] / 2.0
    z_gap = abs(child_bottom_z - parent_top_z)

    ratio = _xy_overlap_ratio(child.position, child.bbox, parent.position, parent.bbox)

    issues: List[str] = []
    if z_gap > _MAX_Z_GAP:
        issues.append(f"Z 高度差 {z_gap:.3f}m 超过阈值 {_MAX_Z_GAP}m")
    if ratio < _MIN_OVERLAP:
        issues.append(f"XY 重叠率 {ratio:.1%} 低于阈值 {_MIN_OVERLAP:.0%}")

    return {
        "ok": len(issues) == 0,
        "z_gap": round(z_gap, 3),
        "xy_overlap_ratio": round(ratio, 3),
        "issues": issues,
    }


def _llm_decide_support(
    child_id: str,
    candidates: List[Dict[str, Any]],
    scene: Any,
    llm: Any,
) -> Dict[str, Any]:
    """Use the LLM to pick the best support parent from candidates."""
    from ..prompts.templates import format_support_prompt

    child = scene.get_asset(child_id)
    prompt = format_support_prompt(
        child_id=child_id,
        child_type=child.asset_id,
        child_position=list(child.position),
        child_bbox=list(child.bbox),
        candidates=candidates,
        context=scene.to_dict(),
    )
    system = "你是一名物理支撑关系专家，帮助选择最合适的支撑父物体。"
    raw = llm.react_call(system, prompt)

    # Parse LLM response
    try:
        import re
        json_match = re.search(r"```json\s*(\{[\s\S]*?\})\s*```", raw)
        if json_match:
            return json.loads(json_match.group(1))
        data = json.loads(raw.strip())
        if isinstance(data, dict):
            return data
    except (json.JSONDecodeError, AttributeError):
        pass

    # Fallback: pick the first candidate
    if candidates:
        return {"parent_id": candidates[0]["instance_id"], "confidence": 0.5, "reason": "几何最优"}
    return {}


class SetSupportTool(BaseTool):
    name = "set_support"
    description = "设置两个资产之间的支撑关系（子物体放在父物体上），支持 LLM 自动选择最佳父物体"

    parameters_schema = {
        "child_id": {
            "type": "str",
            "required": True,
            "description": "子物体实例 ID（被支撑的物体）",
        },
        "parent_id": {
            "type": "str",
            "required": False,
            "description": "父物体实例 ID；省略时由 LLM 或几何规则自动选择",
        },
    }

    def execute(self, params: Dict[str, Any], **ctx: Any) -> ToolResult:
        scene = ctx.get("scene")
        if scene is None:
            return ToolResult(ok=False, error="scene 未提供")

        child_id = params.get("child_id", "")
        if not child_id:
            return ToolResult(ok=False, error="child_id 为必填参数")

        parent_id = params.get("parent_id", "")
        llm = ctx.get("llm")

        # If no parent specified, auto-select
        if not parent_id:
            candidates = find_support_candidates(child_id, scene)
            if not candidates:
                return ToolResult(ok=False, error=f"{child_id} 附近没有找到可支撑的物体")

            if llm is not None:
                # LLM decision with retry
                decision = _llm_decide_support(child_id, candidates, scene, llm)
                parent_id = decision.get("parent_id", "")
                if not parent_id:
                    parent_id = candidates[0]["instance_id"]
            else:
                # Pure geometric: pick best candidate
                parent_id = candidates[0]["instance_id"]

        # Validate geometry
        validation = _validate_support(child_id, parent_id, scene)

        # If invalid and LLM available, retry once with feedback
        if not validation["ok"] and llm is not None:
            candidates = find_support_candidates(child_id, scene)
            # Filter out the failed parent
            candidates = [c for c in candidates if c["instance_id"] != parent_id]
            if candidates:
                decision = _llm_decide_support(child_id, candidates, scene, llm)
                retry_parent = decision.get("parent_id", candidates[0]["instance_id"])
                retry_validation = _validate_support(child_id, retry_parent, scene)
                if retry_validation["ok"]:
                    parent_id = retry_parent
                    validation = retry_validation

        if not validation["ok"]:
            return ToolResult(ok=False, error="; ".join(validation["issues"]))

        scene.set_support(child_id, parent_id)
        return ToolResult(ok=True, result={
            "child_id": child_id,
            "parent_id": parent_id,
            "z_gap": validation["z_gap"],
            "xy_overlap_ratio": validation["xy_overlap_ratio"],
        })
