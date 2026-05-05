"""Extract a lightweight placement skeleton from scene-template text."""
from __future__ import annotations

import re
from typing import Any, Dict, List, Optional


_ASSET_TYPE_PATTERNS = [
    ("IndustrialRobot", re.compile(r"robot|robotic|robotarm|franka|xarm|机械臂|机器人", re.IGNORECASE)),
    ("Workbench", re.compile(r"workbench|worktable|table|工作台|工位|装配台", re.IGNORECASE)),
    ("Conveyor", re.compile(r"conveyor|belt|传送带|输送", re.IGNORECASE)),
    ("AGV", re.compile(r"\bagv\b|mobile robot|移动", re.IGNORECASE)),
    ("Box", re.compile(r"box|carton|crate|纸箱|箱", re.IGNORECASE)),
    ("Pallet", re.compile(r"pallet|托盘", re.IGNORECASE)),
    ("Rack", re.compile(r"rack|shelving|货架", re.IGNORECASE)),
    ("Forklift", re.compile(r"forklift|叉车", re.IGNORECASE)),
    ("Part", re.compile(r"part|parts|零件|工件", re.IGNORECASE)),
]

_DETAIL_HEADER_RE = re.compile(r"^###\s+['`\"]?(?P<path>/[^\n'`\"]+)['`\"]?", re.MULTILINE)
_TREE_LINE_RE = re.compile(r"^\s*\*\s+(?P<name>[A-Za-z0-9_./-]+)\s+\((?:Xform|Prim)\)", re.MULTILINE)
_PRIM_PATH_RE = re.compile(r"Prim路径 \(Prim Path\):\**\s*['`\"]?(?P<path>/[^\n'`\"]+)", re.IGNORECASE)
_TRANSLATE_RE = re.compile(r"平移 \(Translate\):\**\s*['`\"]?(?P<vec>\[[^\]]+\]|\([^)]+\)|[^'\n`\"]+)", re.IGNORECASE)
_ROTATE_RE = re.compile(r"旋转 \(Rotate XYZ, Degrees\):\**\s*['`\"]?(?P<vec>\[[^\]]+\]|\([^)]+\)|[^'\n`\"]+)", re.IGNORECASE)
_CENTER_RE = re.compile(r"Center:\**\s*['`\"]?(?P<vec>\[[^\]]+\]|\([^)]+\)|[^'\n`\"]+)", re.IGNORECASE)


def extract_template_instances(
    hits: List[Dict[str, Any]],
    max_instances: int = 32,
) -> List[Dict[str, Any]]:
    """Return ``asset_type + template path + optional pose`` records from template hits."""
    instances: List[Dict[str, Any]] = []
    seen = set()
    for hit in hits:
        text = str(hit.get("content") or hit.get("preview") or "")
        for item in _extract_from_detail_blocks(text, hit):
            key = (item["template_path"], item["asset_type"])
            if key in seen:
                continue
            instances.append(item)
            seen.add(key)
            if len(instances) >= max_instances:
                return instances
        for item in _extract_from_tree_lines(text, hit):
            key = (item["template_path"], item["asset_type"])
            if key in seen:
                continue
            instances.append(item)
            seen.add(key)
            if len(instances) >= max_instances:
                return instances
    return instances


def _extract_from_detail_blocks(text: str, hit: Dict[str, Any]) -> List[Dict[str, Any]]:
    matches = list(_DETAIL_HEADER_RE.finditer(text))
    items: List[Dict[str, Any]] = []
    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        block = text[start:end]
        path = _find_path(block) or match.group("path").strip()
        asset_type = infer_asset_type(path + "\n" + block)
        if asset_type is None:
            continue
        position = _find_vec3(_TRANSLATE_RE, block) or _find_vec3(_CENTER_RE, block)
        rotation = _find_vec3(_ROTATE_RE, block)
        items.append(_make_item(hit, path, asset_type, position, rotation))
    return items


def _extract_from_tree_lines(text: str, hit: Dict[str, Any]) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    for match in _TREE_LINE_RE.finditer(text):
        name = match.group("name")
        if name.lower() in {"world", "materials", "meshes", "looks", "environment", "factory"}:
            continue
        asset_type = infer_asset_type(name)
        if asset_type is None:
            continue
        path = name if name.startswith("/") else f"/World/{name}"
        items.append(_make_item(hit, path, asset_type, None, None))
    return items


def infer_asset_type(text: str) -> Optional[str]:
    for asset_type, pattern in _ASSET_TYPE_PATTERNS:
        if pattern.search(text):
            return asset_type
    return None


def _make_item(
    hit: Dict[str, Any],
    path: str,
    asset_type: str,
    position: Optional[List[float]],
    rotation_xyz: Optional[List[float]],
) -> Dict[str, Any]:
    name = path.rstrip("/").split("/")[-1] or path
    item = {
        "template_doc_id": hit.get("doc_id"),
        "scene_id": hit.get("scene_id"),
        "template_path": path,
        "template_name": name,
        "asset_type": asset_type,
        "position": position,
        "rotation_deg": rotation_xyz[2] if rotation_xyz else 0.0,
    }
    return item


def _find_path(block: str) -> Optional[str]:
    match = _PRIM_PATH_RE.search(block)
    return match.group("path").strip() if match else None


def _find_vec3(pattern: re.Pattern, text: str) -> Optional[List[float]]:
    match = pattern.search(text)
    if not match:
        return None
    nums = re.findall(r"[-+]?(?:\d*\.\d+|\d+)(?:[eE][-+]?\d+)?", match.group("vec"))
    if len(nums) < 3:
        return None
    return [float(nums[0]), float(nums[1]), float(nums[2])]
