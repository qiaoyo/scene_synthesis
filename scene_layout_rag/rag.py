"""High level pipeline orchestrating ingestion, retrieval, and layout reasoning."""
from __future__ import annotations

from typing import List, Sequence

from .asset_loader import AssetIngestor
from .config import ProjectConfig
from .data_models import AssetDocument, LayoutPlan, LayoutElement, SceneCommand
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
        #self._index: LocalVectorStore | None = None
        self._asset_index: LocalVectorStore | None = None
        self._scene_index: LocalVectorStore | None = None
        self._reasoner = LayoutReasoner()
        self._planner: LLMPlanner | None = None

    @property
    def document_count(self) -> int:
        return len(self._documents)

    @property
    def documents(self) -> List[AssetDocument]:
        return self._documents

    def _ensure_index(self) -> None:
        # if self._index is not None:
        #     return
        # print("[SceneLayoutRAG] 构建向量索引...")
        if self._asset_index is not None and self._scene_index is not None and self._embedder is not None:
            return
        print("[SceneLayoutRAG] 构建向量索引(资产/场景)...")
        self._embedder = EmbeddingBackend(
            model_name=self.config.model.embedding_model,
            device=self.config.model.device,
            batch_size=self.config.model.embedding_batch_size,
        )
        csv_docs = [d for d in self._documents if d.metadata.get("doc_type") == "csv"]
        md_docs  = [d for d in self._documents if d.metadata.get("doc_type") == "md"]
        if csv_docs:
            emb_csv = self._embedder.embed_documents([d.content for d in csv_docs])
            self._asset_index = LocalVectorStore(dimension=self._embedder.embedding_dim)
            self._asset_index.add(emb_csv, csv_docs)
        else:
            self._asset_index = LocalVectorStore(dimension=self._embedder.embedding_dim)

        if md_docs:
            emb_md = self._embedder.embed_documents([d.content for d in md_docs])
            self._scene_index = LocalVectorStore(dimension=self._embedder.embedding_dim)
            self._scene_index.add(emb_md, md_docs)
        else:
            self._scene_index = LocalVectorStore(dimension=self._embedder.embedding_dim)
        print("[SceneLayoutRAG] 索引构建完成")

    # def retrieve(self, query: str, top_k: int = 5) -> List[RetrievalResult]:
    #     self._ensure_index()
    #     assert self._index is not None and self._embedder is not None
    #     print(f"[SceneLayoutRAG] 执行检索: top_k={top_k}")
    #     query_vec = self._embedder.embed_query(query)
    #     return self._index.search(query_vec, top_k=top_k)
    
    def retrieve_assets(self, query: str, top_k: int = 5) -> List[RetrievalResult]:
        self._ensure_index()
        assert self._asset_index is not None and self._embedder is not None
        q = self._embedder.embed_query(query)
        return self._asset_index.search(q, top_k=top_k)

    def retrieve_scenes(self, query: str, top_k: int = 5) -> List[RetrievalResult]:
        self._ensure_index()
        assert self._scene_index is not None and self._embedder is not None
        q = self._embedder.embed_query(query)
        return self._scene_index.search(q, top_k=top_k)
    
    def generate_layout(self, command_text: str, top_k: int = 5) -> LayoutPlan:
        asset_hits = self.retrieve_assets(command_text, top_k=top_k)
        scene_hits = self.retrieve_scenes(command_text, top_k=top_k)
        print(f"[SceneLayoutRAG] 命中(资产/场景): {len(asset_hits)}/{len(scene_hits)}")
        
        command = SceneCommand(raw_text=command_text, language=self.config.language)
        asset_doc_scores = [(h.document, h.score) for h in asset_hits]
        scene_doc_scores = [(h.document, h.score) for h in scene_hits]
        planner_notes = None
        plan_elements: Sequence[LayoutElement] | None = None
        
        if self.config.model.llm_name_or_path and asset_doc_scores:
            try:
                self._planner = self._planner or LLMPlanner(self.config)
                planner_notes, placement_dicts = self._planner.plan(
                    command_text,
                    [doc for doc, _ in asset_doc_scores] + [doc for doc, _ in scene_doc_scores],
                )
                if placement_dicts:
                    plan_elements = self._build_elements_from_llm(placement_dicts, asset_doc_scores)
            except Exception as exc:
                print(f"[SceneLayoutRAG] LLM规划失败，回落到启发式策略: {exc}")
                plan_elements = None
        if plan_elements is None or len(plan_elements) == 0:
            # 启发式仍可利用 scene_hits 做简单加成（略）
            combined = asset_doc_scores if asset_doc_scores else scene_doc_scores
            plan = self._reasoner.build_plan(command, combined)
            plan.planner_notes = planner_notes
            return plan
        #return LayoutPlan(command=command, elements=plan_elements, retrieved_docs=[doc for doc, _ in doc_scores], planner_notes=planner_notes)
        return LayoutPlan(
            command=command,
            elements=plan_elements,
            retrieved_docs=[doc for doc, _ in (asset_doc_scores + scene_doc_scores)],
            planner_notes=planner_notes,
        )
        
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
            print("entry",entry)
            usd_path = entry.get("usd_path") or doc.metadata.get("usd_path", "")
            pos = entry.get("position") or {}
            # transform = {
            #     "x": float(pos.get("x", 0.0)),
            #     "y": float(pos.get("y", 0.0)),
            #     "z": float(pos.get("z", 0.0)),
            # }
            # 兼容 [x,y,z] 或 {"x":..,"y":..,"z":..}
            if isinstance(pos, (list, tuple)) and len(pos) >= 3:
                px, py, pz = float(pos[0]), float(pos[1]), float(pos[2])
            elif isinstance(pos, dict):
                px, py, pz = float(pos.get("x", 0.0)), float(pos.get("y", 0.0)), float(pos.get("z", 0.0))
            else:
                px, py, pz = 0.0, 0.0, 0.0
            transform = {"x": px, "y": py, "z": pz}
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
