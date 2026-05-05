from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scene_layout_rag.config import ProjectConfig
from scene_layout_rag.rag import AssetRAG
from scene_layout_rag.scene_state import SceneStateManager
from scene_layout_rag.tools.base import TOOL_REGISTRY, ToolContext


def _build_context() -> ToolContext:
    cfg = ProjectConfig()
    cfg.enable_faiss = False

    rag = AssetRAG(cfg)
    if (cfg.index_dir / "corpus.jsonl").exists():
        rag.load()
    else:
        rag.build(save=True)

    return ToolContext(scene=SceneStateManager(), rag=rag)


def main() -> None:
    ctx = _build_context()

    for tool_name in ["retrieve_assets", "place_instance"]:
        result = TOOL_REGISTRY[tool_name].run_test(ctx)
        print(tool_name, result.ok, result.error or result.data)

    retrieval = TOOL_REGISTRY["retrieve_assets"](
        ctx,
        query="small conveyor for boxes",
        top_k=1,
        asset_type="Conveyor",
    )
    print(json.dumps(retrieval.to_dict(), ensure_ascii=False, indent=2))
    if not retrieval.ok:
        raise RuntimeError(retrieval.error or "retrieve_assets failed")

    hits = retrieval.data.get("hits", [])
    if not hits:
        raise RuntimeError("retrieve_assets returned no hits")

    asset_doc_id = hits[0]["doc_id"]
    place_result = TOOL_REGISTRY["place_instance"](
        ctx,
        asset_doc_id=asset_doc_id,
        position=[1.0, 2.0, 0.5],
        rotation_deg=45.0,
    )
    print(json.dumps(place_result.to_dict(), ensure_ascii=False, indent=2))
    if not place_result.ok:
        raise RuntimeError(place_result.error or "place_instance failed")

    instance = ctx.scene.get("Conveyor_1")
    print(json.dumps({
        "instance_id": instance.instance_id,
        "asset_type": instance.asset_type,
        "asset_doc_id": instance.asset_doc_id,
        "usd_path": instance.usd_path,
        "position": instance.position,
        "rotation_deg": instance.rotation_deg,
        "bbox_size": instance.bbox_size,
        "tags": instance.tags,
        "description": instance.description,
    }, ensure_ascii=False, indent=2))

    ctx.scene.delete("Conveyor_1")
    print("cleanup", "Conveyor_1", "__deleted__")


if __name__ == "__main__":
    main()
