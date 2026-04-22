"""Mutable scene state -- the runtime data structure for the ReAct agent."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class AssetInstance:
    """Runtime record of a placed asset."""
    instance_id: str                                      # "Conveyor_1"
    asset_id: str                                         # "Conveyor"
    usd_path: str
    position: Tuple[float, float, float]
    rotation: Tuple[float, float, float] = (0.0, 0.0, 0.0)
    bbox: Tuple[float, float, float] = (1.0, 1.0, 1.0)  # width, length, height
    description: str = ""
    support_parent: Optional[str] = None
    support_children: List[str] = field(default_factory=list)


class SceneState:
    """Mutable scene graph that tools read from and write to."""

    def __init__(self, bounds: Tuple[float, float, float] = (20.0, 30.0, 10.0)):
        self.bounds = bounds
        self.assets: Dict[str, AssetInstance] = {}
        self._id_counters: Dict[str, int] = {}

    # ------------------------------------------------------------------
    # ID generation
    # ------------------------------------------------------------------

    def generate_instance_id(self, asset_id: str) -> str:
        """Return the next unique ID for *asset_id*, e.g. ``Conveyor_1``."""
        self._id_counters[asset_id] = self._id_counters.get(asset_id, 0) + 1
        return f"{asset_id}_{self._id_counters[asset_id]}"

    # ------------------------------------------------------------------
    # CRUD
    # ------------------------------------------------------------------

    def add_asset(self, instance: AssetInstance) -> None:
        self.assets[instance.instance_id] = instance

    def remove_asset(self, instance_id: str) -> AssetInstance:
        asset = self.assets.pop(instance_id)
        # Clean up support references
        if asset.support_parent and asset.support_parent in self.assets:
            parent = self.assets[asset.support_parent]
            if instance_id in parent.support_children:
                parent.support_children.remove(instance_id)
        for child_id in list(asset.support_children):
            if child_id in self.assets:
                self.assets[child_id].support_parent = None
        return asset

    def move_asset(self, instance_id: str, new_position: Tuple[float, float, float]) -> None:
        self.assets[instance_id].position = new_position

    def get_asset(self, instance_id: str) -> Optional[AssetInstance]:
        return self.assets.get(instance_id)

    def set_support(self, child_id: str, parent_id: str) -> None:
        child = self.assets[child_id]
        parent = self.assets[parent_id]
        # Remove old parent reference
        if child.support_parent and child.support_parent in self.assets:
            old_parent = self.assets[child.support_parent]
            if child_id in old_parent.support_children:
                old_parent.support_children.remove(child_id)
        child.support_parent = parent_id
        if child_id not in parent.support_children:
            parent.support_children.append(child_id)

    def list_assets(self, asset_type: Optional[str] = None) -> List[AssetInstance]:
        if asset_type:
            return [a for a in self.assets.values() if a.asset_id == asset_type]
        return list(self.assets.values())

    # ------------------------------------------------------------------
    # Serialisation
    # ------------------------------------------------------------------

    def to_dict(self) -> dict:
        """Serialise to a dict suitable for LLM prompt injection."""
        return {
            "bounds": list(self.bounds),
            "asset_count": len(self.assets),
            "assets": [
                {
                    "instance_id": a.instance_id,
                    "asset_id": a.asset_id,
                    "position": list(a.position),
                    "bbox": list(a.bbox),
                    "support_parent": a.support_parent,
                }
                for a in self.assets.values()
            ],
        }

    def to_layout_json(self) -> list:
        """Export to the JSON format consumed by ``scene.py``."""
        return [
            {
                "asset_id": a.asset_id,
                "usd_path": a.usd_path,
                "position": list(a.position),
                "rotation": list(a.rotation),
                "scale": [0.01, 0.01, 0.01],
            }
            for a in self.assets.values()
        ]


__all__ = ["AssetInstance", "SceneState"]
