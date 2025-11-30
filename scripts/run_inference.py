"""Convenience script to run inference on the layout RAG pipeline."""
from __future__ import annotations

import argparse
import json

from scene_layout_rag import ProjectConfig, SceneLayoutRAG


def main() -> None:
    parser = argparse.ArgumentParser(description="Run scene layout inference")
    parser.add_argument("command", help="Scene description prompt")
    parser.add_argument("--top-k", type=int, default=5)
    args = parser.parse_args()

    pipeline = SceneLayoutRAG(ProjectConfig())
    plan = pipeline.generate_layout(args.command, top_k=args.top_k)
    print(json.dumps(plan.summary(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
