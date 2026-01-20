"""Run the ReAct-style agent and print a scene.json-compatible layout."""

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
    parser = argparse.ArgumentParser(description="ReAct agent for scene layout (template imitation)")
    parser.add_argument("command", help="Natural language scene instruction")
    parser.add_argument("--top-k-assets", type=int, default=12)
    parser.add_argument("--max-assets", type=int, default=8)
    parser.add_argument("--llm", action="store_true", help="Use LLM-driven ReAct loop over tools")
    parser.add_argument("--react-max-steps", type=int, default=6)
    parser.add_argument("--out", type=Path, default=None, help="Optional output json path")
    args = parser.parse_args()

    pipeline = SceneLayoutRAG(ProjectConfig())
    if args.llm:
        plan = pipeline.generate_layout_react_llm(
            args.command,
            top_k_assets=args.top_k_assets,
            max_assets=args.max_assets,
            max_steps=args.react_max_steps,
        )
    else:
        plan = pipeline.generate_layout_react(args.command, top_k_assets=args.top_k_assets, max_assets=args.max_assets)
    payload = plan.summary()

    if args.out:
        args.out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
