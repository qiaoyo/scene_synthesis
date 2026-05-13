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
    llm_api_base_url: str = "http://localhost:8000/v1"
    llm_api_key: str = "EMPTY"  # 注意：默认值为字符串 "EMPTY"，而非 None 
    max_new_tokens: int = 512
    max_output_tokens: int = 1024
    temperature: float = 0.2

    
    """llm planner"""
    
    """agent config"""
    max_steps: int = 5
    
    
    
    """Holds model related knobs for embeddings, LLMs, and layout heads.""" 
    use_8bit: bool = False
    load_in_4bit: bool = False
    gradient_checkpointing: bool = True
    lora_rank: int = 32
    lora_alpha: int = 64
    
    """Configuration for the ReAct agent loop."""
    reflection_enabled: bool = True
    strategy_adjust_enabled: bool = True
    max_lessons: int = 10
    max_working_memory: int = 15
    physics_sim_duration: float = 2.0
    collision_method: str = "aabb"
    warm_start: bool = True
    language: str = "en"
    retrieval_top_k: int = 5
    
    def __post_init__(self) -> None:
        csv_dir = self.assets_root/"csv"
        # 扫描 csv/*.csv（非递归）
        self.inventory_csvs = sorted(csv_dir.glob("*.csv"))
        md_dir =self.assets_root/"md"
        # 扫描 md/*.md（非递归）
        self.scene_md_files = sorted(md_dir.glob("*.md"))

__all__ = ["ProjectConfig"]
