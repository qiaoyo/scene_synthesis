"""Load structured asset metadata into normalized documents."""
from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

from .config import ProjectConfig
from .data_models import AssetDocument
from .text_splitter import chunk_text, chunk_by_paragraph


def _hash_text(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:16]


def _normalize_header(value: str) -> str:
    """Normalize CSV headers so BOM/case/spacing differences do not matter."""
    value = value.lstrip("\ufeff").strip().lower()
    return re.sub(r"[^a-z0-9]+", "_", value).strip("_")


def _get_field(row: Dict[str, str], *names: str) -> str:
    for name in names:
        value = row.get(_normalize_header(name), "")
        if value:
            return value.strip()
    return ""


def _parse_vector(raw: Optional[str]) -> Optional[List[float]]:
    if raw is None:
        return None
    value = raw.strip()
    if not value:
        return None
    try:
        parsed = json.loads(value)
        if isinstance(parsed, (list, tuple)) and len(parsed) >= 3:
            return [float(parsed[0]), float(parsed[1]), float(parsed[2])]
    except json.JSONDecodeError:
        pass
    numbers = re.findall(r"[-+]?(?:\d*\.\d+|\d+)(?:[eE][-+]?\d+)?", value)
    if len(numbers) >= 3:
        return [float(n) for n in numbers[:3]]
    return None


def _parse_bbox(raw: Optional[str]) -> Optional[dict]:
    if raw is None:
        return None
    value = raw.strip()
    if not value:
        return None
    try:
        parsed = json.loads(value)
        if isinstance(parsed, dict):
            return parsed
        if isinstance(parsed, (list, tuple)) and len(parsed) >= 3:
            return {"size": [float(parsed[0]), float(parsed[1]), float(parsed[2])], "unit": "m"}
    except json.JSONDecodeError:
        pass
    separators = [",", "x", "X", "*"]
    for sep in separators:
        if sep in value:
            try:
                parts = [float(p.strip()) for p in value.split(sep) if p.strip()]
                if len(parts) >= 3:
                    return {"size": parts[:3], "unit": "m"}
            except ValueError:
                continue
    try:
        parts = [float(p.strip()) for p in value.split() if p.strip()]
        if len(parts) >= 3:
            return {"size": parts[:3], "unit": "m"}
    except ValueError:
        return None
    return None


def _build_bbox(min_raw: Optional[str], max_raw: Optional[str], fallback_raw: Optional[str] = None) -> Optional[dict]:
    bbox_min = _parse_vector(min_raw)
    bbox_max = _parse_vector(max_raw)
    if bbox_min and bbox_max:
        size = [round(abs(bbox_max[i] - bbox_min[i]), 6) for i in range(3)]
        center = [round((bbox_max[i] + bbox_min[i]) / 2.0, 6) for i in range(3)]
        return {
            "min": bbox_min,
            "max": bbox_max,
            "size": size,
            "center": center,
            "unit": "m",
        }
    return _parse_bbox(fallback_raw)


def _parse_tags(raw: str) -> Dict[str, str]:
    tags: Dict[str, str] = {}
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key:
                tags[key] = value
        else:
            tags.setdefault("keywords", line)
    return tags


def _format_tags(tags: Dict[str, str], raw: str) -> str:
    if tags:
        return "; ".join(f"{key}={value}" for key, value in tags.items())
    return raw.replace("\n", "; ")


_DEVICE_ALIASES = {
    "agv": "AGV",
    "自动搬运车": "AGV",
    "移动协作机器人": "AGV",
    "mobile robot": "AGV",
    "workbench": "Workbench",
    "工作台": "Workbench",
    "工位": "Workbench",
    "装配台": "Workbench",
    "conveyor": "Conveyor",
    "conveyor belt": "Conveyor",
    "传送带": "Conveyor",
    "输送线": "Conveyor",
    "industrialrobot": "IndustrialRobot",
    "industrial robot": "IndustrialRobot",
    "robotic arm": "IndustrialRobot",
    "机械臂": "IndustrialRobot",
    "工业机械臂": "IndustrialRobot",
    "机器人": "IndustrialRobot",
    "forklift": "Forklift",
    "叉车": "Forklift",
    "rack": "Rack",
    "货架": "Rack",
    "box": "Box",
    "carton": "Box",
    "cartons": "Box",
    "crate": "Box",
    "纸箱": "Box",
    "箱体": "Box",
    "箱体货物": "Box",
    "木箱": "Box",
    "塑料筐": "Box",
    "pallet": "Pallet",
    "托盘": "Pallet",
    "part": "Part",
    "parts": "Part",
    "零件": "Part",
    "工件": "Part",
}


def _map_device_to_asset_type(device: str) -> Optional[str]:
    normalized = re.sub(r"\s+", " ", device.strip().lower())
    if not normalized:
        return None
    if normalized in _DEVICE_ALIASES:
        return _DEVICE_ALIASES[normalized]
    for alias, asset_type in _DEVICE_ALIASES.items():
        if alias in normalized:
            return asset_type
    return None


def _map_core_devices(devices: Iterable[str]) -> List[str]:
    mapped: List[str] = []
    seen = set()
    for device in devices:
        asset_type = _map_device_to_asset_type(str(device))
        if asset_type and asset_type not in seen:
            mapped.append(asset_type)
            seen.add(asset_type)
    return mapped


def _infer_language(text: str) -> str:
    return "zh" if re.search(r"[\u4e00-\u9fff]", text) else "en"


def _infer_scene_id_from_name(path: Path) -> str:
    stem = path.stem.lower()
    for scene_id in ["assembly", "warehouse", "sorting", "transport", "palletizing"]:
        if stem.startswith(scene_id):
            return scene_id
    return stem.split("-")[0].split("_")[0]


def _infer_template_detail(path: Path) -> str:
    stem = path.stem.lower()
    if "brief" in stem:
        return "brief"
    if "verbose" in stem:
        return "verbose"
    return "unknown"


def load_csv_documents(csv_path: Path, chunk_size: int, chunk_overlap: int) -> List[AssetDocument]:
    documents: List[AssetDocument] = []
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            return documents
        for idx, row in enumerate(reader):
            normalized_row = {
                _normalize_header(key or ""): (value or "")
                for key, value in row.items()
            }
            asset_category = _get_field(normalized_row, "Assets Type", "Asset Type", "Type") or csv_path.stem
            instanceID = _get_field(normalized_row, "InstanceID", "Instance Id", "InstanceID", "instance_id")
            usd_path = _get_field(normalized_row, "Path", "USD", "USD Path")
            tag_raw = _get_field(normalized_row, "Tag", "Tags")
            description = _get_field(normalized_row, "Description", "Functional Features")
            if not usd_path or usd_path.lower() == "path":
                continue

            tags = _parse_tags(tag_raw)
            bbox = _build_bbox(
                _get_field(normalized_row, "bbox_min_meters", "bbox_min", "bbox min"),
                _get_field(normalized_row, "bbox_max_meters", "bbox_max", "bbox max"),
                _get_field(normalized_row, "bbox", "bbox_meters"),
            )
            bbox_size = bbox.get("size") if bbox else None
            tags_text = _format_tags(tags, tag_raw)
            size_text = "unknown" if not bbox_size else " x ".join(f"{v:.3f}" for v in bbox_size)
            base_text = (
                f"Asset type / 资产类型: {asset_category}\n"
                f"Instance ID: {instanceID}\n"
                f"USD path: {usd_path}\n"
                f"Tags / 标签: {tags_text}\n"
                f"Functional description / 功能描述: {description}\n"
                f"Bounding box size / 包围盒尺寸: {size_text} m"
            )
            doc_id = f"{csv_path.stem}-{idx}-{_hash_text(base_text)}"
            documents.append(
                AssetDocument(
                    doc_id=doc_id,
                    content=base_text,
                    metadata={
                        "doc_type": "asset",
                        "asset_type": asset_category,
                        "asset_category": asset_category,
                        "usd_path": usd_path,
                        "tag_raw": tag_raw,
                        "tags": tags,
                        "description": description,
                        "instance_id": instanceID,
                        "source": str(csv_path),
                        "row_index": idx,
                        "bbox": bbox,
                        "bbox_min": bbox.get("min") if bbox else None,
                        "bbox_max": bbox.get("max") if bbox else None,
                        "bbox_size": bbox.get("size") if bbox else None,
                        "bbox_center": bbox.get("center") if bbox else None,
                    },
                )
            )
    return documents

def load_markdown_documents(md_path: Path, block_size: int = 3) -> List[AssetDocument]:
    text = md_path.read_text(encoding="utf-8")
    chunks = chunk_by_paragraph(text, block_size=block_size)
    documents: List[AssetDocument] = []
    scene_id = _infer_scene_id_from_name(md_path)
    detail = _infer_template_detail(md_path)
    language = _infer_language(text)
    for idx, chunk in enumerate(chunks):
        content = (
            f"Scene template / 场景模板: {scene_id}\n"
            f"Detail level / 细节级别: {detail}\n"
            f"Source file: {md_path.name}\n"
            f"{chunk}"
        )
        doc_id = f"{md_path.stem}-md-{idx}-{_hash_text(content)}"
        documents.append(
            AssetDocument(
                doc_id=doc_id,
                content=content,
                metadata={
                    "doc_type": "scene_template",
                    "scene_id": scene_id,
                    "template_detail": detail,
                    "language": language,
                    "source": str(md_path),
                    "section": idx,
                },
            )
        )
    return documents

def _load_scene_description_records(path: Path) -> List[Dict[str, Any]]:
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return []
    if text.startswith("["):
        data = json.loads(text)
        if not isinstance(data, list):
            raise ValueError(f"{path} must contain a JSON array")
        return [item for item in data if isinstance(item, dict)]

    records: List[Dict[str, Any]] = []
    for line_idx, line in enumerate(text.splitlines()):
        line = line.strip()
        if not line:
            continue
        data = json.loads(line)
        if not isinstance(data, dict):
            raise ValueError(f"{path}:{line_idx + 1} must contain a JSON object")
        records.append(data)
    return records


def load_scene_description_documents(jsonl_path: Path, chunk_size: int, chunk_overlap: int) -> List[AssetDocument]:
    """Load scene prior documents from either JSON array files or JSONL files."""
    documents: List[AssetDocument] = []
    for line_idx, data in enumerate(_load_scene_description_records(jsonl_path)):
        scene_id = str(data.get("scene_id", "")).strip()
        scene_name = str(data.get("scene_name", "")).strip()
        text = str(data.get("text", "")).strip()
        core_devices = data.get("core_devices", [])
        if not isinstance(core_devices, list):
            core_devices = [str(core_devices)]
        core_devices = [str(device).strip() for device in core_devices if str(device).strip()]
        core_asset_types = _map_core_devices(core_devices)
        language = _infer_language(" ".join([scene_name, text, " ".join(core_devices)]))
        core_devices_str = ", ".join(core_devices)
        core_asset_types_str = ", ".join(core_asset_types)
        base_text = (
            f"Scene prior / 场景先验: {scene_id}\n"
            f"Scene name / 场景名称: {scene_name}\n"
            f"Language: {language}\n"
            f"Core devices / 核心设备: {core_devices_str}\n"
            f"Mapped asset types / 映射资产类型: {core_asset_types_str}\n"
            f"Description / 描述: {text}"
        )
        chunks = chunk_text(base_text, chunk_size, chunk_overlap)
        for chunk_idx, chunk in enumerate(chunks):
            doc_id = f"{jsonl_path.stem}-scene-prior-{line_idx}-{chunk_idx}-{_hash_text(chunk)}"
            documents.append(
                AssetDocument(
                    doc_id=doc_id,
                    content=chunk,
                    metadata={
                        "doc_type": "scene_prior",
                        "source": str(jsonl_path),
                        "scene_id": scene_id,
                        "scene_name": scene_name,
                        "language": language,
                        "core_devices": core_devices,
                        "core_asset_types": core_asset_types,
                        "line_index": line_idx,
                    },
                )
            )
    return documents


def load_jsonl_documents(jsonl_path: Path, chunk_size: int, chunk_overlap: int) -> List[AssetDocument]:
    """Backward-compatible alias for scene description loading."""
    return load_scene_description_documents(jsonl_path, chunk_size, chunk_overlap)


class AssetIngestor:
    """Aggregates CSV and markdown documents into a single corpus."""

    def __init__(self, config: ProjectConfig):
        self.config = config

    def build_documents(self) -> List[AssetDocument]:
        print("[AssetIngestor] 开始加载 CSV / Markdown / Docs 资产")
        docs: List[AssetDocument] = []
        # 1. 处理 CSV
        for csv_path in self.config.asset_paths.inventory_csvs:
            print(f"[AssetIngestor] 处理 CSV: {csv_path}")
            docs.extend(load_csv_documents(csv_path, self.config.chunk_size, self.config.chunk_overlap))
        #2. 处理 md
        for md_path in self.config.asset_paths.scene_md_files:
            print(f"[AssetIngestor] 处理 Markdown: {md_path}")
            docs.extend(load_markdown_documents(md_path))
        #3. 处理 docs/*.jsonl 
        for jsonl_path in self.config.asset_paths.documents_files:
            print(f"[AssetIngestor] 处理 JSONL: {jsonl_path}")
            docs.extend(load_scene_description_documents(jsonl_path, self.config.chunk_size, self.config.chunk_overlap))
        #处理extra目录
        if self.config.asset_paths.extra_documents_dir and self.config.asset_paths.extra_documents_dir.exists():
            for text_file in self.config.asset_paths.extra_documents_dir.glob("**/*.txt"):
                print(f"[AssetIngestor] 处理附加文本: {text_file}")
                docs.extend(load_markdown_documents(text_file))
        print(f"[AssetIngestor] 资产加载完毕，共 {len(docs)} 条文档")
        return docs


__all__ = [
    "AssetIngestor",
    "load_csv_documents",
    "load_markdown_documents",
    "load_jsonl_documents",
    "load_scene_description_documents",
]
