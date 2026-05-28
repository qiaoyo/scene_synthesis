#!/usr/bin/env bash
set -euo pipefail

ISAAC_PYTHON="/home/simple/isaac-sim5.1/python.sh"
INPUT_DIR="/media/simple/another_Documents/isaacsim_assets/scenedata"
OUTPUT_DIR="/home/simple/Desktop/Scene-Knowledge/scene_ouput/md"
MAIN_SCRIPT="/home/simple/joey/scene_synthesis/dataprocess/usd2md/main.py"

mkdir -p "$OUTPUT_DIR"

shopt -s nullglob
for usda_file in "$INPUT_DIR"/*.usda; do
    scene_name="$(basename "$usda_file" .usda)"

    for mode in brief verbose; do
        output_file="$OUTPUT_DIR/${scene_name}-${mode}.md"
        echo "Generating $output_file"
        "$ISAAC_PYTHON" "$MAIN_SCRIPT" \
            --input "$usda_file" \
            --output "$output_file" \
            --mode "$mode"
    done
done
