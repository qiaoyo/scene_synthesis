"""Rebuild data/indexes for the scene layout RAG system.

The actual indexing logic lives in ``rag.py``. This script only creates the
default project config and calls ``AssetRAG.build(save=True)``.
"""
from __future__ import annotations
import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
import shutil
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INDEX_DIR = PROJECT_ROOT / "data" / "indexes"
TEMP_INDEX_DIR = PROJECT_ROOT / "data" / ".indexes_rebuild_tmp"


if __package__ in {None, ""}:
    sys.path.insert(0, str(PROJECT_ROOT))
    from scene_layout_react.config import ProjectConfig
    from scene_layout_react.rag import AssetRAG
else:
    from .config import ProjectConfig
    from .rag import AssetRAG


def remove_path(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


def rebuild_indexes() -> None:
    remove_path(TEMP_INDEX_DIR)

    config = ProjectConfig(index_dir=TEMP_INDEX_DIR)
    rag = AssetRAG(config)

    print(f"[rebuild_indexes] Building temporary indexes: {TEMP_INDEX_DIR}")
    documents = rag.build(save=True)

    remove_path(INDEX_DIR)
    shutil.move(str(TEMP_INDEX_DIR), str(INDEX_DIR))

    print(f"[rebuild_indexes] Saved indexes: {INDEX_DIR}")
    print(f"[rebuild_indexes] Documents: {len(documents)}")


if __name__ == "__main__":
    rebuild_indexes()
