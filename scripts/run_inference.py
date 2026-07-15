from __future__ import annotations
import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
import argparse
import json
import sys
from pathlib import Path
# Make the package importable when run as a script.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scene_layout_react import ReActAgent  # noqa: E402
from scene_layout_react.config import ProjectConfig  # noqa: E402
from scene_layout_react.rag import AssetRAG  # noqa: E402
from scene_layout_react.scene_state import SceneStateManager  # noqa: E402

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--command",
        type=str,
        default="Retrieve a rack and place it at position (0, 0, 0). Then retrieve a plastic box and place it on top of the rack. Retrieve a part and place it inside the plastic box. Before saving the scene, check for collisions among the rack, the plastic box, and the part, and only save the scene if the layout is collision-free and physically valid.",
        help="Task description for the planner"
        
    )
    parser.add_argument(
        "--result-json",
        type=Path,
        default=None,
        help="Optional path to write a compact machine-readable run summary.",
    )
    return parser.parse_args()
def main() -> int:
    args = parse_args()
    cfg = ProjectConfig()
    batch_output_dir = os.environ.get("SCENE_SYNTHESIS_OUTPUT_DIR")
    if batch_output_dir:
        cfg.output_dir = Path(batch_output_dir).expanduser()
    rag = AssetRAG(cfg)
    if (cfg.index_dir / "corpus.jsonl").exists():
        rag.load()
    else:
        rag.build(save=True)

    scene = (
        SceneStateManager.load(cfg.scene_in_path)
        if cfg.scene_in_path is not None
        else None
    )
    agent = ReActAgent(cfg, rag=rag, scene=scene)
    record = agent.run(args.command,cfg.max_steps)
    if cfg.scene_out_path is not None:
        scene_out_path = Path(cfg.scene_out_path).expanduser()
    else:
        run_dir = agent.tool_context.extras.get("run_dir")
        if run_dir:
            scene_out_path = (
                Path(run_dir).expanduser()
                / "scene_state_final.json"
            )
        else:
            scene_out_path = (
                Path(cfg.output_dir).expanduser()
                / "scene_state_final.json"
            )
    agent.scene.save(scene_out_path)
    run_dir = agent.tool_context.extras.get("run_dir")
    result = {
        "run_id": record.get("run_id"),
        "run_dir": str(run_dir) if run_dir else None,
        "record_path": str(Path(run_dir) / "record.json") if run_dir else None,
        "final_scene_path": str(scene_out_path),
        "ok": record.get("ok"),
        "steps": len(record.get("steps", []) or []),
        "final_instances": len(agent.scene.state.instances),
        "command": args.command,
    }
    if args.result_json is not None:
        result_path = args.result_json.expanduser()
        result_path.parent.mkdir(parents=True, exist_ok=True)
        result_path.write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print(f"[run_inference] {len(record['steps'])} 步, "
          f"final_instances={len(agent.scene.state.instances)}")
    print(f"[run_inference] saved final scene_state={scene_out_path}")
    if args.result_json is not None:
        print(f"[run_inference] result_json={args.result_json.expanduser()}")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
