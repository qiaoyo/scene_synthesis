#!/usr/bin/env python3

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

USD_EXTENSIONS = {".usd", ".usda", ".usdc"}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Package all USD files in a folder into USDZ files via usdzip."
    )
    parser.add_argument(
        "input_dir",
        type=Path,
        help="Directory containing USD files to package.",
    )
    parser.add_argument(
        "output_dir",
        type=Path,
        help="Directory where generated .usdz files will be written.",
    )
    parser.add_argument(
        "-c",
        "--check-compliance",
        action="store_true",
        help="Run usdzip compliance checks before creating each package.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show files as usdzip adds them to each package.",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Scan subdirectories under input_dir.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing .usdz outputs. By default, existing files are skipped.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the usdzip commands without running them.",
    )
    return parser


def shlex_quote(value: str) -> str:
    if not value or any(ch.isspace() for ch in value):
        return f'"{value}"'
    return value


def iter_usd_files(input_dir: Path, recursive: bool) -> list[Path]:
    pattern = "**/*" if recursive else "*"
    files = [path for path in input_dir.glob(pattern) if path.is_file() and path.suffix.lower() in USD_EXTENSIONS]
    return sorted(files)


def build_command(
    usdzip_path: str,
    output_usdz: Path,
    input_usd: Path,
    *,
    check_compliance: bool,
    verbose: bool,
) -> list[str]:
    command = [usdzip_path, str(output_usdz), "--asset", str(input_usd)]
    if check_compliance:
        command.append("-c")
    if verbose:
        command.append("-v")
    return command


def package_file(
    usdzip_path: str,
    input_dir: Path,
    output_dir: Path,
    input_usd: Path,
    *,
    check_compliance: bool,
    verbose: bool,
    overwrite: bool,
    dry_run: bool,
) -> tuple[int, Path]:
    relative = input_usd.relative_to(input_dir)
    output_usdz = (output_dir / relative).with_suffix(".usdz")
    output_usdz.parent.mkdir(parents=True, exist_ok=True)

    if output_usdz.exists() and not overwrite:
        print(f"Skipping existing file: {output_usdz}")
        return 0, output_usdz

    command = build_command(
        usdzip_path,
        output_usdz,
        input_usd,
        check_compliance=check_compliance,
        verbose=verbose,
    )
    print("Running:", " ".join(shlex_quote(part) for part in command))
    if dry_run:
        return 0, output_usdz

    completed = subprocess.run(command, check=False)
    return completed.returncode, output_usdz


def move_failed_output(output_usdz: Path, output_dir: Path) -> Path | None:
    if not output_usdz.exists():
        return None

    failed_root = output_dir / "failed"
    failed_target = failed_root / output_usdz.relative_to(output_dir)
    failed_target.parent.mkdir(parents=True, exist_ok=True)

    if failed_target.exists():
        failed_target.unlink()

    shutil.move(str(output_usdz), str(failed_target))
    return failed_target


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    usdzip_path = shutil.which("usdzip")
    if not usdzip_path:
        parser.error("`usdzip` was not found in PATH.")

    input_dir = args.input_dir.expanduser().resolve()
    output_dir = args.output_dir.expanduser().resolve()

    if not input_dir.exists():
        parser.error(f"Input directory does not exist: {input_dir}")
    if not input_dir.is_dir():
        parser.error(f"Input path is not a directory: {input_dir}")

    usd_files = iter_usd_files(input_dir, args.recursive)
    if not usd_files:
        print(f"No USD files found under: {input_dir}")
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)

    success_count = 0
    fail_count = 0
    failed_files: list[tuple[Path, int, Path | None]] = []

    for index, input_usd in enumerate(usd_files, start=1):
        print(f"[{index}/{len(usd_files)}] Packaging {input_usd}")
        return_code, output_usdz = package_file(
            usdzip_path,
            input_dir,
            output_dir,
            input_usd,
            check_compliance=args.check_compliance,
            verbose=args.verbose,
            overwrite=args.overwrite,
            dry_run=args.dry_run,
        )
        if return_code == 0:
            success_count += 1
        else:
            fail_count += 1
            failed_output = None if args.dry_run else move_failed_output(output_usdz, output_dir)
            failed_files.append((input_usd, return_code, failed_output))
            print(f"Failed with exit code {return_code}: {input_usd}", file=sys.stderr)
            if failed_output is not None:
                print(f"Moved partial output to: {failed_output}", file=sys.stderr)

    print(f"Finished. Success: {success_count}, Failed: {fail_count}, Total: {len(usd_files)}")
    if failed_files:
        print("Failed files:")
        for failed_path, return_code, failed_output in failed_files:
            if failed_output is not None:
                print(f"- {failed_path} (exit code {return_code}, moved to {failed_output})")
            else:
                print(f"- {failed_path} (exit code {return_code})")
    return 1 if fail_count else 0


if __name__ == "__main__":
    sys.exit(main())
"""
python3 /home/simple/joey/scene_synthesis/dataprocess/usdzip_package_folder.py \
/media/simple/another_Documents/isaacsim_assets/device_data/usd/processed \
/media/simple/another_Documents/isaacsim_assets/device_data/usd/processed/usdz \
--recursive --overwrite -c -v

"""
