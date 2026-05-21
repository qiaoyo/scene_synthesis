"""Scene-layout RAG + ReAct agent package."""
from __future__ import annotations

from .config import ProjectConfig
from .data_models import AssetDocument, Instance, SceneState

__all__ = [
    "ProjectConfig",
    "AssetDocument",
    "Instance",
    "SceneState",
    "ReActAgent",
]

def __getattr__(name: str):
    if name == "ReActAgent":
        from .react_agent import ReActAgent

        return ReActAgent
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
