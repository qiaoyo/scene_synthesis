"""Minimal vector index for document retrieval."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List, Sequence

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

    def _to_numpy_matrix(self, embeddings: Any) -> np.ndarray:
        """Convert embeddings from torch / numpy / python lists to float32 numpy matrix."""
        # torch.Tensor (batch, dim)
        if hasattr(embeddings, "detach") and hasattr(embeddings, "cpu"):
            arr = embeddings.detach().cpu().numpy().astype("float32")
            if arr.ndim == 1:
                arr = arr.reshape(1, -1)
            return arr

        # list/tuple of torch.Tensor
        if isinstance(embeddings, (list, tuple)) and embeddings and hasattr(embeddings[0], "detach"):
            stacked = np.stack([e.detach().cpu().numpy() for e in embeddings], axis=0).astype("float32")
            if stacked.ndim == 1:
                stacked = stacked.reshape(1, -1)
            return stacked

        # list/tuple of numpy arrays or python floats
        arr = np.asarray(embeddings, dtype="float32")
        if arr.ndim == 1:
            arr = arr.reshape(1, -1)
        return arr

    def add(self, embeddings: Sequence[Sequence[float]], documents: Sequence[AssetDocument]) -> None:
        # embeddings may be a torch.Tensor (n, dim) or a sequence; normalize to row count.
        if hasattr(embeddings, "shape"):
            emb_len = int(getattr(embeddings, "shape")[0]) if len(getattr(embeddings, "shape")) > 1 else 1
        else:
            emb_len = len(embeddings)
        if emb_len != len(documents):
            raise ValueError("Embeddings and documents must have the same length")
        matrix = self._to_numpy_matrix(embeddings)
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
        query = self._normalize(self._to_numpy_matrix(query_vector))
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
