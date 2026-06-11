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
                "Replace an existing scene instance with a different asset of "
                "the same asset_type. The scene instance ID is migrated to the "
                "replacement asset instance_id with conflict-safe suffixing, "
                "while transform and support relations are preserved. Use this "
                "after repeated collision, support, or stability failures when "
                "moving the existing instance is insufficient."
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
                            "Optional natural language retrieval query for the "
                            "replacement. When omitted, the current asset type "
                            "and description are used."
                        ),
                    },
                    "top_k": {
                        "type": "integer",
                        "minimum": 1,
                        "description": "Number of candidate replacements to consider.",
                    },
                },
                "required": ["instance_id", "query"],
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

        retrieval_query = (query or f"{inst.asset_type} {inst.description or ''}").strip()
        if not retrieval_query:
            retrieval_query = inst.asset_type
        if not retrieval_query:
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

        replacement_base_id = str(doc.metadata.get("instance_id") or "").strip()
        if not replacement_base_id:
            return ToolResult(
                ok=False,
                data={
                    "replacement_doc_id": doc.doc_id,
                    "query": retrieval_query,
                },
                error="replacement asset metadata is missing instance_id",
            )

        old_instance_id = instance_id
        new_instance_id = _unique_instance_id(
            base_id=replacement_base_id,
            existing_ids=context.scene.state.instances,
            current_id=old_instance_id,
        )
        _rename_scene_instance(
            scene=context.scene,
            old_id=old_instance_id,
            new_id=new_instance_id,
        )

        inst = context.scene.state.instances[new_instance_id]
        inst.asset_type = str(doc.metadata.get("asset_type") or replacement_type)
        inst.asset_doc_id = doc.doc_id
        inst.usd_path = str(doc.metadata.get("usd_path") or "")
        inst.bbox = doc.metadata.get("bbox") or inst.bbox
        inst.tags = dict(doc.metadata.get("tags") or {})
        inst.description = str(doc.metadata.get("description") or "")

        return ToolResult(
            ok=True,
            data={
                "old_instance_id": old_instance_id,
                "new_instance_id": new_instance_id,
                "replacement_base_instance_id": replacement_base_id,
                "renamed": old_instance_id != new_instance_id,
                "replaced": True,
                "next_recommended_tools": [
                    "check_collision",
                    "check_support",
                    "simulate_step",
                ],
            },
        )


def _unique_instance_id(
    base_id: str,
    existing_ids: Dict[str, Any],
    current_id: str,
) -> str:
    if base_id == current_id or base_id not in existing_ids:
        return base_id

    index = 1
    while True:
        candidate = f"{base_id}_{index}"
        if candidate == current_id or candidate not in existing_ids:
            return candidate
        index += 1


def _rename_scene_instance(
    scene: Any,
    old_id: str,
    new_id: str,
) -> None:
    inst = scene.state.instances[old_id]
    if old_id != new_id:
        scene.state.instances.pop(old_id)
        scene.state.instances[new_id] = inst

    inst.instance_id = new_id

    for parent_id, children in list(scene.state.support_children.items()):
        scene.state.support_children[parent_id] = _replace_child_id(
            children,
            old_id=old_id,
            new_id=new_id,
        )

    if old_id in scene.state.support_children:
        old_children = scene.state.support_children.pop(old_id)
        existing_children = scene.state.support_children.get(new_id, [])
        scene.state.support_children[new_id] = _merge_children(
            existing_children,
            old_children,
        )

    for child_id, child in scene.state.instances.items():
        if child_id == new_id:
            continue
        if child.parent_instance_id == old_id:
            child.parent_instance_id = new_id


def _replace_child_id(
    children: List[str],
    old_id: str,
    new_id: str,
) -> List[str]:
    replaced = [
        new_id if child_id == old_id else child_id
        for child_id in children
    ]
    return _merge_children([], replaced)


def _merge_children(
    first: List[str],
    second: List[str],
) -> List[str]:
    merged: List[str] = []
    seen: set[str] = set()

    for child_id in list(first) + list(second):
        if child_id in seen:
            continue
        seen.add(child_id)
        merged.append(child_id)

    return merged
