"""Embedding backend built on top of sentence-transformers."""
from __future__ import annotations

from functools import lru_cache
from typing import Sequence

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
        print(f"[EmbeddingBackend] 准备加载嵌入模型: {model_name} (device={device or 'auto'})")
        self._model = self._load_model()

    @lru_cache(maxsize=1)
    def _load_model(self) -> SentenceTransformer:
        print("[EmbeddingBackend] 正在加载 SentenceTransformer 模型...")
        return SentenceTransformer(self.model_name, device=self.device)

    @property
    def embedding_dim(self) -> int:
        return self._model.get_sentence_embedding_dimension()

    def embed_documents(self, texts: Sequence[str]):
        """Embed a batch of texts.

        We return a torch.Tensor when torch is available (SentenceTransformer default backend),
        which keeps downstream code (vector store) consistent across environments.
        """
        print(f"[EmbeddingBackend] 对 {len(texts)} 条文档进行嵌入计算")
        return self._model.encode(
            list(texts),
            batch_size=self.batch_size,
            show_progress_bar=True,
            convert_to_tensor=True,
        )

    def embed_query(self, text: str):
        print("[EmbeddingBackend] 计算查询向量")
        return self._model.encode(
            text,
            batch_size=1,
            show_progress_bar=False,
            convert_to_tensor=True,
        )


__all__ = ["EmbeddingBackend"]
