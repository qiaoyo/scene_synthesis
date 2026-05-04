"""Deprecated compatibility wrapper for the canonical CLI entrypoint."""
from __future__ import annotations

import sys
from pathlib import Path

SRC_ROOT = Path(__file__).resolve().parents[1]
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


def main() -> None:
    print(
        "[Deprecated] scripts/run_inference.py delegates to "
        "`python -m scene_layout_rag.cli`. Please use the module CLI directly.",
        file=sys.stderr,
    )

    from scene_layout_rag.cli import main as cli_main

    cli_main()


if __name__ == "__main__":
    main()
