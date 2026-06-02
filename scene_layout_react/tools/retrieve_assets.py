from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .base import Tool, ToolContext, ToolResult, register_tool

SUPPORT_ASSET_TYPES = [
    "AGV", "Box", "Conveyor", "Forklift", "IndustrialRobot",
        "Pallet", "IndustrialPart", "Rack", "Scene", "Workbench"
]

@register_tool
class RetrieveAssetTool(Tool):
    name = "retrieve_asset"
    description = (
        "Search reusable 3D asset documents. Use expected_asset_type when the "
        "user requests a specific asset category; results are validated against "
        "metadata.asset_type before returning."
    )
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
                        "description": "Natural language query for asset retrieval.",
                    },
                    "top_k": {
                        "type": "integer",
                        "description": "Maximum number of validated asset results.",
                    },
                    "expected_asset_type": {
                        "type": "string",
                        "enum": SUPPORT_ASSET_TYPES,
                        "description": (
                            "Expected asset category from the user command. When omitted, the tool tries to infer it from query."
                        ),
                    },
                },
                "required": ["query","expected_asset_type"],
                "additionalProperties": False,
            },
        },
    }

    def run(
        self,
        context: ToolContext,
        query: str,
        top_k: int = 1,
        expected_asset_type: Optional[str] = None,
    ) -> ToolResult:
        if not query:
            return ToolResult(ok=False, error="query is empty")
        try:
            top_k = int(top_k)
        except Exception:
            return ToolResult(ok=False, error="top_k must be an integer")
        if top_k <= 0:
            return ToolResult(ok=False, error="top_k must be positive")

        if expected_asset_type not in SUPPORT_ASSET_TYPES:
            return ToolResult(
                ok=False,
                error=f"expected_asset_type must be one of {SUPPORT_ASSET_TYPES}"
            )
        
        raw_results = context.rag.retrieve(query, top_k=top_k * 5, doc_type="asset")
        
        if not raw_results:
            return ToolResult(
                ok=True,
                data={
                    "results": [],
                    "count": 0,
                    "query": query,
                    "asset_type": expected_asset_type,
                    "doc_type": "asset"
                }
            )
        
        filtered_items: List[Dict[str, Any]] = []
        for doc, score in raw_results:
            asset_type = doc.metadata.get("asset_type", "")
            # 类型完全匹配
            if asset_type == expected_asset_type:
                filtered_items.append({
                    "doc_id": doc.doc_id,
                    "score": round(float(score), 4),
                    "asset_type": asset_type,
                })
                
        #final_items = filtered_items[:top_k] 
        final_items = random.sample(filtered_items, k=min(top_k, len(filtered_items)))    
        return ToolResult(
            ok=True,
            data={
                "results": final_items,
                "count": len(final_items),
                "query": query,
                "doc_type": "asset",
                "asset_type": expected_asset_type,
            },
        )

@register_tool
class RetrieveSceneTemplateTool(Tool):
    name = "retrieve_scene_template"
    description = (
        "Search scene layout template documents. Use expected_scene_category "
        "and detail_level when the user asks for a specific scene category or "
        "template verbosity."
    )
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
                        "description": "Natural language query for scene template retrieval.",
                    },
                    "top_k": {
                        "type": "integer",
                        "description": "Maximum number of validated scene template results.",
                    },
                },
                "required": ["query"],
                "additionalProperties": False,
            },
        },
    }

    def run(
        self,
        context: ToolContext,
        query: str,
        top_k: int = 1,
    ) -> ToolResult:
        if not query:
            return ToolResult(ok=False, error="query is empty")
        try:
            top_k = int(top_k)
        except Exception:
            return ToolResult(ok=False, error="top_k must be an integer")
        if top_k <= 0:
            return ToolResult(ok=False, error="top_k must be positive")
        results = context.rag.retrieve(query, top_k=top_k, doc_type="scene_template")
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
        
        return ToolResult(
            ok=True,
            data={
                "results": items,
                "count": len(items),
                "query": query,
                "doc_type": "scene_template",
            },
        )

__all__ = [
    "RetrieveAssetTool",
    "RetrieveSceneTemplateTool",
]
