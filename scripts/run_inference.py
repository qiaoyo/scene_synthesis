"""End-to-end inference: load corpus -> spin up ReAct agent -> save trace.

Usage:
    python scripts/run_inference.py --command "Build a small sorting cell with a conveyor and two boxes."

Default model 来自 ``ProjectConfig.model.llm_name_or_path``，默认 cuda:1。
通过 ``--device cpu`` 可强制 CPU（仅用于无 GPU 的烟雾测试，速度会很慢）。
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Make the package importable when run as a script.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scene_layout_rag.agent import ReActAgent  # noqa: E402
from scene_layout_rag.config import ProjectConfig  # noqa: E402
from scene_layout_rag.rag import AssetRAG  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run ReAct scene synthesis end-to-end.")
    parser.add_argument("--command", required=True, help="自然语言场景指令")
    parser.add_argument("--llm-backend", choices=["local", "openai_sdk"], help="选择 LLM 后端")
    parser.add_argument("--device", help="覆盖 LLM device，例如 cuda:0 或 cpu")
    parser.add_argument("--model", help="覆盖 LLM 模型路径")
    parser.add_argument("--api-base-url", help="OpenAI SDK base_url")
    parser.add_argument("--api-key", help="OpenAI SDK api key")
    parser.add_argument("--max-steps", type=int, help="覆盖 max_steps")
    parser.add_argument("--no-faiss", action="store_true", help="禁用 FAISS")
    parser.add_argument("--rebuild-corpus", action="store_true", help="启动前重建 corpus / FAISS")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cfg = ProjectConfig()
    if args.no_faiss:
        cfg.enable_faiss = False
    if args.llm_backend:
        cfg.model.llm_backend = args.llm_backend
    if args.device:
        cfg.model.device = args.device
    if args.model:
        if cfg.model.llm_backend == "openai_sdk":
            cfg.model.llm_api_model = args.model
        else:
            cfg.model.llm_name_or_path = args.model
    if args.api_base_url:
        cfg.model.llm_api_base_url = args.api_base_url
    if args.api_key:
        cfg.model.llm_api_key = args.api_key
    if args.max_steps:
        cfg.agent.max_steps = args.max_steps
    cfg.ensure_directories()

    rag = AssetRAG(cfg)
    if args.rebuild_corpus or not (cfg.index_dir / "corpus.jsonl").exists():
        rag.build(save=True)
    else:
        rag.load()

    agent = ReActAgent(cfg, rag=rag)
    record = agent.run(args.command)
    out_path = agent.save(record)
    print(f"[run_inference] {record.finish_reason}, {len(record.steps)} 步, "
          f"final_instances={len(agent.scene.state.instances)}")
    print(f"[run_inference] trace -> {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
