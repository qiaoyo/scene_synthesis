from __future__ import annotations

import random
from typing import Any, Dict, List

from .base import Tool, ToolContext, ToolResult, register_tool

SUPPORT_ASSET_TYPES = [
    "AGV", "Box", "Conveyor", "Forklift", "IndustrialRobot",
        "Pallet", "IndustrialPart", "Rack", "Scene", "Workbench"
]

@register_tool
class RetrieveAssetTool(Tool):
    name = "retrieve_asset"
    description = (
        "Search reusable 3D asset documents for one or more assets. "
        "Each asset request must provide a query and expected asset_type. "
        "Results are validated against metadata.asset_type before returning."
    )
    schema = {
        "type": "function",
        "function": {
            "name": name,
            "description": description,
            "parameters": {
                "type": "object",
                "properties": {
                    "assets":{
                        "type": "array",
                        "description": "List of asset retrieval requests.", 
                        "minItems": 1,
                        "items": {
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
                        }
                    },
                },
                "required": ["assets"],
                "additionalProperties": False,
            },
        },
    }

    def run(
        self,
        context: ToolContext,
        assets: List[Dict[str, Any]],
    ) -> ToolResult:
        all_results: List[Dict[str, Any]] = []
        
        for req in assets:
            query = req.get("query", "")
            top_k = req.get("top_k", 1)
            asset_type = req.get("expected_asset_type", "")
            
            if not query:
                all_results.append({
                    "query": query,
                    "asset_type": asset_type,
                    "error": "query is empty",
                    "results": [],
                })
                continue
            
            if top_k <= 0:
                all_results.append({
                    "query": query,
                    "asset_type": asset_type,
                    "error": "top_k must be positive",
                    "results": [],
                })
                continue
            
            if asset_type not in SUPPORT_ASSET_TYPES:
                all_results.append({
                    "query": query,
                    "asset_type": asset_type,
                    "error": f"expected_asset_type must be one of {SUPPORT_ASSET_TYPES}",
                    "results": [],
                })
                continue
        
            raw_results = context.rag.retrieve(query, top_k=top_k * 5, doc_type="asset")
        
            if not raw_results:
                all_results.append({
                    "query": query,
                    "asset_type": asset_type,
                    "count": 0,
                    "results": [],
                })
                continue
        
            filtered_items: List[Dict[str, Any]] = []
            for doc, score in raw_results:
                doc_asset_type = doc.metadata.get("asset_type", "")
                # 类型完全匹配
                if doc_asset_type == asset_type:
                    filtered_items.append({
                        "doc_id": doc.doc_id,
                        "score": round(float(score), 4),
                        "asset_type": asset_type,
                        "instance_id":doc.metadata.get("instance_id"),
                        "usd_path":doc.metadata.get("usd_path"),
                        "bbox":doc.metadata.get("bbox"),
                        "tags":doc.metadata.get("tags") or {},
                        "description":doc.metadata.get("description") or "",
                    })
                
            final_items = random.sample(filtered_items, k=min(top_k, len(filtered_items)))
            
            all_results.append({
                "query": query,
                "asset_type": asset_type,
                "count": len(final_items),
                "results": final_items,
            })
            
        context.scene.remember_asset_retrievals(all_results)   
             
        return ToolResult(
            ok=True,
            data={
                "results": all_results,
                "count": len(all_results),
                "doc_type": "asset",
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
