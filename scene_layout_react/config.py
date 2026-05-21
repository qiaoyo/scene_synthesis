"""Configuration objects for the scene layout RAG stack."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Dict, Any

_PROJECT_ROOT = Path(__file__).resolve().parents[1]
_DEFAULT_ASSETS_ROOT = _PROJECT_ROOT / "data" / "assets"

@dataclass
class ProjectConfig:
    """asset_config"""
    assets_root: Path = _DEFAULT_ASSETS_ROOT
    inventory_csvs: List[Path] = field(default_factory=list)
    scene_md_files: List[Path] = field(default_factory=list)
    auto_discover_assets: bool = True
    block_size: int = 3  # 用于 markdown 的段落聚合
    
    
    """embedding_config"""
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    embedding_batch_size: int = 32
    retrieval_top_k: int = 5
    device: str = "cuda:1"
    index_dir: Path = _PROJECT_ROOT / "data" / "indexes"
    output_dir: Path = _PROJECT_ROOT / "outputs"
    
    
    """tool_ctx"""
    physics_enabled: bool = True
    
    
    """model config"""
    model: str = "Qwen/Qwen3-32B-AWQ"
    llm_api_base_url: str = "http://127.0.0.1:8000/v1"
    llm_api_key: str = "EMPTY" 
    max_new_tokens: int = 512
    max_output_tokens: int = 1024
    temperature: float = 0.2
    max_steps: int = 10
    
    """isaacsim config"""
    isaac_python: Path = Path("/home/simple/isaac-sim5.1/python.sh")
    isaac_worker_path: Optional[Path] = _PROJECT_ROOT / "scene_layout_react" / "physics" / "worker.py"
    isaac_worker_timeout_sec: int = 120
    isaac_temp_dir: Path = Path("/tmp/scene_synthesis_isaac")
    isaac_simulation: Dict[str, Any] = field(
        default_factory=lambda: {"headless": True}
    )
    isaac_collision_approximation: str = "convexHull"
    
    def __post_init__(self) -> None:
        self.assets_root = Path(self.assets_root)
        self.index_dir = Path(self.index_dir)
        self.output_dir = Path(self.output_dir)
        self.isaac_python = Path(self.isaac_python)
        if self.isaac_worker_path is not None:
            self.isaac_worker_path = Path(self.isaac_worker_path)

        self.inventory_csvs = [Path(p) for p in self.inventory_csvs]
        self.scene_md_files = [Path(p) for p in self.scene_md_files]

        if self.auto_discover_assets:
            self.discover_asset_inputs()

    def discover_asset_inputs(self) -> None:
        if not self.inventory_csvs:
            self.inventory_csvs = sorted((self.assets_root / "csv").glob("*.csv"))

        if not self.scene_md_files:
            self.scene_md_files = sorted((self.assets_root / "md").glob("*.md"))

__all__ = ["ProjectConfig"]
