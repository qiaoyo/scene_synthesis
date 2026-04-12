#!/usr/bin/env python3

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Package a USD asset and its dependencies into a USDZ file via usdzip."
    )
    parser.add_argument("output_usdz", type=Path, help="Path to the output .usdz file.")
    parser.add_argument("input_usd", type=Path, help="Path to the root USD asset.")
    parser.add_argument(
        "-c",
        "--check-compliance",
        action="store_true",
        help="Run usdzip compliance checks before creating the package.",
    )
    parser.add_argument(
        "-r",
        "--recurse",
        action="store_true",
        help="Pass through usdzip's recursive directory option.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show files as usdzip adds them to the package.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the final usdzip command without running it.",
    )
    return parser


def build_command(
    output_usdz: Path,
    input_usd: Path,
    *,
    check_compliance: bool,
    recurse: bool,
    verbose: bool,
) -> list[str]:
    command = [
        "usdzip",
        str(output_usdz),
        "--asset",
        str(input_usd),
    ]
    if check_compliance:
        command.append("-c")
    if recurse:
        command.append("-r")
    if verbose:
        command.append("-v")
    return command


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    usdzip_path = shutil.which("usdzip")
    if not usdzip_path:
        parser.error("`usdzip` was not found in PATH.")

    input_usd = args.input_usd.expanduser().resolve()
    output_usdz = args.output_usdz.expanduser().resolve()

    if not input_usd.exists():
        parser.error(f"Input USD file does not exist: {input_usd}")
    if not input_usd.is_file():
        parser.error(f"Input USD path is not a file: {input_usd}")

    output_usdz.parent.mkdir(parents=True, exist_ok=True)

    command = build_command(
        output_usdz,
        input_usd,
        check_compliance=args.check_compliance,
        recurse=args.recurse, 
        verbose=args.verbose,
    )
    command[0] = usdzip_path

    print("Running:", " ".join(shlex_quote(part) for part in command))
    if args.dry_run:
        return 0

    completed = subprocess.run(command, check=False)
    return completed.returncode


def shlex_quote(value: str) -> str:
    if not value or any(ch.isspace() for ch in value):
        return f'"{value}"'
    return value


if __name__ == "__main__":
    sys.exit(main())
