# scene_synthesis · ReAct Scene Layout

基于 ``方案/优化.md`` 实现的工业场景合成系统：本地 LLM 规划 + RAG 资产检索 +
9 个工具 + 完整的 思考→行动→观察→反思→策略调整 ReAct 闭环。

## 目录与数据布局

资产从「输入数据」→「索引产物」→「运行轨迹」分三层存放，互不交叉：

```
scene_synthesis/
├── data/
│   ├── assets/                     # 输入：人写或脚本产出的原始资产数据
│   │   ├── csv/*.csv               # 资产清单（含 bbox_min/max、tag、description、USD path）
│   │   ├── md/*.md                 # 场景模板（brief/verbose），按场景类别分文件
│   │   └── docs/*.jsonl            # 场景先验文本（中文 / 英文双套）
│   └── indexes/                    # 索引产物：由 `cli ingest` 写入
│       ├── corpus.jsonl            # ★ 事实源：每行一条 AssetDocument JSON
│       ├── vectors.faiss           # 默认产出：FAISS 向量索引
│       └── index_meta.json         # FAISS 与 corpus.jsonl 的对齐元信息
├── outputs/                        # 运行时产物（轨迹、场景快照），由 ReActAgent.save 写入
│   └── run_<timestamp>.json
├── scene_layout_rag/               # 主代码包
└── scripts/run_inference.py        # 端到端入口
```

### 为什么把数据这样切分？

- **assets/** 是人类编辑或外部脚本产出，**永远不要被代码直接修改**；
  `dataprocess/` 里的脚本负责把 USD/USDA 转换成这些 csv/md/jsonl。
- **indexes/corpus.jsonl** 是「事实源（source of truth）」：
  纯文本、确定性、人类可读、可以 grep/diff，**没有 GPU 也能加载**。
  即便换嵌入模型，也只是重建 FAISS，corpus 不动。
- **indexes/vectors.faiss** 只是「加速层」，可以删掉再重建。
- **outputs/** 是每次运行的副产物（思考链、最终场景快照），可以无脑清掉。

### 资产文档（AssetDocument）的统一结构

无论来自 csv / md / jsonl，都 normalize 成同一种结构落到 `corpus.jsonl`：

```json
{
  "doc_id": "Conveyor_with_bbox_meters-3-8c5f762f26c722e5",
  "content": "Asset type: Conveyor\nUSD path: ...\nTags: ...\nFunctional description: ...\nBounding box size: 1.20 x 0.50 x 0.80 m",
  "metadata": {
    "doc_type": "asset",                 // asset / scene_template / scene_prior
    "asset_type": "Conveyor",
    "usd_path": "/.../usdz/Conveyor/...usdz",
    "bbox": {"min":[...],"max":[...],"size":[...],"center":[...],"unit":"m"},
    "bbox_size": [1.2, 0.5, 0.8],
    "bbox_min": [...], "bbox_max": [...], "bbox_center": [...],
    "tags": {"Shape":"rectangular", ...},
    "description": "...",
    "source": "/abs/path/Conveyor_with_bbox_meters.csv",
    "row_index": 3
  }
}
```

LLM 在 `place_instance` 时必须先用 `retrieve_assets` 查到 `doc_id`，再把它
作为 `asset_doc_id` 传入；这样保证场景里出现的每件资产都能溯源到具体 USD 文件

+ 真实 bbox。

## 安装与运行

```bash
pip install -r requirements.txt
# 1) 一次性：构建索引（第一次或 assets 改动时）
python -m scene_layout_rag.cli ingest
# 2) 检索测试（不需要 LLM）
python -m scene_layout_rag.cli retrieve "warehouse rack with pallet" --top-k 5
# 3) 运行 ReAct
python scripts/run_inference.py --command "Build a small sorting cell"
```

如果暂时不想构建/加载 FAISS（例如调试 BM25 路径）：

```bash
python -m scene_layout_rag.cli --no-faiss retrieve "warehouse" --top-k 3
```

## 架构（对齐 ``方案/优化.md``）

```
┌────────── ReActAgent.run(command) ──────────┐
│                                             │
│  for step in range(max_steps):              │
│    ┌─ 1. THINK ───────────────────────────┐ │
│    │ LLMPlanner.think_and_decide(...)     │ │
│    │   → {thought, action, action_input}  │ │
│    └──────────────────────────────────────┘ │
│    ┌─ 2. ACT ─────────────────────────────┐ │
│    │ TOOL_REGISTRY[action](ctx, **input)  │ │
│    │   → ToolResult                       │ │
│    └──────────────────────────────────────┘ │
│    ┌─ 3. OBSERVE ─────────────────────────┐ │
│    │ Observer.observe(action, result)     │ │
│    │   → Observation:                     │ │
│    │     · validation (collisions)        │ │
│    │     · scene_semantics                │ │
│    │     · support_state                  │ │
│    │     · physics_feedback (AABB / Isaac)│ │
│    │     · suggestions                    │ │
│    └──────────────────────────────────────┘ │
│    ┌─ 4. REFLECT (if not observation.ok) ─┐ │
│    │ LLMPlanner.reflect(...)              │ │
│    │   → {summary, cause, next_strategy}  │ │
│    │ → 沉淀到 record.lessons              │ │
│    └──────────────────────────────────────┘ │
│    ┌─ 5. ADJUST_STRATEGY (≥2 连失败) ────┐ │
│    │ LLMPlanner.adjust_strategy(...)      │ │
│    │   → {strategy}                       │ │
│    │ → 写入 record.strategy，下次注入到     │ │
│    │   THINK prompt 里                    │ │
│    └──────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

## 工具集（9 个）

每个工具的输入输出 schema 在源文件里都写得很死，便于 LLM 严格调用：

| 工具                | 作用                          | 关键输入                                                |
| ------------------- | ----------------------------- | ------------------------------------------------------- |
| `retrieve_assets` | 检索资产/场景文档             | `query`, `asset_type?`, `doc_type?`               |
| `place_instance`  | 放置新资产，可顺带登记 parent | `asset_doc_id`, `position`, `parent_instance_id?` |
| `move_asset`      | 平移已有实例                  | `instance_id`, `new_position`                       |
| `delete_asset`    | 删除实例（自动解绑 children） | `instance_id`                                         |
| `query_scene`     | 行动前的精确状态查询          | `instance_id?`, `asset_type?`                       |
| `check_collision` | AABB 碰撞检测                 | （可选）`instance_id_a/b`                             |
| `check_support`   | 几何验证支撑关系              | （可选）`child_id` + `parent_id`                    |
| `set_support`     | 登记支撑关系 + 几何检查       | `child_id`, `parent_id`                             |
| `simulate_step`   | 静态稳定性 / 物理仿真         | `duration?`                                           |

`adjust_z` 暂未实现（``方案/优化.md`` 注明「可能不需要」）。

### 物理仿真接口

默认走 `validators.run_static_simulation`（AABB + 几何稳定性近似）。要接入
IsaacSim：实现 `scene_layout_rag/physics/isaac_bridge.py` 中的 `IsaacBridge`，
并把实例放到 `ToolContext.extras['isaac_bridge']`，同时让
`AgentConfig.physics_enabled = True`。

## 观测结构（Observation）

每一步的 observation 都是这样一棵 JSON 树（对齐优化方向 2）：

```json
{
  "ok": false,
  "tool_result": {"ok": true, "data": {...}},
  "validation":  {"ok": false, "tool_ok": true, "collisions": [{"a":"...", "b":"..."}]},
  "scene_semantics": {
    "corridors":  [{"from":"A","to":"B","width":2.4,"axis":"x","blocked":false}],
    "work_zones": [{"anchor":"Workbench_1","assets":["IndustrialRobot_1","Box_1"], ...}],
    "flow_paths": [{"type":"conveyor","members":["Conveyor_1","Conveyor_2"],"connected":true}]
  },
  "support_state": {
    "valid_relations": [...],
    "invalid_relations": [{"child":"Box_1","parent":"Conveyor_1","z_gap":...,"xy_coverage":...,"issues":["..."]}]
  },
  "physics_feedback": {"stable": false, "fallen_assets":[...], "contacts":[...], "warnings":[...]},
  "suggestions": ["支撑关系不稳: ...", "物理告警: ..."],
  "error": null
}
```

## 配置（`scene_layout_rag/config.py`）

| 项                                | 默认                                       | 说明                           |
| --------------------------------- | ------------------------------------------ | ------------------------------ |
| `model.llm_backend`             | `"local"`                                | 仅实现了本地 transformers 后端 |
| `model.llm_name_or_path`        | `mistralai/Mistral-7B-Instruct-v0.2`     | 想换模型改这里                 |
| `model.device`                  | `"cuda:1"`                               | 单卡 GPU                       |
| `model.embedding_model`         | `sentence-transformers/all-MiniLM-L6-v2` | 决定 FAISS 嵌入维度            |
| `enable_faiss`                  | `True`                                   | 关闭即只用 BM25 检索           |
| `agent.max_steps`               | 20                                         | ReAct 最大循环步数             |
| `agent.reflection_enabled`      | True                                       | 失败时是否反思                 |
| `agent.strategy_adjust_enabled` | True                                       | 连续失败 ≥2 是否调整策略      |
| `agent.physics_enabled`         | False                                      | True 时启用 IsaacBridge 路径   |

## 端到端调用示例

```python
from scene_layout_rag import ProjectConfig
from scene_layout_rag.rag import AssetRAG
from scene_layout_rag.agent import ReActAgent

cfg = ProjectConfig()
cfg.ensure_directories()

rag = AssetRAG(cfg)
rag.load()                    # 或 rag.build(save=True) 第一次构建

agent = ReActAgent(cfg, rag=rag)
record = agent.run("Build a small sorting cell with one conveyor and two boxes.")
agent.save(record)
print(record.finish_reason, len(record.steps), len(record.lessons))
```

## 烟雾测试

可以不开 GPU 跑通整条链：

```bash
# 用脚本化 planner 模拟 LLM 输出，验证 think→act→observe→reflect→adjust 链路
python3 -c "$(sed -n '/PY$/,$p' README.md | head -1)"  # 见仓库 history 中的 dry-run 片段
```

完整脚本在仓库历史中保留为 `dry-run` snippet；正式运行使用真实 LLM 时直接走
`scripts/run_inference.py`。

## 已知限制

1. AABB 不支持任意旋转 — `Instance.rotation_deg` 只标注朝向。OBB 需配合
   IsaacSim 接入。
2. `analyze_scene_semantics` 走廊判定是简化版（仅空隙宽度 + 中点遮挡），不是
   导航图算法；后续可以替换为 navmesh。
3. `chunk_text` 只支持字符级，未做 token 级；嵌入模型词表对齐由
   sentence-transformers 自行截断。

# 使用

python -m scene_layout_rag.cli ingest                         # 一次性建索引
python scripts/run_inference.py --command "Build a sorting cell"用 config 中的 cuda:1 + Mistral-7B
