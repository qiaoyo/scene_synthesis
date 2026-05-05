"""Command-line entrypoints.

子命令:
  ``ingest``  扫描 ``data/assets/`` 并写入 ``data/indexes/corpus.jsonl`` 与可选 FAISS。
  ``run``     启动 ReAct agent 处理一条用户指令。
  ``retrieve``  快速测试 RAG（无须加载 LLM）。
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .agent import ReActAgent
from .config import ProjectConfig
from .rag import AssetRAG


def _build_config(args: argparse.Namespace) -> ProjectConfig:
    cfg = ProjectConfig()
    if args.no_faiss:
        cfg.enable_faiss = False
    if args.index_dir:
        cfg.index_dir = Path(args.index_dir)
    if args.output_dir:
        cfg.output_dir = Path(args.output_dir)
    if args.device:
        cfg.model.device = args.device
    if args.model:
        if args.llm_backend == "openai_sdk":
            cfg.model.llm_api_model = args.model
        else:
            cfg.model.llm_name_or_path = args.model
    if args.llm_backend:
        cfg.model.llm_backend = args.llm_backend
    if args.api_base_url:
        cfg.model.llm_api_base_url = args.api_base_url
    if args.api_key:
        cfg.model.llm_api_key = args.api_key
    if args.max_steps:
        cfg.agent.max_steps = args.max_steps
    return cfg


def cmd_ingest(args: argparse.Namespace) -> int:
    cfg = _build_config(args)
    cfg.ensure_directories()
    rag = AssetRAG(cfg)
    rag.build(save=True)
    print(f"[ingest] 完成。corpus -> {cfg.index_dir / 'corpus.jsonl'}")
    if cfg.enable_faiss and rag.faiss is not None:
        print(f"[ingest] FAISS  -> {cfg.index_dir / 'vectors.faiss'}")
    return 0


def cmd_retrieve(args: argparse.Namespace) -> int:
    cfg = _build_config(args)
    rag = AssetRAG(cfg)
    rag.load()
    filters = {}
    if args.asset_type:
        filters["asset_type"] = args.asset_type
    if args.doc_type:
        filters["doc_type"] = args.doc_type
    hits = rag.retrieve(args.query, top_k=args.top_k, filters=filters or None)
    for doc, score in hits:
        print(f"{score:.4f}  {doc.metadata.get('doc_type','?')}/{doc.metadata.get('asset_type') or doc.metadata.get('scene_id') or '-'}  {doc.doc_id}")
        if args.show_preview:
            print("  " + doc.content.replace("\n", " | ")[:200])
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    cfg = _build_config(args)
    cfg.ensure_directories()
    rag = AssetRAG(cfg)
    rag.load()
    agent = ReActAgent(cfg, rag=rag)
    record = agent.run(args.command)
    out_path = agent.save(record)
    print(f"[run] 完成 ({record.finish_reason}). {len(record.steps)} 步 -> {out_path}")
    print(f"[run] 最终实例数: {len(agent.scene.state.instances)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(prog="scene_layout_rag", description="ReAct 场景合成 CLI")
    parser.add_argument("--no-faiss", action="store_true", help="跳过 FAISS 构建/加载，仅用关键词检索")
    parser.add_argument("--index-dir", help="覆盖 data/indexes 路径")
    parser.add_argument("--output-dir", help="覆盖 outputs 路径")
    parser.add_argument("--device", help="覆盖 LLM device，例如 cuda:0")
    parser.add_argument("--model", help="覆盖 LLM 模型名称或本地路径")
    parser.add_argument("--llm-backend", choices=["local", "openai_sdk"], help="选择 LLM 后端")
    parser.add_argument("--api-base-url", help="OpenAI SDK base_url，例如 https://api.openai.com/v1")
    parser.add_argument("--api-key", help="OpenAI SDK api key")
    parser.add_argument("--max-steps", type=int, help="覆盖 ReAct 最大步数")

    sub = parser.add_subparsers(dest="cmd", required=True)

    p_ingest = sub.add_parser("ingest", help="构建资产索引")
    p_ingest.set_defaults(func=cmd_ingest)

    p_retrieve = sub.add_parser("retrieve", help="测试 RAG 检索")
    p_retrieve.add_argument("query")
    p_retrieve.add_argument("--top-k", type=int, default=5)
    p_retrieve.add_argument("--asset-type")
    p_retrieve.add_argument("--doc-type")
    p_retrieve.add_argument("--show-preview", action="store_true")
    p_retrieve.set_defaults(func=cmd_retrieve)

    p_run = sub.add_parser("run", help="运行 ReAct agent")
    p_run.add_argument("command", help="自然语言指令，例如 'Build a sorting cell'")
    p_run.set_defaults(func=cmd_run)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
