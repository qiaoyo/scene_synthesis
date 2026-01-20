"""Convenience script to run inference on the layout RAG pipeline."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SRC_ROOT = Path(__file__).resolve().parents[1]
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from scene_layout_rag import ProjectConfig, SceneLayoutRAG


def main() -> None:
    parser = argparse.ArgumentParser(description="Run scene layout inference")
    parser.add_argument("command", help="Scene description prompt")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--react", action="store_true")
    parser.add_argument("--react-llm", action="store_true")
    parser.add_argument("--top-k-assets", type=int, default=12)
    parser.add_argument("--max-assets", type=int, default=8)
    parser.add_argument("--react-max-steps", type=int, default=6)
    args = parser.parse_args()

    print("[Script] 启动推理流程")
    pipeline = SceneLayoutRAG(ProjectConfig())
    if args.react_llm:
        plan = pipeline.generate_layout_react_llm(
            args.command,
            top_k_assets=args.top_k_assets,
            max_assets=args.max_assets,
            max_steps=args.react_max_steps,
        )
    elif args.react:
        plan = pipeline.generate_layout_react(args.command, top_k_assets=args.top_k_assets, max_assets=args.max_assets)
    else:
        plan = pipeline.generate_layout(args.command, top_k=args.top_k)
    print(json.dumps(plan.summary(), ensure_ascii=False, indent=2))
    print("[Script] 推理完成")

if __name__ == "__main__":
    
    main()
