from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..data_models import AssetDocument
from .base import Tool, ToolContext, ToolResult, make_openai_tool_schema, register_tool


def _retrieve_documents(
    context: ToolContext,
    query: str,
    top_k: int,
    doc_type: str,
    asset_type: Optional[Any] = None,
    scene_id: Optional[str] = None,
) -> ToolResult:
    query = query.strip()
    if not query:
        return ToolResult(ok=False, error="query is empty")
    filters: Dict[str, Any] = {"doc_type": doc_type}
    if asset_type is not None:
        filters["asset_type"] = asset_type
    if scene_id:
        filters["scene_id"] = scene_id
    results = context.rag.retrieve(query, top_k=top_k, filters=filters)
    items: List[Dict[str, Any]] = []
    for doc, score in results:
        items.append({
            "doc_id": doc.doc_id,
            "score": round(float(score), 4),
            "asset_type": doc.metadata.get("asset_type"),
            "doc_type": doc.metadata.get("doc_type"),
            "usd_path": doc.metadata.get("usd_path"),
            "instance_id": doc.metadata.get("instance_id"),
            "bbox": doc.metadata.get("bbox"),
            "tags": doc.metadata.get("tags"),
            "description": doc.metadata.get("description"),
            "content": doc.content,
            "preview": doc.content[:240],
        })
    return ToolResult(ok=True, data={"catch": items, "query": query, "filters": filters})

def _retrieve_documents_scene(
    context: ToolContext,
    query: str,
    top_k: int,
    doc_type: str,
    asset_type: Optional[Any] = None,
    scene_id: Optional[str] = None,
) -> ToolResult:
    query = query.strip()
    if not query:
        return ToolResult(ok=False, error="query is empty")
    filters: Dict[str, Any] = {"doc_type": doc_type}
    if asset_type is not None:
        filters["asset_type"] = asset_type
    if scene_id:
        filters["scene_id"] = scene_id
    results = context.rag.retrieve(query, top_k=top_k, filters=filters)
    items: List[Dict[str, Any]] = []
    for doc, score in results:
        items.append({
            "doc_id": doc.doc_id,
            "score": round(float(score), 4),
            "doc_type": doc.metadata.get("doc_type"),
            "scene_id": doc.metadata.get("scene_id"),
            "scene_name": doc.metadata.get("scene_name"),
            "template_detail": doc.metadata.get("template_detail"),
            "content": doc.content,
            "preview": doc.content[:240],
        })
    return ToolResult(ok=True, data={"catch": items, "query": query, "filters": filters})

@register_tool
class RetrieveSceneTemplateTool(Tool):
    name = "retrieve_scene_template"
    description = "检索已有场景模板，用于参考空间组织、对象组合和相对布局；返回结果不能用于 place_instance。"
    schema = make_openai_tool_schema(
        name,
        description,
        {
            "query": {"type": "string", "description": "自然语言布局查询，例如 'sorting cell conveyor robot workbench layout'"},
            "top_k": {"type": "integer", "description": "返回条数，默认 5"},
            "scene_id": {"type": "string", "description": "限定场景类型，例如 assembly / warehouse / sorting"},
        },
        required=["query", "top_k"],
    )

    def run(self, context: ToolContext, **kwargs: Any) -> ToolResult:
        return _retrieve_documents_scene(
            context=context,
            query=str(kwargs["query"]),
            top_k=int(kwargs.get("top_k", 5)),
            doc_type="scene_template",
            scene_id=kwargs.get("scene_id"),
        )

    def run_test(self, context: ToolContext) -> ToolResult:
        doc = _first_doc(context, "scene_template")
        if doc is None:
            return ToolResult(ok=False, error="retrieve_scene_template run_test found no scene_template docs")
        result = self(
            context,
            query=_test_query(doc),
            top_k=1,
            scene_id=doc.metadata.get("scene_id"),
        )
        if not result.ok:
            return result
        if not result.data.get("hits"):
            return ToolResult(ok=False, error="retrieve_scene_template run_test returned no hits")
        if result.data["hits"][0].get("doc_type") != "scene_template":
            return ToolResult(ok=False, error="retrieve_scene_template run_test returned non-template doc")
        return ToolResult(ok=True, data={"tested": self.name})


@register_tool
class RetrieveAssetsTool(Tool):
    name = "retrieve_assets"
    description = "只检索可实例化资产文档，返回含 USD 路径和 bbox 的 doc_id；这些 doc_id 才能传给 place_instance。"
    schema = make_openai_tool_schema(
        name,
        description,
        {
            "query": {"type": "string", "description": "自然语言资产查询，例如 'small conveyor for boxes'"},
            "top_k": {"type": "integer", "description": "返回条数，默认 5"},
            "asset_type": {
                "anyOf": [
                    {"type": "string"},
                    {"type": "array", "items": {"type": "string"}},
                ],
                "description": "限定资产类别，例如 'Conveyor'",
            },
        },
        required=["query", "top_k"],
    )

    def run(self, context: ToolContext, **kwargs: Any) -> ToolResult:
        return _retrieve_documents(
            context=context,
            query=str(kwargs["query"]),
            top_k=int(kwargs.get("top_k", 5)),
            doc_type="asset",
            asset_type=kwargs.get("asset_type"),
        )

    def run_test(self, context: ToolContext) -> ToolResult:
        doc = _first_doc(context, "asset")
        if doc is None:
            return ToolResult(ok=False, error="retrieve_assets run_test found no asset docs")
        result = self(
            context,
            query=_test_query(doc),
            top_k=1,
            asset_type=doc.metadata.get("asset_type"),
        )
        if not result.ok:
            return result
        if not result.data.get("hits"):
            return ToolResult(ok=False, error="retrieve_assets run_test returned no hits")
        if result.data["hits"][0].get("doc_type") != "asset":
            return ToolResult(ok=False, error="retrieve_assets run_test returned non-asset doc")
        return ToolResult(ok=True, data={"tested": self.name})


def _first_doc(context: ToolContext, doc_type: str) -> Optional[AssetDocument]:
    for doc in context.rag.documents:
        if doc.metadata.get("doc_type") == doc_type:
            return doc
    return None


def _test_query(doc: AssetDocument) -> str:
    return doc.content.splitlines()[0] if doc.content else doc.doc_id