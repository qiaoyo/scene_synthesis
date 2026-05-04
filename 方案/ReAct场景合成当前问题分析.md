# ReAct 场景合成当前问题分析

> 分析入口：`/home/simple/joey/scene_synthesis/scene_layout_rag/cli.py`  
> 分析时间：2026-04-26  
> 结论概览：当前项目已经具备 `--react` 参数、`ReActAgent` 类、工具注册表和若干场景工具，但整体仍停留在“LLM 输出工具名 + Python 执行工具”的原型层。它还没有形成真正可靠的 ReAct 场景合成系统：数据检索结果没有和可放置资产强绑定，工具契约不够严格，观察/反思无法有效驱动纠错，最终输出也没有对接可视化或 USD 生成链路。

---

## 一、从入口看真实执行链路

### 1.1 当前 CLI 有两条链路

`scene_layout_rag/cli.py` 当前逻辑是：

1. 解析自然语言 `command`。
2. 创建 `ProjectConfig()`。
3. 实例化 `SceneLayoutRAG(config)`。
4. 如果不加 `--react`，走 `pipeline.generate_layout(...)` 单次 RAG 布局。
5. 如果加 `--react`，走 `pipeline.generate_layout_react(...)`，然后把 `LayoutPlan.summary()` 和简化版 trace 打印/保存。

也就是说，ReAct 并不是默认链路，仍然需要显式传入 `--react`。

### 1.2 入口层存在的问题

- **CLI 无法在轻量环境中启动。** 当前 `scene_layout_rag/__init__.py` 会导入 `rag.py`，`rag.py` 又在模块顶层导入 `llm_planner.py`，而 `llm_planner.py` 顶层导入 `torch` 和 `transformers`。在当前环境中执行 `python -m scene_layout_rag.cli --help` 会直接报错：`ModuleNotFoundError: No module named 'torch'`。这意味着用户连 help、配置检查、数据检查都无法运行。

- **远程 API 模式也被本地模型依赖绑死。** `LLMPlanner.react_call()` 支持 OpenAI-compatible API，但由于 `torch` 是顶层 import，即使只想用远程 API，也必须先安装本地推理依赖。

- **`--assets` 覆盖逻辑破坏默认数据目录结构。** 默认 `AssetPaths.__post_init__()` 会扫描 `assets_root/csv`、`assets_root/md`、`assets_root/docs`。但是 CLI 中 `--assets` 覆盖时只扫 `Path(args.assets).glob("*.csv")` 和 `*.md`，没有继续扫描 `csv/`、`md/`、`docs/` 子目录，也没有处理 jsonl。因此 `--assets data/assets` 反而会丢失默认可用数据。

- **`--top-k` 对 ReAct 无效。** `--top-k` 只传给 single-pass 的 `generate_layout()`。ReAct 模式下检索数量完全由 LLM 给 `retrieve_assets` 的 `top_k` 决定，入口参数没有约束作用。

### 1.3 建议

- 把 `scene_layout_rag/__init__.py` 改成轻量导入，不要默认导入 `SceneLayoutRAG`、`LLMPlanner` 这种重依赖对象。
- 将 `torch`、`transformers` 延迟到 `LLMPlanner._ensure_model()` 内部导入；远程 API 调用路径不应依赖本地模型库。
- 统一 `AssetPaths` 的扫描逻辑，CLI 覆盖资产根目录时重新创建 `AssetPaths(assets_root=args.assets)`，不要手写 `glob("*.csv")`。
- 给 ReAct 模式增加明确参数，如 `--react-top-k`、`--max-assets`、`--asset-doc-type asset`，或者让工具层有默认限制。

---

## 二、数据加载与资产语料问题

### 2.1 当前加载方式

`AssetIngestor.build_documents()` 会混合加载三类文档：

- `data/assets/csv/*.csv`：资产清单，生成 `doc_type=asset`。
- `data/assets/md/*.md`：场景 Markdown 模板，生成 `doc_type=scene_template`。
- `data/assets/docs/*.jsonl`：场景先验描述，生成 `doc_type=scene_prior`。

当前数据规模粗略为：

- CSV 文件 11 个，但真正可解析为资产的记录约 118 条。
- Markdown 文件 32 个，按当前 `chunk_by_paragraph(block_size=3)` 会产生约 8769 个场景模板 chunk。
- docs 下 json/jsonl 文件 2 个，共 30 条 scene prior 记录。

### 2.2 当前问题

- **资产检索语料被场景模板严重淹没。** `retrieve_assets` 使用同一个向量库检索所有文档类型，但实际资产记录只有一百多条，Markdown 模板 chunk 却有数千条。Agent 想检索资产时，很容易命中 `scene_template` 或 `scene_prior`，这些文档没有 `usd_path`、没有可放置 bbox，却仍可能被返回给 LLM。

- **`retrieve_assets` 没有强制过滤 `doc_type=asset`。** 代码中 `cat = doc.metadata.get("asset_category", doc.doc_id)`，非资产文档会被当成一种伪 asset 返回，`usd_path` 为空、`bbox` 为空。这会污染工作记忆，也会诱导 LLM 调用 `place_instance` 时填入不可用资产。

- **CSV schema 不统一导致数据被跳过。** `scene_with_bbox_meters.csv` 使用 `Scene_path` 字段，而加载器只识别 `Path`、`USD`、`USD Path`，所以该文件 8 条场景资产记录全部被跳过。其他资产文件可用，但说明加载器对 schema 演化不够稳健。

- **资产 ID 粒度不对。** CSV 资产在检索结果里返回的 `asset_id` 是类别名，如 `Conveyor`、`Box`，不是具体模型 ID。具体模型只能靠 `doc_id` 或 `usd_path` 区分，但 `SceneState.AssetInstance` 没有保存 `doc_id`。最终输出也只保留 `asset_id` 和 `usd_path`，丢失了“这个实例来自哪条资产记录”的可追踪性。

- **bbox 与 USD 变换没有统一坐标语义。** CSV 中 bbox 是米级包围盒，工具和 validator 直接用它做 AABB。但 `SceneState.to_layout_json()` 和 `scene.py` 又硬编码 `scale=[0.01, 0.01, 0.01]`。如果 bbox 已经是米，渲染时再缩放 USD，物理/碰撞验证与实际视觉尺寸会不一致。

- **位置语义不明确。** Validator 假设 `position` 是 bbox 中心点；Isaac/Usd 加载则把 `position` 用作 prim translate。许多 USD 资产 pivot 不一定在 bbox 中心，且 CSV 里有 `bbox_center` 但放置工具完全没有使用它，最终会出现“验证没问题，渲染位置偏移”的情况。

### 2.3 建议

- 将当前混在一起的知识库拆成三个检索域：
  - `retrieve_scene_prior`：只查 `doc_type=scene_prior`，用于理解用户需求、判断场景类型、提取核心设备类别。
  - `retrieve_scene_template`：只查 `doc_type=scene_template`，用于参考已有场景的功能区、动线、布局模式。
  - `retrieve_assets`：只查 `doc_type=asset`，用于选择真实可放置的 USD 资产。
- 建立标准资产 schema，例如：
  - `asset_uid`：具体资产唯一 ID。
  - `category`：资产类别。
  - `usd_path`：可加载路径。
  - `bbox_min/bbox_max/bbox_size/bbox_center`：统一米单位。
  - `tags`：CSV 中 `Tag` 字段解析后的结构化标签，例如 `Shape`、`Directionality`、`Model`、`Manufacturer`、`DNA`。
  - `functional_summary`：CSV 中 `Description` 的功能用途摘要。
  - `visual_summary`：CSV 中 `Description` 的外观/材质/形态摘要。
  - `use_cases`：从描述中提取的适用场景，例如 sorting、warehouse、assembly。
  - `default_scale`、`pivot_offset`、`up_axis`、`affordances`、`support_surface`。
- `place_instance` 应接受 `asset_uid` 或 `doc_id`，由工具层根据资产注册表自动补齐 `usd_path`、`bbox`、`scale`，不要要求 LLM 手动复制长路径。
- 统一“布局坐标点”定义：建议内部用 bbox center 表示布局位置，导出 USD 时再根据 `bbox_center/pivot_offset/scale` 转换成 prim translate。

### 2.4 三类知识的分层检索策略

这里需要特别澄清：项目里不是“三种资产都要放进场景”，而是有三种不同用途的知识。它们应该在 ReAct 的不同阶段被调用。

| 知识类型 | 来源 | doc_type | 作用 | 什么时候用 | 不应该做什么 |
|---|---|---|---|---|---|
| 场景先验 | `data/assets/docs/*.jsonl` | `scene_prior` | 判断用户要什么类型的场景，需要哪些核心设备 | ReAct 开始阶段，拆解需求时 | 不应该直接拿来放置 |
| 场景模板 | `data/assets/md/*.md` | `scene_template` | 参考已有场景的区域、动线、设备组合方式 | 制定布局策略时，尤其是用户只说“仓储/分拣/装配场景”时 | 不应该被 `place_instance` 当资产 |
| 真实资产 | `data/assets/csv/*.csv` | `asset` | 选择具体可加载模型，提供 `usd_path` 和 bbox | 明确需要某类设备后，例如需要 Conveyor、Rack、AGV 时 | 不应该承担场景规划知识的全部责任 |

推荐的 ReAct 使用顺序是：

```text
用户输入
  ↓
retrieve_scene_prior
  先判断这是仓储、分拣、装配、运输、码垛中的哪类需求，以及核心设备类别
  ↓
retrieve_scene_template
  查类似场景的空间结构：有哪些区域、设备如何排列、物料流向如何组织
  ↓
retrieve_assets
  按具体类别选择真实 USD 资产：Conveyor、Rack、AGV、Workbench 等
  ↓
place_instance / move_asset / set_support
  放置、调整、建立支撑关系
  ↓
validate / finish_scene
  检查数量、碰撞、越界、支撑、输出可加载性
```

这三个检索工具的输出也应该不同：

- `retrieve_scene_prior` 输出：场景类型、核心设备类别、可能的资产数量、关键关系。
- `retrieve_scene_template` 输出：功能区、布局模式、动线建议、典型设备组合。
- `retrieve_assets` 输出：`asset_uid`、`category`、`usd_path`、`bbox`、`tags`、`functional_summary`、`visual_summary`。

这样做的好处是：大模型先知道“要做什么场景”，再知道“这个场景通常怎么布局”，最后才挑“具体放哪个模型”。否则它会直接从资产库里乱找模型，缺少整体布局策略。

### 2.5 CSV 中 Description 和 Tag 的利用不足

当前 CSV 的 `Description` 和 `Tag` 并不是没被读取。`asset_loader.py` 已经把它们放进了文档内容和 metadata：

- `Tag` 会被 `_parse_tags()` 解析成 `metadata["tags"]`。
- `Description` 会被放进 `metadata["description"]` 和检索文本。
- bbox 会被解析成 `metadata["bbox"]`、`bbox_size`、`bbox_center`。

但是问题在于：这些信息现在只是“被塞进文本里参与向量检索”，没有被充分用于后续决策。

#### 2.5.1 Description 应该怎么用

CSV 的 `Description` 里通常包含两类信息：

- `Functional Features`：这个资产能做什么，适合什么工业场景。
- `Visual Features`：它长什么样，材质、颜色、形状是什么。

目前系统只把它当成一段普通文本。更合理的做法是把它拆成可用字段：

```text
functional_summary  功能摘要：运输、分拣、存储、装配、搬运等
use_cases           适用场景：warehouse、sorting、assembly、transport 等
visual_summary      外观摘要：蓝色框架、黑色输送带、金属结构等
capabilities        能力标签：one-way transfer、steering、storage、pallet transport
placement_hints     放置提示：适合放在物流动线中、适合靠近工作台、适合承载箱体
```

这样 `retrieve_assets` 不只是返回“相似文本”，而是能告诉 Agent：

> 这个 Conveyor 是弧形转向输送带，适合分拣中心转向，不适合作为长直主干线。

这对场景合成很关键。

#### 2.5.2 Tag 应该怎么用

CSV 的 `Tag` 比普通描述更重要，因为它天然接近结构化数据。例如：

```text
Shape: circular
Directionality: one-way
DNA: DC(a)
```

或：

```text
Model: Custom Industrial Transport AGV
Manufacturer: Self-made
DNA: DB(a)
```

这些信息应该用于三件事：

1. **过滤。** 用户要“直线传送带”时，优先过滤 `Shape=straight`；用户要“转弯输送”时，优先过滤 `Shape=circular/arc`。
2. **重排。** 向量检索返回多个 Conveyor 后，根据 `Directionality`、`Shape`、`DNA`、尺寸再排序。
3. **放置约束。** `Directionality=one-way` 应影响输送线方向；`Closure=Close` 的 Box 可以堆放或存储；AGV 的型号和尺寸影响通道宽度。

第一版不需要做复杂算法，只需要先把 `tags` 原样返回给 LLM，并在 prompt 中要求它利用这些标签选择资产。第二版再做规则过滤和 rerank。

#### 2.5.3 retrieve_assets 应该返回更完整的信息

当前建议中的返回结果只有：

```json
{
  "asset_uid": "...",
  "category": "...",
  "usd_path": "...",
  "bbox": {},
  "description": "...",
  "score": 0.8
}
```

建议升级为：

```json
{
  "asset_uid": "...",
  "category": "Conveyor",
  "usd_path": "...",
  "bbox": {"size": [4.0, 1.0, 0.8], "unit": "m"},
  "tags": {
    "Shape": "circular",
    "Directionality": "one-way",
    "DNA": "DC(a)"
  },
  "functional_summary": "用于物料转向、分流和输送，适合物流分拣和制造产线。",
  "visual_summary": "蓝色框架、黑色输送带、金属滚筒。",
  "use_cases": ["sorting", "warehouse", "manufacturing"],
  "selection_reason": "匹配用户需要的分拣输送设备，且方向性为 one-way。",
  "score": 0.83
}
```

这样大模型后续选择资产时不会只看 `asset_id=Conveyor`，而是知道这个 Conveyor 到底是直线、转弯、单向、多层，能不能满足当前布局需求。

#### 2.5.4 资产选择应从“语义检索”升级为“检索 + 过滤 + 重排”

推荐流程：

```text
1. 向量检索：先找语义相似的资产
2. 类别过滤：只保留指定 category，例如 Conveyor
3. 标签过滤：按 Shape、Directionality、Closure、Model 等过滤
4. 尺寸过滤：按 bbox 判断是否适合通道、工作台、支撑关系
5. LLM 重排：让大模型在少量候选中选择最合适的资产，并说明原因
```

第一版可以只做第 1、2、3 步，先把 `tags` 和 `description` 原样返回。后续再加尺寸过滤和 LLM 重排。

---

## 三、RAG 与 ReAct 的关系仍不彻底

### 3.1 已经做对的部分

`SceneLayoutRAG.generate_layout_react()` 确实把 `retrieve_assets` 放进工具注册表，并在 ReAct 循环中让 LLM 自主调用。相比旧方案“一次性前置检索 top-k”，这是正确方向。

### 3.2 仍然不是真正闭环的原因

- **检索结果只是文本记忆，不是受控资产池。** `ReActAgent._update_working_memory()` 只把检索结果追加到 `self.retrieved_assets`。后续 `place_instance` 没有检查待放置资产是否来自这个工作记忆，也没有检查 `usd_path` 是否属于检索结果。

- **Agent 可以凭空放置资产。** Prompt 要求“放置前先检索”，但工具层没有强制。LLM 可以直接调用 `place_instance(asset_id="Conveyor", usd_path="...", position=...)`，即使这个资产从未检索到也会被加入 `SceneState`。

- **没有显式任务状态/目标追踪。** ReAct 循环只维护当前场景、上一条 observation、检索工作记忆和 lessons，没有结构化的 `goals`、`required_categories`、`placed_counts`、`unmet_requirements`。因此 “什么时候该 finish” 完全依赖 LLM 自觉。

- **`success` 定义过于宽松。** `AgentTrace.success = any(s.action == "finish" for s in self.history)`。只要 LLM 输出 `finish` 就算成功，不检查最终场景是否满足用户需求、是否无碰撞、是否有必要资产、是否可加载。

- **达到最大步数后的输出不安全。** 如果 LLM 没有 finish，函数仍把当前 `SceneState` 转成 `LayoutPlan` 返回。CLI 会输出布局，但 trace 里只是 `success=false`，没有阻止下游使用半成品。

### 3.3 建议

- 在 ReAct 状态中加入结构化任务板：
  - `requirements`：从用户需求解析出的资产类别、数量、关系、区域、路径约束。
  - `satisfied` / `missing` / `violations`。
  - `selected_assets`：检索后可用资产池。
- `place_instance` 改为只能引用 `asset_uid/doc_id`，工具从资产池中解析真实路径和 bbox。
- `finish` 应该是一个工具或受控动作，例如 `finish_scene`，执行时必须跑最终验证，不通过则返回错误 observation。
- `trace.success` 应改为 `finish_called and final_validation.ok and requirements_satisfied`。

---

## 四、ReAct 主循环实现问题

### 4.1 当前循环结构

`ReActAgent.run()` 当前每步做：

1. 用 `format_step_prompt(...)` 拼接当前状态。
2. `llm.react_call(system_prompt, step_prompt)`。
3. 正则解析 JSON，得到 `thought/action/action_input`。
4. 执行工具。
5. 如果是修改场景工具，调用 `observer.observe(scene)`；否则调用 `observe_retrieval(...)`。
6. 如果 observation 不 ok，调用 `_do_reflection(...)`。

这个框架像 ReAct，但关键反馈链条没有打通。

### 4.2 当前问题

- **工具执行错误没有进入 observation。** 如果工具返回 `ToolResult(ok=False)`，Agent 对非场景工具仍调用 `observe_retrieval({})`，其 validation 固定是 ok；对场景工具则观察当前 scene，可能也是 ok。这样 LLM 下一步看不到真正的工具错误，例如“参数缺失”“资产不存在”“usd_path 为空”。

- **无效 action 被记录为 observation_ok=True。** 当 LLM 输出不存在的工具名时，代码会把建议写进 `last_observation`，但 `ActionRecord.observation_ok=True`。这会让失败统计失真，也不会触发反思。

- **反思只在场景修改后的几何 observation 失败时触发。** 检索失败、工具参数错误、JSON 解析失败、未知工具、LLM 输出空 action 都不会触发反思，而这些恰恰是 agent 系统最常见的失败。

- **策略调整结果被丢弃。** `_do_reflection()` 内部生成了 `strategy_text` 并打印，但没有返回，也没有更新 `run()` 里的 `strategy` 变量。下一轮 prompt 中的 `strategy_section` 仍然是旧值或 None。`AgentConfig.strategy_adjust_enabled` 也没有被使用。

- **没有完整 action history。** Prompt 里只有当前 `scene_state`、上一条 observation、检索资产和 lessons，不包含最近几步完整的 action/result/error。LLM 很容易重复同样的错误。

- **LLM JSON 解析脆弱。** `_parse_llm_output()` 用正则抽取 JSON。遇到嵌套对象、多个代码块、模型输出前后解释文字时容易解析失败。解析失败后 action 为空，进入“无效工具”路径，但这个失败本身又不会被严肃处理。

- **没有重试/修复机制。** 如果 LLM 输出 JSON 格式错误，系统没有调用“修复 JSON”提示，也没有使用函数调用或 schema-constrained decoding。

### 4.3 建议

- 统一每一步 observation 格式，把 `tool_result` 纳入 observation：
  ```json
  {
    "tool": {"name": "...", "ok": false, "error": "...", "result": {}},
    "validation": {...},
    "suggestions": [...]
  }
  ```
- 所有失败都应触发反思或至少进入下一轮上下文，包括解析失败、未知工具、参数错误、检索为空。
- `_do_reflection()` 应返回 `lesson` 和可选 `strategy_text`，主循环更新 `strategy`。
- Prompt 中加入最近 N 步 action/result/error 摘要，而不是只给上一条 observation。
- 优先使用结构化工具调用或 Pydantic/JSON Schema 校验；如果只能用文本 JSON，至少实现括号匹配抽取、schema 校验和一次自动修复重试。

---

## 五、工具定义与执行层问题

### 5.1 当前工具集

当前注册工具包括：

- `retrieve_assets`
- `place_instance`
- `move_asset`
- `delete_asset`
- `query_scene`
- `check_collision`
- `check_support`
- `set_support`
- `simulate_step`

工具数量看起来够了，但“工具契约”和“工具对场景合成的约束能力”仍不足。

### 5.2 通用问题

- **`parameters_schema` 只是给 LLM 看的描述，不是真正 JSON Schema。** `BaseTool` 没有统一参数校验，required、类型、默认值都靠每个 tool 手写，容易漏。

- **工具没有事务/回滚能力。** `place_instance` 或 `move_asset` 会先修改 `SceneState`，再由 observer 发现碰撞或越界。发现失败后不会自动撤销，也没有把“建议移动到哪里”转成可执行候选。

- **没有资产注册表上下文。** 工具不知道“哪些资产是合法资产”，也不知道当前 LLM 引用的 `usd_path` 是否来自数据集。

- **工具返回值过薄。** 很多工具只返回少量字段，无法支撑下一步推理。例如 `place_instance` 不返回 `usd_path`、`asset_uid`、`support_surface`、`bbox_min/max`、`world_aabb`。

### 5.3 关键工具问题

#### retrieve_assets

- 未过滤 `doc_type=asset`。
- category 过滤只做精确相等，不支持别名、大小写、中文类别。
- 返回 `asset_id=category`，没有返回真正的可放置唯一 ID。
- 没有去重策略；同一类别多个相似模型可能挤占 top-k。

建议：返回 `asset_uid/doc_id/category/usd_path/bbox/affordances/score/source`，并默认只查资产索引。

#### place_instance

- schema 里 `usd_path` 是必填，但 execute 实际只要求 `asset_id` 和 `position`。空 `usd_path` 也能进场景。
- 不检查 `position` 长度是否为 3，不检查 bbox 是否为正数，不检查 usd 文件是否存在。
- 不根据 `doc_id` 自动补齐资产信息。
- 不做放置前预检；碰撞/越界后也不回滚。

建议：输入改为 `asset_uid`、`position`、`rotation`、可选 `support_parent`。路径、bbox、scale 从资产注册表读取；执行前先做 schema 校验、文件存在校验、AABB 预检，失败时不修改场景。

#### move_asset / delete_asset

- `move_asset` 不做预检和回滚，容易把场景改坏。
- `delete_asset` 能清理 support 引用，但没有记录删除历史，后续 LLM 不知道它为什么被删。

建议：`move_asset` 增加 dry-run 结果和自动回滚；`delete_asset` 返回完整删除摘要并进入 action history。

#### check_collision / validators

- `check_collision.py` 和 `validators.py` 重复实现 AABB 逻辑。
- AABB 完全忽略旋转和实际 USD scale。

建议：合并几何验证代码；输出 world AABB；后续引入 OBB 或基于 USD mesh/collider 的检测。

#### check_support / set_support

- `check_support.py` 与 `validators.py` 也重复实现支撑候选逻辑。
- 支撑关系只是 SceneState 字段，没有影响物理加载或最终输出。
- `set_support` 只能在已有几何几乎对齐时设置关系，不能主动调整子物体 Z 值。

建议：支撑应是布局约束之一：`place_on(child_asset, parent_instance, surface="top")` 自动计算 z 和 xy 合法区域；`set_support` 只负责声明关系是不够的。

#### simulate_step

- 文件注释仍写着 stub。
- Isaac 不可用时返回 `stable=True`，这会误导 LLM 以为物理验证通过。
- fallback 不复用 observer 的悬浮/支撑检查。

建议：Isaac 不可用时返回 `physics_available=false` 和 `stable=null/unknown`，不要返回稳定；同时提供几何 fallback 的明确警告。

---

## 六、场景状态、观测与验证问题

### 6.1 SceneState 过于薄

`SceneState.AssetInstance` 当前只保存：

- `instance_id`
- `asset_id`
- `usd_path`
- `position`
- `rotation`
- `bbox`
- `description`
- support 关系

缺少：

- `asset_uid/doc_id`
- `scale`
- `bbox_min/bbox_max/bbox_center`
- `pivot_offset`
- `semantic_tags`
- `affordances`
- `zone`
- `constraints`
- `source_retrieval_score`

这些缺失会导致布局过程不可追踪，也难以做可靠验证。

### 6.2 Validator 存在具体错误

- **越界判断公式错误。** 当前 `check_out_of_bounds()` 判断 `abs(position[i]) > half[i] + bbox[i]/2`。正确逻辑应接近 `abs(position[i]) + bbox[i]/2 > half[i]`。当前写法会放过已经伸出边界的物体。

- **默认 z=0 会让物体半截在地面下。** AABB 以 bbox center 为 position，所以高度为 1m 的物体放在 z=0 时底部是 -0.5m。Prompt 又没有明确“position 是中心点还是落地点”，LLM 很容易全部放在 z=0。

- **支撑与碰撞关系没有区分。** 如果一个箱子放在传送带上，正确状态是底面接触父物体顶面；但系统没有专门的接触/支撑几何模型，容易把支撑、穿透、悬浮混在一起。

- **语义观测太弱。** `_analyze_semantics()` 只按类型计数，并按 X 轴估算 corridor。它不能判断分拣线是否连通、AGV 通道是否真的可走、工作区是否完整、货架与叉车是否关系合理。

- **没有需求满足度检查。** 用户说“3 条传送带、2 个货架、1 个 AGV”，observer 不会检查数量是否满足，也不会报告缺失项。

### 6.3 建议

- 修正越界公式，并明确内部坐标为 bbox center。
- 增加 `world_aabb(instance)` 统一计算函数，所有 validator 和工具都复用。
- 增加 goal validator：
  - 类别数量是否满足。
  - 必要功能区是否存在。
  - 资产间关系是否满足，如 Box on Conveyor、Workbench near Robot。
  - 通道宽度是否满足。
- 观测输出应包括：
  - `requirement_status`
  - `geometry_validation`
  - `support_validation`
  - `semantic_validation`
  - `physics_status`
  - `repair_candidates`

---

## 七、LLM 调用与 Prompt 问题

### 7.1 当前问题

- **本地模型默认启用。** `ModelConfig.llm_name_or_path` 默认是 `mistralai/Mistral-7B-Instruct-v0.2`。只要不走远程 API，就会尝试加载本地大模型；没有轻量 mock、规则 planner 或 dry-run 模式。

- **Prompt 与语言配置不一致。** `ProjectConfig.language` 默认是 `en`，但 ReAct prompt 全是中文，单次 LLM planner prompt 也是中文。中英文资产描述混合时，检索和生成的一致性没有设计。

- **上下文容易被截断。** `_react_call_local()` 使用 `max_length=4096` 截断输入。工具描述、资产库摘要、scene_state、retrieved_assets、lessons 累积后，关键信息可能被截掉。

- **没有 stop sequence 和输出修复。** 模型可能输出解释文字、多个 JSON 块、不完整 JSON。当前只有一次正则解析，没有 retry。

- **远程 API 封装过窄。** 只假定 chat completions 响应格式，缺少对 endpoint 路径、模型名为空、超时、错误信息的可读处理。

### 7.2 建议

- 增加 `--llm-backend local|api|mock|heuristic`。
- API 模式完全绕开本地模型依赖。
- 使用严格的工具调用格式：优先采用 function calling；否则使用 Pydantic schema + retry repair。
- 对工作记忆做摘要，而不是无限塞检索文本。
- 建立中英文 query normalization 和类别别名表，确保中文命令能稳定检索英文资产描述。

---

## 八、最终输出与下游对接问题

### 8.1 当前输出

CLI 的 ReAct 输出结构为：

```json
{
  "mode": "react",
  "layout": [
    {
      "asset_id": "...",
      "usd_path": "...",
      "position": [0, 0, 0],
      "score": 1.0
    }
  ],
  "trace": {
    "total_steps": 0,
    "success": false,
    "lessons": [],
    "steps": []
  }
}
```

### 8.2 当前问题

- **输出不是 `scene.py` 可直接加载的格式。** `scene.py.load_layout_from_json()` 期待 JSON 根节点是 layout list，但 CLI 保存的是带 `mode/layout/trace` 的 envelope。

- **`scene.py` 路径硬编码。** 当前 `scene.py` 固定读取 `/home/simple/joey/scene_synthesis/scripts/scene.json`，没有命令行参数，也没有和 CLI 的 `--output` 打通。

- **LayoutPlan.summary() 丢失关键字段。** 输出只有 `asset_id/usd_path/position/score`，没有 `instance_id`、`rotation`、`scale`、`bbox`、`support_parent`、`reasoning`、`asset_uid`。

- **ReAct trace 过度简化。** CLI trace 只保留 step、action、thought、ok，不保留 `action_input`、tool result、error、observation、final_scene_dict。调试 agent 失败时信息不够。

- **没有最终验证报告。** 输出没有 `final_validation`，下游无法知道这个布局是否满足需求、是否无碰撞、是否可加载。

- **没有 USD 生成/导出闭环。** 系统只输出 JSON，不生成 USD，不调用 Isaac 验证，也没有把仿真反馈写回布局。

### 8.3 建议

- 区分两种输出：
  - `--output-layout`：保存纯 layout list，供 `scene.py` 加载。
  - `--output-trace`：保存完整 agent trace。
  - 或者 envelope 中同时提供 `layout_json` 和 `debug_trace`。
- `SceneState.to_layout_json()` 应成为 ReAct 输出主路径，包含 `rotation/scale/support/bbox/instance_id`。
- `scene.py` 改成 CLI 参数：`python scene.py --layout path/to/layout.json`。
- 增加 `final_report`：
  ```json
  {
    "requirements_satisfied": true,
    "geometry_ok": true,
    "physics_available": false,
    "warnings": []
  }
  ```

---

## 九、为什么说当前还没有真正实现 ReAct 场景合成

真正的 ReAct 场景合成至少应满足：

1. Agent 能基于需求拆解目标。
2. Agent 能按需检索资产。
3. 检索结果成为受控资产池。
4. 工具调用有严格 schema 和执行约束。
5. 每次行动后能观察真实场景状态。
6. 失败能进入反思，并影响下一步策略。
7. 最终 finish 前必须验证需求、几何、物理和输出可加载性。

当前代码只部分满足第 2、4、5 点的雏形：

- 有 `retrieve_assets`，但没有资产池约束。
- 有工具 schema 描述，但没有严格校验。
- 有 observer，但没有把工具错误和需求满足度纳入观察。
- 有 reflection prompt，但失败触发条件过窄，策略调整结果也没有生效。
- 有最终 layout 输出，但不是下游直接可用格式，也没有最终验证。

因此它更像是 “RAG + 工具调用循环原型”，还不是完整的 “ReAct 场景合成 agent”。

---

## 十、推荐修复顺序

### P0：先让系统可运行、可调试

- `__init__.py` 轻量化，`torch/transformers` 延迟导入。
- 修复 CLI `--assets` 扫描逻辑。
- 增加 `--llm-backend api/mock/local`。
- CLI trace 输出保留 `action_input/tool_result/error/observation`。

### P1：修正数据与资产池

- 将三类知识拆成三个检索工具或三个过滤域：`retrieve_scene_prior`、`retrieve_scene_template`、`retrieve_assets`。
- 建立 `AssetRegistry`，用 `asset_uid/doc_id` 管理具体模型。
- 将 CSV 的 `Description` 和 `Tag` 转成资产画像字段，例如 `tags`、`functional_summary`、`visual_summary`、`use_cases`。
- `retrieve_assets` 返回具体资产 ID，`place_instance` 只能引用 registry 中的资产。

### P2：强化工具契约

- 引入 Pydantic 或 JSON Schema 做统一参数校验。
- `place_instance/move_asset` 做预检，失败不修改 scene。
- 合并重复 validator，统一 world AABB、bounds、collision、support 计算。

### P3：补全 ReAct 闭环

- 将工具错误纳入 observation。
- 所有失败类型都能触发反思。
- 修复 strategy 更新不生效问题。
- 增加 action history、goal state、requirement status。
- `finish_scene` 做最终验证，不通过则拒绝 finish。

### P4：打通输出和仿真

- 输出纯 layout JSON + 完整 trace JSON。
- `scene.py` 支持命令行 layout 路径。
- 统一 bbox/scale/pivot 坐标转换。
- Isaac 不可用时不要伪装稳定；可用时把仿真结果写入 final report。

---

## 十一、一个更合理的目标架构草图

```text
cli.py
  -> ProjectConfig / AssetPaths
  -> AssetRegistry.load(csv)
  -> VectorStore(asset_docs) + VectorStore(scene_template_docs) + VectorStore(scene_prior_docs)
  -> ReActAgent
       state:
         - SceneState
         - GoalState
         - selected_asset_pool
         - action_history
         - lessons
       tools:
         - retrieve_scene_prior(query) -> scene type / core devices / semantic goals
         - retrieve_scene_template(query) -> zones / flow / layout reference
         - retrieve_assets(query, category, filters, top_k) -> asset_uid list with tags and summaries
         - inspect_asset(asset_uid)
         - place_instance(asset_uid, position, rotation, support_parent)
         - move_asset(instance_id, new_position)
         - query_scene(...)
         - validate_scene(...)
         - finish_scene()
       loop:
         Think -> schema action -> tool execution -> observation -> reflection/repair
  -> final_validation
  -> layout.json + trace.json + report.json
  -> optional Isaac/USD export
```

这个架构的关键点是：LLM 负责规划和决策，Python 工具负责事实、约束、状态和输出。资产选择、几何合法性、最终验证都不能只靠 prompt 约定，必须落到工具层和状态层。

---

## 十二、作为大模型和 Agent 专家的整体修改思路

### 12.1 先用一个通俗比喻理解当前问题

现在这个项目像一个“会说话的调度员”，它能对大模型说：

> 你可以检索资产、放置资产、移动资产、检查碰撞。

但是它缺少几个关键能力：

1. **仓库管理员不严格。** 大模型说要放一个 Conveyor，系统没有严格确认这个 Conveyor 是否真来自资产库。
2. **工具没有安全开关。** 大模型给错参数，工具可能仍然把错误物体放进场景。
3. **验收员太粗糙。** 放完之后只看有没有简单 AABB 碰撞，不看用户要求是否真的完成。
4. **复盘没有改变行为。** 反思写了，但策略没有真正更新到下一轮。
5. **交付物格式不对。** 输出 JSON 不一定能被 `scene.py` 直接加载，也没有完整的最终验收报告。

所以修改思路不是“让大模型更聪明”这么简单，而是要让系统形成清晰分工：

- **大模型负责想办法。** 它决定下一步要检索、放置、移动还是完成。
- **工具负责守规矩。** 它检查参数、资产来源、位置是否合法。
- **状态负责记账。** 它记录已经放了什么、还缺什么、哪里有问题。
- **观察器负责验收。** 它告诉大模型这一步做得对不对。
- **最终输出负责交付。** 它给出可加载的 layout、完整 trace 和最终报告。

### 12.2 不要一次性大重构

建议按“小步可运行”的方式改。每一步改完都应该能运行一个很小的例子，而不是等所有代码都改完才测试。

推荐顺序是：

1. 先让项目在没有本地大模型时也能启动。
2. 再让资产检索只返回真正可放置的资产。
3. 再让放置工具不能乱放。
4. 再让 ReAct 循环能看到工具错误并反思。
5. 最后打通最终输出和 Isaac/scene.py。

---

## 十三、第一阶段：先让系统稳定可运行

### 13.1 要解决什么

当前系统最大的问题之一是：哪怕只是查看 CLI 帮助，也会因为没有安装 `torch` 而失败。这对调试非常不友好。

目标是：

- 不加载本地大模型，也能运行 `python -m scene_layout_rag.cli --help`。
- 使用远程 API 时，不强制安装本地 `torch/transformers`。
- 没有 LLM 时，可以用 mock 模式测试工具链。

### 13.2 修改文件 1：`scene_layout_rag/__init__.py`

当前问题：

```python
from .rag import SceneLayoutRAG
from .llm_planner import LLMPlanner
```

这两行会触发重依赖导入。

建议修改为：只导入轻量对象。

```python
"""Scene layout RAG package."""

from .config import AssetPaths, ModelConfig, AgentConfig, ProjectConfig
from .data_models import AgentTrace

__all__ = [
    "AssetPaths",
    "ModelConfig",
    "AgentConfig",
    "ProjectConfig",
    "AgentTrace",
]
```

这样做的意思是：打开包的时候不要马上搬出所有重设备，真正需要 RAG 或 LLM 时再导入。

### 13.3 修改文件 2：`scene_layout_rag/llm_planner.py`

当前问题：

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
```

这两行在文件顶部，会导致远程 API 模式也依赖本地模型库。

建议：

1. 删除文件顶部的 `import torch` 和 `from transformers ...`。
2. 在 `_ensure_model()` 里面再导入。

示例：

```python
def _ensure_model(self) -> None:
    if self._model is not None and self._tokenizer is not None:
        return

    try:
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
    except ImportError as exc:
        raise ImportError(
            "本地 LLM 模式需要安装 torch 和 transformers；"
            "如果你使用远程 API，请设置 --llm-backend api 或 --api-url。"
        ) from exc

    ...
```

这样做以后，只有真的要加载本地模型时才会检查 `torch`。

### 13.4 修改文件 3：`scene_layout_rag/config.py`

建议给模型配置增加一个后端选择。

```python
@dataclass
class ModelConfig:
    llm_backend: str = "api"  # 可选: api, local, mock
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    ...
```

如果你现在主要用远程大模型，建议默认先用 `"api"` 或 `"mock"`，不要默认加载 Mistral 本地模型。

### 13.5 修改文件 4：`scene_layout_rag/cli.py`

增加参数：

```python
parser.add_argument(
    "--llm-backend",
    choices=["api", "local", "mock"],
    default="api",
    help="选择 LLM 后端：api=远程接口，local=本地模型，mock=假模型测试工具链",
)
```

然后在 `main()` 里写：

```python
config.model.llm_backend = args.llm_backend
```

同时修复 `--assets`：

```python
from .config import AssetPaths

if args.assets:
    config.asset_paths = AssetPaths(assets_root=args.assets)
```

不要再手写：

```python
config.asset_paths.inventory_csvs = sorted(Path(args.assets).glob("*.csv"))
```

因为这会漏掉 `csv/`、`md/`、`docs/` 子目录。

### 13.6 新增文件：`scene_layout_rag/mock_llm.py`

为了不用真实大模型也能测试 ReAct 流程，建议加一个假 LLM。

它的作用是：按固定顺序输出工具调用，例如先检索 Conveyor，再放置 Conveyor，再 finish。

示例：

```python
class MockLLMPlanner:
    def __init__(self):
        self.step = 0

    def react_call(self, system_prompt: str, user_prompt: str) -> str:
        self.step += 1
        if self.step == 1:
            return """
            {
              "thought": "先检索传送带资产",
              "action": "retrieve_assets",
              "action_input": {"query": "conveyor", "category": "Conveyor", "top_k": 3}
            }
            """
        if self.step == 2:
            return """
            {
              "thought": "放置一个传送带",
              "action": "place_instance",
              "action_input": {"asset_uid": "PLACEHOLDER", "position": [0, 0, 0.5]}
            }
            """
        return """
        {
          "thought": "完成",
          "action": "finish_scene",
          "action_input": {}
        }
        """
```

注意：这里的 `asset_uid` 后面会由资产池机制改掉。第一阶段可以先用 mock 测试循环能不能走通。

### 13.7 第一阶段完成标准

改完后至少应该能做到：

```bash
python -m scene_layout_rag.cli --help
```

不再因为 `torch` 报错。

并且：

```bash
python -m scene_layout_rag.cli "创建一个包含传送带的测试场景" --react --llm-backend mock
```

可以进入 ReAct 流程，哪怕生成的布局还很粗糙。

---

## 十四、第二阶段：建立可信资产池和资产画像

### 14.1 要解决什么

当前大模型可以凭空写：

```json
{
  "asset_id": "Conveyor",
  "usd_path": "/some/random/path.usdz"
}
```

工具也可能接受。这样场景就不是从真实资产库生成的。

目标是：

- 所有可放置物体必须来自 CSV 资产库。
- 每个资产都有唯一 ID。
- 大模型只引用这个唯一 ID，不再手写 `usd_path`。
- CSV 中的 `Description` 和 `Tag` 要进入资产画像，帮助系统判断“这个资产适不适合当前场景”，而不是只用于模糊检索。

### 14.2 新增概念：`AssetRegistry`

可以把它理解成“资产登记表”。

每一条资产记录应该包含：

```python
asset_uid       # 唯一编号，例如 Conveyor-0-a1b2c3
category        # 类别，例如 Conveyor
usd_path        # 真实模型路径
bbox_size       # 包围盒尺寸
bbox_center     # 包围盒中心
description     # 文字描述
tags            # 从 CSV Tag 解析出的结构化标签，例如 Shape、Directionality、DNA
functional_summary  # 从 Description 提取的功能摘要
visual_summary      # 从 Description 提取的视觉摘要
use_cases           # 从 Description 推断的适用场景
selection_hints     # 资产选择提示，例如适合分拣转向、适合托盘搬运
source_doc_id   # 来自哪条文档
```

### 14.3 新增文件：`scene_layout_rag/asset_registry.py`

建议新增：

```python
from dataclasses import dataclass
from typing import Dict, List, Optional

from .data_models import AssetDocument


@dataclass
class AssetRecord:
    asset_uid: str
    category: str
    usd_path: str
    bbox_size: tuple[float, float, float]
    bbox_center: tuple[float, float, float]
    description: str
    tags: dict
    functional_summary: str
    visual_summary: str
    use_cases: list[str]
    source_doc_id: str


class AssetRegistry:
    def __init__(self, documents: list[AssetDocument]):
        self.records: Dict[str, AssetRecord] = {}
        self.doc_to_uid: Dict[str, str] = {}
        self._build(documents)

    def _build(self, documents: list[AssetDocument]) -> None:
        for doc in documents:
            if doc.metadata.get("doc_type") != "asset":
                continue
            usd_path = doc.metadata.get("usd_path", "")
            bbox = doc.metadata.get("bbox") or {}
            bbox_size = bbox.get("size") or [1.0, 1.0, 1.0]
            bbox_center = bbox.get("center") or [0.0, 0.0, 0.0]
            category = doc.metadata.get("asset_category", "Asset")
            asset_uid = doc.doc_id
            tags = doc.metadata.get("tags", {})
            description = doc.metadata.get("description", "")

            record = AssetRecord(
                asset_uid=asset_uid,
                category=category,
                usd_path=usd_path,
                bbox_size=tuple(float(v) for v in bbox_size),
                bbox_center=tuple(float(v) for v in bbox_center),
                description=description,
                tags=tags,
                functional_summary=_extract_functional_summary(description),
                visual_summary=_extract_visual_summary(description),
                use_cases=_infer_use_cases(description),
                source_doc_id=doc.doc_id,
            )
            self.records[asset_uid] = record
            self.doc_to_uid[doc.doc_id] = asset_uid

    def get(self, asset_uid: str) -> Optional[AssetRecord]:
        return self.records.get(asset_uid)

    def exists(self, asset_uid: str) -> bool:
        return asset_uid in self.records

    def list_by_category(self, category: str) -> List[AssetRecord]:
        return [r for r in self.records.values() if r.category == category]
```

上面示例里出现的 `_extract_functional_summary()`、`_extract_visual_summary()`、`_infer_use_cases()` 可以先做得非常简单：

- 第一版：用字符串查找 `Functional Features:` 和 `Visual Features:`，把两段拆开。
- 第二版：根据关键词推断 `use_cases`，例如 description 中出现 sorting 就标记为 `sorting`。
- 第三版：再考虑让 LLM 或规则系统生成更精细的 `capabilities` 和 `placement_hints`。

不要一开始就追求完美解析。先把信息从“长文本”变成“字段”，就已经能明显提高后续检索和选择质量。

### 14.4 修改文件：`scene_layout_rag/rag.py`

在 `SceneLayoutRAG.__init__()` 中创建资产登记表：

```python
from .asset_registry import AssetRegistry

self.asset_registry = AssetRegistry(self._documents)
```

然后在创建 `ReActAgent` 时传进去：

```python
agent = ReActAgent(
    ...
    asset_registry=self.asset_registry,
)
```

### 14.5 修改文件：`scene_layout_rag/agent/react_agent.py`

`ReActAgent.__init__()` 增加参数：

```python
asset_registry: Any = None
```

保存：

```python
self.asset_registry = asset_registry
```

执行工具时传入：

```python
result = self.tools.execute(
    action,
    action_input,
    scene=scene,
    vector_store=self.vector_store,
    embedder=self.embedder,
    llm=self.llm,
    asset_registry=self.asset_registry,
)
```

### 14.6 修改文件：`scene_layout_rag/tools/retrieve_assets.py`

当前检索会混入场景模板。必须过滤。

建议改成：

```python
for hit in hits:
    doc = hit.document
    if doc.metadata.get("doc_type") != "asset":
        continue
```

返回结果改为：

```python
assets.append({
    "asset_uid": doc.doc_id,
    "category": cat,
    "usd_path": doc.metadata.get("usd_path", ""),
    "bbox": doc.metadata.get("bbox", {}),
    "tags": doc.metadata.get("tags", {}),
    "functional_summary": functional_summary,
    "visual_summary": visual_summary,
    "use_cases": use_cases,
    "description": doc.content[:200],
    "score": round(hit.score, 3),
})
```

重点是返回 `asset_uid`，同时返回 `tags` 和摘要字段。后面放置资产只能用 `asset_uid`，而资产选择要利用 `tags`、功能摘要、尺寸和场景需求一起判断。

### 14.7 新增工具：`retrieve_scene_prior` 和 `retrieve_scene_template`

只修 `retrieve_assets` 还不够，因为它只能解决“选哪个真实模型”。真正的场景合成还需要先理解场景和布局。

建议新增两个工具：

```text
retrieve_scene_prior
  输入：用户需求或当前目标
  查询：docs/jsonl 里的 scene_prior
  输出：场景类型、核心设备、可能需要的资产类别、关键关系

retrieve_scene_template
  输入：场景类型或布局问题
  查询：md 里的 scene_template
  输出：功能区、动线、设备组合、可参考的布局片段
```

这两个工具不要返回 `usd_path`，也不要参与 `place_instance`。它们是给大模型“想清楚怎么规划”用的。

推荐第一版实现方式：

- 如果暂时不想拆三个独立向量库，就在工具内部按 `doc_type` 过滤。
- `retrieve_scene_prior` 只保留 `doc_type == "scene_prior"`。
- `retrieve_scene_template` 只保留 `doc_type == "scene_template"`。
- `retrieve_assets` 只保留 `doc_type == "asset"`。

等第一版跑通后，再考虑把三类文档拆成三个索引，减少检索污染。

### 14.8 第二阶段完成标准

当 LLM 调用：

```json
{
  "action": "retrieve_assets",
  "action_input": {"query": "conveyor", "category": "Conveyor", "top_k": 3}
}
```

返回结果里必须是：

```json
{
  "asset_uid": "Conveyor_with_bbox_meters-0-xxxx",
  "category": "Conveyor",
  "usd_path": "...",
  "bbox": {...},
  "tags": {"Shape": "circular", "Directionality": "one-way"},
  "functional_summary": "用于物料转向、分流和输送"
}
```

而不是 Markdown 模板，也不是空路径。

当 LLM 需要理解“分拣中心怎么布局”时，应该调用 `retrieve_scene_template`；当它需要知道“分拣中心通常需要哪些核心设备”时，应该调用 `retrieve_scene_prior`；只有当它要选择具体 Conveyor、Rack、AGV 模型时，才调用 `retrieve_assets`。

---

## 十五、第三阶段：让放置工具不能乱放

### 15.1 要解决什么

现在 `place_instance` 让大模型直接传 `usd_path` 和 `bbox`。这很危险，因为大模型可能复制错、漏填、编造。

目标是：

- 大模型只说“我要放 asset_uid 这个资产”。
- 工具自己去资产登记表里查路径和 bbox。
- 如果资产不存在、位置不合法、会碰撞，工具应该拒绝执行。

### 15.2 修改文件：`scene_layout_rag/tools/place_instance.py`

参数建议改成：

```python
parameters_schema = {
    "asset_uid": {
        "type": "str",
        "required": True,
        "description": "从 retrieve_assets 返回的具体资产唯一 ID",
    },
    "position": {
        "type": "list[float]",
        "required": True,
        "description": "物体包围盒中心点 [x, y, z]，单位米",
    },
    "rotation": {
        "type": "list[float]",
        "required": False,
        "description": "欧拉角 [rx, ry, rz]，单位度",
    },
    "description": {
        "type": "str",
        "required": False,
        "description": "该实例在场景中的用途",
    },
}
```

执行逻辑改成：

```python
asset_uid = params.get("asset_uid", "")
registry = ctx.get("asset_registry")

if registry is None:
    return ToolResult(ok=False, error="asset_registry 未提供")

record = registry.get(asset_uid)
if record is None:
    return ToolResult(ok=False, error=f"资产不存在或未检索: {asset_uid}")

usd_path = record.usd_path
bbox = record.bbox_size
asset_id = record.category
```

### 15.3 加入位置校验

建议新增一个小函数：

```python
def _parse_vec3(value, name: str) -> tuple[float, float, float]:
    if not isinstance(value, (list, tuple)) or len(value) != 3:
        raise ValueError(f"{name} 必须是长度为 3 的数组")
    return tuple(float(v) for v in value)
```

在工具里使用：

```python
try:
    position = _parse_vec3(params.get("position"), "position")
except ValueError as exc:
    return ToolResult(ok=False, error=str(exc))
```

### 15.4 加入放置前预检

放置前先临时构造一个 `AssetInstance`，检查是否越界、是否碰撞。只有通过才真正加入 `scene`。

示意：

```python
from ..scene_state import AssetInstance
from ..validators import would_collide, is_within_bounds

instance_id = scene.generate_instance_id(asset_id)
candidate = AssetInstance(
    instance_id=instance_id,
    asset_id=asset_id,
    usd_path=usd_path,
    position=position,
    rotation=rotation,
    bbox=bbox,
    description=description,
    asset_uid=asset_uid,
)

if not is_within_bounds(candidate, scene.bounds):
    return ToolResult(ok=False, error="放置位置超出场景边界")

collisions = would_collide(candidate, scene)
if collisions:
    return ToolResult(ok=False, error=f"放置后会碰撞: {collisions}")

scene.add_asset(candidate)
```

这里需要同步修改 `AssetInstance`，给它增加 `asset_uid` 字段。

### 15.5 修改文件：`scene_layout_rag/scene_state.py`

`AssetInstance` 增加：

```python
asset_uid: str = ""
scale: Tuple[float, float, float] = (1.0, 1.0, 1.0)
```

`to_dict()` 里也输出：

```python
"asset_uid": a.asset_uid,
"rotation": list(a.rotation),
"scale": list(a.scale),
```

### 15.6 第三阶段完成标准

如果大模型没有先检索，直接写：

```json
{
  "action": "place_instance",
  "action_input": {"asset_uid": "fake_asset", "position": [0, 0, 0]}
}
```

系统应该返回：

```json
{
  "ok": false,
  "error": "资产不存在或未检索"
}
```

而不是把假资产放进场景。

---

## 十六、第四阶段：修正几何验证和场景状态

### 16.1 要解决什么

当前几何验证有几个实际问题：

- 越界公式不对。
- 默认 z=0 会让物体半截在地面下。
- 多处重复实现 AABB。
- 不区分中心点、落地点、USD pivot。

### 16.2 修改文件：`scene_layout_rag/validators.py`

先统一定义一个函数：根据物体中心点和 bbox 算世界包围盒。

```python
def world_aabb(position: tuple, bbox: tuple) -> dict:
    return {
        "min": tuple(position[i] - bbox[i] / 2.0 for i in range(3)),
        "max": tuple(position[i] + bbox[i] / 2.0 for i in range(3)),
    }
```

修正越界判断：

当前逻辑类似：

```python
if abs(a.position[i]) > half[i] + a.bbox[i] / 2.0:
```

建议改成：

```python
if abs(a.position[i]) + a.bbox[i] / 2.0 > half[i]:
```

通俗解释：

- 场景半宽是 10 米。
- 物体中心在 x=9.8。
- 物体半宽是 1 米。
- 那么它最右边到 10.8，已经出界。
- 所以要判断 `中心距离 + 半个物体尺寸` 是否超过场景半宽。

### 16.3 增加工具辅助函数

建议在 `validators.py` 增加：

```python
def is_within_bounds_instance(instance, bounds) -> bool:
    half = [bounds[i] / 2.0 for i in range(3)]
    for i in range(3):
        if abs(instance.position[i]) + instance.bbox[i] / 2.0 > half[i]:
            return False
    return True


def find_collisions_for_instance(instance, scene) -> list:
    collisions = []
    for other in scene.assets.values():
        if other.instance_id == instance.instance_id:
            continue
        vol = aabb_overlap_volume(
            instance.position,
            instance.bbox,
            other.position,
            other.bbox,
        )
        if vol > 1e-6:
            collisions.append({
                "a": instance.instance_id,
                "b": other.instance_id,
                "overlap_volume": round(vol, 4),
            })
    return collisions
```

`place_instance` 和 `move_asset` 都应该用这些函数。

### 16.4 明确 Z 坐标规则

建议内部统一规定：

> `position` 永远表示包围盒中心点，不是底部落地点。

那么如果要把一个高度为 1 米的物体放在地面上，它的 z 应该是：

```python
z = bbox_height / 2
```

可以新增工具：

```python
def ground_position(x: float, y: float, bbox: tuple) -> tuple:
    return (x, y, bbox[2] / 2.0)
```

也可以在 prompt 里明确告诉 LLM：

> 如果物体放在地面，z 必须等于 bbox 高度的一半。

但是更可靠的做法是工具层支持：

```json
{
  "asset_uid": "...",
  "placement": {"type": "ground", "x": 0, "y": 0}
}
```

然后工具自动算 z。这样大模型不容易算错。

---

## 十七、第五阶段：让 ReAct 真的形成闭环

### 17.1 要解决什么

当前 ReAct 循环的问题是：工具失败、JSON 解析失败、无效 action 这些错误没有被很好地反馈给下一轮。

目标是：

- 每一步都有完整 observation。
- 工具失败也算失败，能触发反思。
- 反思结果会真的影响下一步。
- finish 之前必须最终验收。

### 17.2 修改文件：`scene_layout_rag/agent/react_agent.py`

#### 17.2.1 统一 observation 格式

建议每一步 observation 都长这样：

```python
last_observation = {
    "tool_result": {
        "tool": action,
        "ok": result.ok,
        "result": result.result,
        "error": result.error,
    },
    "validation": validation,
    "suggestions": suggestions,
}
```

这样大模型下一轮能看见：

- 刚才调用了什么工具。
- 工具成功还是失败。
- 失败原因是什么。
- 当前场景还有什么问题。

#### 17.2.2 工具失败必须进入 observation

当前代码工具失败后仍可能得到 `observation_ok=True`。建议改成：

```python
result = self.tools.execute(...)

if not result.ok:
    observation = {
        "tool_result": result.to_dict(),
        "validation": {"ok": False, "collisions": [], "out_of_bounds": []},
        "suggestions": [result.error],
    }
    obs_ok = False
else:
    ...
```

#### 17.2.3 无效工具也算失败

当前无效工具记录 `observation_ok=True`。建议改成：

```python
self.history.append(ActionRecord(
    step=step,
    thought=thought,
    action=action,
    action_input=action_input,
    result_ok=False,
    observation_ok=False,
))
```

然后如果开启反思，就调用 `_do_reflection()`。

#### 17.2.4 修复 strategy 不生效

当前 `_do_reflection()` 内部打印了策略调整，但没有返回。

建议让它返回：

```python
return lesson, strategy_text
```

主循环中：

```python
lesson, new_strategy = self._do_reflection(...)
if new_strategy:
    strategy = new_strategy
```

这样下一轮 `format_step_prompt(..., strategy=strategy)` 才能真的带上新策略。

#### 17.2.5 增加最近历史

当前 prompt 缺少完整历史。建议在 `format_step_prompt()` 里增加：

```python
recent_history=[
    {
        "step": h.step,
        "action": h.action,
        "ok": h.observation_ok,
        "input": h.action_input,
    }
    for h in self.history[-5:]
]
```

这样大模型知道自己刚才已经试过什么，避免重复犯错。

### 17.3 新增工具：`finish_scene`

不要让 `finish` 只是一个字符串。建议做成工具。

新文件：

`scene_layout_rag/tools/finish_scene.py`

功能：

1. 检查是否满足用户需求。
2. 检查是否无碰撞、无越界。
3. 检查关键支撑关系。
4. 返回最终报告。

最小版本可以先做几何检查：

```python
class FinishSceneTool(BaseTool):
    name = "finish_scene"
    description = "结束场景生成，并执行最终验证"

    @property
    def modifies_scene(self) -> bool:
        return False

    parameters_schema = {}

    def execute(self, params, **ctx):
        scene = ctx.get("scene")
        if scene is None:
            return ToolResult(ok=False, error="scene 未提供")

        from ..validators import find_all_collisions, check_out_of_bounds

        collisions = find_all_collisions(scene)
        out_of_bounds = check_out_of_bounds(scene)

        ok = len(collisions) == 0 and len(out_of_bounds) == 0 and len(scene.assets) > 0
        if not ok:
            return ToolResult(ok=False, error="最终验证未通过", result={
                "collisions": collisions,
                "out_of_bounds": out_of_bounds,
                "asset_count": len(scene.assets),
            })

        return ToolResult(ok=True, result={
            "message": "最终验证通过",
            "asset_count": len(scene.assets),
        })
```

然后在 `tools/__init__.py` 注册它。

`ReActAgent.run()` 里把原来的：

```python
if action == "finish":
```

改为：

```python
if action == "finish_scene" and result.ok:
    finished = True
    break
```

### 17.4 第五阶段完成标准

一个真正的 ReAct 闭环至少要满足：

1. 大模型放错位置，工具拒绝。
2. 拒绝原因进入下一轮 observation。
3. 大模型下一轮根据错误移动或重新放置。
4. 大模型调用 `finish_scene`。
5. `finish_scene` 验证通过后，trace.success 才是 true。

---

## 十八、第六阶段：让输出可以真正交付

### 18.1 要解决什么

当前 CLI 输出是：

```json
{
  "mode": "react",
  "layout": [...],
  "trace": {...}
}
```

但 `scene.py` 期待的是：

```json
[
  {
    "asset_id": "...",
    "usd_path": "...",
    "position": [...],
    "rotation": [...],
    "scale": [...]
  }
]
```

所以当前保存的 JSON 不能直接给 `scene.py` 用。

### 18.2 修改文件：`scene_layout_rag/cli.py`

建议增加三个输出参数：

```python
parser.add_argument("--output-layout", type=Path, default=None)
parser.add_argument("--output-trace", type=Path, default=None)
parser.add_argument("--output-report", type=Path, default=None)
```

ReAct 模式下：

```python
plan, trace = pipeline.generate_layout_react(args.command)

layout_json = trace.final_scene_dict.get("layout_json")
trace_json = trace_to_dict(trace)
report_json = trace.final_scene_dict.get("final_report", {})

if args.output_layout:
    args.output_layout.write_text(
        json.dumps(layout_json, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
```

如果暂时没有把 layout 放进 `final_scene_dict`，可以直接从 `scene.to_layout_json()` 生成。

### 18.3 修改文件：`scene_layout_rag/scene_state.py`

`to_layout_json()` 应输出更多字段：

```python
def to_layout_json(self) -> list:
    return [
        {
            "instance_id": a.instance_id,
            "asset_uid": a.asset_uid,
            "asset_id": a.asset_id,
            "usd_path": a.usd_path,
            "position": list(a.position),
            "rotation": list(a.rotation),
            "scale": list(a.scale),
            "bbox": list(a.bbox),
            "support_parent": a.support_parent,
        }
        for a in self.assets.values()
    ]
```

### 18.4 修改文件：`scene.py`

当前 `scene.py` 硬编码：

```python
load_layout_from_json("/home/simple/joey/scene_synthesis/scripts/scene.json")
```

建议改成命令行参数：

```python
import argparse

def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--layout", required=True, help="布局 JSON 文件路径")
    return parser

if __name__ == "__main__":
    args = build_parser().parse_args()
    load_layout_from_json(args.layout)
```

这样以后可以运行：

```bash
python scene.py --layout outputs/layout.json
```

### 18.5 第六阶段完成标准

一次完整流程应该是：

```bash
python -m scene_layout_rag.cli \
  "规划一个包含传送带、工作台和AGV的简单场景" \
  --react \
  --llm-backend api \
  --output-layout outputs/layout.json \
  --output-trace outputs/trace.json \
  --output-report outputs/report.json
```

然后：

```bash
python scene.py --layout outputs/layout.json
```

能加载刚生成的场景。

---

## 十九、第七阶段：让需求验收不只看碰撞

### 19.1 要解决什么

用户说：

> 放 3 条传送带、2 个货架、1 个 AGV。

当前系统不会严格检查是否真的有这些数量。

目标是：让系统知道“用户要求是什么”和“当前完成了多少”。

### 19.2 新增文件：`scene_layout_rag/goal_state.py`

先做简单版本，不需要复杂 NLP。可以用关键词和数字规则解析。

```python
from dataclasses import dataclass, field


@dataclass
class GoalState:
    required_counts: dict[str, int] = field(default_factory=dict)

    @classmethod
    def from_command(cls, command: str) -> "GoalState":
        # 第一版可以写得简单一些，后续再让 LLM 输出结构化需求
        goals = cls()
        if "传送带" in command or "conveyor" in command.lower():
            goals.required_counts["Conveyor"] = 1
        if "货架" in command or "rack" in command.lower():
            goals.required_counts["Rack"] = 1
        if "AGV" in command.upper():
            goals.required_counts["AGV"] = 1
        return goals

    def evaluate(self, scene) -> dict:
        actual = {}
        for asset in scene.assets.values():
            actual[asset.asset_id] = actual.get(asset.asset_id, 0) + 1

        missing = {}
        for category, count in self.required_counts.items():
            if actual.get(category, 0) < count:
                missing[category] = count - actual.get(category, 0)

        return {
            "ok": len(missing) == 0,
            "required_counts": self.required_counts,
            "actual_counts": actual,
            "missing": missing,
        }
```

后续高级版本可以让 LLM 先把用户需求解析成：

```json
{
  "required_counts": {"Conveyor": 3, "Rack": 2, "AGV": 1},
  "relations": [
    {"type": "near", "a": "AGV", "b": "Conveyor"},
    {"type": "on", "child": "Box", "parent": "Conveyor"}
  ]
}
```

### 19.3 修改 observer

`SceneObserver.observe()` 增加 goal_state：

```python
def observe(self, scene: SceneState, goal_state=None):
    validation = self._validate(scene)
    requirement_status = goal_state.evaluate(scene) if goal_state else {}
    return {
        "validation": validation,
        "requirement_status": requirement_status,
        ...
    }
```

### 19.4 修改 finish_scene

`finish_scene` 最终必须检查：

```python
goal_status = goal_state.evaluate(scene)
if not goal_status["ok"]:
    return ToolResult(ok=False, error="用户需求未满足", result=goal_status)
```

### 19.5 第七阶段完成标准

如果用户要求 2 个货架，但场景里只有 1 个，`finish_scene` 必须拒绝完成，并告诉大模型：

```json
{
  "missing": {"Rack": 1}
}
```

下一轮大模型就应该继续检索并放置 Rack。

---

## 二十、最后建议的开发任务清单

下面这份清单可以直接当成后续开发计划。

### 20.1 第一批任务：让项目能跑

- 修改 `scene_layout_rag/__init__.py`，移除重依赖导入。
- 修改 `llm_planner.py`，把 `torch/transformers` 延迟导入。
- 修改 `config.py`，增加 `llm_backend`。
- 修改 `cli.py`，增加 `--llm-backend`，修复 `--assets`。
- 新增 `mock_llm.py`。

验收标准：

- `python -m scene_layout_rag.cli --help` 能运行。
- mock 模式能输出一个 trace。

### 20.2 第二批任务：让资产可信

- 新增 `asset_registry.py`。
- `SceneLayoutRAG` 初始化 `AssetRegistry`。
- 将 CSV 的 `Tag` 解析结果、`Description` 功能/视觉信息写入 `AssetRecord`。
- 新增或预留三类检索工具：`retrieve_scene_prior`、`retrieve_scene_template`、`retrieve_assets`。
- `retrieve_assets` 只返回 `doc_type=asset`。
- `retrieve_assets` 返回 `asset_uid`、`tags`、`functional_summary`、`visual_summary`、`use_cases`。
- `place_instance` 改用 `asset_uid`。

验收标准：

- 非资产 Markdown 不再出现在 `retrieve_assets` 结果中。
- 场景先验和场景模板可以通过单独工具检索，不会被误当成可放置资产。
- `retrieve_assets` 的结果能看见 CSV 里的标签和功能描述摘要。
- 假资产 ID 不能被放入场景。

### 20.3 第三批任务：让工具安全

- 修改 `AssetInstance`，增加 `asset_uid`、`scale`。
- 修改 `validators.py`，统一 AABB 和越界判断。
- `place_instance` 放置前检查资产、坐标、边界、碰撞。
- `move_asset` 移动前检查边界和碰撞，失败不修改场景。
- 合并重复的碰撞和支撑计算。

验收标准：

- 越界物体不能被放置。
- 明显碰撞的物体不能被放置，或至少会返回失败 observation。

### 20.4 第四批任务：让 ReAct 闭环有效

- `ReActAgent` 每一步 observation 包含 `tool_result`。
- 工具失败、无效 action、JSON 解析失败都算失败。
- 反思结果能更新 `strategy`。
- Prompt 加入最近 5 步历史。
- 更新 `SYSTEM_PROMPT`：明确告诉大模型先用 `retrieve_scene_prior` 理解需求，再用 `retrieve_scene_template` 参考布局，最后用 `retrieve_assets` 选择真实资产，并且选择资产时要看 `tags`、功能摘要、bbox。
- 新增并注册 `finish_scene` 工具。

验收标准：

- 工具失败后，大模型下一轮能看到失败原因。
- 只有 `finish_scene` 验证通过，trace.success 才为 true。

### 20.5 第五批任务：让输出能交付

- `SceneState.to_layout_json()` 输出完整 layout。
- CLI 增加 `--output-layout`、`--output-trace`、`--output-report`。
- `scene.py` 支持 `--layout` 参数。
- 输出 final report。

验收标准：

- CLI 生成的 `layout.json` 能直接被 `scene.py` 加载。
- `trace.json` 能看到每一步 action、参数、结果、观察和反思。

### 20.6 第六批任务：让系统懂用户需求

- 新增 `goal_state.py`。
- 第一版用规则解析需求数量。
- observer 输出 `requirement_status`。
- `finish_scene` 检查需求是否满足。

验收标准：

- 用户要求的资产数量不够时，系统不能 finish。
- observation 能明确告诉大模型还缺什么。

---

## 二十一、最小可用版本应该长什么样

如果只做最小可用版本，不追求一次到位，我建议做到下面这个程度：

1. 能启动 CLI。
2. 能用 API 或 mock LLM 跑 ReAct。
3. `retrieve_assets` 只返回真实资产，并返回 `asset_uid`、`tags`、功能摘要。
4. 至少能按 `doc_type` 区分 `scene_prior`、`scene_template`、`asset`，避免三类知识互相污染。
5. `place_instance` 只能放 `asset_uid`。
6. 工具失败会进入 observation。
7. `finish_scene` 验证无碰撞、无越界、场景非空。
8. 输出 `layout.json` 可以被 `scene.py` 加载。

做到这 8 点以后，这个项目就从“概念原型”变成“可调试的 ReAct 场景合成系统”。后面再慢慢加入更复杂的需求解析、支撑关系、Isaac 物理仿真、自动修复策略，才会比较稳。

---

## 二十二、给没有代码基础的执行建议

如果你自己不写代码，而是安排别人或让 AI 编程助手去改，可以按下面方式发任务：

### 任务 1：修复启动和 LLM 后端

请修改 `scene_layout_rag/__init__.py`、`llm_planner.py`、`config.py`、`cli.py`，目标是：

- `python -m scene_layout_rag.cli --help` 不依赖 torch。
- 支持 `--llm-backend api|local|mock`。
- API 模式不加载本地模型。
- `--assets` 使用 `AssetPaths(assets_root=...)` 重新扫描。

完成后给出运行截图或命令输出。

### 任务 2：新增资产登记表

请新增 `scene_layout_rag/asset_registry.py`，从 `AssetDocument` 中提取所有 `doc_type=asset` 的记录，建立 `asset_uid -> AssetRecord` 映射。`AssetRecord` 除了保存 `usd_path` 和 `bbox`，还必须保存 CSV 里的 `tags`、功能摘要、视觉摘要和适用场景。然后修改 `SceneLayoutRAG` 和 `ReActAgent`，把 `asset_registry` 传给所有工具。

完成后证明 `retrieve_assets` 返回的每条结果都有 `asset_uid`、`usd_path`、`bbox`、`tags`、`functional_summary`。

### 任务 3：改造检索和放置工具

请修改 `retrieve_assets.py` 和 `place_instance.py`，并新增或预留 `retrieve_scene_prior.py`、`retrieve_scene_template.py`：

- `retrieve_assets` 只返回真实资产，不返回 Markdown 场景模板。
- `retrieve_assets` 返回 CSV 中的 `tags` 和 `Description` 摘要，用于资产选择。
- `retrieve_scene_prior` 只检索 JSONL 场景先验，用于理解场景类型和核心设备。
- `retrieve_scene_template` 只检索 Markdown 场景模板，用于参考功能区和动线。
- `place_instance` 输入从 `asset_id/usd_path/bbox` 改为 `asset_uid/position/rotation`。
- `place_instance` 根据 `asset_registry` 自动补齐路径和 bbox。
- 假 `asset_uid` 必须返回失败，不能修改 SceneState。

完成后写一个小测试：假资产不能放，真实资产能放；Markdown 模板不会出现在 `retrieve_assets` 结果里；CSV 的 `Tag` 能出现在检索返回结果里。

### 任务 4：修复验证器

请修改 `validators.py`：

- 修复越界公式。
- 新增 `world_aabb`。
- 新增单实例碰撞检查函数。
- 让 `place_instance` 和 `move_asset` 使用这些函数做预检。

完成后写一个例子：把大物体放在边界外，工具必须拒绝。

### 任务 5：修复 ReAct 闭环

请修改 `agent/react_agent.py`：

- 工具执行结果必须进入 observation。
- 工具失败、无效工具、JSON 解析失败都要被记录为失败。
- 失败可以触发 reflection。
- strategy 调整结果要保存，并进入下一轮 prompt。
- 最近 5 步历史要进入 prompt。

同时修改 `prompts/templates.py`：

- 系统提示中写清楚三类检索工具的职责。
- 要求 Agent 不要把 `scene_prior` 或 `scene_template` 当成可放置资产。
- 要求 Agent 调用 `retrieve_assets` 后，结合 `tags`、功能摘要、bbox 选择资产，而不是只看类别名。

完成后提供一段 trace，证明失败原因会出现在下一轮上下文中。

### 任务 6：新增完成工具和输出

请新增 `finish_scene` 工具并注册。只有最终验证通过，trace.success 才能为 true。请修改 CLI，支持输出：

- `layout.json`
- `trace.json`
- `report.json`

请修改 `scene.py`，支持：

```bash
python scene.py --layout outputs/layout.json
```

完成后证明 CLI 输出的 layout 可以被 `scene.py` 读取。

---

## 二十三、我会优先改哪几个点

如果我是这个项目的主要修改者，我会按这个优先级做：

1. **先改轻量启动。** 因为现在连 help 都会因为 torch 失败，调试成本太高。
2. **再改资产池。** 因为场景合成的基础是真实资产，不能让大模型编造路径。
3. **再改 `place_instance`。** 因为所有布局最终都靠这个工具落地，它必须安全。
4. **再改 ReAct observation。** 因为 agent 能不能自修复，关键看它能不能看到错误。
5. **最后改输出。** 因为用户真正需要的是可以加载的场景，而不是一段看起来合理的 JSON。

这条路线的核心原则是：

> 让大模型做选择，让代码做校验；让大模型做规划，让工具守住事实边界。

只有这样，ReAct 场景合成才会从“看起来像 agent”变成“真的能迭代生成场景的 agent”。
