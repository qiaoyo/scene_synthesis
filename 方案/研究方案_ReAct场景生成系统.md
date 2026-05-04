# ReAct 工业场景自动布局系统 -- 研究方案与代码重构计划

> 版本: v2.0 | 日期: 2026-04-12

---

## 一、项目概述

### 1.1 研究目标

构建一个基于 **ReAct (Reasoning + Acting)** 范式的工业场景自动布局系统。系统接收自然语言指令，通过 LLM 驱动的 **"推理 → 行动 → 观测 → 反思"** 迭代循环，在 Isaac Sim 中自动生成物理合理、语义正确的 3D 工业场景布局。

### 1.2 现状分析

当前系统为**单次 Retrieve → Plan → Output 管线**，核心链路：

```
cli.py → rag.py:generate_layout() → llm_planner.py:plan() → LayoutPlan
```

存在以下瓶颈：

| 维度 | 现状 | 问题 |
|------|------|------|
| 工具 | 仅隐式 `place_instance`（嵌入 prompt） | 无法移动/删除/查询，LLM 动作空间极小 |
| 检索 | 一次性前置检索，固定资产集合 | 规划中途无法获取新资产，检索与规划割裂 |
| 观测 | 无观测环节 | 放置后不验证碰撞、支撑、物理稳定性 |
| 循环 | 单次生成，不迭代 | 错误无法自修正，质量完全依赖单次推理 |
| 反思 | 无 | LLM 不能从错误中学习和调整策略 |
| 物理 | Isaac Sim 仅用于可视化 | 不参与规划验证，布局可能物理不合理 |
| 支撑关系 | 无 | 物体之间的承载关系未建模 |

---

## 二、核心架构决策：RAG 与 ReAct 的关系

### 2.1 问题分析

当前系统将 RAG 检索作为 ReAct 的前置阶段：

```
[RAG 检索 Top-K 资产] ──→ [ReAct 在固定资产集上规划]
```

这一设计存在根本性问题：

| 问题 | 场景示例 |
|------|----------|
| **初始检索无法预见所有需求** | 用户说"规划分拣中心"，初始检索到了传送带和货架，但规划到一半发现还需要安全围栏和标识牌 |
| **检索粒度与规划需求不匹配** | 初始检索返回了泛化的"Box"类别，但规划时发现需要"能放在 2m 传送带上的小型周转箱" |
| **无法根据场景上下文精确检索** | 已放置的传送带高度 0.8m，需要找"高度匹配的工作台"，但初始检索时不知道这个约束 |
| **违反 ReAct 核心范式** | ReAct 的核心是 Agent 自主决定何时获取信息、获取什么信息，前置检索剥夺了这一能力 |

### 2.2 架构决策：RAG 检索作为 ReAct 的工具

**将 `retrieve_assets` 作为一个 Tool 纳入 ReAct 工具集**，Agent 在推理过程中按需检索：

```
ReAct 循环 {
    Think:  "当前场景缺少传送带，需要检索适合的传送带资产"
    Act:    retrieve_assets(query="分拣用传送带，长度2m左右")
    Observe: [Conveyor_A (2.1m), Conveyor_B (1.8m), ...]
    
    Think:  "Conveyor_A 尺寸合适，放置在场景中心"
    Act:    place_instance(asset_id="Conveyor_A", position=[0,0,0])
    Observe: ok, no collision
    
    Think:  "需要一个高度匹配的工作台放在传送带旁"
    Act:    retrieve_assets(query="工作台，高度约0.8m，适配传送带")  ← 带上下文的精确检索
    Observe: [Workbench_C (h=0.82m), ...]
    ...
}
```

### 2.3 方案对比

| 维度 | 方案 A: RAG 前置 | 方案 B: RAG 作为 Tool（采用） |
|------|-------------------|-------------------------------|
| 检索时机 | 一次性，循环前 | 按需，循环内任意时刻 |
| 检索上下文 | 仅用户原始指令 | 用户指令 + 当前场景状态 + 已有资产 + 教训 |
| 资产集合 | 固定 Top-K | 动态扩展，随需检索 |
| 检索精度 | 粗粒度（泛化查询） | 细粒度（基于当前约束的精确查询） |
| 符合 ReAct | 否（信息获取在循环外） | 是（信息获取是 Action 的一种） |
| 额外开销 | 1 次检索 | 多次检索（但每次更精确，总检索量可控） |

### 2.4 热启动机制（可选优化）

为避免 Agent 前几步全在检索，可在循环启动时做一次**粗粒度热启动检索**，让 Agent 了解资产库概况：

```python
# 热启动：给 Agent 提供资产库摘要，而非具体资产
warm_start_context = {
    "available_categories": ["AGV", "Box", "Conveyor", "Rack", ...],  # 有哪些大类
    "category_counts": {"AGV": 5, "Box": 12, "Conveyor": 8, ...},    # 每类有多少种
    "scene_templates": ["assembly", "sorting", "warehouse", ...],     # 可参考的场景模板
}
```

Agent 看到这个摘要后，知道资产库里有什么大类可用，然后在规划过程中按需检索具体资产。

---

## 三、数据输入

### 3.1 资产数据（已有，保持不变）

| 数据类型 | 格式 | 路径 | 内容 |
|----------|------|------|------|
| 资产清单 | CSV | `data/assets/csv/*.csv` | 10 大类资产（AGV, Box, Conveyor, Decoration, Forklift, IndustrialRobot, Pallet, Part, Rack, Workbench），每类含 USD 路径、功能描述、包围盒 |
| 场景描述 | Markdown | `data/assets/md/*.md` | 6 种场景模板（assembly, palletizing, sorting, transport, warehouse, scene），每种含 brief/verbose 两版 |
| 向量索引 | FAISS | `data/indexes/` | 预计算的资产嵌入，用于语义检索 |

**CSV 字段结构**（以 `Conveyor_with_bbox_meters.csv` 为例）：

```
列1: Category（资产类别）
列2: USD Path（模型路径）
列3: Short Description（简短描述）
列4: Long Description（详细描述）
列5: BBox（包围盒，格式 {"size": [x,y,z], "unit": "m"}）
```

### 3.2 用户输入

```python
# 自然语言指令
command = "规划一个分拣中心，包含3条传送带、2个货架、1个工作台和1辆AGV"
```

### 3.3 运行时数据（新增）

| 数据 | 说明 | 来源 |
|------|------|------|
| 场景状态 `SceneState` | 当前已放置资产的实时快照 | 工具执行结果累积 |
| 观测报告 `Observation` | 每步行动后的验证结果 | 观测器自动生成 |
| 反思记录 `Lesson` | LLM 对错误的分析与经验 | LLM 反思模块 |
| 物理仿真反馈 | 稳定性、碰撞、接触点 | Isaac Sim 物理引擎 |

---

## 四、系统架构

### 4.1 整体架构图

```
┌───────────────────────────────────────────────────────────────────────┐
│                         用户自然语言指令                               │
└────────────────────────────┬──────────────────────────────────────────┘
                             │
                             ▼
┌───────────────────────────────────────────────────────────────────────┐
│                    ReAct Agent 迭代循环                                │
│                                                                       │
│   ┌───────────┐    ┌───────────┐    ┌───────────┐    ┌───────────┐   │
│   │  1. 推理   │──→│  2. 行动   │──→│  3. 观测   │──→│  4. 反思   │  │
│   │  Think    │    │   Act     │    │  Observe  │    │  Reflect  │   │
│   └─────┬─────┘    └───────────┘    └───────────┘    └─────┬─────┘   │
│         │                                                   │         │
│         └──────────────── 循环迭代 ◄────────────────────────┘         │
│                                                                       │
│   工具集 (Act 可调用):                                                │
│   ┌────────────────┐  ┌────────────────┐  ┌────────────────┐         │
│   │ retrieve_assets│  │ place_instance │  │ move_asset     │         │
│   │ (RAG 语义检索) │  │ (放置资产)      │  │ (移动资产)     │         │
│   ├────────────────┤  ├────────────────┤  ├────────────────┤         │
│   │ delete_asset   │  │ query_scene    │  │ check_collision│         │
│   │ (删除资产)     │  │ (查询场景)      │  │ (碰撞检测)     │         │
│   ├────────────────┤  ├────────────────┤  ├────────────────┤         │
│   │ check_support  │  │ set_support    │  │ simulate_step  │         │
│   │ (检查支撑)     │  │ (设置支撑)      │  │ (物理仿真)     │         │
│   └────────────────┘  └────────────────┘  └────────────────┘         │
│                                                                       │
│   支撑模块:                                                          │
│   ┌────────────────┐  ┌────────────────┐  ┌────────────────┐         │
│   │ SceneState     │  │ Observer       │  │ FAISS 向量库   │         │
│   │ (可变场景状态)  │  │ (观测器)       │  │ (资产语义检索)  │         │
│   └────────────────┘  └────────────────┘  └────────────────┘         │
└────────────────────────────┬──────────────────────────────────────────┘
                             │ 最终布局
                             ▼
┌───────────────────────────────────────────────────────────────────────┐
│                   Isaac Sim 渲染与物理验证                             │
│                                                                       │
│   scene.py: USD 加载 → 物理仿真 → 碰撞检测 → 稳定性反馈              │
└───────────────────────────────────────────────────────────────────────┘
```

**关键区别**：RAG 检索（FAISS 向量库）不再是独立的前置层，而是 ReAct 循环内部的一个工具 `retrieve_assets`，与 `place_instance`、`move_asset` 等工具并列，由 Agent 在推理阶段自主决定何时调用。

### 4.2 ReAct 主循环详细流程

```
Agent 初始化:
  - 加载 FAISS 向量索引 (离线已构建)
  - 注册全部工具 (含 retrieve_assets)
  - 构建资产库摘要 (热启动上下文)
  - 初始化空 SceneState

for step in range(max_steps):

    ┌─────────────────────────────────────────────────────┐
    │ Step 1: 推理 (Think)                                │
    │                                                     │
    │ 输入:                                               │
    │   - command (用户指令)                               │
    │   - asset_catalog_summary (资产库摘要/热启动上下文)  │
    │   - scene_state (当前场景快照)                       │
    │   - last_observation (上一步观测)                    │
    │   - lessons_learned (历史教训)                       │
    │   - available_tools (含 retrieve_assets)            │
    │                                                     │
    │ 输出:                                               │
    │   - thought: "当前缺少传送带，需要先检索合适的..."  │
    │   - action: "retrieve_assets" 或 "place_instance"   │
    │   - action_input: {query/asset_id/position/...}     │
    └──────────────────────┬──────────────────────────────┘
                           │
                           ▼
    ┌─────────────────────────────────────────────────────┐
    │ Step 2: 行动 (Act)                                  │
    │                                                     │
    │ ToolRegistry.execute(action, action_input)          │
    │                                                     │
    │ 若 action == "retrieve_assets":                     │
    │   → 执行 FAISS 语义检索                              │
    │   → 返回匹配的资产文档列表 (存入 Agent 工作记忆)     │
    │   → 不改变 SceneState                               │
    │                                                     │
    │ 若 action == "place_instance" / "move_asset" / ...: │
    │   → 更新 SceneState                                 │
    │   → 返回执行结果                                    │
    └──────────────────────┬──────────────────────────────┘
                           │
                           ▼
    ┌─────────────────────────────────────────────────────┐
    │ Step 3: 观测 (Observe)                              │
    │                                                     │
    │ 对于修改场景的 action:                               │
    │   SceneObserver.observe(scene_state) → {            │
    │     validation: {ok, collisions},                   │
    │     scene_semantics: {corridors, work_zones, flows},│
    │     support_state: {valid, invalid},                │
    │     physics_feedback: {stable, contacts, warnings}, │
    │     suggestions: ["建议..."]                        │
    │   }                                                 │
    │                                                     │
    │ 对于 retrieve_assets:                               │
    │   返回检索结果摘要作为 observation                    │
    └──────────────────────┬──────────────────────────────┘
                           │
                           ▼
    ┌─────────────────────────────────────────────────────┐
    │ Step 4: 反思 (Reflect) -- 仅当 observation 异常时    │
    │                                                     │
    │ LLM 分析: 什么出错了？为什么？下次怎么避免？          │
    │   → 更新 lessons_learned                            │
    │   → 必要时调整全局策略 (strategy)                    │
    └──────────────────────┬──────────────────────────────┘
                           │
                           ▼
                   继续下一次迭代 / 终止
```

---

## 五、技术路线（分步实施）

整个重构分为 **5 个阶段**，每阶段独立可测试：

```
阶段1 (工具层 + RAG工具化) ──→ 阶段2 (场景状态+观测) ──→ 阶段3 (ReAct主循环+反思)
                                                               │
                                                               ├──→ 阶段4 (LLM支撑决策)
                                                               └──→ 阶段5 (物理仿真接入)
```

---

### 阶段 1：工具注册与调度层（含 RAG 工具化）

**目标**：建立显式工具调度机制，将 RAG 检索改造为可在循环中调用的工具。

#### 1.1 新增文件结构

```
scene_layout_rag/
├── tools/
│   ├── __init__.py           # 导出 ToolRegistry 和所有工具
│   ├── base.py               # ToolSpec 基类 + ToolRegistry 注册表
│   ├── retrieve_assets.py    # ★ RAG 语义检索工具 (核心新增)
│   ├── place_instance.py     # 放置新资产
│   ├── move_asset.py         # 移动已有资产
│   ├── delete_asset.py       # 删除资产
│   ├── query_scene.py        # 查询场景状态
│   ├── check_collision.py    # 检测碰撞
│   ├── check_support.py      # 检查支撑关系
│   ├── set_support.py        # 设置支撑关系
│   └── simulate_step.py      # 运行物理仿真步
```

#### 1.2 核心代码设计

**工具基类与注册表** (`tools/base.py`)：

```python
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional

@dataclass
class ToolParam:
    """单个工具参数的描述"""
    name: str
    type: str                      # "str", "float", "list", "dict"
    description: str
    required: bool = True

@dataclass
class ToolSpec:
    """工具规格定义"""
    name: str
    description: str               # 给 LLM 看的说明
    parameters: List[ToolParam]
    returns: str                   # 返回值描述
    execute_fn: Callable           # 实际执行函数
    modifies_scene: bool = True    # 是否修改场景状态 (retrieve_assets 不修改)

    def to_prompt_text(self) -> str:
        """生成供 LLM 阅读的工具描述文本"""
        params_text = "\n".join(
            f"    - {p.name} ({p.type}, {'必填' if p.required else '可选'}): {p.description}"
            for p in self.parameters
        )
        return (
            f"工具名: {self.name}\n"
            f"功能: {self.description}\n"
            f"参数:\n{params_text}\n"
            f"返回: {self.returns}"
        )


class ToolRegistry:
    """工具注册表 -- 管理所有可用工具"""

    def __init__(self):
        self._tools: Dict[str, ToolSpec] = {}

    def register(self, spec: ToolSpec) -> None:
        self._tools[spec.name] = spec

    def get(self, name: str) -> Optional[ToolSpec]:
        return self._tools.get(name)

    def list_names(self) -> List[str]:
        return list(self._tools.keys())

    def is_scene_modifier(self, name: str) -> bool:
        """判断工具是否修改场景（决定是否触发观测）"""
        spec = self._tools.get(name)
        return spec.modifies_scene if spec else False

    def generate_tools_prompt(self) -> str:
        """生成所有工具的文本描述，注入 LLM prompt"""
        sections = [spec.to_prompt_text() for spec in self._tools.values()]
        return "\n\n".join(sections)

    def execute(self, tool_name: str, params: Dict[str, Any], **context) -> Dict[str, Any]:
        """执行指定工具，返回标准化结果"""
        spec = self._tools.get(tool_name)
        if spec is None:
            return {"ok": False, "error": f"未知工具: {tool_name}"}
        try:
            result = spec.execute_fn(params=params, **context)
            return {"ok": True, "result": result}
        except Exception as e:
            return {"ok": False, "error": str(e)}
```

#### 1.3 RAG 检索工具 (`tools/retrieve_assets.py`)

这是本次重构最关键的新工具——将现有 `SceneLayoutRAG.retrieve()` 封装为 ReAct 可调用工具：

```python
def retrieve_assets(params: dict, vector_store=None, embedder=None, **kw) -> dict:
    """
    在资产库中执行语义检索，返回匹配的资产列表。
    Agent 可在规划过程中随时调用以获取所需资产。

    params:
      - query: str         检索查询 (自然语言，如 "高度0.8m左右的工作台")
      - top_k: int         返回数量 (默认 5)
      - category: str      按类别过滤 (可选，如 "Conveyor")

    返回:
      - assets: list       匹配的资产文档列表，每项含 asset_id, usd_path, bbox, description
    """
    query = params["query"]
    top_k = params.get("top_k", 5)
    category = params.get("category", None)

    # 执行向量检索 (复用现有 EmbeddingBackend + LocalVectorStore)
    query_vec = embedder.embed_query(query)
    hits = vector_store.search(query_vec, top_k=top_k)

    # 可选: 按类别过滤
    if category:
        hits = [h for h in hits if h.document.metadata.get("asset_category") == category]

    # 格式化返回给 Agent
    assets = []
    for hit in hits:
        doc = hit.document
        assets.append({
            "asset_id": doc.metadata.get("asset_category", doc.doc_id),
            "doc_id": doc.doc_id,
            "usd_path": doc.metadata.get("usd_path", ""),
            "bbox": doc.metadata.get("bbox", {}),
            "description": doc.content[:200],  # 截断避免过长
            "score": round(hit.score, 3),
        })

    return {"query": query, "count": len(assets), "assets": assets}
```

**与现有代码的关系**：
- 复用 `embedding.py` 的 `EmbeddingBackend`（向量编码）
- 复用 `vector_store.py` 的 `LocalVectorStore`（FAISS 检索）
- 复用 `asset_loader.py` 的预处理流程（CSV/MD → AssetDocument）
- 向量索引在 Agent 初始化时一次性构建，`retrieve_assets` 工具调用时仅做查询

#### 1.4 完整工具清单（10 个）

| 工具名 | 功能 | 修改场景 | 输入 | 输出 | 实现依赖 |
|--------|------|----------|------|------|----------|
| **`retrieve_assets`** | **语义检索资产** | **否** | **query, top_k, category** | **匹配资产列表** | **EmbeddingBackend + FAISS** |
| `place_instance` | 放置新资产 | 是 | asset_id, position, rotation, description | instance_id, position, bbox | SceneState |
| `move_asset` | 移动已有资产 | 是 | instance_id, new_position | old_pos, new_pos | SceneState |
| `delete_asset` | 删除资产 | 是 | instance_id | deleted_id | SceneState |
| `query_scene` | 查询场景状态 | 否 | filters (可选) | 资产列表/统计 | SceneState |
| `check_collision` | 检测碰撞 | 否 | instance_id 或 all | collision_pairs | SceneState (几何) / Isaac Sim |
| `check_support` | 检查支撑关系 | 否 | instance_id | parent, valid | SceneState + 规则 |
| `set_support` | 设置支撑关系 | 是 | child_id, parent_id | relation | SceneState + LLM 决策 |
| `simulate_step` | 运行物理仿真 | 否 | duration_seconds | stable, fallen, contacts | Isaac Sim |

> 注: 原方案中的 `adjust_z` 合并到 `move_asset` 中（通过 `new_position` 的 z 分量实现），减少工具数量。

#### 1.5 工具示例 -- place_instance (`tools/place_instance.py`)

```python
def place_instance(params: dict, scene=None, **kw) -> dict:
    """
    在场景中放置一个新的资产实例。

    params:
      - asset_id: str        资产类别 ID (如 "Conveyor")
      - doc_id: str          具体资产文档 ID (从 retrieve_assets 获取)
      - usd_path: str        USD 模型路径
      - position: [x, y, z]  世界坐标 (米)
      - rotation: [rx,ry,rz] 欧拉角 (度), 可选
      - bbox: [w, l, h]      包围盒尺寸, 可选
      - description: str     语义描述, 可选
    """
    asset_id = params["asset_id"]
    position = tuple(params["position"])
    rotation = tuple(params.get("rotation", [0, 0, 0]))
    bbox = tuple(params.get("bbox", [1.0, 1.0, 1.0]))
    usd_path = params.get("usd_path", "")
    description = params.get("description", "")

    instance_id = scene.generate_instance_id(asset_id)

    placed = PlacedAsset(
        instance_id=instance_id,
        asset_id=asset_id,
        usd_path=usd_path,
        position=position,
        rotation=rotation,
        bbox=bbox,
        description=description,
    )
    scene.add_asset(placed)

    return {
        "instance_id": instance_id,
        "position": list(position),
        "bbox": list(bbox),
    }
```

#### 1.6 需修改的现有文件

**`llm_planner.py`** -- Prompt 模板重写：

```python
# 现有 prompt (单次输出全部放置)
_PROMPT_TEMPLATE = """你是一名工业场景布局规划助手...请只输出JSON数组..."""

# 改为 ReAct 格式 prompt (每次输出一个 thought + 一个 action)
_REACT_PROMPT_TEMPLATE = """你是一名工业场景布局规划助手，使用工具逐步构建场景。

## 可用工具
{tools_description}

## 资产库概况
{catalog_summary}

## 当前场景状态
{scene_state}

## 上一步观测结果
{last_observation}

## 历史教训
{lessons_learned}

## 用户需求
{command}

## 工作记忆 (已检索到的资产)
{retrieved_assets}

请按以下 JSON 格式输出你的下一步决策:
{{
  "thought": "你的推理过程（中文）",
  "action": "工具名称",
  "action_input": {{参数字典}}
}}

当你认为场景已完成时，输出:
{{
  "thought": "场景已满足所有需求",
  "action": "finish",
  "action_input": {{}}
}}
"""
```

> 注意: prompt 中新增了 `catalog_summary`（热启动上下文）和 `retrieved_assets`（Agent 工作记忆中已检索到的资产），替代了原来固定注入的资产列表。

---

### 阶段 2：场景状态管理 + 观测系统

**目标**：建立可变的运行时场景状态，每步行动后生成标准化观测报告。

#### 2.1 新增文件

```
scene_layout_rag/
├── scene_state.py        # 可变场景状态管理
├── observer.py           # 观测器 (验证 + 语义分析 + 建议)
├── validators.py         # 碰撞检测 / 支撑验证 / 规则校验
```

#### 2.2 场景状态管理 (`scene_state.py`)

```python
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

@dataclass
class PlacedAsset:
    """已放置资产的运行时记录"""
    instance_id: str                          # "Conveyor_1"
    asset_id: str                             # "Conveyor"
    usd_path: str
    position: Tuple[float, float, float]
    rotation: Tuple[float, float, float] = (0, 0, 0)
    bbox: Tuple[float, float, float] = (1.0, 1.0, 1.0)  # 长宽高
    description: str = ""
    support_parent: Optional[str] = None      # 被谁支撑
    support_children: List[str] = field(default_factory=list)  # 支撑了谁


class SceneState:
    """可变场景状态 -- ReAct 循环的核心数据结构"""

    def __init__(self, bounds: Tuple[float, float, float] = (20.0, 30.0, 10.0)):
        self.bounds = bounds                  # 场景尺寸 (宽, 长, 高)
        self.assets: Dict[str, PlacedAsset] = {}
        self._id_counters: Dict[str, int] = {}

    def generate_instance_id(self, asset_id: str) -> str:
        self._id_counters[asset_id] = self._id_counters.get(asset_id, 0) + 1
        return f"{asset_id}_{self._id_counters[asset_id]}"

    def add_asset(self, asset: PlacedAsset) -> None: ...
    def remove_asset(self, instance_id: str) -> PlacedAsset: ...
    def move_asset(self, instance_id: str, new_pos) -> None: ...
    def get_asset(self, instance_id: str) -> Optional[PlacedAsset]: ...
    def set_support(self, child_id: str, parent_id: str) -> None: ...

    def to_dict(self) -> dict:
        """序列化为字典，供 LLM prompt 注入"""
        return {
            "bounds": list(self.bounds),
            "asset_count": len(self.assets),
            "assets": [
                {
                    "instance_id": a.instance_id,
                    "asset_id": a.asset_id,
                    "position": list(a.position),
                    "bbox": list(a.bbox),
                    "support_parent": a.support_parent,
                }
                for a in self.assets.values()
            ],
        }

    def to_layout_json(self) -> list:
        """导出为 scene.py 可加载的 JSON 格式"""
        return [
            {
                "asset_id": a.asset_id,
                "usd_path": a.usd_path,
                "position": list(a.position),
                "rotation": list(a.rotation),
                "scale": [0.01, 0.01, 0.01],
            }
            for a in self.assets.values()
        ]
```

#### 2.3 观测系统 (`observer.py`)

```python
class SceneObserver:
    """每步行动后生成标准化观测报告"""

    def __init__(self, physics_enabled: bool = False):
        self.physics_enabled = physics_enabled
        self._validators = SceneValidators()

    def observe(self, scene: SceneState) -> dict:
        """对修改了场景的 action 生成完整观测"""
        validation = self._validators.validate_all(scene)
        return {
            "validation": validation,
            "scene_semantics": self._analyze_semantics(scene),
            "support_state": self._check_supports(scene),
            "physics_feedback": self._physics_feedback(scene),
            "suggestions": self._generate_suggestions(scene, validation),
        }

    def observe_retrieval(self, retrieval_result: dict) -> dict:
        """对 retrieve_assets 结果生成轻量观测"""
        return {
            "type": "retrieval",
            "query": retrieval_result["query"],
            "found": retrieval_result["count"],
            "assets_summary": [
                f"{a['asset_id']} (bbox={a['bbox']}, score={a['score']})"
                for a in retrieval_result.get("assets", [])[:5]
            ],
        }
```

#### 2.4 观测数据结构定义

```python
# 修改场景的 action 的完整观测格式
observation = {
    "validation": {
        "ok": True/False,
        "collisions": [
            {"a": "Conveyor_1", "b": "Rack_1", "overlap": 0.3}
        ],
        "out_of_bounds": ["Box_3"],
    },
    "scene_semantics": {
        "corridors": [
            {"from": "WorkZone_A", "to": "WorkZone_B", "width": 2.0, "blocked": False}
        ],
        "work_zones": [
            {"center": [3.0, 2.0, 0], "assets": ["Workbench_1", "Robot_1"], "type": "assembly"}
        ],
        "flow_paths": [
            {"type": "conveyor_chain", "segments": ["Conveyor_1", "Conveyor_2"], "connected": True}
        ],
    },
    "support_state": {
        "valid_relations": [
            {"child": "Box_1", "parent": "Conveyor_1", "contact_ratio": 0.85}
        ],
        "invalid_relations": [
            {"child": "Box_2", "issue": "outside_parent_bbox", "parent": "Rack_1"}
        ],
    },
    "physics_feedback": {
        "stable": True,
        "contacts": [{"a": "Box_1", "b": "Conveyor_1", "force": 9.8}],
        "fallen_assets": [],
        "warnings": ["Box_1 slightly tilted (2.3 degrees)"],
    },
    "suggestions": [
        "Conveyor_1 和 Rack_2 之间间距不足，AGV 无法通过，建议增加 1.5m",
    ],
}
```

#### 2.5 碰撞检测器 (`validators.py`)

```python
class SceneValidators:
    def validate_all(self, scene: SceneState) -> dict:
        collisions = self._check_aabb_collisions(scene)
        oob = self._check_out_of_bounds(scene)
        return {
            "ok": len(collisions) == 0 and len(oob) == 0,
            "collisions": collisions,
            "out_of_bounds": oob,
        }

    def _check_aabb_collisions(self, scene: SceneState) -> list:
        """AABB 轴对齐包围盒两两碰撞检测"""
        ...

    def _check_out_of_bounds(self, scene: SceneState) -> list:
        """检测资产是否超出场景边界"""
        ...

    def validate_support(self, child_id, parent_id, scene) -> dict:
        """验证支撑关系的几何合理性"""
        ...
```

---

### 阶段 3：ReAct 主循环 + 反思机制

**目标**：将单次管线改为 Think → Act → Observe → Reflect 迭代循环。

#### 3.1 新增文件

```
scene_layout_rag/
├── react_agent.py          # ReAct 主循环控制器
├── prompts/
│   ├── __init__.py
│   ├── think.py            # 推理阶段 prompt 模板
│   ├── reflect.py          # 反思阶段 prompt 模板
│   └── strategy.py         # 策略调整 prompt 模板
```

#### 3.2 ReAct Agent 核心实现 (`react_agent.py`)

```python
class ReActAgent:
    """ReAct 主循环控制器 -- 系统核心"""

    def __init__(self, llm, tool_registry, observer, vector_store, embedder, config):
        self.llm = llm
        self.tools = tool_registry
        self.observer = observer
        self.vector_store = vector_store   # FAISS 向量库 (供 retrieve_assets 使用)
        self.embedder = embedder           # 嵌入模型 (供 retrieve_assets 使用)
        self.max_steps = config.max_steps
        self.lessons_learned: List[dict] = []
        self.retrieved_assets: List[dict] = []  # Agent 工作记忆：已检索到的资产
        self.history: List[dict] = []

    def run(self, command: str, catalog_summary: dict) -> SceneState:
        """执行 ReAct 循环"""
        scene = SceneState(bounds=(20.0, 30.0, 10.0))
        last_observation = {"validation": {"ok": True}, "suggestions": []}
        strategy = None

        for step in range(self.max_steps):
            # ── Step 1: 推理 ──
            context = self._build_context(
                command, catalog_summary, scene,
                last_observation, strategy
            )
            llm_output = self.llm.think_and_decide(context)
            thought = llm_output["thought"]
            action = llm_output["action"]
            action_input = llm_output["action_input"]

            # ── 终止判断 ──
            if action == "finish":
                break

            # ── Step 2: 行动 ──
            result = self.tools.execute(
                action, action_input,
                scene=scene,
                vector_store=self.vector_store,
                embedder=self.embedder,
            )

            # 若是检索，将结果存入工作记忆
            if action == "retrieve_assets" and result["ok"]:
                self._update_working_memory(result["result"])

            # ── Step 3: 观测 ──
            if self.tools.is_scene_modifier(action):
                observation = self.observer.observe(scene)
            else:
                observation = self.observer.observe_retrieval(result.get("result", {}))
            last_observation = observation

            # ── Step 4: 反思 (仅场景修改 action 且异常时) ──
            if (self.tools.is_scene_modifier(action)
                    and not observation.get("validation", {}).get("ok", True)):
                reflection = self.llm.reflect(
                    thought=thought, action=action,
                    action_input=action_input, observation=observation,
                )
                self.lessons_learned.append({
                    "step": step,
                    "situation": f"{action}({action_input})",
                    "mistake": reflection["mistake"],
                    "correction": reflection["correction"],
                })
                if self._needs_strategy_change(step):
                    strategy = self.llm.adjust_strategy(
                        command, self.lessons_learned, observation
                    )

            self.history.append({
                "step": step, "thought": thought,
                "action": action, "action_input": action_input,
                "result_ok": result.get("ok"), 
                "observation_ok": observation.get("validation", {}).get("ok", True),
            })

        return scene

    def _build_context(self, command, catalog_summary, scene,
                       observation, strategy) -> dict:
        return {
            "command": command,
            "catalog_summary": catalog_summary,
            "tools_description": self.tools.generate_tools_prompt(),
            "scene_state": scene.to_dict(),
            "last_observation": observation,
            "lessons_learned": self.lessons_learned[-5:],
            "strategy": strategy,
            "retrieved_assets": self.retrieved_assets[-15:],  # 工作记忆
        }

    def _update_working_memory(self, retrieval_result: dict):
        """将新检索到的资产加入工作记忆（去重）"""
        existing_ids = {a["doc_id"] for a in self.retrieved_assets}
        for asset in retrieval_result.get("assets", []):
            if asset["doc_id"] not in existing_ids:
                self.retrieved_assets.append(asset)
                existing_ids.add(asset["doc_id"])

    def _needs_strategy_change(self, current_step: int) -> bool:
        recent = self.history[-3:]
        fail_count = sum(1 for h in recent if not h.get("observation_ok", True))
        return fail_count >= 2
```

#### 3.3 LLM 接口改造

对现有 `llm_planner.py` 的 `LLMPlanner` 类新增方法：

| 方法 | 输入 | 输出 | Prompt 来源 |
|------|------|------|-------------|
| `think_and_decide(context)` | 完整上下文 dict | `{"thought", "action", "action_input"}` | `prompts/think.py` |
| `reflect(thought, action, observation)` | 单步信息 | `{"mistake", "correction"}` | `prompts/reflect.py` |
| `adjust_strategy(command, lessons, obs)` | 宏观信息 | 策略文本 | `prompts/strategy.py` |
| `decide_support(child, candidates, context)` | 支撑候选 | `{"parent", "confidence", "reason"}` | 内联 prompt |

#### 3.4 反思 Prompt 模板 (`prompts/reflect.py`)

```python
REFLECT_PROMPT = """你是一名场景布局专家，正在分析上一步操作的失败原因。

## 你的推理
{thought}

## 你执行的操作
工具: {action}
参数: {action_input}

## 观测结果
{observation}

请分析失败原因并总结经验教训，输出 JSON:
{{
  "mistake": "具体错误描述",
  "root_cause": "根本原因分析",
  "correction": "下次应该怎么做"
}}
"""
```

#### 3.5 对 `rag.py` 的改造

```python
class SceneLayoutRAG:
    def generate_layout(self, command_text: str) -> LayoutPlan:
        # Step 1: 初始化向量索引 (保留现有逻辑)
        self._ensure_index()

        # Step 2: 构建资产库摘要 (热启动上下文)
        catalog_summary = self._build_catalog_summary()

        # Step 3: 构建 ReAct Agent
        agent = ReActAgent(
            llm=self._get_planner(),
            tool_registry=self._build_tool_registry(),
            observer=SceneObserver(physics_enabled=self.config.agent.physics_enabled),
            vector_store=self._index,       # ← 传入向量库供 retrieve_assets 使用
            embedder=self._embedder,        # ← 传入嵌入模型
            config=self.config.agent,
        )

        # Step 4: 运行 ReAct 循环 (Agent 内部按需调用 retrieve_assets)
        final_scene = agent.run(command_text, catalog_summary)

        # Step 5: 转换为 LayoutPlan (兼容现有输出)
        return self._scene_to_layout_plan(command_text, final_scene)

    def _build_catalog_summary(self) -> dict:
        """构建资产库摘要，作为热启动上下文"""
        categories = {}
        for doc in self._documents:
            cat = doc.metadata.get("asset_category", "unknown")
            categories[cat] = categories.get(cat, 0) + 1
        return {
            "available_categories": list(categories.keys()),
            "category_counts": categories,
            "total_assets": len(self._documents),
        }
```

---

### 阶段 4：LLM 参与支撑关系决策

**目标**：支撑关系由 LLM 语义推理 + 规则几何验证协同决定。

#### 4.1 设计流程

```
                    ┌─────────────┐
                    │ LLM 语义推理 │  "Box 应该放在 Conveyor 上进行分拣"
                    └──────┬──────┘
                           │ 候选支撑关系
                           ▼
                    ┌─────────────┐
                    │ 规则几何验证 │  检查 bbox 重叠、高度差、承重
                    └──────┬──────┘
                           │
                    ┌──────┴──────┐
                    │ 验证通过？   │
                    ├─ 是 → 应用   │
                    └─ 否 → LLM   ─→ 重新推理 (带失败反馈)
                           再决策
```

#### 4.2 `set_support` 工具内部流程

```python
def set_support_tool(params, scene, llm, **kw):
    child_id = params["child_id"]

    # Step 1: 找候选父物体
    candidates = find_support_candidates(child_id, scene)

    # Step 2: LLM 决策
    decision = llm.decide_support(
        child=child_id, candidates=candidates, context=scene.to_dict()
    )

    # Step 3: 规则验证
    validation = validate_support_geometry(child_id, decision["parent"], scene)

    # Step 4: 失败 → LLM 重新决策 (最多2次)
    retries = 0
    while not validation["ok"] and retries < 2:
        decision = llm.reconsider_support(
            previous=decision, feedback=validation, candidates=candidates
        )
        validation = validate_support_geometry(child_id, decision["parent"], scene)
        retries += 1

    if validation["ok"]:
        scene.set_support(child_id, decision["parent"])

    return {"ok": validation["ok"], "child": child_id, "parent": decision["parent"]}
```

#### 4.3 支撑验证规则

| 规则 | 检查内容 | 阈值 |
|------|----------|------|
| XY 重叠率 | child 底面投影在 parent 顶面内的比例 | >= 60% |
| Z 高度差 | child 底面 - parent 顶面 | <= 0.05m |
| 尺寸比 | child 面积 / parent 面积 | <= 1.5 |
| 承重类型 | parent 是否为承载类 (Conveyor, Rack, Workbench, Pallet) | 白名单 |

---

### 阶段 5：物理仿真接入

**目标**：将 Isaac Sim 物理引擎接入观测环节。

#### 5.1 架构

Isaac Sim 作为独立常驻服务，Agent 通过 API 调用：

```
┌─────────────────┐         ┌──────────────────────┐
│  ReAct Agent    │  gRPC/  │  Isaac Sim Service   │
│  (主进程)       │ ◄─────► │  (GPU Worker 进程)    │
│                 │  REST   │                      │
│  observe() ─────┼────────►│  load_scene()        │
│  ◄──────────────┼─────────│  simulate(5s)        │
│  physics_fb     │         │  get_contacts()      │
└─────────────────┘         └──────────────────────┘
```

#### 5.2 仿真接口

```python
class PhysicsSimulator:
    def load_scene(self, scene: SceneState) -> None: ...
    def simulate(self, duration: float = 5.0) -> None: ...
    def get_feedback(self) -> dict:
        return {
            "stable": bool,
            "stable_assets": [...],
            "fallen_assets": [...],
            "contacts": [{"a": str, "b": str, "point": [...], "force": float}],
            "warnings": [...],
        }
```

#### 5.3 降级策略

当 Isaac Sim 不可用时，系统在纯几何模式下运行：

| 功能 | Isaac Sim 模式 | 几何降级模式 |
|------|---------------|-------------|
| 碰撞检测 | 精确网格碰撞 | AABB 包围盒重叠 |
| 稳定性 | 物理仿真 (重力+接触) | 重心是否在支撑面内 |
| 接触点 | 仿真接触力 | 估算接触面积 |
| 掉落检测 | 仿真后位置变化 | 无支撑则标记不稳定 |

---

## 六、工作流（端到端）

### 6.1 完整执行流程

```
用户输入: "规划一个分拣中心，包含3条传送带、2个货架、1个工作台和1辆AGV"
                │
                ▼
    ┌───────────────────────────┐
    │  Agent 初始化              │
    │  - 加载 FAISS 向量索引    │  (离线已构建，一次性加载)
    │  - 注册 10 个工具          │  (含 retrieve_assets)
    │  - 构建资产库摘要          │  {categories: [AGV, Box, ...], counts: {...}}
    │  - 初始化空 SceneState    │
    └─────────────┬─────────────┘
                  │
                  ▼
    ┌─────────────────────────────────────────────────────────┐
    │  Step 0:                                                │
    │  Think: "用户需要传送带、货架等，先检索传送带资产"        │
    │  Act:   retrieve_assets(query="分拣用传送带")           │
    │  Obs:   找到 5 个传送带资产，已存入工作记忆              │
    └─────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌─────────────────────────────────────────────────────────┐
    │  Step 1:                                                │
    │  Think: "Conveyor_A (2.1m) 适合作为主分拣线，放在中心"  │
    │  Act:   place_instance(asset_id="Conveyor_A", pos=[0,0,0]) │
    │  Obs:   ok=True, no collision                           │
    └─────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌─────────────────────────────────────────────────────────┐
    │  Step 2:                                                │
    │  Think: "第2条传送带应平行放置，间距留AGV通道"           │
    │  Act:   place_instance(asset_id="Conveyor_B", pos=[4,0,0]) │
    │  Obs:   ok=True, corridor_width=4.0                     │
    └─────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌─────────────────────────────────────────────────────────┐
    │  Step 3:                                                │
    │  Think: "需要货架，还没检索过，先搜索"                   │
    │  Act:   retrieve_assets(query="仓储货架，适合分拣中心")  │
    │  Obs:   找到 4 个货架资产，已存入工作记忆                │
    └─────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌─────────────────────────────────────────────────────────┐
    │  Step 7:                                                │
    │  Think: "在传送带末端放Box，需要合适尺寸的"              │
    │  Act:   retrieve_assets(query="小型周转箱，适合放在2m传送带上") │
    │  Obs:   找到 Box_C (0.3×0.3×0.2m)，适配                │
    │                                                         │
    │  ← 注意：这个检索查询包含了当前场景约束（2m传送带），    │
    │     这在前置RAG方案中是做不到的                          │
    └─────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌─────────────────────────────────────────────────────────┐
    │  Step 8:                                                │
    │  Think: "把 Box 放在 Conveyor_1 上面"                   │
    │  Act:   place_instance(Box_C, pos=[0, 0, 0.5])         │
    │  Obs:   ok=False, collision!                            │
    │  Reflect: "没查 Conveyor 高度就放了，应先 query_scene"   │
    │  Lesson: "放置承载物前，先查询父物体精确尺寸"            │
    └─────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌─────────────────────────────────────────────────────────┐
    │  Step 9:                                                │
    │  Think: "根据教训，先查询 Conveyor_1 的尺寸"            │
    │  Act:   query_scene(instance_id="Conveyor_1")          │
    │  Obs:   bbox=[2.1, 0.6, 0.8], top_z=0.8               │
    └─────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌─────────────────────────────────────────────────────────┐
    │  Step 10:                                               │
    │  Think: "Conveyor 顶面 z=0.8，Box 放在 z=0.8"          │
    │  Act:   place_instance(Box_C, pos=[0, 0, 0.8])         │
    │  Act:   set_support(child=Box_1, parent=Conveyor_1)    │
    │  Obs:   ok=True, support_valid=True                    │
    └─────────────────────────────────────────────────────────┘
                  │
                  ▼
               ...继续迭代...
                  │
                  ▼
    ┌─────────────────────────────────────────────────────────┐
    │  Step 18:                                               │
    │  Think: "所有需求的资产已放置完毕，布局合理"             │
    │  Act:   finish                                         │
    └─────────────────────────────────────────────────────────┘
                  │
                  ▼
    ┌───────────────────────┐
    │  输出                  │
    │  - layout.json        │  → scene.py 加载到 Isaac Sim
    │  - agent_trace.json   │  → 完整执行轨迹 (含每步的检索/放置/反思)
    └───────────────────────┘
```

### 6.2 数据流图

```
                    ┌─────────────┐
                    │ CSV 资产库   │ ── 离线预处理 ──→ ┌─────────────┐
                    │ MD 场景描述  │                    │ FAISS 向量库│
                    └─────────────┘                    └──────┬──────┘
                                                              │
┌──────────┐                                                  │
│ 用户指令  │ ─────────────────────────────┐                   │
└──────────┘                               │                   │
                                           ▼                   │
                              ┌────────────────────────┐       │
                              │    ReAct Agent 主循环   │       │
                              │                        │       │
                              │  Think ──→ Act ──→ Obs │       │
                              │    ↑                │   │       │
                              │    └── Reflect ◄────┘   │       │
                              │                        │       │
                              │  工具:                  │       │
                              │  ┌──────────────────┐  │       │
                              │  │ retrieve_assets  │◄─┼───────┘
                              │  │ (调用 FAISS 检索) │  │  按需调用
                              │  └──────────────────┘  │
                              │  ┌──────────────────┐  │
                              │  │ place / move /   │  │
                              │  │ delete / query   │──┼──→ SceneState
                              │  └──────────────────┘  │
                              │  ┌──────────────────┐  │
                              │  │ simulate_step    │──┼──→ Isaac Sim (可选)
                              │  └──────────────────┘  │
                              └────────────┬───────────┘
                                           │
                                           ▼
                              ┌────────────────────────┐
                              │  layout.json           │ → 3D 场景
                              │  agent_trace.json      │ → 可复现轨迹
                              └────────────────────────┘
```

---

## 七、代码重构方案

### 7.1 文件变更总览

```
scene_layout_rag/
├── __init__.py              # [改] 新增导出
├── config.py                # [改] 新增 AgentConfig
├── data_models.py           # [改] 新增 ActionRecord, Lesson 等
├── rag.py                   # [改] generate_layout() 接入 ReActAgent
├── llm_planner.py           # [改] 新增 think_and_decide / reflect 等方法
├── cli.py                   # [改] 适配新输出格式
│
├── scene_state.py           # [新] 可变场景状态
├── react_agent.py           # [新] ReAct 主循环
├── observer.py              # [新] 观测器
├── validators.py            # [新] 碰撞/支撑/边界验证
│
├── tools/                   # [新] 工具模块
│   ├── __init__.py
│   ├── base.py              # ToolSpec + ToolRegistry
│   ├── retrieve_assets.py   # ★ RAG 检索工具
│   ├── place_instance.py
│   ├── move_asset.py
│   ├── delete_asset.py
│   ├── query_scene.py
│   ├── check_collision.py
│   ├── check_support.py
│   ├── set_support.py
│   └── simulate_step.py
│
├── prompts/                 # [新] Prompt 模板
│   ├── __init__.py
│   ├── think.py
│   ├── reflect.py
│   └── strategy.py
│
├── physics/                 # [新] 物理仿真接口 (阶段5)
│   ├── __init__.py
│   ├── simulator.py
│   └── geometric.py         # 几何降级计算
│
│  --- 以下保持不变 ---
├── asset_loader.py          # 保留: CSV/MD → AssetDocument
├── embedding.py             # 保留: SentenceTransformer 嵌入
├── layout_reasoner.py       # 保留: 作为降级回退
├── text_splitter.py         # 保留: 文档切分
└── vector_store.py          # 保留: FAISS 索引 (现在被 retrieve_assets 工具调用)
```

### 7.2 配置扩展 (`config.py` 新增)

```python
@dataclass
class AgentConfig:
    """ReAct Agent 配置"""
    max_steps: int = 20
    reflection_enabled: bool = True
    strategy_adjust_enabled: bool = True
    max_lessons: int = 10
    max_working_memory: int = 15        # retrieve_assets 工作记忆最大条目
    physics_enabled: bool = False
    physics_sim_duration: float = 2.0
    collision_method: str = "aabb"      # "aabb" | "isaac"
    warm_start: bool = True             # 是否提供资产库摘要作为热启动


@dataclass
class ProjectConfig:
    asset_paths: AssetPaths = field(default_factory=AssetPaths)
    model: ModelConfig = field(default_factory=ModelConfig)
    agent: AgentConfig = field(default_factory=AgentConfig)  # ← 新增
    index_dir: Path = _DEFAULT_PROJECT_ROOT / "data" / "indexes"
    chunk_size: int = 512
    chunk_overlap: int = 64
    language: str = "zh"
```

### 7.3 数据结构扩展 (`data_models.py` 新增)

```python
@dataclass
class ActionRecord:
    """单步行动记录"""
    step: int
    thought: str
    action: str
    action_input: Dict[str, Any]
    result: Dict[str, Any]
    observation_ok: bool

@dataclass
class Lesson:
    """反思教训"""
    step: int
    situation: str
    mistake: str
    correction: str

@dataclass
class AgentTrace:
    """Agent 完整执行轨迹"""
    command: str
    steps: List[ActionRecord]
    lessons: List[Lesson]
    final_observation: Dict[str, Any]
    total_steps: int
    success: bool
```

---

## 八、预期效果

### 8.1 定性对比

| 维度 | 现有系统 | 重构后系统 |
|------|----------|-----------|
| 检索方式 | 一次性前置，固定资产集 | Agent 按需检索，带场景上下文 |
| 布局方式 | 单次 LLM 生成全部位置 | 逐步放置 + 迭代修正 |
| 碰撞处理 | 无 | AABB 检测 + Isaac Sim 验证 |
| 支撑关系 | 无 | LLM 语义推理 + 几何规则验证 |
| 物理合理性 | 不保证 | 仿真验证稳定性 |
| 错误修正 | 不可能 | 反思机制自动修正 |
| 动作空间 | 仅放置 | 检索/放置/移动/删除/查询/仿真 10 种工具 |
| 可解释性 | reason 字段 | 完整 thought + lesson 轨迹 |

### 8.2 定量评估指标

| 指标 | 定义 | 评估方式 |
|------|------|----------|
| 碰撞率 | 最终布局碰撞对数 / 总资产对数 | AABB 自动检测 |
| 支撑合理率 | 合理支撑数 / 总支撑数 | 规则验证 |
| 物理稳定率 | 仿真后保持原位数 / 总资产数 | Isaac Sim 5s 仿真 |
| 指令满足率 | 实际放置资产数 / 要求总数 | 自动统计 |
| 检索精准率 | 最终使用的资产 / 总检索资产 | trace 统计 |
| 迭代收敛步数 | 达到全部验证通过所需步数 | trace 统计 |
| 反思有效率 | 反思后下一步成功率 | 对比反思前后 |

### 8.3 消融实验设计

| 实验 | 配置 | 验证假设 |
|------|------|----------|
| Baseline | 现有单次生成 | 基线对照 |
| +ReAct (RAG前置) | ReAct 循环，但 RAG 仍前置 | 迭代优于单次 |
| +ReAct (RAG工具化) | ReAct 循环，RAG 作为工具 | 按需检索优于前置检索 |
| +Reflect | ReAct + RAG工具化 + 反思 | 反思提高修正效率 |
| +Physics | 全部 + 物理仿真 | 物理反馈提高合理性 |
| -Support LLM | 全部但支撑用纯规则 | LLM 支撑推理的价值 |

---

## 九、实施计划

### 9.1 里程碑

| 阶段 | 内容 | 交付物 | 前置依赖 |
|------|------|--------|----------|
| **P1** | 工具层 + RAG 工具化 | `tools/` 模块，10 个工具实现，`retrieve_assets` 封装 | 无 |
| **P2** | 场景状态 + 观测 | `scene_state.py`, `observer.py`, `validators.py` | P1 |
| **P3** | ReAct 主循环 + 反思 | `react_agent.py`, `prompts/`, `rag.py` 改造 | P1 + P2 |
| **P4** | LLM 支撑决策 | `set_support` 工具增强 | P3 |
| **P5** | 物理仿真接入 | `physics/` 模块，Isaac Sim 服务 | P3 |
| **P6** | 评估与调优 | 评估脚本，消融实验结果 | P3-P5 |

### 9.2 最小可验证产品 (MVP)

完成 **P1 + P2 + P3** 后即可获得可运行的 ReAct 系统：

- 工具: `retrieve_assets` + `place_instance` + `move_asset` + `delete_asset` + `query_scene` 5 个核心工具
- 观测: AABB 碰撞检测 + 越界检测
- 循环: Think → Act(含检索) → Observe → Reflect 完整闭环
- 物理: 几何降级模式（不依赖 Isaac Sim）

**验证命令**:

```bash
python -m scene_layout_rag.cli "规划一个分拣中心" --mode react --max-steps 20 --verbose
```

---

## 十、关键技术决策

| 决策点 | 选择 | 理由 |
|--------|------|------|
| **RAG 与 ReAct 关系** | **RAG 作为 ReAct 内部工具** | Agent 按需检索更精确，符合 ReAct 范式，避免固定资产集的局限 |
| 热启动 | 提供资产库摘要而非具体资产 | 让 Agent 知道有什么可检索，但不预设检索结果 |
| LLM 输出格式 | 每步一个 `{thought, action, action_input}` | 可控，便于逐步验证 |
| 碰撞检测首选 | AABB 几何检测 | 快速、无依赖，Isaac Sim 作为增强 |
| Isaac Sim 架构 | 独立服务进程 | 避免在 Agent 循环中反复加载 |
| 反思触发条件 | observation 异常时 | 仅在需要时反思，降低 LLM 调用成本 |
| 策略调整触发 | 连续 2 步以上失败 | 避免频繁调整导致策略振荡 |
| 教训记忆窗口 | 最近 5 条 | 控制 prompt 长度 |
| 检索工作记忆 | 最近 15 条资产 | 避免 prompt 过长，保留足够选择 |

---

## 十一、风险与应对

| 风险 | 影响 | 应对措施 |
|------|------|----------|
| LLM 频繁调用 retrieve_assets | 步数浪费在检索上 | 热启动摘要减少盲目检索；限制连续检索次数 |
| LLM 输出格式不稳定 | 工具调用解析失败 | 严格 JSON Schema + 重试 + 结构化输出 |
| ReAct 循环不收敛 | 达到 max_steps 仍未完成 | 保底策略：超时输出当前最佳状态 |
| Isaac Sim 启动慢 | 每步仿真延迟大 | 预加载 + 持久进程 + 降级模式 |
| 工作记忆溢出 | 检索过多资产撑满 prompt | 限制 15 条 + LRU 淘汰旧资产 |
| 场景状态同步 | SceneState 与 Isaac Sim 不一致 | 仿真前全量同步 |
