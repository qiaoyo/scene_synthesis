from __future__ import annotations
import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from .asset_loader import AssetIngestor
from .config import ProjectConfig
from .data_models import AssetDocument
from sentence_transformers import SentenceTransformer  # noqa: WPS433
import faiss  # noqa: WPS433
# ---------- 顶层封装 ----------
class AssetRAG:
    """统一的检索入口；优先使用 FAISS，依赖缺失时回退关键词。"""

    def __init__(self, config: ProjectConfig):
        self.config = config
        self.documents: List[AssetDocument] = []
        self.index = None
        self.embedding_model = None
        self.encoder = None
        
    # 构建 
    def build(self, save: bool = True) -> List[AssetDocument]:
        #加载数据
        ingestor = AssetIngestor(self.config)
        self.documents = ingestor.build_documents()
        #构建 FAISS 索引
        print(f"[AssetRAG] 构建 FAISS 索引，模型: {self.config.embedding_model}")
        self.embedding_model = self.config.embedding_model
        self.encoder = SentenceTransformer(
            self.embedding_model, 
            device=self.config.device)
        #生成向量
        texts = [d.content for d in self.documents]
        embeddings = self.encoder.encode(
            texts,
            batch_size=self.config.embedding_batch_size,
            convert_to_numpy=True,
            show_progress_bar=True, 
            normalize_embeddings=True, # 归一化以便使用内积计算余弦相似度
        )
        #创建索引
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dim)
        self.index.add(embeddings.astype("float32"))
        
        #保存到磁盘
        if save:
            self._save()
            print(f"[AssetRAG] 构建完成，共 {len(self.documents)} 条文档")
        return self.documents

    def load(self) -> List[AssetDocument]:
        # 从磁盘加载语料和（如果可用）FAISS 索引，构建检索器实例。
        corpus_path = self.config.index_dir / "corpus.jsonl"
        if not corpus_path.exists():
            raise FileNotFoundError(
                f"Corpus file not found at {corpus_path}."
                f"请先调用 build() 方法构建索引，或检查配置中的 index_dir 是否正确。"
            )
        self.documents: List[AssetDocument] = []
        with corpus_path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    self.documents.append(
                        AssetDocument.from_dict(json.loads(line)))
        print(f"[AssetRAG] 已加载语料: {corpus_path} ({len(self.documents)} 条)")
        
        #加载FAISS索引
        index_path = self.config.index_dir / "vectors.faiss"
        meta_path = self.config.index_dir / "index_meta.json"
        
        if not (index_path.exists() and meta_path.exists()):
            raise FileNotFoundError(
                f"FAISS index files missing in {self.config.index_dir}."
                f"请先调用 build() 方法构建索引，或检查配置中的 index_dir 是否正确。"
            )
        #加载元数据
        with meta_path.open("r", encoding="utf-8") as f:
            meta = json.load(f)
        if meta.get("doc_ids") != [d.doc_id for d in self.documents]:
            raise RuntimeError(
                "FAISS index doc_ids 与 corpus.jsonl 不一致，请删除 vectors.faiss 后重建。"
            )
            
        #加载索引和编码器
        self.index = faiss.read_index(str(index_path))
        self.embedding_model = meta["encoder"]
        self.encoder = SentenceTransformer(
            self.embedding_model, 
            device=self.config.device)

        print(f"[AssetRAG] 加载完成，共 {len(self.documents)} 条文档")
        return self.documents

     # ========== 查询检索 ==========
    def retrieve(
        self,
        query: str,
        top_k: Optional[int] = None,
        filters: Optional[Dict[str, Any]] = None,
    ) -> List[Tuple[AssetDocument, float]]:
        """检索相关文档"""
        if self.index is None or self.encoder is None:
            raise RuntimeError("索引未初始化，请先调用 build() 或 load()")
        
        k = top_k or self.config.retrieval_top_k
        
        # 编码查询
        query_vec = self.encoder.encode(
            [query],
            convert_to_numpy=True,
            normalize_embeddings=True
        ).astype("float32")
        
        # 检索（如果需要过滤，多召回一些）
        oversample = len(self.documents) if filters else k
        search_k = min(oversample, len(self.documents))
        scores, indices = self.index.search(query_vec, search_k)
        
        # 过滤和整理结果
        results = []
        for idx, score in zip(indices[0].tolist(), scores[0].tolist()):
            if idx < 0:
                continue
            doc = self.documents[idx]
            #直接内联过滤逻辑，不调用外部函数
            if filters:
                match = True
                for key, expected in filters.items():
                    actual = doc.metadata.get(key)
                    if isinstance(expected, (list, tuple, set)):
                        if actual not in expected:
                            match = False
                            break
                    else:
                        if actual != expected:
                            match = False
                            break
                if not match:
                    continue
            results.append((doc, float(score)))
            
            if len(results) >= k:
                break
        
        return results
    
    # ========== 辅助方法 ==========
    def _save(self) -> None:
        """保存索引到磁盘"""
        # 创建目录
        self.config.index_dir.mkdir(parents=True, exist_ok=True)
        
        # 保存语料库
        corpus_path = self.config.index_dir / "corpus.jsonl"
        with corpus_path.open("w", encoding="utf-8") as f:
            for doc in self.documents:
                f.write(json.dumps(doc.to_dict(), ensure_ascii=False) + "\n")
        
        # 保存 FAISS 索引
        faiss.write_index(self.index, str(self.config.index_dir / "vectors.faiss"))
        
        # 保存元数据
        meta = {
            "doc_ids": [d.doc_id for d in self.documents],
            "dim": self.index.d,
            "encoder": self.embedding_model,
            "num_docs": len(self.documents),
        }
        meta_path = self.config.index_dir / "index_meta.json"
        meta_path.write_text(
            json.dumps(meta, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
        print(f"[AssetRAG] 索引已保存到: {self.config.index_dir}")
    
    def info(self) -> Dict[str, Any]:
        """获取索引信息"""
        return {
            "num_documents": len(self.documents),
            "embedding_model": self.embedding_model,
            "index_dimension": self.index.d if self.index else None,
            "index_dir": str(self.config.index_dir),
        }

__all__ = [
    "AssetRAG"
]