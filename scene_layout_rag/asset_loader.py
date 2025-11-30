"""Load structured asset metadata into normalized documents."""
from __future__ import annotations

import csv
import hashlib
from pathlib import Path
from typing import Iterable, List

from .config import ProjectConfig
from .data_models import AssetDocument
from .text_splitter import chunk_text, chunk_by_paragraph


def _hash_text(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:16]


def load_csv_documents(csv_path: Path, chunk_size: int, chunk_overlap: int) -> List[AssetDocument]:
    documents: List[AssetDocument] = []
    with csv_path.open("r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if not row or len(row) < 4:
                continue
            asset_category = row[0].strip() or csv_path.stem
            usd_path = row[1].strip()
            short_desc = row[2].strip()
            long_desc = row[3].strip()
            base_text = f"类型:{asset_category}\nUSD:{usd_path}\n{short_desc}\n{long_desc}"
            chunks = chunk_text(base_text, chunk_size, chunk_overlap)
            for chunk_idx, chunk in enumerate(chunks):
                doc_id = f"{csv_path.stem}-{idx}-{chunk_idx}-{_hash_text(chunk)}"
                documents.append(
                    AssetDocument(
                        doc_id=doc_id,
                        content=chunk,
                        metadata={
                            "asset_category": asset_category,
                            "usd_path": usd_path,
                            "source": str(csv_path),
                            "row_index": idx,
                        },
                    )
                )
    return documents


def load_markdown_documents(md_path: Path, block_size: int = 3) -> List[AssetDocument]:
    text = md_path.read_text(encoding="utf-8")
    chunks = chunk_by_paragraph(text, block_size=block_size)
    documents: List[AssetDocument] = []
    for idx, chunk in enumerate(chunks):
        doc_id = f"{md_path.stem}-md-{idx}-{_hash_text(chunk)}"
        documents.append(
            AssetDocument(
                doc_id=doc_id,
                content=chunk,
                metadata={"source": str(md_path), "section": idx},
            )
        )
    return documents


class AssetIngestor:
    """Aggregates CSV and markdown documents into a single corpus."""

    def __init__(self, config: ProjectConfig):
        self.config = config

    def build_documents(self) -> List[AssetDocument]:
        docs: List[AssetDocument] = []
        for csv_path in self.config.asset_paths.inventory_csvs:
            docs.extend(load_csv_documents(csv_path, self.config.chunk_size, self.config.chunk_overlap))
        for md_path in self.config.asset_paths.scene_md_files:
            docs.extend(load_markdown_documents(md_path))
        if self.config.asset_paths.extra_documents_dir and self.config.asset_paths.extra_documents_dir.exists():
            for text_file in self.config.asset_paths.extra_documents_dir.glob("**/*.txt"):
                docs.extend(load_markdown_documents(text_file))
        return docs


__all__ = ["AssetIngestor", "load_csv_documents", "load_markdown_documents"]
