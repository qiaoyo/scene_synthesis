"""Configuration objects for the scene layout RAG stack."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

_MODULE_DIR = Path(__file__).resolve().parent
_SRC_ROOT = _MODULE_DIR.parent
_DEFAULT_PROJECT_ROOT = _SRC_ROOT


def _detect_assets_root() -> Path:
    candidates = [
        _SRC_ROOT / "data" / "assets",
        _SRC_ROOT.parent / "assets",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


_DEFAULT_ASSETS_ROOT = _detect_assets_root()


@dataclass
class AssetPaths:
    """Paths describing where structured and semi-structured assets are stored."""

    assets_root: Path = _DEFAULT_ASSETS_ROOT
    inventory_csvs: List[Path] = field(default_factory=list)
    scene_md_files: List[Path] = field(default_factory=list)
    extra_documents_dir: Optional[Path] = None

    def __post_init__(self) -> None:
        csv_dir = self.assets_root / "csv"
        md_dir = self.assets_root / "md"
        if not self.inventory_csvs:
            csv_files: List[Path] = []
            csv_files.extend(self.assets_root.glob("*.csv"))
            if csv_dir.exists():
                csv_files.extend(csv_dir.glob("*.csv"))
            self.inventory_csvs = sorted(csv_files)
        if not self.scene_md_files:
            md_files: List[Path] = []
            md_files.extend(self.assets_root.glob("*.md"))
            if md_dir.exists():
                md_files.extend(md_dir.glob("*.md"))
            self.scene_md_files = sorted(md_files)
        if self.extra_documents_dir is None:
            custom_dir = self.assets_root / "docs"
            self.extra_documents_dir = custom_dir if custom_dir.exists() else None


@dataclass
class ModelConfig:
    """Holds model related knobs for embeddings, LLMs, and layout heads."""

    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    embedding_batch_size: int = 32
    llm_name_or_path: str = "mistralai/Mistral-7B-Instruct-v0.2"
    max_new_tokens: int = 512
    temperature: float = 0.2
    device: str = "cuda:1"
    use_8bit: bool = False
    load_in_4bit: bool = False
    gradient_checkpointing: bool = True
    lora_rank: int = 32
    lora_alpha: int = 64


@dataclass
class ProjectConfig:
    """Top-level configuration consumed by the CLI entrypoints."""

    asset_paths: AssetPaths = field(default_factory=AssetPaths)
    model: ModelConfig = field(default_factory=ModelConfig)
    index_dir: Path = _DEFAULT_PROJECT_ROOT / "data" / "indexes"
    chunk_size: int = 512
    chunk_overlap: int = 64
    #language: str = "zh"
    language: str = "en"

    def ensure_directories(self) -> None:
        self.index_dir.mkdir(parents=True, exist_ok=True)


__all__ = ["AssetPaths", "ModelConfig", "ProjectConfig"]
