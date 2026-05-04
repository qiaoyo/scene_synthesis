"""High level pipeline orchestrating ingestion, retrieval, and layout reasoning."""
from __future__ import annotations

import json
from typing import Dict, List, Sequence, Tuple

from .asset_loader import AssetIngestor
from .config import ProjectConfig
from .data_models import (
    AgentTrace,
    AssetDocument,
    LayoutPlan,
    LayoutElement,
    SceneCommand,
)
from .embedding import EmbeddingBackend
from .layout_reasoner import LayoutReasoner
from .llm_planner import LLMPlanner
from .vector_store import LocalVectorStore, RetrievalResult


class SceneLayoutRAG:
    def __init__(self, config: ProjectConfig | None = None):
        self.config = config or ProjectConfig()
        self.config.ensure_directories()
        print(f"[SceneLayoutRAG] 初始化，索引目录: {self.config.index_dir}")
        self.ingestor = AssetIngestor(self.config)
        self._documents = self.ingestor.build_documents()
        print(f"[SceneLayoutRAG] 文档总数: {len(self._documents)}")
        self._embedder: EmbeddingBackend | None = None
        self._index: LocalVectorStore | None = None
        self._reasoner = LayoutReasoner()
        self._planner: LLMPlanner | None = None

    @property
    def document_count(self) -> int:
        return len(self._documents)

    @property
    def documents(self) -> List[AssetDocument]:
        return self._documents

    def _ensure_index(self) -> None:
        if self._index is not None:
            return
        print("[SceneLayoutRAG] 构建向量索引...")
        self._embedder = EmbeddingBackend(
            model_name=self.config.model.embedding_model,
            device=self.config.model.device,
            batch_size=self.config.model.embedding_batch_size,
        )
        embeddings = self._embedder.embed_documents([doc.content for doc in self._documents])
        self._index = LocalVectorStore(dimension=self._embedder.embedding_dim)
        self._index.add(embeddings, self._documents)
        print("[SceneLayoutRAG] 向量索引构建完成")

    def retrieve(self, query: str, top_k: int = 5) -> List[RetrievalResult]:
        self._ensure_index()
        assert self._index is not None and self._embedder is not None
        print(f"[SceneLayoutRAG] 执行检索: top_k={top_k}")
        query_vec = self._embedder.embed_query(query)
        return self._index.search(query_vec, top_k=top_k)

    def generate_layout(self, command_text: str, top_k: int = 5) -> LayoutPlan:
        hits = self.retrieve(command_text, top_k=top_k)
        print(f"[SceneLayoutRAG] 根据查询构建布局方案, 命中数量: {len(hits)}")
        command = SceneCommand(raw_text=command_text, language=self.config.language)
        doc_scores = [(hit.document, hit.score) for hit in hits]
        planner_notes = None
        plan_elements: Sequence[LayoutElement] | None = None
        if (self.config.model.llm_backend == "local"
            and self.config.model.llm_name_or_path):
            try:
                self._planner = self._planner or LLMPlanner(self.config)
                planner_notes, placement_dicts = self._planner.plan(command_text, [doc for doc, _ in doc_scores])
                if placement_dicts:
                    plan_elements = self._build_elements_from_llm(placement_dicts, doc_scores)
            except Exception as exc:  # pragma: no cover - defensive logging
                print(f"[SceneLayoutRAG] LLM规划失败，回落到启发式策略: {exc}")
                plan_elements = None
        if plan_elements is None or len(plan_elements) == 0:
            plan = self._reasoner.build_plan(command, doc_scores)
            plan.planner_notes = planner_notes
            return plan
        return LayoutPlan(command=command, elements=plan_elements, retrieved_docs=[doc for doc, _ in doc_scores], planner_notes=planner_notes)

    # ------------------------------------------------------------------
    # ReAct mode
    # ------------------------------------------------------------------

    def generate_layout_react(self, command_text: str) -> Tuple[LayoutPlan, AgentTrace]:
        """Generate a layout using the ReAct agent loop.

        Unlike :meth:`generate_layout`, this method runs an iterative
        Think → Act → Observe → Reflect cycle.  RAG retrieval happens
        *inside* the loop via the ``retrieve_assets`` tool.
        """
        from .agent import ReActAgent
        from .observer import SceneObserver
        from .tools import build_default_registry

        self._ensure_index()
        assert self._index is not None and self._embedder is not None

        catalog_summary = self._build_catalog_summary()

        planner = self._planner or LLMPlanner(self.config)
        self._planner = planner

        registry = build_default_registry()
        observer = SceneObserver(physics_enabled=self.config.agent.physics_enabled)

        agent = ReActAgent(
            llm=planner,
            tool_registry=registry,
            observer=observer,
            vector_store=self._index,
            embedder=self._embedder,
            max_steps=self.config.agent.max_steps,
            reflection_enabled=self.config.agent.reflection_enabled,
            max_lessons=self.config.agent.max_lessons,
            max_working_memory=self.config.agent.max_working_memory,
        )

        scene, trace = agent.run(command_text, catalog_summary)

        # Convert SceneState → LayoutPlan for backward compatibility
        command = SceneCommand(raw_text=command_text, language=self.config.language)
        elements = [
            LayoutElement(
                asset_id=a.asset_id,
                usd_path=a.usd_path,
                transform={"x": a.position[0], "y": a.position[1], "z": a.position[2]},
                score=1.0,
                reasoning=a.description or "ReAct agent placement",
            )
            for a in scene.assets.values()
        ]
        plan = LayoutPlan(command=command, elements=elements, planner_notes=f"ReAct: {trace.total_steps} steps")
        return plan, trace

    def _build_catalog_summary(self) -> Dict[str, Any]:
        """Build a summary of the asset catalog for the agent's warm-start context."""
        categories: Dict[str, int] = {}
        for doc in self._documents:
            cat = doc.metadata.get("asset_category", "unknown")
            categories[cat] = categories.get(cat, 0) + 1
        return {
            "available_categories": sorted(categories.keys()),
            "category_counts": categories,
            "total_assets": len(self._documents),
        }

    def _build_elements_from_llm(self, placement_dicts: Sequence[dict], doc_scores: Sequence[tuple[AssetDocument, float]]) -> List[LayoutElement]:
        doc_by_id = {doc.doc_id: (doc, score) for doc, score in doc_scores}
        doc_by_asset = {doc.metadata.get("asset_category", doc.doc_id): (doc, score) for doc, score in doc_scores}
        elements: List[LayoutElement] = []
        for entry in placement_dicts:
            asset_id = str(entry.get("asset_id") or "")
            doc_entry = doc_by_id.get(asset_id) or doc_by_asset.get(asset_id)
            if doc_entry is None:
                continue
            doc, score = doc_entry
            usd_path = entry.get("usd_path") or doc.metadata.get("usd_path", "")
            pos = entry.get("position") or {}
            transform = {
                "x": float(pos.get("x", 0.0)),
                "y": float(pos.get("y", 0.0)),
                "z": float(pos.get("z", 0.0)),
            }
            reasoning = entry.get("reason") or "由LLM规划得出的位置"
            elements.append(
                LayoutElement(
                    asset_id=asset_id or doc.metadata.get("asset_category", doc.doc_id),
                    usd_path=usd_path,
                    transform=transform,
                    score=score,
                    reasoning=reasoning,
                )
            )
        return elements


__all__ = ["SceneLayoutRAG"]
