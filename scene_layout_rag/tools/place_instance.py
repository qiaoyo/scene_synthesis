"""place_instance — 在场景中新增一个资产实例。

输入要求：必须给出 ``asset_doc_id``（语料库里查到的真实资产）；位置 ``position``
必填；``bbox_size`` 不传时从资产文档读取；可选 ``parent_instance_id`` 把
新实例直接登记为某个已有实例的支撑子项。
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..data_models import AssetDocument, Instance
from .base import Tool, ToolContext, ToolResult, make_openai_tool_schema, register_tool


@register_tool
class PlaceInstanceTool(Tool):
    name = "place_instance"
    description = "在场景中放置一个新资产实例。必须先用 retrieve_assets 拿到 asset_doc_id。"
    schema = make_openai_tool_schema(
        name,
        description,
        {
            "asset_doc_id": {"type": "string", "description": "来自 corpus 的资产文档 id"},
            "position": {
                "type": "array",
                "items": {"type": "number"},
                "minItems": 3,
                "maxItems": 3,
                "description": "[x, y, z]，米",
            },
            "rotation_deg": {"type": "number", "description": "绕 Z 轴旋转角度，默认 0"},
            "bbox_size": {
                "type": "array",
                "items": {"type": "number"},
                "minItems": 3,
                "maxItems": 3,
                "description": "[sx, sy, sz]，缺省取资产文档的 bbox.size",
            },
            "instance_id": {"type": "string", 
                            "description": "查看retrieve_assets返回结果里 instance_id 字段，必须保证唯一性，不要随意编造"},
            "parent_instance_id": {"type": "string", 
                                   "description": "若指定，则同时登记支撑关系"},
        },
        required=["asset_doc_id", "position"],
    )

    def run(self, context: ToolContext, **kwargs: Any) -> ToolResult:
        doc_id = str(kwargs["asset_doc_id"])
        position = _validate_vec3(kwargs["position"], "position")
        rotation = float(kwargs.get("rotation_deg", 0.0))

        doc = _find_doc(context, doc_id)
        if doc is None:
            return ToolResult(ok=False, error=f"asset_doc_id 不在语料库中: {doc_id}")
        if doc.metadata.get("doc_type") != "asset":
            return ToolResult(ok=False, error=f"asset_doc_id 必须指向 doc_type=asset 的文档: {doc_id}")

        asset_type = str(doc.metadata.get("asset_type") or "Unknown")
        usd_path = str(doc.metadata.get("usd_path") or "")
        bbox_size = kwargs.get("bbox_size") or doc.metadata.get("bbox_size") or [1.0, 1.0, 1.0]
        bbox_size = _validate_vec3(bbox_size, "bbox_size")
        instance_id = str(doc.metadata.get("instance_id") or "") or context.scene.next_instance_id(asset_type)
        if instance_id in context.scene.state.instances:
            return ToolResult(ok=False, error=f"instance_id 已存在: {instance_id}")

        inst = Instance(
            instance_id=instance_id,
            asset_type=asset_type,
            asset_doc_id=doc_id,
            usd_path=usd_path,
            position=list(position),
            rotation_deg=rotation,
            bbox_size=list(bbox_size),
            tags=dict(doc.metadata.get("tags") or {}),
            description=str(doc.metadata.get("description") or ""),
        )
        context.scene.add_instance(inst)

        parent_id: Optional[str] = kwargs.get("parent_instance_id")
        if parent_id:
            try:
                context.scene.set_support(instance_id, parent_id)
            except (KeyError, ValueError) as exc:
                # 放置成功但支撑登记失败，回滚实例避免不一致
                context.scene.delete(instance_id)
                return ToolResult(ok=False, error=f"set_support 失败: {exc}")

        return ToolResult(ok=True, data={
            "instance_id": instance_id,
            "asset_type": asset_type,
            "usd_path": usd_path,
            "position": inst.position,
            "bbox_size": inst.bbox_size,
            "tags": inst.tags,
            "description": inst.description,
        })

    def run_test(self, context: ToolContext) -> ToolResult:
        doc = _first_asset_doc(context)
        if doc is None:
            return ToolResult(ok=False, error="place_instance run_test found no asset docs")
        result = self(
            context,
            asset_doc_id=doc.doc_id,
            position=[0.0, 0.0, 0.5],
        )
        if not result.ok:
            return result
        
        instance_id = result.data.get("instance_id")
        if not instance_id:
            return ToolResult(ok=False, error="place_instance run_test did not return instance_id")
        if instance_id not in context.scene.state.instances:
            return ToolResult(ok=False, error="place_instance run_test did not add instance")
        context.scene.delete(instance_id)
        return ToolResult(ok=True, data={"tested": self.name})


def _validate_vec3(value: Any, label: str) -> List[float]:
    if not isinstance(value, (list, tuple)) or len(value) != 3:
        raise ValueError(f"{label} 必须是长度为 3 的列表")
    return [float(v) for v in value]


def _find_doc(context: ToolContext, doc_id: str):
    for doc in context.rag.documents:
        if doc.doc_id == doc_id:
            return doc
    return None


def _first_asset_doc(context: ToolContext) -> Optional[AssetDocument]:
    for doc in context.rag.documents:
        if doc.metadata.get("doc_type") == "asset":
            return doc
    return None