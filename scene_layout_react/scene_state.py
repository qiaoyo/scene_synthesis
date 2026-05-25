from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict, List, Optional
from .data_models import Instance, SceneState

class SceneStateManager:
    """对 ``SceneState`` 的薄封装：提供 CRUD + 支撑关系维护 + 持久化。"""

    def __init__(self, state: Optional[SceneState] = None):
        self.state: SceneState = state or SceneState()
        self._auto_id_counter: Dict[str, int] = {}

    # -- 实例 CRUD --
    def add_instance(self, inst: Instance) -> Instance:
        if inst.instance_id in self.state.instances:
            raise ValueError(f"instance_id 已存在: {inst.instance_id}")
        self.state.instances[inst.instance_id] = inst
        return inst

    def get(self, instance_id: str) -> Instance:
        if instance_id not in self.state.instances:
            raise KeyError(f"未找到实例: {instance_id}")
        return self.state.instances[instance_id]

    def move(self, instance_id: str, new_position: List[float]) -> Instance:
        inst = self.get(instance_id)
        if len(new_position) != 3:
            raise ValueError("new_position 必须是长度为 3 的列表")
        inst.position = [float(v) for v in new_position]
        return inst

    def delete(self, instance_id: str) -> None:
        self.get(instance_id)  # 触发 KeyError
        # 清理被它支撑的子实例的 parent 字段
        for child_id in list(self.state.support_children.get(instance_id, [])):
            child = self.state.instances.get(child_id)
            if child is not None:
                child.parent_instance_id = None
        self.state.support_children.pop(instance_id, None)
        # 清理它自己的 parent 关系
        parent_id = self.state.instances[instance_id].parent_instance_id
        if parent_id and parent_id in self.state.support_children:
            siblings = self.state.support_children[parent_id]
            self.state.support_children[parent_id] = [c for c in siblings if c != instance_id]
        del self.state.instances[instance_id]

    # -- 支撑关系 --
    def set_support(self, child_id: str, parent_id: str) -> None:
        """登记 ``child`` 被 ``parent`` 支撑。会先解除 child 之前的 parent。"""
        if child_id == parent_id:
            raise ValueError("child 与 parent 不能相同")
        child = self.get(child_id)
        self.get(parent_id)
        # 先解绑旧 parent
        if child.parent_instance_id and child.parent_instance_id in self.state.support_children:
            siblings = self.state.support_children[child.parent_instance_id]
            self.state.support_children[child.parent_instance_id] = [c for c in siblings if c != child_id]
        child.parent_instance_id = parent_id
        self.state.support_children.setdefault(parent_id, [])
        if child_id not in self.state.support_children[parent_id]:
            self.state.support_children[parent_id].append(child_id)

    def clear_support(self, child_id: str) -> None:
        child = self.get(child_id)
        parent_id = child.parent_instance_id
        # 父节点的子节点删除
        if parent_id and parent_id in self.state.support_children:
            siblings = self.state.support_children[parent_id]
            self.state.support_children[parent_id] = [c for c in siblings if c != child_id]
        # 子节点的父节点删除
        child.parent_instance_id = None
    # -- 序列化 --

    def to_dict(self) -> Dict[str, Any]:
        return self.state.to_dict()

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")

__all__ = ["SceneStateManager"]
