"""AABB collision / support / scene-semantics validators.

按用户选择「AABB 默认 + 留 IsaacSim 接入点」实现：
- ``aabb_collisions``: 检查所有未处于支撑关系的实例对是否互相穿透。
- ``check_support_geometry``: 几何上验证 child 是否真的「站」在 parent 上。
- ``analyze_scene_semantics``: 简单走廊/工作区/流水路径分析。
- ``run_static_simulation``: 当前作为 IsaacSim 的占位符，只做静态稳定性检查；
  ``physics/isaac_bridge.py`` 留空接口给后续接入。
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple

from .data_models import Instance, SceneState


# ---------- 基础 AABB 工具 ----------

def aabb_overlap(a_min, a_max, b_min, b_max, tol: float = 1e-4) -> bool:
    for i in range(3):
        if a_max[i] <= b_min[i] + tol:
            return False
        if b_max[i] <= a_min[i] + tol:
            return False
    return True


def aabb_xy_overlap_area(a_min, a_max, b_min, b_max) -> float:
    dx = max(0.0, min(a_max[0], b_max[0]) - max(a_min[0], b_min[0]))
    dy = max(0.0, min(a_max[1], b_max[1]) - max(a_min[1], b_min[1]))
    return dx * dy


def _is_supporting(parent_id: Optional[str], other_id: Optional[str], state: SceneState) -> bool:
    """两实例是否处于直接的父子支撑关系（任意方向）。"""
    if parent_id is None or other_id is None:
        return False
    children_of_parent = state.support_children.get(parent_id, [])
    children_of_other = state.support_children.get(other_id, [])
    if other_id in children_of_parent:
        return True
    if parent_id in children_of_other:
        return True
    return False


# ---------- 碰撞 ----------

def aabb_collisions(state: SceneState) -> List[Dict[str, Any]]:
    """返回所有 AABB 重叠的实例对（去重后）。

    跳过：直接父子支撑关系（child 必然与 parent 顶部接触/嵌入）。
    """
    instances = list(state.instances.values())
    collisions: List[Dict[str, Any]] = []
    for i in range(len(instances)):
        a = instances[i]
        a_min, a_max = a.aabb()
        for j in range(i + 1, len(instances)):
            b = instances[j]
            if _is_supporting(a.instance_id, b.instance_id, state):
                continue
            b_min, b_max = b.aabb()
            if aabb_overlap(a_min, a_max, b_min, b_max):
                collisions.append({
                    "a": a.instance_id,
                    "b": b.instance_id,
                    "a_type": a.asset_type,
                    "b_type": b.asset_type,
                })
    return collisions


# ---------- 支撑关系几何验证 ----------

def check_support_geometry(
    child: Instance,
    parent: Instance,
    z_tolerance: float = 0.05,
    overlap_threshold: float = 0.4,
) -> Dict[str, Any]:
    """检查 child 是否真的能被 parent 支撑。
    判据：
      1) child 底面应贴近 parent 顶面：``|child_min_z - parent_max_z| <= z_tolerance``
      2) XY 投影重叠占 child 底面积比例 >= ``overlap_threshold``
    """
    c_min, c_max = child.aabb()
    p_min, p_max = parent.aabb()
    z_gap = c_min[2] - p_max[2]
    z_aligned = abs(z_gap) <= z_tolerance
    xy_overlap = aabb_xy_overlap_area(c_min, c_max, p_min, p_max)
    child_xy_area = max(1e-9, (c_max[0] - c_min[0]) * (c_max[1] - c_min[1]))
    coverage = xy_overlap / child_xy_area
    inside_parent_xy = coverage >= overlap_threshold
    ok = z_aligned and inside_parent_xy
    issues: List[str] = []
    if not z_aligned:
        issues.append(f"z_gap={z_gap:.3f} 超出阈值 ±{z_tolerance:.3f}")
    if not inside_parent_xy:
        issues.append(f"xy_coverage={coverage:.2f} 低于阈值 {overlap_threshold:.2f}")
    return {
        "ok": ok,
        "z_gap": z_gap,
        "xy_coverage": round(coverage, 3),
        "issues": issues,
    }

def evaluate_support_state(state: SceneState) -> Dict[str, Any]:
    valid: List[Dict[str, Any]] = []
    invalid: List[Dict[str, Any]] = []
    for parent_id, children in state.support_children.items():
        if parent_id not in state.instances:
            continue
        parent = state.instances[parent_id]
        for child_id in children:
            if child_id not in state.instances:
                continue
            child = state.instances[child_id]
            geo = check_support_geometry(child, parent)
            entry = {
                "child": child_id,
                "parent": parent_id,
                **geo,
            }
            (valid if geo["ok"] else invalid).append(entry)
    return {"valid_relations": valid, "invalid_relations": invalid}


# ---------- 场景语义 ----------

_FLOW_TYPE_KEYWORDS = {
    "Conveyor": "conveyor",
    "AGV": "agv",
    "Forklift": "forklift",
}

_WORK_ZONE_ANCHOR_TYPES = {"Workbench", "IndustrialRobot"}


def analyze_scene_semantics(state: SceneState, corridor_width_min: float = 1.5) -> Dict[str, Any]:
    """从当前布局抽取走廊 / 工作区 / 流水路径等高层结构。

    设计取舍：当前用规则启发式（XY 投影 + 类型聚类）。后续可替换为 LLM
    语义识别，见 ``observer.Observer`` 注释。
    """
    instances = list(state.instances.values())

    # 工作区：以 Workbench/IndustrialRobot 为锚点，吸纳半径 2.5m 内的资产
    work_zones: List[Dict[str, Any]] = []
    used: set = set()
    for anchor in instances:
        if anchor.asset_type not in _WORK_ZONE_ANCHOR_TYPES:
            continue
        if anchor.instance_id in used:
            continue
        nearby = [anchor.instance_id]
        used.add(anchor.instance_id)
        for other in instances:
            if other.instance_id in used or other.instance_id == anchor.instance_id:
                continue
            if _planar_distance(anchor, other) <= 2.5:
                nearby.append(other.instance_id)
                used.add(other.instance_id)
        work_zones.append({
            "anchor": anchor.instance_id,
            "anchor_type": anchor.asset_type,
            "center": anchor.position[:2],
            "assets": nearby,
        })

    # 流水路径：所有 Conveyor/AGV/Forklift 视为节点；同类型相邻聚合
    flow_paths: List[Dict[str, Any]] = []
    for asset_type, label in _FLOW_TYPE_KEYWORDS.items():
        members = [inst.instance_id for inst in instances if inst.asset_type == asset_type]
        if not members:
            continue
        flow_paths.append({
            "type": label,
            "members": members,
            "connected": _flow_connectivity(members, state) if asset_type == "Conveyor" else None,
        })

    # 走廊：极简版——成对资产之间未被占据的 XY 间隙。仅给 LLM 做提示，不作硬约束。
    corridors: List[Dict[str, Any]] = []
    for i in range(len(instances)):
        for j in range(i + 1, len(instances)):
            a = instances[i]
            b = instances[j]
            gap = _xy_gap(a, b)
            if gap is None:
                continue
            width, axis = gap
            if width >= corridor_width_min:
                blocked = _corridor_blocked(a, b, instances)
                corridors.append({
                    "from": a.instance_id,
                    "to": b.instance_id,
                    "width": round(width, 3),
                    "axis": axis,
                    "blocked": blocked,
                })

    return {
        "corridors": corridors,
        "work_zones": work_zones,
        "flow_paths": flow_paths,
    }


def _planar_distance(a: Instance, b: Instance) -> float:
    dx = a.position[0] - b.position[0]
    dy = a.position[1] - b.position[1]
    return (dx * dx + dy * dy) ** 0.5


def _flow_connectivity(member_ids: List[str], state: SceneState) -> bool:
    """简单连通判定：相邻两条传送带 XY 距离 <= 自身长边的 1.5 倍即视为连通。"""
    if len(member_ids) <= 1:
        return True
    members = [state.instances[mid] for mid in member_ids]
    for i in range(len(members) - 1):
        a = members[i]
        b = members[i + 1]
        max_extent = max(a.bbox_size[0], a.bbox_size[1], b.bbox_size[0], b.bbox_size[1])
        if _planar_distance(a, b) > max_extent * 1.5:
            return False
    return True


def _xy_gap(a: Instance, b: Instance) -> Optional[Tuple[float, str]]:
    a_min, a_max = a.aabb()
    b_min, b_max = b.aabb()
    if a_max[0] < b_min[0]:
        return (b_min[0] - a_max[0], "x")
    if b_max[0] < a_min[0]:
        return (a_min[0] - b_max[0], "x")
    if a_max[1] < b_min[1]:
        return (b_min[1] - a_max[1], "y")
    if b_max[1] < a_min[1]:
        return (a_min[1] - b_max[1], "y")
    return None


def _corridor_blocked(a: Instance, b: Instance, instances: List[Instance]) -> bool:
    """简化判定：a/b 中点是否被任何第三方 AABB 包含。"""
    midx = (a.position[0] + b.position[0]) / 2.0
    midy = (a.position[1] + b.position[1]) / 2.0
    for other in instances:
        if other.instance_id in (a.instance_id, b.instance_id):
            continue
        o_min, o_max = other.aabb()
        if o_min[0] <= midx <= o_max[0] and o_min[1] <= midy <= o_max[1]:
            return True
    return False


# ---------- 静态「物理」反馈（IsaacSim 占位符） ----------

def run_static_simulation(state: SceneState) -> Dict[str, Any]:
    """用静态稳定性近似 ``simulate_step``。

    注意：真正的 IsaacSim 接入点在 ``physics/isaac_bridge.py``。这里的反馈
    用于在没有 GPU/Isaac 时保持 ReAct 闭环不空转。
    """
    warnings: List[str] = []
    contacts: List[Dict[str, Any]] = []
    fallen: List[str] = []

    # 1) 已声明支撑关系的几何检查
    support_eval = evaluate_support_state(state)
    for bad in support_eval["invalid_relations"]:
        warnings.append(
            f"{bad['child']} 不能稳定支撑在 {bad['parent']} 上："
            + "; ".join(bad["issues"])
        )
        fallen.append(bad["child"])

    # 2) 未声明 parent 但底面悬空（z_min 远大于 0 且没有 parent）的实例
    for inst in state.instances.values():
        if inst.parent_instance_id is not None:
            continue
        z_min = inst.position[2] - inst.bbox_size[2] / 2.0
        if z_min > 0.05:
            warnings.append(f"{inst.instance_id} 底面悬空 (z_min={z_min:.3f})")
            fallen.append(inst.instance_id)

    # 3) 父子接触点
    for parent_id, children in state.support_children.items():
        if parent_id not in state.instances:
            continue
        for child_id in children:
            if child_id not in state.instances:
                continue
            contacts.append({"child": child_id, "parent": parent_id, "type": "support"})

    return {
        "stable": len(fallen) == 0,
        "fallen_assets": list(dict.fromkeys(fallen)),
        "contacts": contacts,
        "warnings": warnings,
    }


__all__ = [
    "aabb_overlap",
    "aabb_collisions",
    "check_support_geometry",
    "evaluate_support_state",
    "analyze_scene_semantics",
    "run_static_simulation",
]
