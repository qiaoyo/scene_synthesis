"""Common dataclasses shared across the RAG stack."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence


@dataclass
class AssetDocument:
    """Represents a single text chunk that can be embedded and retrieved."""

    doc_id: str
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)

    def as_dict(self) -> Dict[str, Any]:
        return {"id": self.doc_id, "content": self.content, "metadata": self.metadata}


@dataclass
class SceneCommand:
    """Normalized scene instruction from a user prompt or script."""

    raw_text: str
    language: str = "zh"
    structured_goals: Dict[str, Any] = field(default_factory=dict)


@dataclass
class LayoutElement:
    """Minimal unit describing an asset placement candidate."""

    asset_id: str
    usd_path: str
    transform: Dict[str, float]
    score: float
    reasoning: str


@dataclass
class LayoutPlan:
    """Aggregate of layout elements for downstream USD generation."""

    command: SceneCommand
    elements: Sequence[LayoutElement]
    retrieved_docs: Sequence[AssetDocument] = field(default_factory=list)
    planner_notes: Optional[str] = None

    def summary(self) -> List[Dict[str, Any]]:
        return [
            {
                "asset_id": e.asset_id,
                "usd_path": e.usd_path,
                "position": [
                    e.transform.get("x", 0.0),
                    e.transform.get("y", 0.0),
                    e.transform.get("z", 0.0),
                ],
                "scale":[0.01,0.01,0.01],
                "score": e.score,
            }
            for e in self.elements
        ]


__all__ = ["AssetDocument", "SceneCommand", "LayoutElement", "LayoutPlan"]
