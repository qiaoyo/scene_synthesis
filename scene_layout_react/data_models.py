from __future__ import annotations
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional, Tuple

SUPPORT_TYPE_SURFACE = "surface"
SUPPORT_TYPE_CONTAINER_INNER = "container_inner"
VALID_SUPPORT_TYPES = {
    SUPPORT_TYPE_SURFACE,
    SUPPORT_TYPE_CONTAINER_INNER,
}


def normalize_support_type(value: Any) -> str:
    text = str(value or SUPPORT_TYPE_SURFACE).strip().lower()
    if text in VALID_SUPPORT_TYPES:
        return text
    return SUPPORT_TYPE_SURFACE


@dataclass
class AssetDocument:
    """统一的资产/场景文档结构，落到 ``data/indexes/corpus.jsonl``。"""
    doc_id: str
    content: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)
    embedding: Optional[List[float]] = None
    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        # embedding 体积大且只在 FAISS 模式下需要持久
        if data.get("embedding") is None:
            data.pop("embedding", None)
        return data
    @classmethod
    def from_dict(cls, payload: Dict[str, Any]) -> "AssetDocument":
        return cls(
            doc_id=payload["doc_id"],
            content=payload.get("content", ""),
            metadata=dict(payload.get("metadata", {})),
            embedding=payload.get("embedding"),
        )
# ---------- 场景运行时 ----------
Vec3 = Tuple[float, float, float]
@dataclass
class Instance:
    """场景中已经放置好的一个资产实例。"""
    instance_id: str
    asset_type: str
    asset_doc_id: str  # 指向语料库里的某条 AssetDocument
    usd_path: str
    position: List[float] = field(default_factory=lambda: [0.0, 0.0, 0.0])
    rotation_deg: float = 0.0  # 仅绕 Z 轴
    bbox: dict = field(default_factory=lambda: {
                        "min": [0.0, 0.0, 0.0],
                        "max": [1.0, 1.0, 1.0]
                    })

    parent_instance_id: Optional[str] = None  # set_support 之后才会有
    tags: Dict[str, str] = field(default_factory=dict)
    description: Optional[str] = None  # 从资产文档继承的文本描述

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, payload: Dict[str, Any]) -> "Instance":
        return cls(
            instance_id=str(payload["instance_id"]),
            asset_type=str(payload["asset_type"]),
            asset_doc_id=str(payload["asset_doc_id"]),
            usd_path=str(payload.get("usd_path") or ""),
            position=[float(value) for value in payload.get("position", [0.0, 0.0, 0.0])],
            rotation_deg=float(payload.get("rotation_deg", 0.0)),
            bbox=dict(payload.get("bbox") or {
                "min": [0.0, 0.0, 0.0],
                "max": [1.0, 1.0, 1.0],
            }),
            parent_instance_id=payload.get("parent_instance_id"),
            tags=dict(payload.get("tags") or {}),
            description=payload.get("description"),
        )

@dataclass
class SceneState:
    """整张场景的运行时快照。"""
    instances: Dict[str, Instance] = field(default_factory=dict)
    support_children: Dict[str, List[str]] = field(default_factory=dict)
    support_relation_types: Dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "instances": {iid: inst.to_dict() for iid, inst in self.instances.items()},
            "support_children": dict(self.support_children),
            "support_relation_types": dict(self.support_relation_types),
        }

    @classmethod
    def from_dict(cls, payload: Dict[str, Any]) -> "SceneState":
        raw_instances = payload.get("instances", {}) or {}
        instances = {
            str(instance_id): Instance.from_dict(instance_payload)
            for instance_id, instance_payload in raw_instances.items()
            if isinstance(instance_payload, dict)
        }
        support_children = {
            str(parent_id): [
                str(child_id)
                for child_id in children
            ]
            for parent_id, children in (payload.get("support_children", {}) or {}).items()
            if isinstance(children, list)
        }
        raw_support_types = payload.get("support_relation_types", {}) or {}
        if not isinstance(raw_support_types, dict):
            raw_support_types = {}
        support_relation_types: Dict[str, str] = {}
        for children in support_children.values():
            for child_id in children:
                support_relation_types[child_id] = normalize_support_type(
                    raw_support_types.get(child_id, SUPPORT_TYPE_SURFACE)
                )
        return cls(
            instances=instances,
            support_children=support_children,
            support_relation_types=support_relation_types,
        )
        
__all__ = [
    "AssetDocument",
    "Instance",
    "SceneState",
    "SUPPORT_TYPE_CONTAINER_INNER",
    "SUPPORT_TYPE_SURFACE",
    "VALID_SUPPORT_TYPES",
    "normalize_support_type",
]
