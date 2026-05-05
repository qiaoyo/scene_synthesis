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

    retrieval = TOOL_REGISTRY["retrieve_assets"](
        ctx,
        query="small conveyor for boxes",
        top_k=1,
        asset_type="Conveyor",
    )
    print("retrieve_assets result:")
    print(json.dumps(retrieval.to_dict(), ensure_ascii=False, indent=2))
    if not retrieval.ok:
        raise RuntimeError(retrieval.error or "retrieve_assets failed")

    hits = retrieval.data.get("hits", [])
    if not hits:
        raise RuntimeError("retrieve_assets returned no hits")

    asset_doc_id = hits[0]["doc_id"]
    asset_type = hits[0]["asset_type"]

    place_result = TOOL_REGISTRY["place_instance"](
        ctx,
        asset_doc_id=asset_doc_id,
        position=[0.0, 0.0, 0.5],
    )
    print("place_instance result:")
    print(json.dumps(place_result.to_dict(), ensure_ascii=False, indent=2))
    if not place_result.ok:
        raise RuntimeError(place_result.error or "place_instance failed")

    instance_id = place_result.data.get("instance_id")
    if not instance_id:
        raise RuntimeError("place_instance did not return instance_id")
    if not str(instance_id).startswith(f"{asset_type}_"):
        raise RuntimeError(f"auto-generated instance_id has unexpected prefix: {instance_id}")

    before_move = ctx.scene.get(instance_id)
    print("before_move result:")
    print(json.dumps({
        "stage": "before_move",
        "instance_id": before_move.instance_id,
        "asset_type": before_move.asset_type,
        "position": before_move.position,
    }, ensure_ascii=False, indent=2))

    move_result = TOOL_REGISTRY["move_asset"](
        ctx,
        instance_id=instance_id,
        new_position=[1.0, 2.0, 0.5],
    )
    print("move_asset result:")
    print(json.dumps(move_result.to_dict(), ensure_ascii=False, indent=2))
    if not move_result.ok:
        raise RuntimeError(move_result.error or "move_asset failed")

    moved = ctx.scene.get(instance_id)
    if moved.position != [1.0, 2.0, 0.5]:
        raise RuntimeError(f"move_asset did not update position: {moved.position}")

    print(json.dumps({
        "stage": "after_move",
        "instance_id": moved.instance_id,
        "asset_type": moved.asset_type,
        "asset_doc_id": moved.asset_doc_id,
        "usd_path": moved.usd_path,
        "position": moved.position,
        "rotation_deg": moved.rotation_deg,
        "bbox_size": moved.bbox_size,
        "tags": moved.tags,
        "description": moved.description,
    }, ensure_ascii=False, indent=2))

    ctx.scene.delete(instance_id)
    print("cleanup", instance_id, "__deleted__")


if __name__ == "__main__":
    main()
