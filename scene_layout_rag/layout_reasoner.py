"""Lightweight layout reasoning heuristics."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Sequence

from .data_models import AssetDocument, LayoutElement, LayoutPlan, SceneCommand


@dataclass
class SceneContext:
    width: float = 20.0
    length: float = 30.0
    height: float = 10.0


_ZONE_KEYWORDS = {
    "入口": (0.1, 0.5),
    "收货": (0.2, 0.8),
    "发货": (0.8, 0.5),
    "装配": (0.5, 0.7),
    "存储": (0.5, 0.3),
}


class LayoutReasoner:
    """Converts retrieval hits into coarse layout proposals."""

    def __init__(self, context: SceneContext | None = None):
        self.context = context or SceneContext()

    def _pick_zone(self, text: str) -> tuple[float, float]:
        for keyword, coord in _ZONE_KEYWORDS.items():
            if keyword in text:
                return coord
        return (0.5, 0.5)

    def _build_element(self, doc: AssetDocument, score: float) -> LayoutElement:
        rel_x, rel_y = self._pick_zone(doc.content)
        x = (rel_x - 0.5) * self.context.width
        y = (rel_y - 0.5) * self.context.length
        transform = {"x": round(x, 2), "y": round(y, 2), "z": 0.0}
        reasoning = f"放置在{rel_x:.2f},{rel_y:.2f}区域以满足描述中的功能需求"
        usd_path = doc.metadata.get("usd_path", "")
        asset_id = doc.metadata.get("asset_category", doc.doc_id)
        scale_value = doc.metadata.get("scale")
        scale = [float(scale_value)] * 3 if isinstance(scale_value, (int, float)) else [0.01, 0.01, 0.01]
        return LayoutElement(
            asset_id=str(asset_id),
            usd_path=usd_path,
            transform=transform,
            score=score,
            reasoning=reasoning,
            scale=scale,
        )

    def build_plan(self, command: SceneCommand, docs: Sequence[tuple[AssetDocument, float]]) -> LayoutPlan:
        elements = [self._build_element(doc, score) for doc, score in docs]
        retrieved_docs = [doc for doc, _ in docs]
        return LayoutPlan(command=command, elements=elements, retrieved_docs=retrieved_docs)


__all__ = ["LayoutReasoner", "SceneContext"]
