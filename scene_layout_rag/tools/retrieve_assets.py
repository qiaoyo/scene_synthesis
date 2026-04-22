"""RAG retrieval tool -- searches the asset vector store on demand."""
from __future__ import annotations

from typing import Any, Dict

from .base import BaseTool, ToolResult


class RetrieveAssetsTool(BaseTool):
    name = "retrieve_assets"
    description = "在资产库中执行语义检索，返回匹配的资产列表（不修改场景）"

    parameters_schema = {
        "query": {
            "type": "str",
            "required": True,
            "description": "自然语言检索查询，如 '分拣用传送带，长度约2m'",
        },
        "top_k": {
            "type": "int",
            "required": False,
            "description": "返回结果数量，默认5",
        },
        "category": {
            "type": "str",
            "required": False,
            "description": "按资产类别过滤，如 'Conveyor'、'Rack'",
        },
    }

    @property
    def modifies_scene(self) -> bool:
        return False

    def execute(self, params: Dict[str, Any], **ctx: Any) -> ToolResult:
        query = params.get("query", "")
        if not query:
            return ToolResult(ok=False, error="query 参数不能为空")

        top_k = int(params.get("top_k", 5))
        category = params.get("category")

        embedder = ctx.get("embedder")
        vector_store = ctx.get("vector_store")
        if embedder is None or vector_store is None:
            return ToolResult(ok=False, error="embedder 或 vector_store 未提供")

        query_vec = embedder.embed_query(query)
        hits = vector_store.search(query_vec, top_k=top_k * 2 if category else top_k)

        assets = []
        for hit in hits:
            doc = hit.document
            cat = doc.metadata.get("asset_category", doc.doc_id)
            if category and cat != category:
                continue
            assets.append({
                "asset_id": cat,
                "doc_id": doc.doc_id,
                "usd_path": doc.metadata.get("usd_path", ""),
                "bbox": doc.metadata.get("bbox", {}),
                "description": doc.content[:200],
                "score": round(hit.score, 3),
            })
            if len(assets) >= top_k:
                break

        return ToolResult(ok=True, result={
            "query": query,
            "count": len(assets),
            "assets": assets,
        })
