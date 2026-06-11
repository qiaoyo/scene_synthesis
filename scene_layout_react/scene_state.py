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
        self.retrieval_memory: Dict[str, Any] = {"asset_queries": [],}

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

    # -- 状态校验 --
    def validate_integrity(self) -> Dict[str, Any]:
        invalid = []
        child_to_parent = {}

        for parent_id, children in self.state.support_children.items():
            if parent_id not in self.state.instances:
                invalid.append({
                    "source": "local_state",
                    "parent": parent_id,
                    "issue": "missing parent instance",
                })
                continue

            for child_id in children:
                child = self.state.instances.get(child_id)
                if child is None:
                    invalid.append({
                        "source": "local_state",
                        "child": child_id,
                        "parent": parent_id,
                        "issue": "missing child instance",
                    })
                    continue

                if child_id == parent_id:
                    invalid.append({
                        "source": "local_state",
                        "child": child_id,
                        "parent": parent_id,
                        "issue": "self support",
                    })

                if child_id in child_to_parent:
                    invalid.append({
                        "source": "local_state",
                        "child": child_id,
                        "parent": parent_id,
                        "issue": "multiple parents",
                    })

                if child.parent_instance_id != parent_id:
                    invalid.append({
                        "source": "local_state",
                        "child": child_id,
                        "parent": parent_id,
                        "issue": "parent link mismatch",
                        "instance_parent": child.parent_instance_id,
                    })

                child_to_parent[child_id] = parent_id

        for child_id, inst in self.state.instances.items():
            parent_id = inst.parent_instance_id
            if parent_id is None:
                continue
            if parent_id not in self.state.instances:
                invalid.append({
                    "source": "local_state",
                    "child": child_id,
                    "parent": parent_id,
                    "issue": "missing parent instance",
                })
            elif child_id not in self.state.support_children.get(parent_id, []):
                invalid.append({
                    "source": "local_state",
                    "child": child_id,
                    "parent": parent_id,
                    "issue": "missing support_children edge",
                })

        return {
            "backend": "local_state",
            "ok": len(invalid) == 0,
            "instance_count": len(self.state.instances),
            "support_edge_count": sum(
                len(children)
                for children in self.state.support_children.values()
            ),
            "invalid_relations": invalid,
        }

    # -- 序列化 --
    def remember_asset_retrievals(self, records: List[Dict[str, Any]]) -> None:
        queries = self.retrieval_memory.setdefault("asset_queries", [])
        for record in records:
            candidates = []
            for item in record.get("results", []) or []:
                candidates.append({
                    "doc_id": item.get("doc_id"),
                    "instance_id": item.get("instance_id"),
                    "usd_path": item.get("usd_path"),
                })
            compact = {
                "query": record.get("query", ""),
                "asset_type": record.get("asset_type", ""),
                "count": len(candidates),
                "candidates": candidates,
            }
            queries[:] = [
                item for item in queries
                if not (
                    item.get("query") == compact["query"]
                    and item.get("asset_type") == compact["asset_type"]
                )
            ]
            queries.append(compact)

    def to_dict(self) -> Dict[str, Any]:
        payload = self.state.to_dict()
        payload["retrieval_memory"] = self.retrieval_memory
        return payload

    @classmethod
    def from_dict(cls, payload: Dict[str, Any]) -> "SceneStateManager":
        manager = cls(SceneState.from_dict(payload))
        manager.retrieval_memory = dict(payload.get("retrieval_memory") or {"asset_queries": []})
        return manager

    @classmethod
    def load(cls, path: Path) -> "SceneStateManager":
        path = Path(path).expanduser()
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError(f"scene state file must contain a JSON object: {path}")
        return cls.from_dict(payload)

    def save(self, path: Path) -> None:
        path = Path(path).expanduser()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")

__all__ = ["SceneStateManager"]
