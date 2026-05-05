"""Asset corpus + retrieval (JSON-first, FAISS by default).

数据布局（用户问题里特别要求的「数据放在哪儿」）:

    data/assets/csv/*.csv         <- 原始资产清单（已存在）
    data/assets/md/*.md           <- 场景模板（已存在）
    data/assets/docs/*.jsonl      <- 场景先验文本（已存在）
    data/indexes/corpus.jsonl     <- ★ 索引产物：每行一个 AssetDocument
    data/indexes/vectors.faiss    <- 默认产出：FAISS 索引文件
    data/indexes/index_meta.json  <- 默认产出：FAISS 与文档的对齐元信息

为什么用 JSONL 作为「事实源」：
- 确定性、人类可读、可 diff、可被 grep；不依赖 GPU 也能加载。
- FAISS 是默认的加速层。当 sentence-transformers/faiss 依赖缺失时，自动
  回退到 BM25-lite 关键词检索；corpus.jsonl 是数据本体，不会丢。
"""
from __future__ import annotations

import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

from .asset_loader import AssetIngestor
from .config import ProjectConfig
from .data_models import AssetDocument


CORPUS_FILE = "corpus.jsonl"
FAISS_FILE = "vectors.faiss"
FAISS_META_FILE = "index_meta.json"


# ---------- 持久化 ----------

def save_corpus(documents: Iterable[AssetDocument], index_dir: Path) -> Path:
    index_dir.mkdir(parents=True, exist_ok=True)
    out_path = index_dir / CORPUS_FILE
    with out_path.open("w", encoding="utf-8") as f:
        for doc in documents:
            f.write(json.dumps(doc.to_dict(), ensure_ascii=False) + "\n")
    return out_path


def load_corpus(index_dir: Path) -> List[AssetDocument]:
    path = index_dir / CORPUS_FILE
    if not path.exists():
        raise FileNotFoundError(
            f"Corpus not found at {path}. Run `python -m scene_layout_rag.cli ingest` first."
        )
    docs: List[AssetDocument] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            docs.append(AssetDocument.from_dict(json.loads(line)))
    return docs


# ---------- 关键词检索（无 GPU 依赖） ----------

_TOKEN_RE = re.compile(r"[a-z0-9]+|[一-鿿]")


def _tokenize(text: str) -> List[str]:
    return _TOKEN_RE.findall(text.lower())


def _match_filters(metadata: Dict[str, Any], filters: Dict[str, Any]) -> bool:
    """支持 ``{"asset_type": "Conveyor"}`` 与 ``{"asset_type": ["Conveyor","Box"]}``。"""
    for key, expected in filters.items():
        actual = metadata.get(key)
        if isinstance(expected, (list, tuple, set)):
            if actual not in expected:
                return False
        else:
            if actual != expected:
                return False
    return True


class KeywordRetriever:
    """轻量的 BM25-lite 检索器，作为始终可用的兜底。

    选择理由：避免 100% 依赖嵌入模型。当 sentence-transformers 不可用或 corpus
    很小（几千条）时，BM25 已能覆盖主要查询。
    """

    k1 = 1.5
    b = 0.75

    def __init__(self, documents: List[AssetDocument]):
        self.documents = documents
        self.tokens: List[List[str]] = [_tokenize(d.content) for d in documents]
        self.doc_lens = [len(t) for t in self.tokens]
        self.avgdl = (sum(self.doc_lens) / len(self.doc_lens)) if self.doc_lens else 0.0
        self.df: Counter = Counter()
        for tokens in self.tokens:
            for term in set(tokens):
                self.df[term] += 1
        self.n_docs = len(documents)

    def _idf(self, term: str) -> float:
        df = self.df.get(term, 0)
        return math.log((self.n_docs - df + 0.5) / (df + 0.5) + 1.0)

    def search(
        self,
        query: str,
        top_k: int = 5,
        filters: Optional[Dict[str, Any]] = None,
    ) -> List[Tuple[AssetDocument, float]]:
        q_tokens = _tokenize(query)
        if not q_tokens:
            return []
        scores: List[Tuple[int, float]] = []
        for idx, tokens in enumerate(self.tokens):
            if filters and not _match_filters(self.documents[idx].metadata, filters):
                continue
            if not tokens:
                continue
            tf = Counter(tokens)
            dl = self.doc_lens[idx]
            score = 0.0
            for term in q_tokens:
                if term not in tf:
                    continue
                idf = self._idf(term)
                tf_t = tf[term]
                denom = tf_t + self.k1 * (1.0 - self.b + self.b * dl / max(self.avgdl, 1e-6))
                score += idf * (tf_t * (self.k1 + 1.0)) / max(denom, 1e-6)
            if score > 0:
                scores.append((idx, score))
        scores.sort(key=lambda x: x[1], reverse=True)
        return [(self.documents[i], s) for i, s in scores[:top_k]]


# ---------- FAISS 加速层 ----------

class FaissRetriever:
    """sentence-transformers 嵌入 + FAISS IndexFlatIP 余弦相似度。

    依赖缺失时由 ``AssetRAG`` 捕获 ImportError 并回退到关键词检索。
    """

    def __init__(
        self,
        documents: List[AssetDocument],
        embedding_model: str,
        batch_size: int = 32,
        device: Optional[str] = None,
    ):
        from sentence_transformers import SentenceTransformer  # noqa: WPS433
        import faiss  # noqa: WPS433
        import numpy as np  # noqa: WPS433

        self.documents = documents
        self.encoder = SentenceTransformer(embedding_model, device=device)
        self.embedding_model = embedding_model
        texts = [d.content for d in documents]
        embeddings = self.encoder.encode(
            texts,
            batch_size=batch_size,
            convert_to_numpy=True,
            show_progress_bar=True,
            normalize_embeddings=True,
        )
        self.embeddings = embeddings.astype("float32")
        self.dim = int(self.embeddings.shape[1])
        self.index = faiss.IndexFlatIP(self.dim)
        self.index.add(self.embeddings)
        self._faiss = faiss
        self._np = np

    @classmethod
    def from_disk(
        cls,
        documents: List[AssetDocument],
        index_dir: Path,
        embedding_model: str,
        device: Optional[str] = None,
    ) -> "FaissRetriever":
        """跳过重新嵌入，直接从磁盘载入向量索引。"""
        from sentence_transformers import SentenceTransformer  # noqa: WPS433
        import faiss  # noqa: WPS433
        import numpy as np  # noqa: WPS433

        meta_path = index_dir / FAISS_META_FILE
        index_path = index_dir / FAISS_FILE
        if not (meta_path.exists() and index_path.exists()):
            raise FileNotFoundError(f"FAISS artifacts missing in {index_dir}")
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        if meta.get("doc_ids") != [d.doc_id for d in documents]:
            raise RuntimeError(
                "FAISS index doc_ids 与 corpus.jsonl 不一致，请删除 vectors.faiss 后重建。"
            )
        obj = cls.__new__(cls)
        obj.documents = documents
        obj.encoder = SentenceTransformer(meta.get("encoder", embedding_model), device=device)
        obj.embedding_model = meta.get("encoder", embedding_model)
        obj.dim = int(meta["dim"])
        obj.index = faiss.read_index(str(index_path))
        obj._faiss = faiss
        obj._np = np
        obj.embeddings = None  # 加载模式下不需要重持有原向量
        return obj

    def save(self, index_dir: Path) -> None:
        index_dir.mkdir(parents=True, exist_ok=True)
        self._faiss.write_index(self.index, str(index_dir / FAISS_FILE))
        meta = {
            "doc_ids": [d.doc_id for d in self.documents],
            "dim": self.dim,
            "encoder": self.embedding_model,
        }
        (index_dir / FAISS_META_FILE).write_text(
            json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    def search(
        self,
        query: str,
        top_k: int = 5,
        filters: Optional[Dict[str, Any]] = None,
    ) -> List[Tuple[AssetDocument, float]]:
        q = self.encoder.encode(
            [query], convert_to_numpy=True, normalize_embeddings=True
        ).astype("float32")
        oversample = len(self.documents) if filters else top_k
        scores, ids = self.index.search(q, min(oversample, len(self.documents)))
        results: List[Tuple[AssetDocument, float]] = []
        for idx, score in zip(ids[0].tolist(), scores[0].tolist()):
            if idx < 0:
                continue
            doc = self.documents[idx]
            if filters and not _match_filters(doc.metadata, filters):
                continue
            results.append((doc, float(score)))
            if len(results) >= top_k:
                break
        return results


# ---------- 顶层封装 ----------

class AssetRAG:
    """统一的检索入口；优先使用 FAISS，依赖缺失时回退关键词。"""

    def __init__(self, config: ProjectConfig):
        self.config = config
        self.documents: List[AssetDocument] = []
        self.keyword: Optional[KeywordRetriever] = None
        self.faiss: Optional[FaissRetriever] = None

    # -- 构建 / 持久化 --

    def build(self, save: bool = True) -> List[AssetDocument]:
        ingestor = AssetIngestor(self.config)
        self.documents = ingestor.build_documents()
        if save:
            self.config.ensure_directories()
            corpus_path = save_corpus(self.documents, self.config.index_dir)
            print(f"[AssetRAG] 写入语料: {corpus_path} ({len(self.documents)} 条)")
        self.keyword = KeywordRetriever(self.documents)
        if self.config.enable_faiss:
            self._build_faiss(save=save)
        return self.documents

    def load(self) -> List[AssetDocument]:
        self.documents = load_corpus(self.config.index_dir)
        self.keyword = KeywordRetriever(self.documents)
        if self.config.enable_faiss:
            self._load_or_build_faiss()
        return self.documents

    def _build_faiss(self, save: bool) -> None:
        try:
            self.faiss = FaissRetriever(
                self.documents,
                embedding_model=self.config.model.embedding_model,
                batch_size=self.config.model.embedding_batch_size,
                device=self.config.model.device,
            )
        except ImportError as exc:
            print(f"[AssetRAG] FAISS 依赖缺失，跳过向量索引构建: {exc}")
            self.faiss = None
            return
        if save:
            self.faiss.save(self.config.index_dir)
            print(f"[AssetRAG] 写入 FAISS: {self.config.index_dir / FAISS_FILE}")

    def _load_or_build_faiss(self) -> None:
        try:
            self.faiss = FaissRetriever.from_disk(
                self.documents,
                index_dir=self.config.index_dir,
                embedding_model=self.config.model.embedding_model,
                device=self.config.model.device,
            )
            print(f"[AssetRAG] 已加载 FAISS: {self.config.index_dir / FAISS_FILE}")
        except FileNotFoundError:
            print("[AssetRAG] 未发现 FAISS 文件，按 corpus.jsonl 现场构建并落盘")
            self._build_faiss(save=True)
        except ImportError as exc:
            print(f"[AssetRAG] FAISS 不可用，回退关键词检索: {exc}")
            self.faiss = None

    # -- 查询 --

    def retrieve(
        self,
        query: str,
        top_k: Optional[int] = None,
        filters: Optional[Dict[str, Any]] = None,
        prefer: str = "auto",
    ) -> List[Tuple[AssetDocument, float]]:
        """检索资产/场景文档。

        prefer:
          - ``"auto"``: 有 FAISS 时优先，没有则关键词。
          - ``"keyword"``: 强制关键词。
          - ``"faiss"``: 强制 FAISS（不可用则报错）。
        """
        k = top_k or self.config.retrieval_top_k
        retriever = self._select_retriever(prefer)
        return retriever.search(query, top_k=k, filters=filters)

    def _select_retriever(self, prefer: str):
        if prefer == "faiss":
            if self.faiss is None:
                raise RuntimeError("FAISS retriever 不可用，请检查 enable_faiss / 依赖安装")
            return self.faiss
        if prefer == "keyword":
            if self.keyword is None:
                raise RuntimeError("Keyword retriever 未初始化，请先调用 build/load")
            return self.keyword
        if self.faiss is not None:
            return self.faiss
        if self.keyword is None:
            raise RuntimeError("Retriever 未初始化，请先调用 build/load")
        return self.keyword


__all__ = [
    "AssetRAG",
    "KeywordRetriever",
    "FaissRetriever",
    "save_corpus",
    "load_corpus",
    "CORPUS_FILE",
    "FAISS_FILE",
    "FAISS_META_FILE",
]
