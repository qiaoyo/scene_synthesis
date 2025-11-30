"""Precompute embeddings for all assets and persist index artifacts."""
from __future__ import annotations

import argparse
from pathlib import Path

from scene_layout_rag import ProjectConfig, SceneLayoutRAG


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the asset embedding index")
    parser.add_argument("--index-dir", type=Path, default=None, help="Optional directory for vector indexes")
    args = parser.parse_args()

    config = ProjectConfig()
    if args.index_dir:
        config.index_dir = args.index_dir
    pipeline = SceneLayoutRAG(config)
    pipeline.retrieve("初始化测试", top_k=1)
    print(f"Indexed {pipeline.document_count} documents. Index directory: {config.index_dir}")


if __name__ == "__main__":
    main()
