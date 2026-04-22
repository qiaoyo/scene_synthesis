"""Inspect normalized asset corpus documents produced by AssetIngestor."""
from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scene_layout_rag.asset_loader import AssetIngestor
from scene_layout_rag.config import ProjectConfig


def _shorten(value: object, limit: int = 180) -> str:
    text = str(value).replace("\n", " ")
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def main() -> None:
    config = ProjectConfig()
    docs = AssetIngestor(config).build_documents()

    by_doc_type: Counter[str] = Counter()
    by_asset_type: Counter[str] = Counter()
    by_scene_prior: Counter[str] = Counter()
    by_template_scene: Counter[str] = Counter()
    by_template_detail: Counter[str] = Counter()
    samples: dict[str, list] = defaultdict(list)

    asset_count = 0
    asset_bbox_count = 0
    asset_tags_count = 0
    asset_missing_usd = 0
    suspicious_headers = []

    for doc in docs:
        meta = doc.metadata
        doc_type = str(meta.get("doc_type", "unknown"))
        by_doc_type[doc_type] += 1
        if len(samples[doc_type]) < 3:
            samples[doc_type].append(doc)

        if doc_type == "asset":
            asset_count += 1
            asset_type = str(meta.get("asset_type") or meta.get("asset_category") or "unknown")
            by_asset_type[asset_type] += 1
            if meta.get("bbox_size"):
                asset_bbox_count += 1
            if meta.get("tags"):
                asset_tags_count += 1
            if not meta.get("usd_path"):
                asset_missing_usd += 1
            if asset_type.lower() in {"assets type", "asset type"} or str(meta.get("usd_path", "")).lower() == "path":
                suspicious_headers.append(doc.doc_id)
        elif doc_type == "scene_prior":
            by_scene_prior[str(meta.get("scene_id", "unknown"))] += 1
        elif doc_type == "scene_template":
            by_template_scene[str(meta.get("scene_id", "unknown"))] += 1
            by_template_detail[str(meta.get("template_detail", "unknown"))] += 1

    print("Corpus Summary")
    print(f"  total_documents: {len(docs)}")
    print(f"  doc_type: {dict(sorted(by_doc_type.items()))}")
    print()

    print("Assets")
    print(f"  total: {asset_count}")
    print(f"  by_asset_type: {dict(sorted(by_asset_type.items()))}")
    print(f"  bbox_success: {asset_bbox_count}/{asset_count}")
    print(f"  tags_success: {asset_tags_count}/{asset_count}")
    print(f"  missing_usd_path: {asset_missing_usd}")
    print(f"  suspicious_header_docs: {suspicious_headers[:10]}")
    print()

    print("Scene Priors")
    print(f"  by_scene_id: {dict(sorted(by_scene_prior.items()))}")
    print()

    print("Scene Templates")
    print(f"  by_scene_id: {dict(sorted(by_template_scene.items()))}")
    print(f"  by_detail: {dict(sorted(by_template_detail.items()))}")
    print()

    print("Samples")
    for doc_type, docs_for_type in sorted(samples.items()):
        print(f"  [{doc_type}]")
        for doc in docs_for_type:
            meta = doc.metadata
            print(f"    id: {doc.doc_id}")
            print(f"    metadata: {_shorten(meta)}")
            print(f"    content: {_shorten(doc.content)}")


if __name__ == "__main__":
    main()
