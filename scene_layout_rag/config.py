"""Configuration objects for the scene layout RAG stack."""
from __future__ import annotations

import os
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
    documents_files: List[Path] = field(default_factory=list)
    extra_documents_dir: Optional[Path] = None

    def __post_init__(self) -> None:
        csv_dir = self.assets_root/"csv"
        if csv_dir.is_dir():
            # 子目录存在：只扫描 csv/*.csv（非递归）
            self.inventory_csvs = sorted(csv_dir.glob("*.csv"))
        else:
            # 子目录不存在：兼容旧结构，扫描顶层 *.csv
            self.inventory_csvs = sorted(self.assets_root.glob("*.csv"))
        
        md_dir =self.assets_root/"md"
        if md_dir.is_dir():
            # 子目录存在：只扫描 md/*.md（非递归）
            self.scene_md_files = sorted(md_dir.glob("*.md"))
        else:
            # 子目录不存在：兼容旧结构，扫描顶层 *.md
            self.scene_md_files = sorted(self.assets_root.glob("*.md"))
            
        doc_dir =self.assets_root/"docs"
        if doc_dir.is_dir():
            # 子目录存在：只扫描 md/*.md（非递归）
            self.documents_files = sorted(doc_dir.glob("*.jsonl"))
        else:
            # 子目录不存在：兼容旧结构，扫描顶层 *.md
            self.documents_files = sorted(self.assets_root.glob("*.jsonl"))
                # ===================== 额外文档目录（必须保留）=====================
        if self.extra_documents_dir is None:
            custom_dir = self.assets_root / "extra"
            self.extra_documents_dir = custom_dir if custom_dir.exists() else None



@dataclass
class ModelConfig:
    """Holds model related knobs for embeddings, LLMs, and layout heads."""
    llm_backend: str = "local"  # 仅实现了 local（transformers）；其它值会抛错
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
    # OpenAI SDK / Responses API support
    llm_api_base_url: str = "https://openrouter.ai/api/v1"
    #llm_api_key: str = os.environ.get("OPENROUTER_API_KEY", "")
    llm_api_key: str = "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"
    llm_api_model: str = "inclusionai/ling-2.6-1t:free"


@dataclass
class AgentConfig:
    """Configuration for the ReAct agent loop."""

    max_steps: int = 20
    reflection_enabled: bool = True
    strategy_adjust_enabled: bool = True
    max_lessons: int = 10
    max_working_memory: int = 15
    physics_enabled: bool = False
    physics_sim_duration: float = 2.0
    collision_method: str = "aabb"
    warm_start: bool = True


@dataclass
class ProjectConfig:
    """Top-level configuration consumed by the CLI entrypoints."""

    asset_paths: AssetPaths = field(default_factory=AssetPaths)
    model: ModelConfig = field(default_factory=ModelConfig)
    agent: AgentConfig = field(default_factory=AgentConfig)
    index_dir: Path = _DEFAULT_PROJECT_ROOT / "data" / "indexes"
    output_dir: Path = _DEFAULT_PROJECT_ROOT / "outputs"
    chunk_size: int = 512
    chunk_overlap: int = 64
    #language: str = "zh"
    language: str = "en"
    # 资产索引：始终写 corpus.jsonl；默认同时构建 FAISS 向量索引（依赖缺失会自动回退）
    enable_faiss: bool = True
    retrieval_top_k: int = 5

    def ensure_directories(self) -> None:
        self.index_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)


__all__ = ["AssetPaths", "ModelConfig", "AgentConfig", "ProjectConfig"]
