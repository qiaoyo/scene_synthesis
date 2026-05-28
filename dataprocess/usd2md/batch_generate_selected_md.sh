#!/usr/bin/env bash
set -euo pipefail

ISAAC_PYTHON="/home/simple/isaac_env/bin/python"
MAIN_SCRIPT="/home/simple/joey/scene_synthesis/dataprocess/usd2md/main.py"
OUTPUT_DIR="/home/simple/Desktop/Scene-Knowledge/scene_output/md_selected"

# Put the USD/USDA files you want to process here.
USD_FILES=(
    "/media/simple/another_Documents/isaacsim_assets/scenedata/IsaacScene/Collected_Factory/Factory_kong.usd"
    "/media/simple/another_Documents/isaacsim_assets/scenedata/IsaacScene/Collected_full_warehouse/full_kong.usd"
    "/media/simple/another_Documents/isaacsim_assets/scenedata/IsaacScene/Collected_IsaacWarehouse/IsaacWarehouse_kong.usd"
    "/media/simple/another_Documents/isaacsim_assets/scenedata/IsaacScene/Collected_warehouse/warehouse_kong.usd"
    "/media/simple/another_Documents/isaacsim_assets/scenedata/IsaacScene/Collected_warehouse_multiple_shelves/warehouse_multiple_shelve_kong.usd"
    "/media/simple/another_Documents/isaacsim_assets/scenedata/IsaacScene/Collected_warehouse_with_forklifts/warehouse_with_forklifts_kong.usd"
    "/media/simple/another_Documents/isaacsim_assets/scenedata/IsaacScene/Assembly_kong.usd"
    "/media/simple/another_Documents/isaacsim_assets/scenedata/IsaacScene/fac_kong.usd"
    "/media/simple/another_Documents/isaacsim_assets/scenedata/IsaacScene/log_kong.usd"
)

mkdir -p "$OUTPUT_DIR"

for usd_file in "${USD_FILES[@]}"; do
    if [[ ! -f "$usd_file" ]]; then
        echo "Skipping missing file: $usd_file" >&2
        continue
    fi

    scene_name="$(basename "$usd_file")"
    scene_name="${scene_name%.*}"

    for mode in brief verbose; do
        output_file="$OUTPUT_DIR/${scene_name}-${mode}.md"
        echo "Generating $output_file"
        "$ISAAC_PYTHON" "$MAIN_SCRIPT" \
            --input "$usd_file" \
            --output "$output_file" \
            --mode "$mode"
    done
done
