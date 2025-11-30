"""Minimal vector index for document retrieval."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Sequence, Tuple

import numpy as np

try:  # pragma: no cover - optional dependency
    import faiss  # type: ignore
except ImportError:  # pragma: no cover
    faiss = None

from .data_models import AssetDocument


@dataclass
class RetrievalResult:
    document: AssetDocument
    score: float


class LocalVectorStore:
    """A compact vector store with optional FAISS acceleration."""

    def __init__(self, dimension: int, use_faiss: bool = True):
        self.dimension = dimension
        self._use_faiss = use_faiss and faiss is not None
        self._index = faiss.IndexFlatIP(dimension) if self._use_faiss else None
        self._vectors: np.ndarray = np.zeros((0, dimension), dtype="float32")
        self._documents: List[AssetDocument] = []

    def _normalize(self, vectors: np.ndarray) -> np.ndarray:
        if vectors.ndim == 1:
            vectors = vectors.reshape(1, -1)
        if vectors.size == 0:
            return vectors
        norms = np.linalg.norm(vectors, axis=1, keepdims=True) + 1e-10
        return vectors / norms

    def add(self, embeddings: Sequence[Sequence[float]], documents: Sequence[AssetDocument]) -> None:
        if len(embeddings) != len(documents):
            raise ValueError("Embeddings and documents must have the same length")
        matrix = [foo.cpu().detach().numpy().astype("float32") for foo in embeddings]
        matrix = np.asarray(matrix, dtype="float32")
        if matrix.ndim == 1:
            matrix = matrix.reshape(1, -1)
        if matrix.size == 0:
            print("[VectorStore] 收到空的嵌入矩阵，跳过添加")
            return
        print(f"[VectorStore] 添加 {matrix.shape[0]} 条向量到索引")
        matrix = self._normalize(matrix)
        if self._use_faiss:
            self._index.add(matrix)
        else:
            self._vectors = np.vstack([self._vectors, matrix])
        self._documents.extend(documents)

    def search(self, query_vector: Sequence[float], top_k: int = 5) -> List[RetrievalResult]:
        query = np.asarray([query_vector.cpu().detach()], dtype="float32")
        query = self._normalize(query)
        if self._use_faiss:
            scores, indices = self._index.search(query, top_k)
        else:
            sims = self._vectors @ query.T
            scores = sims.T
            top_idx = np.argsort(-scores, axis=1)[:, :top_k]
            indices = top_idx
        results: List[RetrievalResult] = []
        for rank, idx in enumerate(indices[0]):
            if idx < 0 or idx >= len(self._documents):
                continue
            score = float(scores[0][rank])
            results.append(RetrievalResult(document=self._documents[idx], score=score))
        return results


__all__ = ["LocalVectorStore", "RetrievalResult"]
