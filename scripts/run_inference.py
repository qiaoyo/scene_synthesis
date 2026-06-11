from __future__ import annotations
import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
import argparse
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
        default="Retrieve a robot then place it on (0,0,0) and retrivel a workbench then place it on (0,0,0) and set support between them",
        help="Task description for the planner"
        
    )
    return parser.parse_args()
def main() -> int:
    args = parse_args()
    cfg = ProjectConfig()
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
    print(f"[run_inference] {len(record['steps'])} 步, "
          f"final_instances={len(agent.scene.state.instances)}")
    print(f"[run_inference] saved final scene_state={scene_out_path}")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
