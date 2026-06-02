from __future__ import annotations
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional, Tuple

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

@dataclass
class SceneState:
    """整张场景的运行时快照。"""
    instances: Dict[str, Instance] = field(default_factory=dict)
    # 反向索引：parent_id -> [child_ids]
    support_children: Dict[str, List[str]] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "instances": {iid: inst.to_dict() for iid, inst in self.instances.items()},
            "support_children": dict(self.support_children),
        }
__all__ = [
    "AssetDocument",
    "Instance",
    "SceneState",
]