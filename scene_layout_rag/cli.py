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
    # ReAct agent options
    parser.add_argument("--react", action="store_true", help="Use ReAct agent loop instead of single-pass generation")
    parser.add_argument("--max-steps", dest="max_steps", type=int, default=20, help="Max ReAct iterations (default: 20)")
    parser.add_argument("--no-reflect", dest="no_reflect", action="store_true", help="Disable reflection in ReAct mode")
    parser.add_argument("--physics", action="store_true", help="Enable Isaac Sim physics validation")
    # LLM API options
    parser.add_argument("--api-url", dest="api_url", type=str, default="", help="OpenAI-compatible API URL for LLM")
    parser.add_argument("--api-key", dest="api_key", type=str, default="", help="API key for remote LLM")
    parser.add_argument("--api-model", dest="api_model", type=str, default="", help="Model name for remote LLM")
    # Output options
    parser.add_argument("--output", "-o", type=Path, default=None, help="Save layout JSON to file")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    config = ProjectConfig()
    if args.assets:
        config.asset_paths.assets_root = args.assets
        config.asset_paths.inventory_csvs = sorted(Path(args.assets).glob("*.csv"))
        config.asset_paths.scene_md_files = sorted(Path(args.assets).glob("*.md"))
    if args.api_url:
        config.model.llm_api_url = args.api_url
    if args.api_key:
        config.model.llm_api_key = args.api_key
    if args.api_model:
        config.model.llm_api_model = args.api_model
    config.agent.max_steps = args.max_steps
    config.agent.reflection_enabled = not args.no_reflect
    config.agent.physics_enabled = args.physics

    pipeline = SceneLayoutRAG(config)

    if args.react:
        plan, trace = pipeline.generate_layout_react(args.command)
        output = {
            "mode": "react",
            "layout": plan.summary(),
            "trace": {
                "total_steps": trace.total_steps,
                "success": trace.success,
                "lessons": [
                    {"step": l.step, "mistake": l.mistake, "correction": l.correction}
                    for l in trace.lessons
                ],
                "steps": [
                    {"step": s.step, "action": s.action, "thought": s.thought, "ok": s.observation_ok}
                    for s in trace.steps
                ],
            },
        }
    else:
        plan = pipeline.generate_layout(args.command, top_k=args.top_k)
        output = {
            "mode": "single_pass",
            "layout": plan.summary(),
            "reasoning": [e.reasoning for e in plan.elements],
        }

    result_json = json.dumps(output, ensure_ascii=False, indent=2)
    print(result_json)

    if args.output:
        args.output.write_text(result_json, encoding="utf-8")
        print(f"\n[CLI] 布局已保存到: {args.output}")


if __name__ == "__main__":
    main()
