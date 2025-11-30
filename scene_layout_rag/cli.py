"""Simple CLI for experimenting with the layout RAG pipeline."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .config import ProjectConfig
from .rag import SceneLayoutRAG


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Scene layout RAG CLI")
    parser.add_argument("command", help="Natural language scene instruction")
    parser.add_argument("--assets", type=Path, default=None, help="Optional override for assets directory")
    parser.add_argument("--top-k", dest="top_k", type=int, default=5)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    config = ProjectConfig()
    if args.assets:
        config.asset_paths.assets_root = args.assets
        config.asset_paths.inventory_csvs = sorted(Path(args.assets).glob("*.csv"))
        config.asset_paths.scene_md_files = sorted(Path(args.assets).glob("*.md"))
    pipeline = SceneLayoutRAG(config)
    plan = pipeline.generate_layout(args.command, top_k=args.top_k)
    print(json.dumps({"layout": plan.summary(), "reasoning": [e.reasoning for e in plan.elements]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
