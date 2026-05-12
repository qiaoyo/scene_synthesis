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
    bbox_size: List[float] = field(default_factory=lambda: [1.0, 1.0, 1.0])
    parent_instance_id: Optional[str] = None  # set_support 之后才会有
    tags: Dict[str, str] = field(default_factory=dict)
    description: Optional[str] = None  # 从资产文档继承的文本描述

    def aabb(self) -> Tuple[List[float], List[float]]:
        cx, cy, cz = self.position
        sx, sy, sz = self.bbox_size
        half = [sx / 2.0, sy / 2.0, sz / 2.0]
        bbox_min = [cx - half[0], cy - half[1], cz - half[2]]
        bbox_max = [cx + half[0], cy + half[1], cz + half[2]]
        return bbox_min, bbox_max

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

# ---------- ReAct 三段式 ----------

@dataclass
class Action:
    """LLM 决策出的一次动作。"""
    tool: str
    tool_input: Dict[str, Any] = field(default_factory=dict)
    thought: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Observation:
    """一次工具执行后的全面观测。结构对齐 ``方案/优化.md`` 中的优化方向 2。"""
    ok: bool = True
    tool_result: Dict[str, Any] = field(default_factory=dict)
    validation: Dict[str, Any] = field(default_factory=dict)
    scene_semantics: Dict[str, Any] = field(default_factory=dict)
    support_state: Dict[str, Any] = field(default_factory=dict)
    physics_feedback: Dict[str, Any] = field(default_factory=dict)
    suggestions: List[str] = field(default_factory=list)
    error: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Reflection:
    """LLM 在观察失败后产出的反思。"""

    summary: str = ""
    cause: str = ""
    next_strategy: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Lesson:
    """沉淀到 lessons_learned 中的复用经验。"""

    situation: str
    mistake: str
    correction: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


__all__ = [
    "AssetDocument",
    "Instance",
    "SceneState",
    "Action",
    "Observation",
    "Reflection",
    "Lesson",
]
