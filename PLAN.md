# PLAN.md

## 当前完成情况

项目主架构已经基本成型：

- 已实现 `ProjectConfig` / `ModelConfig` / `AgentConfig` 配置层。
- 已实现资产摄取链路：CSV、Markdown、JSONL 统一转成 `AssetDocument`。
- 已实现 RAG 索引链路：`corpus.jsonl` 作为事实源，FAISS 作为加速层，关键词检索作为兜底。
- 已实现 ReAct 主循环：think -> act -> observe -> reflect -> adjust strategy。
- 已实现工具注册系统和 10 个具体工具。
- 已实现运行时场景状态：实例 CRUD、支撑关系维护、JSON 序列化。
- 已实现观测器：工具结果、AABB 碰撞、支撑状态、场景语义、静态稳定性反馈。
- 已实现本地 transformers 后端和 `openai_sdk` 后端的 planner 封装。
- 已有端到端入口：
  - `python -m scene_layout_rag.cli ingest`
  - `python -m scene_layout_rag.cli retrieve ...`
  - `python -m scene_layout_rag.cli run ...`
  - `python scripts/run_inference.py --command "..."`
- 已有离线数据处理脚本：
  - USD/USDA 转 Markdown
  - USD bbox 计算
  - USD 预处理、flatten、center、xformop 检查等

## 当前数据与索引状态

当前索引统计：

- `data/indexes/corpus.jsonl`: 10,775 条文档。
- `asset`: 119 条。
- `scene_template`: 10,656 条。
- 当前未看到 `scene_prior` 文档进入 corpus。

资产类型分布：

```text
AGV              6
Box             21
Conveyor        17
Forklift         5
IndustrialRobot 14
Pallet           6
Part            10
Rack             4
Scene            7
Workbench       29
```

场景模板分布：

```text
assembly     1685
palletizing  1510
sorting      1792
transport    1919
warehouse    3750
```

## 实验管理现状

当前实验管理采用三层目录：

```text
data/assets/   # 原始输入资产与场景模板
data/indexes/  # corpus.jsonl / vectors.faiss / index_meta.json
outputs/       # 每次 ReAct 运行轨迹 run_*.json
```

`RunRecord` 当前记录内容：

- `command`
- `steps`
- `lessons`
- `strategy`
- `final_scene`
- `finish_reason`

已有运行轨迹：

```text
outputs/run_20260427-170735.json  finish     6 steps   3 final instances   Build a tiny demo sorting cell.
outputs/run_20260427-172241.json  max_steps 20 steps   0 final instances   Create an assembly scenario
outputs/run_20260427-202101.json  max_steps 20 steps   0 final instances   Create an assembly scenario
outputs/run_20260427-204320.json  max_steps 20 steps   0 final instances   Create an assembly scenario
outputs/run_20260427-205336.json  max_steps 20 steps   0 final instances   Create an assembly scenario
outputs/run_20260427-213015.json  max_steps 20 steps   0 final instances   Create an assembly scenario
outputs/run_20260427-214312.json  max_steps 20 steps   0 final instances   Create an assembly scenario
outputs/run_20260428-015933.json  max_steps 20 steps   0 final instances   Create an assembly scenario
```

实验管理还缺少：

- 每次运行的配置快照。
- LLM 模型名、embedding 模型名、device、backend。
- 索引版本或 corpus hash。
- git commit / dirty 状态。
- 随机种子。
- 运行耗时。
- 每轮工具调用统计。
- 成功/失败原因归类。
- 自动汇总多次实验结果的 report。

## 未完成与风险点

### 1. `retrieve_scene_prior` 链路不完整

Prompt 和 agent working memory 都把 `retrieve_scene_prior` 当作第一阶段：

- `THINK_SYSTEM` 要求先调用 `retrieve_scene_prior`。
- `build_think_prompt` 也提示 scene type 不清楚时调用 `retrieve_scene_prior`。
- `ReActAgent._is_repeated_retrieval()` 和 `_update_working_memory()` 都包含 `retrieve_scene_prior`。

但当前实际注册工具中没有 `retrieve_scene_prior`，当前 corpus 里也没有 `scene_prior` 文档。

影响：

- LLM 很容易按 prompt 调不存在的工具。
- agent 会返回 unknown tool。
- assembly 场景多次运行停在 `max_steps` 且最终实例数为 0，可能与此有关。

建议：

- 要么实现 `RetrieveScenePriorTool`，并补齐 `data/assets/docs/*.jsonl`。
- 要么删除 prompt 和 agent 中的 `retrieve_scene_prior` 阶段，直接从 `retrieve_scene_template` 开始。

### 2. 检索工具返回字段不一致

`retrieve_assets.py` 当前返回：

```python
ToolResult(ok=True, data={"catch": items, "query": query, "filters": filters})
```

但以下代码期望读取 `hits`：

- `ReActAgent._update_working_memory()`
- `RetrieveAssetsTool.run_test()`
- `RetrieveSceneTemplateTool.run_test()`
- 多个脚本式测试

影响：

- 检索本身成功，但 agent working memory 不会更新。
- 工具自测和脚本测试报 “returned no hits”。
- LLM 即使拿到结果，系统内部进度状态也可能保持为空。

建议：

- 将返回字段统一为 `hits`。
- 如需兼容旧测试，可以短期同时返回 `hits` 和 `catch`，后续删除 `catch`。

### 3. `place_instance.instance_id` schema 与实现不一致

Schema 中声明了可传 `instance_id`，但实现中实际忽略调用参数，只使用：

```python
doc.metadata.get("instance_id") or context.scene.next_instance_id(asset_type)
```

影响：

- LLM 以为可以指定实例 ID，但实际不会生效。
- 如果 CSV 中自带 `instance_id`，重复放同一个资产会更容易撞 ID。

建议：

- 明确策略：要么允许用户传入并优先使用 `kwargs["instance_id"]`，要么从 schema 移除该字段。
- 如果保留 CSV `instance_id`，需要处理重复放置时的自动后缀。

### 4. IsaacSim 仍是占位

`scene_layout_rag/physics/isaac_bridge.py` 当前只定义接口，`simulate()` 和 `query_contacts()` 都抛 `NotImplementedError`。

当前物理反馈实际来自 `validators.run_static_simulation()`，只做：

- 支撑关系几何检查。
- 未声明 parent 的悬空检查。
- 父子支撑 contact 记录。

建议：

- 若短期没有 IsaacSim 环境，就把文档中“物理仿真”统一称为“静态稳定性近似”。
- 若要接入 IsaacSim，需要实现 bridge，并把实例注入 `ToolContext.extras["isaac_bridge"]` 和 `Observer`。

### 5. `adjust_z` 未实现

`方案/优化.md` 和 README 提到 `adjust_z`，但工具列表中没有实现。

建议：

- 如果不需要，文档明确标为 deferred。
- 如果需要，作为 `move_asset` 的垂直专用包装实现，便于 LLM 修正支撑高度。

### 6. 输出还不是可直接使用的 USD 场景

当前运行产物是 JSON 轨迹和 `final_scene`，还没有看到从 `SceneState` 导出 USD/USDA/Isaac stage 的主链路。

建议：

- 增加 `export_scene` 工具或离线脚本。
- 输入 `final_scene.instances[*].usd_path / position / rotation / support`。
- 输出 `.usd/.usda/.json` 场景包。

### 7. 测试体系混杂脚本与 pytest

当前 `scene_layout_rag/test/` 中既有 pytest 单元测试，也有 import 时直接联网调用 OpenAI/OpenRouter 的脚本。

影响：

- `pytest -q scene_layout_rag/test` 在收集阶段就会联网失败。
- 脚本式测试不会被 pytest 收集为真正用例，容易出现“pytest 通过但脚本运行失败”的错觉。

建议：

- 把联网测试移到 `examples/` 或改名为非 `test_*.py`。
- 需要联网的测试加 `pytest.mark.integration` 和环境变量开关。
- 本地单元测试只覆盖纯函数、工具、RAG keyword 路径和 agent dry-run。

## 验证结果

已执行的验证：

```bash
python -m scene_layout_rag.cli --no-faiss retrieve "conveyor" --top-k 2 --doc-type asset
```

结果：可以正常返回两个 Conveyor 资产文档。

```bash
pytest -q scene_layout_rag/test
```

结果：失败。原因是以下测试在 pytest 收集阶段直接联网调用 OpenAI/OpenRouter，而当前沙箱禁止网络：

- `scene_layout_rag/test/test_tool_place.py`
- `scene_layout_rag/test/test_tool_state.py`
- `scene_layout_rag/test/test_tool_use.py`

```bash
pytest -q scene_layout_rag/test/test_retrieve_tools.py \
  scene_layout_rag/test/test_place_instance_tool.py \
  scene_layout_rag/test/test_move_asset_tool.py \
  scene_layout_rag/test/test_delete_asset_tool.py \
  scene_layout_rag/test/test_query_scene_tool.py \
  scene_layout_rag/test/test_set_support_tool.py \
  scene_layout_rag/test/test_tool_schema.py
```

结果：pytest 收集到 3 个真正测试并通过。

直接运行脚本式工具测试时，多个测试失败，核心原因一致：

```text
retrieve_assets 返回 data.catch
测试和 agent 读取 data.hits
```

相关失败包括：

- `test_retrieve_tools.py`: `retrieve_scene_template run_test returned no hits`
- `test_place_instance_tool.py`: `retrieve_assets returned no hits`
- `test_move_asset_tool.py`: `retrieve_assets returned no hits`
- `test_query_scene_tool.py`: `retrieve_assets returned no hits for Workbench`
- `test_delete_asset_tool.py`: `retrieve_assets returned no hits for Conveyor`
- `test_set_support_tool.py`: `retrieve_assets returned no hits for Workbench`

## 建议优先级

### P0

- 统一检索返回字段为 `hits`。
- 补齐或移除 `retrieve_scene_prior`。
- 整理测试：避免 pytest 收集阶段联网。

### P1

- 修正 `place_instance.instance_id` 语义。
- 给 `RunRecord` 增加实验元数据。
- 增加 agent dry-run 测试，使用假 planner 跑通 think -> act -> observe。

### P2

- 实现 `adjust_z` 或正式标记为 deferred。
- 增加 `SceneState` 到 USD/USDA 的导出链路。
- 接入或明确延后 IsaacSim bridge。

### P3

- 清理仓库生成物和 `.gitignore`。
- 将 `dataprocess/` 脚本参数化，减少硬编码绝对路径。
- 建立多次实验汇总报告。
