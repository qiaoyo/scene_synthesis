"""Precompute embeddings for all assets and persist index artifacts."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

SRC_ROOT = Path(__file__).resolve().parents[1]
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from scene_layout_rag import ProjectConfig, SceneLayoutRAG


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the asset embedding index")
    parser.add_argument("--index-dir", type=Path, default=None, help="Optional directory for vector indexes")
    args = parser.parse_args()

    print("[Script] 启动资产索引构建流程")
    config = ProjectConfig()
    if args.index_dir:
        config.index_dir = args.index_dir
        print(f"[Script] 使用自定义索引目录: {config.index_dir}")
    pipeline = SceneLayoutRAG(config)
    # Trigger index build (assets + scene templates).
    pipeline.retrieve_assets("初始化测试", top_k=1)
    pipeline.retrieve_scenes("初始化测试", top_k=1)
    print(f"Indexed {pipeline.document_count} documents. Index directory: {config.index_dir}")
    print("[Script] ingest_assets 完成")


if __name__ == "__main__":
    main()
