# USD to Markdown Documenter

This tool generates a detailed, human-readable Markdown document from a Universal Scene Description (USD) text file('.usda'). The output is structured to be easily understood by Large Languange Models and is ideal  for building a knowledge base for Retrieval-Augmented Generation(RAG) systems.

## Features

- Extracts scene metadata (up-axis, units, etc.).
- Generates a clear scene hierarchy tree.
- Supports `'verbose'/'brief' `两种输出模式，满足完整文档与快速概览的不同需求.
- Provides detailed descriptions for individual Prims, including:
  - Transform(Translate, Rotate, Scale)
  - Geometry details (for Meshes)
  - Physics properties (for Rigid Bodies and Colliders)
  - Light parameters
  - Material and Shader properties with texture bindings
    -Highly modular code structure for easy extension.

## Installation

1. **Prerequisites**: Python 3.7+
2. **Install dependencies**:

```bash
  pip install -r requirements.txt
```

## Usage

Run the script from the command line, providing the input USDA file and the desired output Markdown file path, 并可通过 '--mode {verbose,brief}' 控制输出详略 (默认 `'verbose'`).

```bash
python src/main.py 
  --input /path/to/your/scene.usda 
  --output /path/to/your/scene_doc.md 
  --mode brief

python usd2md/main.py --input /media/simple/another_Documents/isaacsim_assets/scenedata/sorting.usda --output /home/simple/Desktop/Scene-Knowledge/md/sorting-brief.md --mode brief
```
