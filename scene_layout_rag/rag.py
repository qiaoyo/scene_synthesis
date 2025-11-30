"""High level pipeline orchestrating ingestion, retrieval, and layout reasoning."""
from __future__ import annotations

from typing import List

from .asset_loader import AssetIngestor
from .config import ProjectConfig
from .data_models import AssetDocument, LayoutPlan, SceneCommand
from .embedding import EmbeddingBackend
from .layout_reasoner import LayoutReasoner
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
        return self._reasoner.build_plan(command, doc_scores)


__all__ = ["SceneLayoutRAG"]
