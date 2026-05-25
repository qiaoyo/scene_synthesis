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

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--command",
        type=str,
        default="Get a big robotic arm and place it on the workbench(set support), put a long straight conveyor belt beside it, then place one part on the belt(set support). ",
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
    agent = ReActAgent(cfg, rag=rag)
    record = agent.run(args.command,cfg.max_steps)
    print(f"[run_inference] {len(record['steps'])} 步, "
        f"final_instances={len(agent.scene.state.instances)}")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())