# Scene Layout RAG

该目录包含一个可本地运行的RAG原型，用于将IsaacSim场景资产(MD/CSV)整理为可检索的知识库，并基于自然语言指令给出物体布局建议。

## 软件环境建议
1. **基础系统**: Ubuntu 22.04 + Python 3.10 (推荐使用 [micromamba](https://mamba.readthedocs.io) 或 Conda 管理虚拟环境)。
2. **GPU 驱动**: 安装与 48G + 24G 双显卡匹配的最新 NVIDIA 驱动，随后安装 CUDA 12.1 对应的 `cudnn`。
3. **PyTorch**: 通过 `pip install torch --index-url https://download.pytorch.org/whl/cu121` 获取GPU版 PyTorch 2.1+。
4. **Python 依赖**: `pip install -r requirements.txt` (包含 sentence-transformers、transformers、accelerate、peft、datasets、faiss-gpu、bitsandbytes 等)。
5. **开发工具**: 可选安装 `uv` 或 `poetry` 做包管理，`pre-commit` 做静态检查。

## 项目结构
```
scene_layout_rag/   # RAG核心库（以 src 作为项目根）
scripts/            # 训练 / 推理 / 构建脚本
requirements.txt
```

## 典型工作流
> 请在 `/home/qiaoyo/python_proj/scene_synthesis/src` 下执行命令；`scene_layout_rag` 模块会自动把当前 `src` 视为项目根。如需在其他路径运行脚本，可通过 `PYTHONPATH=/path/to/src` 暴露此目录。

1. **构建索引**
   ```bash
   cd /home/qiaoyo/python_proj/scene_synthesis/src
   python scripts/ingest_assets.py
   ```
2. **即时推理**
   ```bash
   python scripts/run_inference.py "在入库区放置两排可折叠纸箱"
   ```
   > 说明：推理阶段会先使用 sentence-transformers 检索相关资产，再将命中的资产（含 bbox）连同需求一起喂给本地 LLM（`ModelConfig.llm_name_or_path` 对应的模型）生成布局方案。若 LLM 解析失败，则自动回落到启发式推理。
3. **LoRA 微调**
   ```bash
   python scripts/train_layout_model.py --model mistralai/Mistral-7B-Instruct-v0.2 --output runs/lora-layout
   ```
4. **CLI 快速测试**
   ```bash
   python -m scene_layout_rag.cli "请给出AGV通道与传送带的布局"
   ```

## 资产CSV格式扩展
- 在原有 `类别, USD路径, 短描述, 长描述` 基础上，第5列可填写 `bbox`（JSON 或 `长,宽,高` 数值），例如：`0.8,0.6,0.5` 或 `{"size":[0.8,0.6,0.5],"unit":"m"}`。若留空则使用 1m 的默认值。
- `ingest_assets.py` 会自动解析该列并将 bbox 信息加入文档元数据，供 LLM 推理阶段使用。

## 下一步可扩展方向
- 接入企业内部的 USD 元数据或实时库存系统（通过 `AssetPaths` 自定义 CSV/MD 路径）。
- 将 `layout_reasoner` 替换为学习型策略（例如训练一个小型几何网络或RL agent）。
- 使用 `FastAPI`/`Gradio` 暴露在线接口，与IsaacSim USD生成脚本直接联动。
