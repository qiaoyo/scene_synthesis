"""Load structured asset metadata into normalized documents."""
from __future__ import annotations

import csv
import hashlib
import json
import math
import re
from pathlib import Path
from typing import Iterable, List, Optional

from .config import ProjectConfig
from .data_models import AssetDocument
from .text_splitter import chunk_text, chunk_by_paragraph


def _hash_text(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:16]


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


_XFORM_HEADER_RE = re.compile(r"^###\s*'([^']+)'\s*\(([^)]+)\)\s*$", re.MULTILINE)
_BBOX_WORLD_RE = re.compile(
    r"^\*\s*BBox\s*\(world\):\s*size=\(([^)]+)\)\s*,\s*center=\(([^)]+)\)\s*$",
    re.MULTILINE,
)
_PAYLOAD_RE = re.compile(r"^\*\s*引用:\s*payload:(.+)\s*$", re.MULTILINE)
_SCALE_RE = re.compile(r"Scale\s*:\s*([0-9.]+)", re.IGNORECASE)


def _parse_scale(tag: str | None) -> float | None:
    if not tag:
        return None
    m = _SCALE_RE.search(tag)
    if not m:
        return None
    try:
        return float(m.group(1))
    except ValueError:
        return None


def _parse_triplet(text: str) -> Optional[tuple[float, float, float]]:
    parts = [p.strip() for p in text.split(",")]
    if len(parts) < 3:
        return None
    try:
        return float(parts[0]), float(parts[1]), float(parts[2])
    except Exception:
        return None


def _valid_vec3(v: tuple[float, float, float], abs_max: float = 1e7) -> bool:
    return all(math.isfinite(x) and abs(x) <= abs_max for x in v)


def _extract_scene_meta(text: str) -> dict:
    """Best-effort extraction of global scene metadata from the md header."""
    meta: dict = {}
    m = re.search(r"\*\s+\*\*USDA文件路径.*?\*\*`([^`]+)`", text)
    if m:
        meta["usda_path"] = m.group(1).strip()
    m = re.search(r"\*\s+\*\*默认Prim.*?\*\*'([^']+)'", text)
    if m:
        meta["default_prim"] = m.group(1).strip()
    m = re.search(r"米\(Meters Per Unit\).*?\*\*([0-9.]+)", text)
    if m:
        meta["meters_per_unit"] = m.group(1).strip()
    m = re.search(r"\*\*\s*Up Axis\s*\*\*:\s*([XYZ])", text)
    if m:
        meta["up_axis"] = m.group(1).strip()
    return meta


def _parse_referenced_xforms(text: str) -> List[dict]:
    """Parse 'Referenced Xforms' blocks that include payload + world bbox/center.

    We use these as scene anchors/constraints for the planner.
    """
    section_idx = text.find("## 3. 外部引用Xform简报")
    if section_idx == -1:
        section_idx = text.find("## 3.")
    if section_idx == -1:
        return []
    section = text[section_idx:]
    matches = list(_XFORM_HEADER_RE.finditer(section))
    if not matches:
        return []

    results: List[dict] = []
    for i, m in enumerate(matches):
        prim_path = m.group(1).strip()
        xform_type = m.group(2).strip()
        block_start = m.end()
        block_end = matches[i + 1].start() if i + 1 < len(matches) else len(section)
        block = section[block_start:block_end]

        payload = ""
        pm = _PAYLOAD_RE.search(block)
        if pm:
            payload = pm.group(1).strip()

        size: Optional[tuple[float, float, float]] = None
        center: Optional[tuple[float, float, float]] = None
        bm = _BBOX_WORLD_RE.search(block)
        if bm:
            size = _parse_triplet(bm.group(1))
            center = _parse_triplet(bm.group(2))

        if size is None or center is None:
            continue
        # Some source exports contain absurd sentinel bbox values; drop them.
        if not (_valid_vec3(size) and _valid_vec3(center)):
            continue

        results.append(
            {
                "prim_path": prim_path,
                "xform_type": xform_type,
                "payload": payload,
                "bbox_world": {"size": [size[0], size[1], size[2]], "center": [center[0], center[1], center[2]], "unit": "m"},
            }
        )
    return results


def load_csv_documents(csv_path: Path, chunk_size: int, chunk_overlap: int) -> List[AssetDocument]:
    documents: List[AssetDocument] = []
    with csv_path.open("r", encoding="utf-8") as f:
        # 过滤空白物理行
        reader = csv.reader(line for line in f if line.strip())
        # 跳过首行（表头）
        next(reader, None)
        content_idx = 0  # 仅统计有效数据行
        for raw_idx, row in enumerate(reader,start=2):
            # 跳过空行或无效行（列数不足或整行都为空白）
            if len(row) < 4 or not any(c.strip() for c in row):
                continue
            
            asset_category = row[0].strip() or csv_path.stem
            usd_path = row[1].strip()
            short_desc = row[2].strip()
            long_desc = row[3].strip()
            scale = _parse_scale(short_desc)
            base_text = f"类型:{asset_category}\nUSD:{usd_path}\n{short_desc}\n{long_desc}"
            chunks = chunk_text(base_text, chunk_size, chunk_overlap)
            bbox = _parse_bbox(row[4]) if len(row) >= 5 else None
            for chunk_idx, chunk in enumerate(chunks):
                doc_id = f"{csv_path.stem}-{content_idx}-{chunk_idx}-{_hash_text(chunk)}"
                documents.append(
                    AssetDocument(
                        doc_id=doc_id,
                        content=chunk,
                        metadata={
                            "asset_category": asset_category,
                            "usd_path": usd_path,
                            "scale": scale,
                            "source": str(csv_path),
                            "row_index": content_idx,   # 连续有效行号
                            "raw_row_index": raw_idx,   # 原始文件行号（含跳过的行）
                            "bbox": bbox,
                            "doc_type": "csv",          #标记为资产文档
                        },
                    )
                )
            content_idx += 1
    return documents


def load_markdown_documents(md_path: Path, block_size: int = 3) -> List[AssetDocument]:
    text = md_path.read_text(encoding="utf-8")
    documents: List[AssetDocument] = []

    # Prefer structured "Referenced Xforms" anchors (payload + world bbox/center) if present.
    anchors = _parse_referenced_xforms(text)
    if anchors:
        scene_meta = _extract_scene_meta(text)
        meta_content = (
            f"Scene: {md_path.stem}\n"
            f"USDA: {scene_meta.get('usda_path', '')}\n"
            f"DefaultPrim: {scene_meta.get('default_prim', '')}\n"
            f"MetersPerUnit: {scene_meta.get('meters_per_unit', '')}\n"
            f"UpAxis: {scene_meta.get('up_axis', '')}\n"
        ).strip()
        documents.append(
            AssetDocument(
                doc_id=f"{md_path.stem}-scene-meta-{_hash_text(meta_content)}",
                content=meta_content,
                metadata={
                    "source": str(md_path),
                    "doc_type": "md",
                    "md_kind": "scene_meta",
                    "scene_name": md_path.stem,
                    **scene_meta,
                },
            )
        )

        # Cap to keep index size reasonable (anchors are still retrievable via semantic similarity).
        max_anchors = 800
        for idx, a in enumerate(anchors[:max_anchors]):
            bbox = a["bbox_world"]
            content = (
                f"Scene: {md_path.stem}\n"
                f"Prim: {a['prim_path']}\n"
                f"Type: {a['xform_type']}\n"
                f"Payload: {a.get('payload', '')}\n"
                f"BBox(world).size: {bbox['size']}\n"
                f"BBox(world).center: {bbox['center']}\n"
            ).strip()
            documents.append(
                    AssetDocument(
                        doc_id=f"{md_path.stem}-xform-{idx}-{_hash_text(content)}",
                        content=content,
                        metadata={
                            "source": str(md_path),
                            "doc_type": "md",
                            "md_kind": "referenced_xform",
                            "scene_name": md_path.stem,
                            "prim_path": a["prim_path"],
                            "payload": a.get("payload", ""),
                            "bbox_world": bbox,
                        },
                    )
                )
        return documents

    # Fallback: chunk by paragraphs.
    chunks = chunk_by_paragraph(text, block_size=block_size)
    for idx, chunk in enumerate(chunks):
        doc_id = f"{md_path.stem}-md-{idx}-{_hash_text(chunk)}"
        documents.append(
            AssetDocument(
                doc_id=doc_id,
                content=chunk,
                metadata={
                    "source": str(md_path),
                    "scene_name": md_path.stem,
                    "section": idx,
                    "doc_type": "md",
                    "md_kind": "raw",
                },
            )
        )
    return documents


class AssetIngestor:
    """Aggregates CSV and markdown documents into a single corpus."""

    def __init__(self, config: ProjectConfig):
        self.config = config

    def build_documents(self) -> List[AssetDocument]:
        print("[AssetIngestor] 开始加载 CSV / Markdown 资产")
        docs: List[AssetDocument] = []
        for csv_path in self.config.asset_paths.inventory_csvs:
            print(f"[AssetIngestor] 处理 CSV: {csv_path}")
            docs.extend(load_csv_documents(csv_path, self.config.chunk_size, self.config.chunk_overlap))
        for md_path in self.config.asset_paths.scene_md_files:
            print(f"[AssetIngestor] 处理 Markdown: {md_path}")
            docs.extend(load_markdown_documents(md_path))
        if self.config.asset_paths.extra_documents_dir and self.config.asset_paths.extra_documents_dir.exists():
            for text_file in self.config.asset_paths.extra_documents_dir.glob("**/*.txt"):
                print(f"[AssetIngestor] 处理附加文本: {text_file}")
                docs.extend(load_markdown_documents(text_file))
        print(f"[AssetIngestor] 资产加载完毕，共 {len(docs)} 条文档")
        return docs


__all__ = ["AssetIngestor", "load_csv_documents", "load_markdown_documents"]
