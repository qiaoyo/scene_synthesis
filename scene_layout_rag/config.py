"""Configuration objects for the scene layout RAG stack."""
from __future__ import annotations
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional
_DEFAULT_ASSETS_ROOT = Path("/home/simple/joey/scene_synthesis/data/assets")

@dataclass
class ProjectConfig:
    """asset_config"""
    assets_root: Path = _DEFAULT_ASSETS_ROOT
    inventory_csvs: List[Path] = field(default_factory=list)
    scene_md_files: List[Path] = field(default_factory=list)
    block_size: int = 3  # 用于 markdown 的段落聚合
    """embedding_config"""
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    embedding_batch_size: int = 32
    device: str = "cuda:1"
    index_dir: Path = Path("/home/simple/joey/scene_synthesis/data/indexes")
    output_dir: Path = Path("/home/simple/joey/scene_synthesis/outputs")
    """tool_ctx"""
    physics_enabled: bool = False
    """model config"""
    model = "Qwen/Qwen3-32B-AWQ"
    #llm_api_base_url: str = "http://localhost:8000/v1"
    llm_api_base_url: str = "http://127.0.0.1:8000/v1"
    llm_api_key: str = "EMPTY" 
    max_new_tokens: int = 512
    max_output_tokens: int = 1024
    temperature: float = 0.2
    max_steps: int = 10
__all__ = ["ProjectConfig"]
