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


def _retrieve_single_asset(ctx: ToolContext, query: str, asset_type: str) -> dict:
    result = TOOL_REGISTRY["retrieve_assets"](
        ctx,
        query=query,
        top_k=1,
        asset_type=asset_type,
    )
    print(f"retrieve_assets ({asset_type}) result:")
    print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
    if not result.ok:
        raise RuntimeError(result.error or f"retrieve_assets failed for {asset_type}")

    hits = result.data.get("hits", [])
    if not hits:
        raise RuntimeError(f"retrieve_assets returned no hits for {asset_type}")
    return hits[0]


def main() -> None:
    ctx = _build_context()

    parent_hit = _retrieve_single_asset(
        ctx,
        query="industrial workbench table",
        asset_type="Workbench",
    )
    child_hit = _retrieve_single_asset(
        ctx,
        query="small open box",
        asset_type="Box",
    )

    parent_bbox = parent_hit.get("bbox") or {}
    parent_size = parent_bbox.get("size") or [1.0, 1.0, 1.0]
    parent_z = float(parent_size[2]) / 2.0

    parent_place = TOOL_REGISTRY["place_instance"](
        ctx,
        asset_doc_id=parent_hit["doc_id"],
        position=[0.0, 0.0, parent_z],
    )
    print("place_instance (parent) result:")
    print(json.dumps(parent_place.to_dict(), ensure_ascii=False, indent=2))
    if not parent_place.ok:
        raise RuntimeError(parent_place.error or "place_instance failed for parent")

    parent_id = parent_place.data.get("instance_id")
    parent_bbox_size = parent_place.data.get("bbox_size") or parent_size
    if not parent_id:
        raise RuntimeError("parent place_instance did not return instance_id")
    if not str(parent_id).startswith("Workbench_"):
        raise RuntimeError(f"auto-generated parent instance_id has unexpected prefix: {parent_id}")

    child_bbox = child_hit.get("bbox") or {}
    child_size = child_bbox.get("size") or [1.0, 1.0, 1.0]
    child_z = float(parent_bbox_size[2]) + float(child_size[2]) / 2.0

    child_place = TOOL_REGISTRY["place_instance"](
        ctx,
        asset_doc_id=child_hit["doc_id"],
        position=[0.0, 0.0, child_z],
    )
    print("place_instance (child) result:")
    print(json.dumps(child_place.to_dict(), ensure_ascii=False, indent=2))
    if not child_place.ok:
        raise RuntimeError(child_place.error or "place_instance failed for child")

    child_id = child_place.data.get("instance_id")
    if not child_id:
        raise RuntimeError("child place_instance did not return instance_id")
    if not str(child_id).startswith("Box_"):
        raise RuntimeError(f"auto-generated child instance_id has unexpected prefix: {child_id}")

    print("scene before set_support:")
    print(json.dumps({
        "parent_id": parent_id,
        "child_id": child_id,
        "parent_position": ctx.scene.get(parent_id).position,
        "child_position": ctx.scene.get(child_id).position,
        "support_children": ctx.scene.state.support_children,
    }, ensure_ascii=False, indent=2))

    set_support_result = TOOL_REGISTRY["set_support"](
        ctx,
        child_id=child_id,
        parent_id=parent_id,
    )
    print("set_support result:")
    print(json.dumps(set_support_result.to_dict(), ensure_ascii=False, indent=2))
    if not set_support_result.ok:
        raise RuntimeError(set_support_result.error or "set_support failed")

    child_after = ctx.scene.get(child_id)
    if child_after.parent_instance_id != parent_id:
        raise RuntimeError(
            f"set_support did not register parent correctly: {child_after.parent_instance_id}"
        )
    if child_id not in ctx.scene.state.support_children.get(parent_id, []):
        raise RuntimeError("set_support did not update support_children")
    if not set_support_result.data.get("geometry_ok"):
        raise RuntimeError(
            f"set_support geometry check failed: {set_support_result.data.get('geometry')}"
        )

    print("scene after set_support:")
    print(json.dumps({
        "parent_id": parent_id,
        "child_id": child_id,
        "child_parent": child_after.parent_instance_id,
        "support_children": ctx.scene.state.support_children,
        "geometry": set_support_result.data.get("geometry"),
    }, ensure_ascii=False, indent=2))

    ctx.scene.delete(child_id)
    ctx.scene.delete(parent_id)
    print("cleanup", child_id, parent_id, "__deleted__")


if __name__ == "__main__":
    main()
