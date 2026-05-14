from __future__ import annotations
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import faiss  # noqa: WPS433
import numpy as np
from sentence_transformers import SentenceTransformer  # noqa: WPS433
from .asset_loader import AssetIngestor
from .config import ProjectConfig
from .data_models import AssetDocument

class AssetRAG:
    """
    Multi-index RAG retriever.

    """
    def __init__(self, config: ProjectConfig):
        self.config = config

        # 全量文档（仅用于调试/info）
        self.documents: List[AssetDocument] = []

        # encoder
        self.embedding_model: Optional[str] = None
        self.encoder: Optional[SentenceTransformer] = None

        # 按类型组织
        self.documents_by_type: Dict[str, List[AssetDocument]] = {}
        self.embeddings_by_type: Dict[str, np.ndarray] = {}
        self.indices_by_type: Dict[str, faiss.Index] = {}

    # ==========================================================================
    # Build
    # ==========================================================================

    def build(self, save: bool = True) -> List[AssetDocument]:
        """
        Build corpus + FAISS indices.
        """
        ingestor = AssetIngestor(self.config)
        self.documents = ingestor.build_documents()

        print(
            f"[AssetRAG] Building indices "
            f"(model={self.config.embedding_model})"
        )

        self.embedding_model = self.config.embedding_model

        self.encoder = SentenceTransformer(
            self.embedding_model,
            device=self.config.device,
        )

        grouped: Dict[str, List[AssetDocument]] = defaultdict(list)
        for doc in self.documents:
            doc_type = doc.metadata.get(
                "doc_type",
                "default",
            )
            grouped[doc_type].append(doc)
        grouped_docs = dict(grouped)
        
        self.documents_by_type.clear()
        self.embeddings_by_type.clear()
        self.indices_by_type.clear()

        for doc_type, docs in grouped_docs.items():
            texts = [doc.content for doc in docs]

            embeddings = self.encoder.encode(
                texts,
                batch_size=self.config.embedding_batch_size,
                convert_to_numpy=True,
                show_progress_bar=True,
                normalize_embeddings=True,
            ).astype("float32")

            index = faiss.IndexFlatIP(embeddings.shape[1])
            index.add(embeddings)

            self.documents_by_type[doc_type] = docs
            self.embeddings_by_type[doc_type] = embeddings
            self.indices_by_type[doc_type] = index

            print(
                f"[AssetRAG] Built index "
                f"(doc_type={doc_type}, num_docs={len(docs)})"
            )
        if save:
            self._save()

        print(
            f"[AssetRAG] Finished building "
            f"({len(self.documents)} documents)"
        )

        return self.documents

    # ==========================================================================
    # Load
    # ==========================================================================
    def load(self) -> List[AssetDocument]:
        """
        Load corpus + all FAISS indices from disk.
        """
        corpus_path = self.config.index_dir / "corpus.jsonl"

        if not corpus_path.exists():
            raise FileNotFoundError(
                f"Corpus not found: {corpus_path}\n"
                f"Please run build() first."
            )

        self.documents: List[AssetDocument] = []
        with corpus_path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    self.documents.append(
                        AssetDocument.from_dict(json.loads(line)))
        print(f"[AssetRAG] Loaded corpus: {corpus_path} ({len(self.documents)} documents)")
        
        meta_path = self.config.index_dir / "index_meta.json"

        if not meta_path.exists():
            raise FileNotFoundError(
                f"Index metadata not found: {meta_path}"
            )

        meta = json.loads(meta_path.read_text(encoding="utf-8"))

        self.embedding_model = meta["encoder"]
        self.encoder = SentenceTransformer(
            self.embedding_model,
            device=self.config.device,
        )

        self.documents_by_type.clear()
        self.embeddings_by_type.clear()
        self.indices_by_type.clear()

        grouped: Dict[str, List[AssetDocument]] = defaultdict(list)
        for doc in self.documents:
            doc_type = doc.metadata.get(
                "doc_type",
                "default",
            )
            grouped[doc_type].append(doc)
        grouped_docs = dict(grouped)

        for doc_type, docs in grouped_docs.items():
            index_path = self.config.index_dir / f"{doc_type}.faiss"
            if not index_path.exists():
                raise FileNotFoundError(
                    f"Missing FAISS index for doc_type={doc_type}: "
                    f"{index_path}"
                )

            index = faiss.read_index(str(index_path))

            self.documents_by_type[doc_type] = docs
            self.indices_by_type[doc_type] = index

        print(
            f"[AssetRAG] Loaded indices "
            f"({len(self.documents)} documents)"
        )

        return self.documents

    # ==========================================================================
    # Retrieve
    # ==========================================================================

    def retrieve(
        self,
        query: str,
        doc_type: Optional[List[str]] = None,
        top_k: Optional[int] = None,
    ) -> List[Tuple[AssetDocument, float]]:
        if self.encoder is None:
            raise RuntimeError(
                "Encoder not initialized. "
                "Please call build() or load()."
            )
        if not self.indices_by_type:
            raise RuntimeError(
                "No indices loaded. "
                "Please call build() or load()."
            )

        k = top_k or self.config.retrieval_top_k

        query_vec = self.encoder.encode(
            [query],
            convert_to_numpy=True,
            normalize_embeddings=True,
        ).astype("float32")

        results: List[Tuple[AssetDocument, float]] = []
        if doc_type:
            index = self.indices_by_type.get(doc_type)
            docs = self.documents_by_type[doc_type]
            scores, indices = index.search(query_vec,min(k, len(docs)),)
            for idx, score in zip(indices[0].tolist(),scores[0].tolist(),):
                if idx < 0:
                    continue
                results.append((docs[idx],float(score)))
        else:
            search_types =  list(self.indices_by_type.keys())
            for doc_type in search_types:
                index = self.indices_by_type.get(doc_type)
                if index is None:
                    continue
                docs = self.documents_by_type[doc_type]
                scores, indices = index.search(query_vec,min(k, len(docs)),)
                for idx, score in zip(indices[0].tolist(),scores[0].tolist(),):
                    if idx < 0:
                        continue
                    results.append((docs[idx],float(score)))

        results.sort(
            key=lambda item: item[1],
            reverse=True,
        )
        return results[:k]

    # ==========================================================================
    # Save
    # ==========================================================================
    def _save(self) -> None:
        """
        Save corpus + all indices.
        """
        self.config.index_dir.mkdir(parents=True,exist_ok=True,)
        
        corpus_path = self.config.index_dir / "corpus.jsonl"

        with corpus_path.open("w",encoding="utf-8",) as f:
            for doc in self.documents:
                f.write(json.dumps(doc.to_dict(),ensure_ascii=False,)+ "\n")
        type_metadata = {}        
        for doc_type, index in self.indices_by_type.items():
            faiss.write_index(
                index,
                str(self.config.index_dir / f"{doc_type}.faiss"),
            )
            doc_ids = [doc.doc_id for doc in self.documents_by_type[doc_type]]
            type_metadata[doc_type] = {
                "num_docs": len(doc_ids),
                "doc_ids": doc_ids,
                "dim": index.d,
                "index_file":f"{doc_type}.faiss",
            }
        meta = {
            "encoder": self.embedding_model,
            "total_documents": len(self.documents),
            "doc_types": list(self.indices_by_type.keys()),
            "type_metadata": type_metadata,
        }
        meta_path = self.config.index_dir / "index_meta.json"
        meta_path.write_text(
            json.dumps(meta, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(
            f"[AssetRAG] Saved indices to "
            f"{self.config.index_dir}"
        )
__all__ = [
    "AssetRAG",
]