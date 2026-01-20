"""Template-driven layout planner.

This module converts MD "Referenced Xforms" anchors (payload + bbox centers) into a
layout template, then places selected CSV assets in a similar arrangement.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

from .data_models import AssetDocument, LayoutElement


@dataclass(frozen=True)
class SelectedAsset:
    asset_id: str
    usd_path: str
    scale: List[float]
    score: float = 0.0
    description: str = ""


def _anchor_label(doc: AssetDocument) -> str:
    payload = str(doc.metadata.get("payload") or "")
    if payload:
        name = Path(payload).name
        if name:
            return Path(name).stem
    prim_path = str(doc.metadata.get("prim_path") or "")
    if prim_path:
        return prim_path.rsplit("/", 1)[-1]
    return doc.doc_id


def _anchor_center(doc: AssetDocument) -> Tuple[float, float, float] | None:
    bbox = doc.metadata.get("bbox_world") or {}
    center = bbox.get("center")
    if isinstance(center, (list, tuple)) and len(center) >= 3:
        try:
            return float(center[0]), float(center[1]), float(center[2])
        except Exception:
            return None
    return None


def _normalize_centers(
    centers: Sequence[Tuple[float, float, float]],
    target_radius_xy: float = 8.0,
) -> List[Tuple[float, float, float]]:
    if not centers:
        return []
    cx = sum(p[0] for p in centers) / len(centers)
    cy = sum(p[1] for p in centers) / len(centers)
    # keep z at 0 for placement; template z can be large/noisy depending on source export.
    shifted = [(p[0] - cx, p[1] - cy, 0.0) for p in centers]
    max_r = max((p[0] ** 2 + p[1] ** 2) ** 0.5 for p in shifted) or 1.0
    scale = min(1.0, target_radius_xy / max_r) if max_r > 0 else 1.0
    return [(p[0] * scale, p[1] * scale, 0.0) for p in shifted]


def _match_score(asset_id: str, usd_path: str, anchor_label: str, anchor_payload: str) -> int:
    cat = asset_id.lower().replace(" ", "")
    label = anchor_label.lower().replace(" ", "")
    payload = anchor_payload.lower().replace(" ", "")
    usd_name = Path(usd_path).stem.lower().replace(" ", "")
    score = 0
    if cat and (cat in label or label in cat):
        score += 10
    if cat and (cat in payload):
        score += 8
    if usd_name and (usd_name in label or usd_name in payload):
        score += 6
    return score


class TemplateLayoutPlanner:
    """Plan placements by reusing MD template anchor geometry."""

    def __init__(self, target_radius_xy: float = 8.0):
        self.target_radius_xy = target_radius_xy

    def plan(self, assets: Sequence[SelectedAsset], anchors: Sequence[AssetDocument]) -> List[LayoutElement]:
        usable: List[AssetDocument] = []
        centers: List[Tuple[float, float, float]] = []
        labels: List[str] = []
        for doc in anchors:
            c = _anchor_center(doc)
            if c is None:
                continue
            usable.append(doc)
            centers.append(c)
            labels.append(_anchor_label(doc))

        norm_centers = _normalize_centers(centers, target_radius_xy=self.target_radius_xy)
        used_anchor_idx: set[int] = set()

        elements: List[LayoutElement] = []
        for asset_idx, asset in enumerate(assets):
            best_i = None
            best_s = -1
            for i, doc in enumerate(usable):
                if i in used_anchor_idx:
                    continue
                s = _match_score(asset.asset_id, asset.usd_path, labels[i], str(doc.metadata.get("payload") or ""))
                if s > best_s:
                    best_s = s
                    best_i = i
            if best_i is None:
                # No anchors available: fall back to a simple line.
                px = (asset_idx - (len(assets) - 1) / 2.0) * 1.5
                py = 0.0
                pz = 0.0
                reason = "模板锚点不足，使用简单线性队列放置"
            else:
                used_anchor_idx.add(best_i)
                px, py, pz = norm_centers[best_i]
                reason = f"匹配模板锚点: {labels[best_i]}"

            elements.append(
                LayoutElement(
                    asset_id=asset.asset_id,
                    usd_path=asset.usd_path,
                    transform={"x": float(px), "y": float(py), "z": float(pz)},
                    score=float(asset.score),
                    reasoning=reason,
                    scale=list(asset.scale),
                )
            )
        return elements


__all__ = ["SelectedAsset", "TemplateLayoutPlanner"]

