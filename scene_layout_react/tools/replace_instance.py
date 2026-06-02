from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..data_models import AssetDocument
from .base import Tool, ToolContext, ToolResult, register_tool


@register_tool
class ReplaceInstanceTool(Tool):
    schema = {
        "type": "function",
        "function": {
            "name": "replace_instance",
            "description": (
                "Replace an existing scene instance with a different retrieved asset of the same or requested asset type. The scene instance ID, transform, and support relations are preserved; only the asset metadata is changed. Use this when an instance repeatedly fails collision or support validation."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "instance_id": {
                        "type": "string",
                        "description": "Existing scene instance ID to replace.",
                    },
                    "query": {
                        "type": "string",
                        "description": (
                            "Natural language retrieval query for the replacement. "
                            "When omitted, the old instance asset type and "
                            "description are used."
                        ),
                    },
                    "top_k": {
                        "type": "integer",
                        "description": "Number of candidate replacements to consider.",
                    },
                },
                "required": ["instance_id","query"],
                "additionalProperties": False,
            },
        },
    }

    def run(
        self,
        context: ToolContext,
        instance_id: str,
        query: Optional[str] = None,
        top_k: int = 5,
    ) -> ToolResult:
        if instance_id not in context.scene.state.instances:
            return ToolResult(ok=False, error=f"instance not found: {instance_id}")

        try:
            top_k = int(top_k)
        except Exception:
            return ToolResult(ok=False, error="top_k must be an integer")
        if top_k <= 0:
            return ToolResult(ok=False, error="top_k must be positive")

        inst = context.scene.state.instances[instance_id]
        replacement_type = inst.asset_type

        retrieval_query = query
        if not retrieval_query.strip():
            return ToolResult(ok=False, error="query is empty")

        excluded_doc_ids = {inst.asset_doc_id}

        raw_results = context.rag.retrieve(
            retrieval_query,
            top_k=max(top_k * 8, 5),
            doc_type="asset",
        )
        candidates: List[tuple[AssetDocument, float]] = []

        for doc, score in raw_results:
            if doc.doc_id in excluded_doc_ids:
                continue
            if doc.metadata.get("doc_type") != "asset":
                continue
            if doc.metadata.get("asset_type") != replacement_type:
                continue
            candidates.append((doc, score))

        preview_items = []
        for doc,score in candidates[:top_k]:
            preview_items.append({
                "doc_id": doc.doc_id,
                "score": round(float(score), 4),
                "asset_type": doc.metadata.get("asset_type"),
                "usd_path": doc.metadata.get("usd_path"),
                "instance_id": doc.metadata.get("instance_id"),
                "bbox": doc.metadata.get("bbox"),
                "tags": doc.metadata.get("tags"),
                "description": doc.metadata.get("description"),
                "content": doc.content,
                "preview": doc.content[:240],
            })
            
        if not candidates:
            return ToolResult(
                ok=False,
                data={
                    "instance_id": instance_id,
                    "query": retrieval_query,
                    "expected_asset_type": replacement_type,
                    "excluded_doc_ids": sorted(excluded_doc_ids),
                    "candidates": preview_items,
                },
                error="no replacement asset found after excluding the current instance asset"
            )

        doc, score = candidates[0]

        inst.instance_id = doc.metadata.get("instance_id")
        inst.asset_type = str(doc.metadata.get("asset_type") or replacement_type)
        inst.asset_doc_id = doc.doc_id
        inst.usd_path = str(doc.metadata.get("usd_path") or "")
        inst.bbox = doc.metadata.get("bbox") or inst.bbox
        inst.tags = dict(doc.metadata.get("tags") or {})
        inst.description = str(doc.metadata.get("description") or "")

        children = list(context.scene.state.support_children.get(instance_id, []))
        inherited_relations = {
            "parent": inst.parent_instance_id,
            "children": children,
        }

        return ToolResult(
            ok=True,
            data={
                "replaced_instance_id": instance_id,
                "new_instance_id": inst.instance_id,
                "replaced": True,
                "next_recommended_tools": [
                    "check_collision",
                    "check_support",
                    "simulate_step",
                ],
            },
        )
