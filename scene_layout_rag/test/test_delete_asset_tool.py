from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scene_layout_rag.config import ProjectConfig
from scene_layout_rag.rag import AssetRAG
from scene_layout_rag.scene_state import SceneStateManager
from scene_layout_rag.tools.base import TOOL_REGISTRY, ToolContext



###
#测试脚本里， 增加测试内容，vllm 快速启动一个本地的qwen-32B， 和一条指定的使用指定工具的命令输入。（测试多次，多次使用不同的命令）， 检查llm是否能够hit tool和正确的给require的参数和参数变量。
###

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
        query="small conveyor for boxes",
        asset_type="Conveyor",
    )
    child_hit = _retrieve_single_asset(
        ctx,
        query="small open box",
        asset_type="Box",
    )

    parent_place = TOOL_REGISTRY["place_instance"](
        ctx,
        asset_doc_id=parent_hit["doc_id"],
        position=[0.0, 0.0, 0.5],
    )
    print("place_instance (parent) result:")
    print(json.dumps(parent_place.to_dict(), ensure_ascii=False, indent=2))
    if not parent_place.ok:
        raise RuntimeError(parent_place.error or "place_instance failed for parent")

    parent_id = parent_place.data.get("instance_id")
    if not parent_id:
        raise RuntimeError("parent place_instance did not return instance_id")
    if not str(parent_id).startswith("Conveyor_"):
        raise RuntimeError(f"auto-generated parent instance_id has unexpected prefix: {parent_id}")

    child_place = TOOL_REGISTRY["place_instance"](
        ctx,
        asset_doc_id=child_hit["doc_id"],
        position=[0.0, 0.0, 1.2],
        parent_instance_id=parent_id,
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

    child_before = ctx.scene.get(child_id)
    if child_before.parent_instance_id != parent_id:
        raise RuntimeError(
            f"child support relation not set correctly: {child_before.parent_instance_id}"
        )

    print("scene before delete:")
    print(json.dumps({
        "parent_id": parent_id,
        "child_id": child_id,
        "support_children": ctx.scene.state.support_children,
        "child_parent": child_before.parent_instance_id,
    }, ensure_ascii=False, indent=2))

    delete_result = TOOL_REGISTRY["delete_asset"](
        ctx,
        instance_id=parent_id,
    )
    print("delete_asset result:")
    print(json.dumps(delete_result.to_dict(), ensure_ascii=False, indent=2))
    if not delete_result.ok:
        raise RuntimeError(delete_result.error or "delete_asset failed")

    if parent_id in ctx.scene.state.instances:
        raise RuntimeError(f"parent instance still exists after delete: {parent_id}")

    child_after = ctx.scene.get(child_id)
    if child_after.parent_instance_id is not None:
        raise RuntimeError(
            f"child should have been unparented, got: {child_after.parent_instance_id}"
        )
    if child_id not in delete_result.data.get("unparented_children", []):
        raise RuntimeError("delete_asset did not report child in unparented_children")

    print("scene after delete:")
    print(json.dumps({
        "deleted_parent_id": parent_id,
        "remaining_child_id": child_id,
        "child_parent": child_after.parent_instance_id,
        "support_children": ctx.scene.state.support_children,
    }, ensure_ascii=False, indent=2))

    ctx.scene.delete(child_id)
    print("cleanup", child_id, "__deleted__")


if __name__ == "__main__":
    main()
