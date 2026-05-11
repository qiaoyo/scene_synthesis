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

def load_csv_documents(csv_path: Path, chunk_size: int, chunk_overlap: int) -> List[AssetDocument]:
    documents: List[AssetDocument] = []
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            return documents
        for idx, row in enumerate(reader):
            normalized_row = {}
            for key, value in row.items():
                norm_key = (key or "").lstrip("\ufeff").strip().lower()
                norm_key = re.sub(r"[^a-z0-9]+", "_", norm_key).strip("_")
                norm_value = value or "" 
                normalized_row[norm_key] = norm_value
            asset_category = normalized_row.get("assets_type", "")
            instanceID = normalized_row.get("instanceid", "")
            usd_path = normalized_row.get("path", "")
            tag_raw = normalized_row.get("tag", "")
            description = normalized_row.get("description", "")
            if not usd_path or usd_path.lower() == "path":
                continue
            tags:Dict[str,str] = {}
            if tag_raw:
                for line in tag_raw.splitlines():
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
            bbox_min = normalized_row.get("bbox_min_meters")
            bbox_max = normalized_row.get("bbox_max_meters")
            bbox = None
            if bbox_min and bbox_max:
                min_vals = [float(bbox_min[0]), float(bbox_min[1]), float(bbox_min[2])]
                max_vals = [float(bbox_max[0]), float(bbox_max[1]), float(bbox_max[2])]
                size = [round(max_vals[i] - min_vals[i], 6) for i in range(3)]
                center = [round((max_vals[i] + min_vals[i]) / 2.0, 6) for i in range(3)]
                bbox = {
                    "min": min_vals,
                    "max": max_vals,
                    "size": size,
                    "center": center,
                    "unit": "m",
                }
                content = f"Asset Type: {asset_category}\nDescription: {description}\nTags: {json.dumps(tags)}\n"
                metadata={  
                        "doc_type": "asset",
                        "asset_type": asset_category,
                        "instance_id": instanceID,
                        "usd_path": usd_path,
                        "tags": tags,
                        "description": description,
                        "source": str(csv_path),
                        "row_index": idx,
                        "bbox": bbox,
                    }
            doc_id = f"{csv_path.stem}-{idx}-{hashlib.md5(content.encode()).hexdigest()[:8]}"
            documents.append(
                AssetDocument(
                    doc_id=doc_id,
                    content=content,
                    metadata=metadata
                )
                )
    return documents

def load_markdown_documents(md_path: Path, block_size: int = 3) -> List[AssetDocument]:
    text = md_path.read_text(encoding="utf-8")
    text = text.strip()
    if not text:
        return []
    _PARA_SEP = re.compile(r"\n\s*\n+")
    paragraphs = [p.strip() for p in _PARA_SEP.split(text) if p.strip()]
    if not paragraphs:
        return []
    block_size = max(1, block_size)
    chunks: List[str] = []
    for i in range(0, len(paragraphs), block_size):
        block = "\n\n".join(paragraphs[i : i + block_size])
        chunks.append(block)
    documents: List[AssetDocument] = []
    stem = md_path.stem.lower()
    scene_id, detail = stem.split("-", 1)
    
    for idx, chunk in enumerate(chunks):
        doc_id = f"{md_path.stem}-md-{idx}-{hashlib.md5(chunk.encode()).hexdigest()[:8]}"
        documents.append(
            AssetDocument(
                doc_id=doc_id,
                content = chunk,
                metadata={
                    "doc_type": "scene_template",
                    "scene_id": scene_id,
                    "detail_level": detail,
                    "language": "en",
                    "source": str(md_path),
                    "chunk_idx": idx,
                },
            )
        )
    return documents

class AssetIngestor:
    """Aggregates CSV and markdown documents into a single corpus."""

    def __init__(self, config: ProjectConfig):
        self.config = config

    def build_documents(self) -> List[AssetDocument]:
        print("[AssetIngestor] 开始加载 CSV / Markdown / Docs 资产")
        docs: List[AssetDocument] = []
        # 1. 处理 CSV
        for csv_path in self.config.inventory_csvs:
            print(f"[AssetIngestor] 处理 CSV: {csv_path}")
            docs.extend(load_csv_documents(csv_path, self.config.chunk_size, self.config.chunk_overlap))
        #2. 处理 md
        for md_path in self.config.scene_md_files:
            print(f"[AssetIngestor] 处理 Markdown: {md_path}")
            docs.extend(load_markdown_documents(md_path, self.config.block_size))
        print(f"[AssetIngestor] 资产加载完毕，共 {len(docs)} 条文档")
        return docs
    
__all__ = [
    "AssetIngestor",
    "load_csv_documents",
    "load_markdown_documents",
]
