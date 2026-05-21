# scene_synthesis · scene_layout_react

这是一个工业场景合成实验框架，当前代码包名为 `scene_layout_react`。
核心流程是：

1. 从 `data/assets/csv` 和 `data/assets/md` 读取资产与场景模板。
2. 用 `scene_layout_react.rag.AssetRAG` 加载或构建 FAISS 检索索引。
3. 用 OpenAI-compatible 本地服务驱动 `LLMPlanner` 生成工具调用。
4. `ReActAgent` 执行工具，维护 `SceneState`，并通过 `Observer` 检查碰撞、支撑关系和可选物理反馈。

当前仓库更接近研究原型，而不是可直接发布的 Python 包。README 只描述当前代码真实存在的接口和限制。

## 目录结构

```text
scene_synthesis/
├── data/
│   ├── assets/
│   │   ├── csv/                    # 资产清单，含 Path、Tag、Description、bbox_min/max 等字段
│   │   └── md/                     # 场景模板文档
│   └── indexes/
│       ├── corpus.jsonl            # AssetDocument JSONL 语料
│       ├── asset.faiss             # asset 类型 FAISS 索引
│       ├── scene_template.faiss    # scene_template 类型 FAISS 索引
│       ├── vectors.faiss           # 旧索引产物，当前代码不优先使用
│       └── index_meta.json         # 索引元数据
├── dataprocess/                    # USD/USDA/CSV 数据处理脚本集合
├── outputs/                        # agent 运行日志
├── scene_layout_react/             # 当前主代码包
│   ├── asset_loader.py             # CSV/Markdown -> AssetDocument
│   ├── config.py                   # ProjectConfig
│   ├── data_models.py              # AssetDocument、Instance、SceneState
│   ├── llm_planner.py              # OpenAI-compatible planner
│   ├── observer.py                 # 碰撞、支撑、物理反馈观察
│   ├── rag.py                      # FAISS + SentenceTransformer 检索
│   ├── react_agent.py              # ReAct 主循环
│   ├── scene_state.py              # SceneStateManager
│   ├── physics/                    # Isaac Sim 子进程桥接实验代码
│   ├── tools/                      # 工具注册与工具实现
│   └── test/                       # 当前是脚本/实验用例混合目录
├── scripts/
│   └── run_inference.py            # 当前端到端入口
├── requirements.txt
└── 方案/
```

## 安装

```bash
pip install -r requirements.txt
```

`requirements.txt` 目前包含 GPU/LLM 相关依赖，例如 `torch`、`transformers`、`sentence-transformers`、`faiss-gpu`、`openai`、`jsonschema`。

注意：

- 当前没有 `pyproject.toml`、`setup.py` 或安装包配置。
- 当前没有 `scene_layout_react.cli` 或 `scene_layout_rag.cli`。
- 本地环境必须能导入 `openai`，否则 `import scene_layout_react` 会失败。
- 默认配置硬编码了本机路径、`cuda:1`、本地 LLM 服务地址和 Isaac Sim 路径，需要按机器环境修改。

## 当前配置

主要配置位于 `scene_layout_react/config.py` 的 `ProjectConfig`。

| 字段 | 当前默认值 | 说明 |
| --- | --- | --- |
| `assets_root` | `/home/simple/joey/scene_synthesis/data/assets` | 资产根目录 |
| `inventory_csvs` | `[]` | 需要手动传入 CSV 文件列表，默认不会自动扫描 |
| `scene_md_files` | `[]` | 需要手动传入 Markdown 文件列表，默认不会自动扫描 |
| `embedding_model` | `sentence-transformers/all-MiniLM-L6-v2` | 检索嵌入模型 |
| `device` | `cuda:1` | SentenceTransformer 运行设备 |
| `index_dir` | `/home/simple/joey/scene_synthesis/data/indexes` | 索引目录 |
| `output_dir` | `/home/simple/joey/scene_synthesis/outputs` | agent 日志目录 |
| `physics_enabled` | `True` | 默认启用 Isaac 物理反馈 |
| `model` | `Qwen/Qwen3-32B-AWQ` | OpenAI-compatible 服务中的模型名 |
| `llm_api_base_url` | `http://127.0.0.1:8000/v1` | 本地 LLM 服务地址 |
| `llm_api_key` | `EMPTY` | 本地服务占位 key |
| `max_steps` | `10` | ReAct 最大步数 |
| `isaac_python` | `/home/simple/isaac-sim5.1/python.sh` | Isaac Sim Python 启动脚本 |
| `isaac_worker_path` | `scene_layout_react/physics/worker.py` 的绝对路径 | Isaac worker 路径 |

## 运行入口

当前唯一端到端入口是：

```bash
python scripts/run_inference.py --command "Build a sorting cell"
```

脚本行为：

1. 设置 `HF_ENDPOINT=https://hf-mirror.com`。
2. 创建 `ProjectConfig()`。
3. 如果 `data/indexes/corpus.jsonl` 存在，调用 `AssetRAG.load()`。
4. 否则调用 `AssetRAG.build(save=True)`。
5. 创建 `ReActAgent(cfg, rag=rag)`。
6. 执行 `agent.run(args.command, cfg.max_steps)`。

重要限制：

- 如果索引不存在，默认 `ProjectConfig.inventory_csvs` 和 `scene_md_files` 为空，`build()` 不会自动读取 `data/assets`。
- 如果本地 OpenAI-compatible 服务没有运行，planner 调用会失败。
- 默认 `physics_enabled=True`，每步观察会尝试 Isaac 物理反馈。

## 手动加载资产并构建索引

当前没有 CLI，需要通过 Python 代码显式指定输入文件：

```python
from pathlib import Path

from scene_layout_react.config import ProjectConfig
from scene_layout_react.rag import AssetRAG

root = Path("/home/simple/joey/scene_synthesis")
cfg = ProjectConfig(
    inventory_csvs=sorted((root / "data/assets/csv").glob("*.csv")),
    scene_md_files=sorted((root / "data/assets/md").glob("*.md")),
)

rag = AssetRAG(cfg)
rag.build(save=True)
```

加载已有索引：

```python
from scene_layout_react.config import ProjectConfig
from scene_layout_react.rag import AssetRAG

cfg = ProjectConfig()
rag = AssetRAG(cfg)
rag.load()
results = rag.retrieve("industrial robot", doc_type="asset", top_k=3)
```

## ReAct 主流程

`scene_layout_react/react_agent.py` 中的 `ReActAgent.run()` 当前流程如下：

```text
for each step:
  1. planner.reason(...)
     -> JSON strategy
  2. planner.decide_action(...)
     -> OpenAI tool calls or final response
  3. execute each tool call through TOOL_REGISTRY
  4. observer.observe()
     -> current_state, collision validation, support_state, optional physics_feedback
  5. if observation failed or any tool failed:
     planner.reflect(...)
     store lesson
```

`run()` 返回普通 `dict`，不是 dataclass；当前 `ReActAgent` 没有 `save()` 方法。

## 数据模型

`AssetDocument`：

```python
AssetDocument(
    doc_id="...",
    content="...",
    metadata={...},
    embedding=None,
)
```

资产文档通常包含：

- `metadata["doc_type"]`: `asset` 或 `scene_template`
- `metadata["asset_type"]`
- `metadata["instance_id"]`
- `metadata["usd_path"]`
- `metadata["bbox"]["size"]`
- `metadata["tags"]`
- `metadata["description"]`

`Instance`：

```python
Instance(
    instance_id="...",
    asset_type="...",
    asset_doc_id="...",
    usd_path="...",
    position=[0.0, 0.0, 0.0],
    rotation_deg=0.0,
    bbox_size=[1.0, 1.0, 1.0],
)
```

`SceneState` 持有：

- `instances: dict[str, Instance]`
- `support_children: dict[str, list[str]]`

## 当前工具

工具注册通过 `scene_layout_react.tools` 的导入副作用完成；每个工具的 schema 在对应文件中定义。

| 工具名 | 文件 | 当前作用 |
| --- | --- | --- |
| `retrieve_tool` | `tools/retrieve_assets.py` | 检索 `asset` 或 `scene_template` |
| `place_instance` | `tools/place_instance.py` | 根据 `doc_id` 放置资产实例 |
| `move_asset` | `tools/move_asset.py` | 移动已有实例 |
| `delete_asset` | `tools/delete_asset.py` | 删除已有实例并解绑 children |
| `query_scene` | `tools/query_scene.py` | 查询当前场景状态 |
| `set_support` | `tools/set_support.py` | 登记 child -> parent 支撑关系 |
| `check_collision` | `tools/check_collision.py` | 通过 Isaac bridge 做碰撞检查 |
| `check_support` | `tools/check_support.py` | 通过 Isaac bridge 做支撑检查 |
| `simulate_step` | `tools/simulate_step.py` | 通过 Isaac bridge 做仿真步进 |

注意：README 旧版中的 `retrieve_assets` 不是当前 schema 名；当前工具名是 `retrieve_tool`。

## 物理与观察

`Observer.observe()` 当前会执行：

- AABB 碰撞检测
- 支撑关系几何检查
- 可选 Isaac 物理反馈

当 `ProjectConfig.physics_enabled=True` 时，`ReActAgent` 会通过 `run_isaac_physics_feedback()` 调用 `scene_layout_react/physics/worker.py`。

当前物理桥接仍是实验状态。`worker.py` 需要补全入口调度和内部错误后，`check_collision`、`check_support`、`simulate_step` 才能稳定工作。

## 当前已知问题

这些问题来自当前代码状态，README 保留它们是为了避免把实验代码误认为稳定框架。

### Blocking

1. `import scene_layout_react` 会强制导入 `ReActAgent`，间接要求 `openai` 已安装；缺依赖时连子模块导入都会失败。
2. 默认配置不自动扫描 `data/assets/csv` 和 `data/assets/md`；索引不存在时 `rag.build()` 可能构建空语料。
3. `physics_enabled=True` 是默认值，但 Isaac worker 当前不完整，默认运行会频繁得到失败物理反馈。
4. `scene_layout_react/physics/worker.py` 没有 stdin/stdout 主入口调度，并存在未定义变量和缺失导入。
5. `place_instance` 使用资产 metadata 里的 `instance_id` 作为场景实例 ID，同一资产不能重复放置。
6. 测试目录当前不是可靠 pytest 测试集：部分文件是脚本，部分测试引用了已经不存在的 helper，部分在顶层创建 OpenAI client。

### Important

1. `PlaceInstanceTool.run()` 在 doc_id 未命中时会引用未初始化的 `doc`。
2. CSV ingestion 对坏 bbox 数据没有错误边界，且 `content`/`metadata` 可能在未赋值时被使用。
3. `AssetRAG.retrieve()` 在 `top_k=None` 时读取不存在的 `config.retrieval_top_k`。
4. `set_support` 只登记关系，不执行它描述中的几何验证。
5. `LLMPlanner._tool_chat()` 返回 `tool_error` 时，`ReActAgent.run()` 仍可能访问不存在的 `decision["calls"]`。
6. `ReActAgent` 从 `tools.base` 读取 `TOOL_REGISTRY`；使用方需要确保 `scene_layout_react.tools` 已被导入以触发工具注册。
7. `Observer` 的 AABB 碰撞不考虑 `rotation_deg`。
8. 数据处理脚本中存在大量硬编码本机路径和 Isaac 环境路径。
9. `.gitignore` 当前为空，工作区里已有 `__pycache__`、运行日志等产物进入 git 状态。
10. 缺少 package metadata、lint/format 配置、pytest 配置和 CI 入口。

## 建议修复顺序

1. 先关闭默认物理或补全 Isaac worker，保证 `scripts/run_inference.py` 可稳定跑通。
2. 修复 `ProjectConfig` 的数据自动发现或要求入口显式传入 CSV/Markdown。
3. 修复工具注册路径，确保 `ReActAgent` 初始化时一定有完整工具列表。
4. 修复 `place_instance` 的实例 ID 生成，使同一资产可重复放置。
5. 将 `scene_layout_react/test` 拆分为真正的 pytest 单元测试和手动 smoke scripts。
6. 补齐 `.gitignore`、包配置、测试命令和最小 CI。

## 当前不支持的旧命令

以下旧 README 中出现过的命令或 API 当前不存在：

```bash
python -m scene_layout_rag.cli ingest
python -m scene_layout_rag.cli retrieve "warehouse" --top-k 3
python -m scene_layout_react.cli ingest
```

以下旧 API 当前也不存在：

```python
cfg.ensure_directories()
agent.save(record)
from scene_layout_rag import ProjectConfig
from scene_layout_rag.agent import ReActAgent
```
