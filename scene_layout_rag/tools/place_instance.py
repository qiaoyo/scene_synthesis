from __future__ import annotations
from typing import Any, Dict, List, Optional
from ..data_models import AssetDocument, Instance
from .base import Tool, ToolContext, ToolResult,register_tool

@register_tool
class PlaceInstanceTool(Tool):
    schema = {
        "type": "function",
        "function": {
            "name": "place_instance",
            "description": "Place a new asset instance into the scene.",
            "parameters": {
                "type": "object",
                "properties": {
                    "doc_id": {
                        "type": "string",
                        "description": "Asset document ID from retrieve_assets result."
                    },
                    "position": {
                        "type": "array",
                        "items": {"type": "number"},
                        "minItems": 3,
                        "maxItems": 3,
                        "description": "[x, y, z] in meters."
                    },
                    "rotation_deg": {
                        "type": "number",
                        "description": "Rotation around Z axis in degrees, default 0."
                    }
                },
                "required": ["doc_id", "position"],
                "additionalProperties": False
            },
        }
    }

    def run(self, context: ToolContext, doc_id: str, position: list[float], rotation_deg: float = 0.0) -> ToolResult:
        for d in context.rag.documents:
            if d.doc_id == doc_id:
                doc = d
        if doc is None:
            return ToolResult(ok=False, error=f"asset_doc_id 不在语料库中: {doc_id}")
        if doc.metadata.get("doc_type") != "asset":
            return ToolResult(ok=False, error=f"asset_doc_id 必须指向 doc_type=asset 的文档: {doc_id}")
        asset_type = str(doc.metadata.get("asset_type"))
        usd_path = str(doc.metadata.get("usd_path"))
        bbox = doc.metadata.get("bbox")
        bbox_size = bbox.get("size",[1.0,1.0,1.0])
        instance_id = str(doc.metadata.get("instance_id"))
        if instance_id in context.scene.state.instances:
            return ToolResult(ok=False, error=f"instance_id 已存在: {instance_id}")
        inst = Instance(
            instance_id=instance_id,
            asset_type=asset_type,
            asset_doc_id=doc_id,
            usd_path=usd_path,
            position=position,
            rotation_deg=rotation_deg,
            bbox_size=bbox_size,
            tags=dict(doc.metadata.get("tags") or {}),
            description=str(doc.metadata.get("description") or ""),
        )
        context.scene.add_instance(inst)
        return ToolResult(ok=True, data={
            "instance_id": instance_id,
            "asset_type": asset_type,
            "usd_path": usd_path,
            "position": inst.position,
            "bbox_size": inst.bbox_size,
            "tags": inst.tags,
            "description": inst.description,
        })