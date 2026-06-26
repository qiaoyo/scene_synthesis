# Metrics 分类与实现方法总结

本文档说明当前 metrics 的分类、实现状态，以及本目录中直接可实现指标的计算方法。

## 分类

### 工业/物理指标

| 指标    | 名称                        | 当前状态 | 数据来源                                                                           |
| ------- | --------------------------- | -------- | ---------------------------------------------------------------------------------- |
| `SR`  | 任务成功率                  | 已实现   | `record.json` 中的 `save_scene_usd` 工具结果、USD 文件存在性、最终 observation |
| `CFR` | 碰撞无关率                  | 已实现   | 最终 observation 的 `validation.collision_free`                                  |
| `PSR` | 物理稳定率                  | 已实现   | 最终 observation 的 `physics_feedback.stable`                                    |
|         | 场景任务可行性/<br />合理性 | 规划中   |                                                                                    |

### 场景语义指标

| 指标    | 名称           | 当前状态 | 数据来源或缺口                                                                                   |
| ------- | -------------- | -------- | ------------------------------------------------------------------------------------------------ |
| `SVR` | 支撑关系正确率 | 已实现   | 最终 observation 的 `support_state.valid_relation_count` 和 `current_state.support_children` |
| `ACR` | 资产覆盖率     | 暂未实现 | 需要每条任务的 `required_assets` 标注                                                          |
| `RSR` | 空间关系满足率 | 暂未实现 | 需要 `required_relations` 标注，并实现空间关系 checker                                         |
| `PE`  | 位置误差       | 暂未实现 | 需要专家位置、人工标注位置或 gold scene state                                                    |

### Agent 行为指标

| 指标    | 名称           | 当前状态 | 数据来源或缺口                                    |
| ------- | -------------- | -------- | ------------------------------------------------- |
| `AS`  | 平均步数       | 已实现   | `len(record.steps)`                             |
| `ATC` | 平均工具调用数 | 已实现   | `sum(len(step.tools) for step in record.steps)` |
| `TCA` | 工具调用准确率 | 暂未实现 | 需要专家 trace 或 gold tool sequence              |
| `TPS` | 工具参数相似度 | 暂未实现 | 需要 gold 参数，并实现参数相似度函数              |
| `RE`  | 纠错效率       | 暂未实现 | 需要从 trace 中追踪碰撞、修复动作和解决事件       |

## 已实现指标的具体方法

实现脚本：[evaluate_runs.py](evaluate_runs.py)

### SR

`SR` 不直接使用 `record.ok`，因为 `record.ok=true` 只表示 agent 返回了 final response。当前实现要求同时满足：

1. `save_scene_usd` 被调用并且工具记录 `ok=true`。
2. 工具结果中 `data.usd_path` 存在。
3. 对应 USD 文件在文件系统中存在。
4. 最终 observation 的 `ok=true`。

### CFR

从最终 observation 读取：

```text
observation.validation.collision_free
```

默认只统计有明确布尔值的 run。使用 `--strict-unknown` 时，`None` 会按失败处理。

### PSR

从最终 observation 读取：

```text
observation.physics_feedback.stable
```

默认只统计有明确布尔值的 run。使用 `--strict-unknown` 时，`None` 会按失败处理。

### SVR

分子：

```text
sum(observation.support_state.valid_relation_count)
```

分母：

```text
sum(count_edges(observation.current_state.support_children))
```

如果没有声明任何支撑关系，则 `SVR` 输出为 `null`。

### AS

每个 run 的 step 数：

```text
len(record.steps)
```

批量指标取平均值。

### ATC

每个 run 的工具调用数：

```text
sum(len(step.tools) for step in record.steps)
```

批量指标取平均值。

## 辅助诊断指标

脚本额外输出：

| 指标                        | 含义                                                |
| --------------------------- | --------------------------------------------------- |
| `AAS`                     | 平均 action steps，即至少包含一次工具调用的 step 数 |
| `S_max`                   | 当前 batch 中最大 step 数，用于步数惩罚归一化       |
| `quality_score_available` | 只使用当前已实现指标计算的 QS 子集                  |

当前 `quality_score_available` 使用：

```text
QS_available =
  alpha * SR
+ beta  * CFR
+ gamma * PSR
+ delta * SVR
- mu    * AS / S_max
```

由于 `ACR` 和 `RSR` 需要额外标注数据，因此当前不纳入该分数。

## 使用方法

默认读取 `outputs/runs`，输出到 `outputs/metrics`：

```bash
/home/simple/isaac_env/bin/python scripts/metrics/evaluate_runs.py
```

包含每个 run 的详细指标：

```bash
/home/simple/isaac_env/bin/python scripts/metrics/evaluate_runs.py --include-run-details
```

将未知碰撞/稳定状态按失败处理：

```bash
/home/simple/isaac_env/bin/python scripts/metrics/evaluate_runs.py --strict-unknown
```

## 后续需要补充的数据或代码

### ACR

需要为任务增加资产需求标注：

```json
{
  "task_id": "001",
  "required_assets": ["Box", "Pallet", "Workbench"]
}
```

### RSR

需要为空间关系增加标注和 checker：

```json
{
  "required_relations": [
    {"type": "on", "subject": "Box", "object": "Pallet"},
    {"type": "nearby", "subject": "AGV", "object": "Pallet"}
  ]
}
```

关系 checker 可基于最终 observation 中的 position、bbox 和 support graph 实现。

### TCA/TPS

需要 gold tool trace，例如：

```json
{
  "gold_tool_calls": [
    {"name": "retrieve_asset", "arguments": {"assets": []}},
    {"name": "place_instance", "arguments": {"doc_id": "...", "position": [0, 0, 0]}}
  ]
}
```

### PE

需要 gold/reference position，用于和最终实例位置比较。

### RE

需要增加事件追踪逻辑，识别：

1. `check_collision` 返回碰撞。
2. 后续 `move_asset`、`replace_instance`、`delete_asset` 或重新 `place_instance`。
3. 后续 observation 或 `check_collision` 显示碰撞解决。

## 暂未实现场景与工业指标的实现分析

本节分析 `场景任务可行性/合理性`、`ACR`、`RSR`、`PE`。这些指标主要衡量最终场景是否满足任务语义，而不是 agent 的工具过程。它们通常需要额外的任务标注、规则 checker，或参考场景。

### 场景任务可行性/合理性

该指标目前在工业/物理指标表中处于规划状态。它可以用于回答一个更高层的问题：即使场景无碰撞、稳定、支撑关系正确，它是否仍然是一个“工业上合理、任务上可执行”的场景。

建议将它定义为一个组合诊断指标，而不是单一布尔值。可拆成以下子项：

| 子项 | 含义 | 可用数据 |
| --- | --- | --- |
| `layout_accessible` | 关键设备周围是否有可用通道/操作空间 | bbox、position、场景边界 |
| `task_flow_valid` | 任务流程是否合理，例如 infeed -> workbench -> outfeed | 任务标注、空间关系 |
| `orientation_valid` | 设备朝向是否符合任务，例如 conveyor east-west、robot facing bench | rotation、任务标注 |
| `clearance_valid` | forklift、AGV、robot 周围是否保留安全间距 | bbox、position、阈值规则 |
| `semantic_role_valid` | 资产角色是否合理，例如 pallet 承载 box，rack 存储 box | required_assets、required_relations |

第一版可以实现为规则分数：

```text
Feasibility = mean(layout_accessible, task_flow_valid, orientation_valid, clearance_valid, semantic_role_valid)
```

也可以先只做布尔判定：

```text
feasible = collision_free
           and stable
           and support_valid
           and clearance_valid
           and required_relations_satisfied
```

需要补充的数据：

```json
{
  "task_id": "001",
  "scene_bounds": {"x": [-5, 5], "y": [-5, 5]},
  "clearance_rules": [
    {"asset_type": "AGV", "min_clearance": 0.8},
    {"asset_type": "Forklift", "min_clearance": 1.2}
  ],
  "orientation_rules": [
    {"asset_type": "Conveyor", "axis": "east-west"}
  ],
  "workflow": ["Pallet", "Workbench", "Conveyor"]
}
```

实现方式建议放在 relation checker 之后，因为它依赖很多同类几何判断。第一阶段可只做 `clearance_valid` 和 `orientation_valid` 两个最明确的规则，避免过早引入复杂主观判断。

### ACR 资产覆盖率

`ACR` 衡量任务要求的资产类别是否都出现在最终场景中：

```text
ACR = mean(|placed_assets intersect required_assets| / |required_assets|)
```

当前最终 observation 已经有实际放置资产：

```text
observation.current_state.instances[*].asset_type
```

缺少的是每条任务的必需资产标注：

```json
{
  "task_id": "001",
  "command": "place a box on a pallet near a conveyor",
  "required_assets": ["Box", "Pallet", "Conveyor"]
}
```

第一版可以用集合计算：

```text
placed = set(final_instances.asset_type)
required = set(annotation.required_assets)
ACR_i = len(placed & required) / len(required)
```

但工业场景经常要求多个同类资产，例如“两个 box”或“两个 pallet”。因此更推荐支持计数版本：

```json
{
  "required_asset_counts": {
    "Box": 2,
    "Pallet": 1,
    "Conveyor": 1
  }
}
```

计数版公式：

```text
ACR_count_i =
  sum(min(placed_count[type], required_count[type]))
  / sum(required_count[type])
```

需要注意：

- `IndustrialPart` 和任务文本里的 `part` 应该建立 alias 映射。
- `IndustrialRobot` 和 `robot` 也需要 alias 映射。
- 如果资产类型粒度不同，例如 `Conveyor` vs `ConveyorBelt`，需要统一 taxonomy。
- 如果 agent 放置了额外资产，`ACR` 不惩罚；额外资产可另设 `extra_asset_count` 或 `asset_precision`。

建议输出：

| 字段 | 含义 |
| --- | --- |
| `ACR_set` | 按资产类别集合计算 |
| `ACR_count` | 按资产数量计算 |
| `missing_assets` | 缺失资产类型 |
| `extra_assets` | 额外放置资产类型 |

### RSR 空间关系满足率

`RSR` 衡量任务要求的空间关系是否被最终场景满足：

```text
RSR = sum(satisfied_relations) / sum(required_relations)
```

需要新增任务关系标注：

```json
{
  "task_id": "001",
  "required_relations": [
    {"type": "on", "subject": "Box", "object": "Pallet"},
    {"type": "nearby", "subject": "AGV", "object": "Pallet"},
    {"type": "in_front_of", "subject": "Forklift", "object": "Rack"},
    {"type": "left_of", "subject": "IndustrialRobot", "object": "Conveyor"}
  ]
}
```

最终场景可用数据：

```text
instances[*].asset_type
instances[*].position
instances[*].rotation_deg
instances[*].bbox
current_state.support_children
```

第一版 relation checker 可以按关系类型实现：

| 关系 | 判断方法 |
| --- | --- |
| `on` | 优先检查 support graph；否则检查 z 接触和 xy overlap |
| `beside` | 两个物体水平距离低于阈值，且没有明显上下支撑关系 |
| `nearby` | 中心点水平距离低于 `near_threshold` |
| `in_front_of` | subject 位于 object 的前方方向；需要约定前方轴或使用 object rotation |
| `left_of/right_of` | 根据世界坐标或 object local frame 判断相对方向 |
| `center` | subject 中心接近 object 或 scene center |
| `fixed_on` | 类似 `on`，但要求位置偏差更小、稳定性更强 |
| `carrying` | 可建模为 support relation + subject/object 类型约束 |

推荐 checker 返回详细结果，而不是只返回 true/false：

```json
{
  "type": "nearby",
  "subject": "AGV.a.2",
  "object": "Pallet.a.3",
  "satisfied": true,
  "score": 0.87,
  "distance": 0.52,
  "threshold": 1.0
}
```

实例匹配是 RSR 的关键难点。标注里通常写资产类型或语义角色，但最终场景中是具体 instance。可以按以下策略匹配：

1. 如果 annotation 指定 `instance_id`，直接匹配。
2. 如果指定 `role`，使用 role 到 instance 的映射。
3. 如果只指定 `asset_type`，在所有同类实例中寻找最能满足关系的组合。
4. 多个关系共享同一实体时，需要保持一致匹配，避免每条关系单独挑最优导致虚高。

第一版可以采取“每条关系独立最优匹配”，实现简单：

```text
relation_score = max(score(candidate_subject, candidate_object))
```

第二版再做全局实体一致性约束。

建议输出：

| 字段 | 含义 |
| --- | --- |
| `RSR` | 满足的关系比例 |
| `relation_score_avg` | 关系软分平均值 |
| `unsatisfied_relations` | 未满足关系列表 |
| `ambiguous_relations` | 找不到唯一实体映射的关系 |

### PE 位置误差

`PE` 衡量预测位置和参考位置之间的距离：

```text
PE = mean(norm(pred_position_k - gold_position_k))
```

它需要参考位置来源。可选来源有三类：

1. 专家 trace 中的 `place_instance.position` 或 `move_asset.new_position`。
2. 人工标注的 gold scene state。
3. 从成功 run 中筛选出的 canonical final scene。

推荐使用 gold scene state，因为它比工具 trace 更接近最终目标：

```json
{
  "task_id": "001",
  "gold_instances": [
    {"role": "main_box", "asset_type": "Box", "position": [0.0, 0.0, 1.0]},
    {"role": "target_pallet", "asset_type": "Pallet", "position": [0.0, 0.0, 0.0]}
  ]
}
```

实现时同样需要实体对齐：

```text
gold instance -> predicted instance
```

第一版可以按 `asset_type + occurrence_index` 对齐。第二版可按 Hungarian matching 或最近邻匹配，使总位置误差最小。

对于旋转也可以扩展出 `RE_rot` 或 `Orientation Error`：

```text
OE = mean(angle_distance(pred_rotation, gold_rotation))
```

需要注意：

- 对称物体的 rotation 误差不能简单按角度绝对差计算，例如方箱 180 度可能等价。
- 如果任务只要求相对关系，不要求绝对坐标，PE 的意义会弱于 RSR。
- 如果 gold scene 只标了类别，没有角色，多实例同类资产会导致对齐不稳定。

建议输出：

| 字段 | 含义 |
| --- | --- |
| `PE` | 平均位置误差 |
| `PE_by_asset_type` | 按资产类型分组的位置误差 |
| `matched_instances` | 成功对齐的实例数量 |
| `unmatched_gold_instances` | gold 中未匹配到的实例 |
| `unmatched_pred_instances` | 预测中多出的实例 |

## 暂未实现 Agent 指标的实现分析

本节只分析 Agent 行为指标中暂未实现的 `TCA`、`TPS`、`RE`。这些指标和场景最终质量不同，重点衡量 agent 的决策过程是否接近专家、参数是否合理、以及发现问题后的修复效率。

### TCA 工具调用准确率

`TCA` 衡量模型预测的工具名是否和目标工具名一致：

```text
TCA = mean(pred_tool_name_j == gold_tool_name_j)
```

当前项目已经有预测侧 trace：

```text
outputs/runs/<run_id>/planner_steps.jsonl
record.json -> steps[*].decision.calls
record.json -> steps[*].tools
```

但还缺少目标侧 trace，也就是每个任务对应的专家工具序列。建议新增一个 gold trace 文件，例如：

```json
{
  "task_id": "001",
  "command": "place a box on a pallet",
  "gold_tool_calls": [
    {"name": "retrieve_asset", "arguments": {"assets": [{"expected_asset_type": "Box"}]}},
    {"name": "retrieve_asset", "arguments": {"assets": [{"expected_asset_type": "Pallet"}]}},
    {"name": "place_instance", "arguments": {"doc_id": "box_doc", "position": [0, 0, 1]}},
    {"name": "place_instance", "arguments": {"doc_id": "pallet_doc", "position": [0, 0, 0]}},
    {"name": "set_support", "arguments": {"child_id": "box", "parent_id": "pallet"}},
    {"name": "check_collision", "arguments": {}},
    {"name": "check_support", "arguments": {"child_id": "box", "parent_id": "pallet"}},
    {"name": "simulate_step", "arguments": {}},
    {"name": "save_scene_usd", "arguments": {"include_physics": true}}
  ]
}
```

实现时需要先把预测 trace 和 gold trace 展平成线性序列：

```text
pred = flatten(record.steps[*].decision.calls)
gold = annotation.gold_tool_calls
```

最简单的对齐方式是按 index 对齐：

```text
pair_j = (pred[j], gold[j])
```

如果长度不同，缺失位置按错误计算。这个方法实现简单，适合第一版，但对“多一步 check”或“检索多个资产合并到一次 retrieve_asset”比较敏感。

更稳的第二版可以使用编辑距离或动态规划对齐：

```text
match_cost = 0 if pred.name == gold.name else 1
insert/delete_cost = 1
```

这样可以区分“工具顺序基本正确但多调用了一次工具”和“工具选择完全错误”。最终可同时输出：

| 指标 | 含义 |
| --- | --- |
| `TCA_index` | 严格按位置对齐的工具准确率 |
| `TCA_aligned` | 编辑距离对齐后的工具准确率 |
| `extra_tool_calls` | 预测多出的工具调用数 |
| `missing_tool_calls` | gold 中缺失的工具调用数 |

建议第一阶段先实现 `TCA_index`，因为数据结构最直接；等 gold trace 稳定后再实现动态规划对齐。

### TPS 工具参数相似度

`TPS` 衡量预测参数和 gold 参数是否相似：

```text
TPS = mean(sim(pred_args_j, gold_args_j))
```

它依赖 `TCA` 的工具调用对齐结果。只有工具名相同或被对齐为同一类工具时，参数相似度才有意义。不同工具之间可以直接记为 0，或者跳过并单独统计。

建议按工具和参数类型拆分计算，而不是对 JSON 做字符串比较。

#### 通用参数类型规则

| 参数类型 | 相似度规则 |
| --- | --- |
| bool | exact match |
| enum/string category | exact match |
| number | `max(0, 1 - abs(pred - gold) / max_error)` |
| position/vector | `max(0, 1 - distance(pred, gold) / d_max)` |
| doc_id | exact match，或映射到 asset_type 后比较 |
| instance_id | 先做实体对齐，再比较对齐后的实体 |
| list | 按元素语义对齐后求平均 |
| dict | 对关键字段加权平均 |

位置参数可使用已有公式：

```text
sim_pos(pred, gold) = max(0, 1 - norm(pred - gold) / d_max)
```

其中 `d_max` 可以先设为 2.0 米或根据场景尺度配置。

#### 按工具定义参数相似度

`retrieve_asset`：

- 重点比较 `assets[*].expected_asset_type`。
- `query` 可以暂时不评分，或用文本相似度后续扩展。
- `top_k` 可 exact match 或按数值误差评分。
- 如果一次调用里包含多个 assets，建议按 `expected_asset_type` 对齐元素。

`place_instance`：

- `doc_id`：先 exact match；如果不同但对应资产类型相同，可给部分分。
- `position`：用距离相似度。
- `rotation_deg`：用角度误差相似度。

`move_asset`：

- `instance_id`：需要实体对齐。
- `new_position`：用距离相似度。

`set_support` / `check_support`：

- `child_id`、`parent_id`：需要实体对齐。
- 如果实体 id 不一致但 asset_type 和语义角色一致，可以给部分分。

`check_collision`：

- 空参数全局检查：exact match。
- 成对检查：比较 `instance_id_a`、`instance_id_b`，顺序可视为无关。

`simulate_step`：

- `duration`、`dt`：按数值相似度。
- `write_back`：exact match。

`save_scene_usd`：

- `include_physics`：exact match。

#### 实体对齐问题

`TPS` 的难点是预测 run 中的 `instance_id` 可能和 gold trace 不完全一致。例如 gold 写 `box_1`，实际预测是 `Box.a.6`。因此需要一个 entity alignment 层：

```text
gold entity -> predicted instance
```

可按以下优先级对齐：

1. `doc_id` exact match。
2. `asset_type` + 出现顺序。
3. `asset_type` + 空间位置最近。
4. 人工标注的语义角色，例如 `main_box`、`target_pallet`。

第一版可以先用 `asset_type + occurrence_index`，后续再加入位置和语义角色。

### RE 纠错效率

`RE` 衡量 agent 发现碰撞后，用多少修复动作解决问题：

```text
RE = N_collision_resolved / (N_repair_steps + epsilon)
```

这个指标不一定需要人工 gold trace，但需要更细的事件追踪逻辑。当前可从 `record.json` 中的工具结果和 observation 推断。

#### 事件定义

碰撞事件：

```text
check_collision tool result data.collision_free == false
或 step.observation.validation.collision_free == false
```

修复动作：

```text
move_asset
replace_instance
delete_asset
place_instance
set_support
```

其中 `move_asset` 和 `replace_instance` 是主要修复动作；`delete_asset` 和重新 `place_instance` 可视为结构性修复；`set_support` 只在支撑关系导致碰撞判断或稳定性问题时计入。

解决事件：

```text
后续 check_collision tool result data.collision_free == true
或后续 observation.validation.collision_free == true
```

#### 第一版 run-level 实现

第一版可以用 run 级别粗略统计：

1. 找到第一次碰撞出现的 step。
2. 从该 step 之后统计修复工具调用数。
3. 如果最终 observation `collision_free == true`，则认为本 run 的碰撞被解决。

公式：

```text
collision_resolved_i = has_collision_i and final_collision_free_i
repair_steps_i = count_repair_tools_after_first_collision_i
RE = sum(collision_resolved_i) / (sum(repair_steps_i) + epsilon)
```

优点是实现简单，不需要 collision pair 跟踪。缺点是无法区分多个碰撞是否分别解决。

#### 第二版 pair-level 实现

更精确的实现可以追踪 collision pair：

```text
collision_key = sorted([instance_id_a, instance_id_b])
```

每次 `check_collision` 返回 collisions 时，记录每个 pair 的 active 状态。后续修复动作如果移动了 pair 中任一实例，则关联到该 collision。再遇到该 pair 不在 collisions 中时，认为该 pair resolved。

可输出：

| 字段 | 含义 |
| --- | --- |
| `collision_events` | 碰撞 pair 出现次数 |
| `resolved_collision_events` | 最终被解决的 pair 数 |
| `repair_tool_calls` | 修复工具调用总数 |
| `repair_steps` | 包含修复工具的 step 数 |
| `RE_call_based` | `resolved_collision_events / repair_tool_calls` |
| `RE_step_based` | `resolved_collision_events / repair_steps` |

#### RE 的注意点

- 如果 run 一开始没有碰撞，不能直接把 RE 记为 1；应从 RE 分母/分子中排除，另设 `collision_seen_runs`。
- 如果 agent 通过删除资产解决碰撞，但导致任务资产缺失，RE 可能很高但场景质量低，因此需要和 `ACR`、`SR`、`SVR` 一起看。
- 如果 `check_collision` 没有显式调用，但 observation 已经包含 collision 状态，也可以作为事件来源。
- 如果有多个修复动作后仍未解决，分母增加、分子不增加，RE 会自然降低。

### 推荐落地顺序

建议按以下顺序实现这些暂未完成的 Agent 指标：

1. `RE_run_level`：不需要 gold trace，只需要基于现有 `record.json` 做事件扫描。
2. `TCA_index`：需要先准备 gold tool sequence，但实现逻辑简单。
3. `TPS_basic`：在 `TCA_index` 对齐基础上，实现 bool、enum、number、position、doc_id 的基础相似度。
4. `TCA_aligned`：用编辑距离或动态规划改善工具序列对齐。
5. `TPS_entity_aligned`：加入实体对齐，提升 `instance_id`、support relation 参数的评分可靠性。
