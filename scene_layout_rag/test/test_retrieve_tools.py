from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scene_layout_rag.config import ProjectConfig
from scene_layout_rag.rag import AssetRAG
from scene_layout_rag.scene_state import SceneStateManager
from scene_layout_rag.tools.base import TOOL_REGISTRY, ToolContext


def main() -> None:
    cfg = ProjectConfig()
    cfg.enable_faiss = False

    rag = AssetRAG(cfg)
    if (cfg.index_dir / "corpus.jsonl").exists():
        rag.load()
    else:
        rag.build(save=True)

    ctx = ToolContext(scene=SceneStateManager(), rag=rag)

    for tool_name in ["retrieve_scene_template", "retrieve_assets"]:
        result = TOOL_REGISTRY[tool_name].run_test(ctx)
        print(tool_name, result.ok, result.error or result.data)

    result = TOOL_REGISTRY["retrieve_assets"](
        ctx,
        query="small conveyor for boxes",
        top_k=1,
        asset_type="Conveyor",
    )
    print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))

    # result = TOOL_REGISTRY["retrieve_scene_template"](
    #     ctx,
    #     query="sorting scene",
    #     top_k=1,
    #     scene_id="sorting",
    # )
    # print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))


if __name__ == "__main__":

    main()
