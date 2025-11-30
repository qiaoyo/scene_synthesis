"""Embedding backend built on top of sentence-transformers."""
from __future__ import annotations

from functools import lru_cache
from typing import List, Sequence

try:
    from sentence_transformers import SentenceTransformer
except ImportError:  # pragma: no cover
    SentenceTransformer = None


class EmbeddingBackend:
    """Thin wrapper around SentenceTransformer."""

    def __init__(self, model_name: str, device: str | None = None, batch_size: int = 32):
        if SentenceTransformer is None:
            raise ImportError("sentence-transformers is required for EmbeddingBackend")
        self.model_name = model_name
        self.batch_size = batch_size
        self.device = device
        self._model = self._load_model()

    @lru_cache(maxsize=1)
    def _load_model(self) -> SentenceTransformer:
        return SentenceTransformer(self.model_name, device=self.device)

    @property
    def embedding_dim(self) -> int:
        return self._model.get_sentence_embedding_dimension()

    def embed_documents(self, texts: Sequence[str]) -> List[List[float]]:
        return self._model.encode(list(texts), batch_size=self.batch_size, show_progress_bar=True, convert_to_numpy=False)

    def embed_query(self, text: str) -> List[float]:
        return self._model.encode(text, batch_size=1, show_progress_bar=False, convert_to_numpy=False)


__all__ = ["EmbeddingBackend"]
