from __future__ import annotations
from typing import Any, Dict, List
from .base import Tool, ToolContext, ToolResult, register_tool

@register_tool
class RetrieveTool(Tool):
    name = "retrieve_tool"
    description = "Search the retrieval database for reusable 3D assets or scene layout templates using natural language. Use this tool when the user requests robots, workcells, furniture, equipment, or industrial scene layouts."
    schema = {
        "type": "function",
        "function": {
            "name": name,
            "description": description,
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string", 
                        "description": "Natural language query to search for assets or scene layouts"},
                    "top_k": {
                        "type": "integer", 
                        "description": "Maximum number of results"},
                    "doc_type": {
                        "type": "string", 
                        "enum":["asset","scene_template"], 
                        "description": "Type of documents to retrieve"},
                },
                "required": ["query","doc_type"],
                "additionalProperties": False,
            },
        },
    }

    def run(self, context: ToolContext, query: str, doc_type: str, top_k: int =5) -> ToolResult:
        if not query:
            return ToolResult(ok=False, error="query is empty")
        # RAG 检索
        results = context.rag.retrieve(query, top_k=top_k, doc_type=doc_type)
        items: List[Dict[str, Any]] = []
        if doc_type == "asset":
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
        elif doc_type == "scene_template":
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
        return ToolResult(
            ok=True,
            data={"results": items, "count":len(items), "query": query, "doc_type":doc_type}
        )