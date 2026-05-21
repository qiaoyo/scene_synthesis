# Code Review and Framework Review

审查日期：2026-05-21

审查范围：`scene_layout_react` 主框架、工具系统、RAG、Isaac 物理桥接、测试目录、数据处理脚本、依赖和仓库结构。

结论：当前状态不建议继续合入新功能或作为稳定框架使用。代码仍处于研究原型阶段，主流程、物理链路、测试体系和导入边界都有会阻断运行的确定性问题。优先级最高的是让最小端到端流程可复现，然后再做物理能力和工具能力扩展。

## 验证结果

只读验证命令和结果：

- `PYTHONDONTWRITEBYTECODE=1 pytest --collect-only -p no:cacheprovider -q`
  - 失败：`pytest: command not found`
- `PYTHONDONTWRITEBYTECODE=1 python -c "import scene_layout_react; print('ok')"`
  - 失败：`ModuleNotFoundError: No module named 'openai'`
- 注入假 `openai` 后再导入
  - 失败：`ModuleNotFoundError: No module named 'faiss'`
- 同时注入假 `openai`、`faiss`、`sentence_transformers` 后
  - 工具注册表可得到 9 个工具：`check_collision`、`check_support`、`delete_asset`、`move_asset`、`place_instance`、`query_scene`、`retrieve_tool`、`set_support`、`simulate_step`

这说明当前导入边界过重：导入包本身就依赖 OpenAI、FAISS、SentenceTransformer 等运行时重依赖。

## Blocking Issues

### 1. 包级导入被重依赖阻断

位置：

- `scene_layout_react/__init__.py:9`
- `scene_layout_react/react_agent.py:6`
- `scene_layout_react/llm_planner.py:5`
- `scene_layout_react/tools/base.py:6`
- `scene_layout_react/rag.py:6-8`

问题：

`import scene_layout_react` 会立刻导入 `ReActAgent`，再导入 `OpenAI`、`ToolContext`、`AssetRAG`，最终要求 `openai`、`faiss`、`sentence_transformers` 都已安装。结果是用户无法只导入 `ProjectConfig`、`AssetDocument` 或普通数据模型。

影响：

- 基础单元测试无法独立跑。
- 工具 schema、配置、数据模型都被 GPU/LLM/RAG 依赖绑死。
- 新环境很难定位真实缺失依赖，因为导入链太深。

建议：

- `__init__.py` 只导出轻量对象，或使用 lazy import。
- `ToolContext.rag` 使用 `Any`、`Protocol` 或 `typing.TYPE_CHECKING`，避免 `tools.base` 运行时导入 `AssetRAG`。
- 将 OpenAI、FAISS、SentenceTransformer 放进可选 extras，例如 `pip install .[rag,llm,physics]`。

### 2. 默认索引构建路径不可复现

位置：

- `scene_layout_react/config.py:12-13`
- `scene_layout_react/asset_loader.py:128-139`
- `scene_layout_react/rag.py:37-92`
- `scripts/run_inference.py:26-29`

问题：

`ProjectConfig.inventory_csvs` 和 `scene_md_files` 默认都是空列表。如果 `data/indexes/corpus.jsonl` 不存在，`run_inference.py` 会直接 `rag.build(save=True)`，但 build 不会自动扫描 `data/assets/csv` 和 `data/assets/md`。

影响：

- 新 clone 或清空索引后可能构建空语料。
- 空语料下仍会加载 embedding model，浪费资源。
- 后续检索会因为没有索引而失败。

建议：

- 选择一种明确策略：
  - 默认自动扫描 `assets_root / "csv"` 和 `assets_root / "md"`。
  - 或者如果输入列表为空，直接 raise 明确错误，不构建空索引。
- 在 `AssetRAG.build()` 中加入 `if not self.documents: raise ValueError(...)`。

### 3. 默认开启物理，但物理 worker 仍会确定性失败

位置：

- `scene_layout_react/config.py:22`
- `scene_layout_react/react_agent.py:42-48`
- `scene_layout_react/observer.py:80-87`
- `scene_layout_react/physics/worker.py:119-124`
- `scene_layout_react/physics/worker.py:269-277`
- `scene_layout_react/physics/worker.py:346-353`
- `scene_layout_react/physics/worker.py:407-416`

问题：

`physics_enabled=True` 是默认值，每一步 observation 都会调用 Isaac。worker 虽然已经补了 `main()`，但仍有多个确定性错误：

- `_build_stage()` 中 `name` 在 `while name in used_names` 前未定义。
- `_open_stage_in_isaac()` 返回 `(stage, context.get_stage())` 元组，但 `_dispatch()` 把它当作 stage 使用。
- `_apply_rigid_body_and_colliders()` 使用 `UsdGeom`，但只导入了 `UsdPhysics`。
- `_collect_bboxes()` 调用不存在的 `_instance(scene)`，实际函数名是 `_instances(scene)`。
- `_final_positions()` 使用 `Usd.TimeCode.Default()`，但只导入了 `UsdGeom`。
- `_apply_instance_physics()` 从 `request.get("support_children")` 取支撑关系，但支撑关系实际在 `request["scene"]["support_children"]`。

影响：

- 默认端到端运行会持续得到失败 physics feedback。
- `Observer.ok` 会因为物理不 stable 而变成 false，导致 agent 反复反思。
- `check_collision`、`check_support`、`simulate_step` 工具目前不可作为可信能力。

建议：

- 在 worker 修好并有测试前，将 `physics_enabled` 默认改为 false。
- 为 worker 增加不启动 Isaac 的纯函数单元测试：`_instances`、`_collision_pairs`、`_check_support`、request schema。
- 修复 stage 返回值、变量名、导入、support_children 层级。
- 给 `run_isaac_operation()` 增加 worker 路径和 Isaac python 路径预检。

### 4. `place_instance` 会在正常错误路径崩溃

位置：

- `scene_layout_react/tools/place_instance.py:38-43`

问题：

`doc` 只在循环命中时赋值，doc_id 不存在时直接执行 `if doc is None`，会触发 `UnboundLocalError`。

影响：

- LLM 传错 doc_id 或 RAG 返回过期 doc_id 时，工具不会返回设计好的错误，而是被 `Tool.__call__` 捕获为非结构化异常字符串。

建议：

- 初始化 `doc = None`。
- 命中后立即 `break`。
- 给无效 doc_id 写单元测试。

### 5. 同一资产不能重复放置，破坏核心场景合成能力

位置：

- `scene_layout_react/tools/place_instance.py:50-52`
- `scene_layout_react/data_models.py:31-38`

问题：

`place_instance` 使用资产 metadata 里的 `instance_id` 作为场景实例 ID。一个资产文档只能放一次，再放第二个同类对象会返回 `instance_id 已存在`。

影响：

- 用户需求中常见的多个 box、多个 AGV、多个 conveyor 无法用同一个资产生成。
- LLM 会被迫检索多个不同资产文档来绕过 ID 冲突，结果不可控。

建议：

- 场景实例 ID 应由 `SceneStateManager` 生成，例如 `Box_1`、`Box_2`。
- 保留资产原始 ID 到 `asset_doc_id` 或 `source_instance_id`，不要拿它当运行时实例 ID。
- 启用并使用当前未使用的 `_auto_id_counter`。

### 6. RAG 检索 API 有确定性崩溃路径

位置：

- `scene_layout_react/rag.py:177-206`
- `scene_layout_react/config.py:8-40`

问题：

- `doc_type` 类型标注是 `Optional[List[str]]`，实际调用传字符串。
- `top_k=None` 时读取 `self.config.retrieval_top_k`，但 `ProjectConfig` 没有这个字段。
- `doc_type` 不存在时 `index = None`，下一行 `docs = self.documents_by_type[doc_type]` 可能 `KeyError`，或 `index.search` 可能 `AttributeError`。
- `top_k=0` 会被 `top_k or ...` 当作未设置。

影响：

- 公开 API 不稳定。
- LLM 工具参数稍有偏差就会走异常路径。

建议：

- 增加 `retrieval_top_k: int = 5`。
- 将签名改为 `doc_type: Optional[str] = None` 或明确支持 `Sequence[str]`。
- 对未知 doc_type 返回空结果或明确 `ValueError`。
- 使用 `k = self.config.retrieval_top_k if top_k is None else top_k`。

### 7. 测试目录当前不可作为质量门禁

位置：

- `scene_layout_react/test/test_tool_schema.py:5`
- `scene_layout_react/test/test_tool_schema.py:50-57`
- `scene_layout_react/test/test_tool_use.py:22-67`
- `scene_layout_react/test/test_tool_place.py:20-81`
- `scene_layout_react/test/test_tool_state.py:23-89`
- `scene_layout_react/test/test_physics_tools.py:48-158`

问题：

- 当前环境没有 `pytest`。
- 多个 `test_*.py` 在模块顶层创建 OpenAI client 或发起 LLM 请求。
- 测试引用不存在的 `list_openai_tools`、`get_tool_function_spec`、`make_openai_tool_schema`、`_local_tool_system_prompt`。
- 部分文件是人工 smoke script，不是可收集测试。

影响：

- 任何 CI 都无法稳定收集测试。
- 测试导入本身会访问外部服务或重依赖。

建议：

- 将 `scene_layout_react/test` 拆成 `tests/` 和 `scripts/smoke/`。
- 单元测试禁止顶层网络调用。
- 用 fake RAG、fake planner、fake physics bridge 测核心逻辑。
- 把 pytest 加入开发依赖，并配置 `pytest.ini` 或 `pyproject.toml`。

## Important Issues

### 8. `set_support` 的描述与实现不一致

位置：

- `scene_layout_react/tools/set_support.py:9-10`
- `scene_layout_react/tools/set_support.py:37-44`

问题：

schema 描述说“also returns geometric validation results”，但实现只登记关系并返回 child/parent。

影响：

LLM 会把未验证的支撑关系当成已验证事实。

建议：

- 要么修改描述为“只登记逻辑关系”。
- 要么在工具内调用 observer 支撑检查或 `check_support`，并返回 `ok`、`z_gap`、`xy_coverage`、`issues`。

### 9. 支撑关系缺少环检测和业务约束

位置：

- `scene_layout_react/scene_state.py:47-60`

问题：

`set_support()` 只禁止 child 等于 parent，但不禁止 A 支撑 B 后 B 再支撑 A，也不禁止多层循环。

影响：

- 可能生成循环 support graph。
- 物理和观察逻辑难以解释循环支撑。

建议：

- 设置 parent 前沿 parent chain 向上遍历，发现 child 即拒绝。
- 将支撑关系抽象为显式 graph 校验。

### 10. 观察器会忽略丢失的支撑关系节点

位置：

- `scene_layout_react/observer.py:136-142`

问题：

如果 `support_children` 中 parent 或 child 不在 `instances`，当前逻辑直接 `continue`，不会把它报告为 invalid relation。

影响：

场景状态被外部构造、加载或异常中断后，损坏关系不会暴露。

建议：

- parent 缺失和 child 缺失都应进入 `invalid_relations`。
- 增加 state integrity check。

### 11. AABB 和物理语义忽略资产本地 bbox center

位置：

- `scene_layout_react/asset_loader.py:56-63`
- `scene_layout_react/tools/place_instance.py:48-60`
- `scene_layout_react/data_models.py:42-48`

问题：

ingestion 计算了 bbox `min`、`max`、`center`，但 `Instance` 只保存 `bbox_size`。`Instance.aabb()` 假设 `position` 是 bbox 中心，而 USD transform 通常是资产 local origin。

影响：

- 碰撞检测、支撑检测、放置高度可能系统性偏移。
- 对 bbox center 不在原点的资产尤其明显。

建议：

- `Instance` 保存 `bbox_min_local`、`bbox_max_local` 或 `bbox_center`。
- world AABB 使用 `position + local_bbox_min/max`，或 ingestion 阶段统一 normalize 资产 origin。

### 12. AABB 碰撞不考虑旋转

位置：

- `scene_layout_react/data_models.py:36`
- `scene_layout_react/data_models.py:42-48`
- `scene_layout_react/observer.py:99-126`

问题：

`rotation_deg` 被保存但 AABB 计算完全忽略旋转。

影响：

旋转后的长条资产、conveyor、rack 等碰撞结果会不可信。

建议：

- 明确声明只支持 axis-aligned assets。
- 或实现 OBB / rotated AABB。
- 或只让 Isaac 作为旋转场景的权威验证，但默认不要同时声称本地 AABB 可靠。

### 13. 观察器跳过 parent-child 碰撞可能掩盖真实穿模

位置：

- `scene_layout_react/observer.py:107-108`

问题：

只要两个实例存在支撑关系，就完全跳过碰撞检查。

影响：

child 和 parent 深度穿透、位置错误时，本地 collision 不会报告，只依赖 support check。

建议：

- 对支撑关系使用“允许接触但不允许大体积重叠”的特殊判定。
- support check 应同时报告 penetration depth。

### 14. Observer 与 worker 的 `z_gap` 符号不一致

位置：

- `scene_layout_react/observer.py:150`
- `scene_layout_react/physics/worker.py:319`

问题：

Observer 用 `child_min_z - parent_max_z`，worker 用 `parent_max_z - child_min_z`。

影响：

两个后端返回同名字段但符号相反，LLM 和调用方无法稳定解释。

建议：

- 统一定义：建议 `z_gap = child_bottom_z - parent_top_z`。
- 正数表示悬空，负数表示穿透。

### 15. Agent 对 planner 错误返回缺少保护

位置：

- `scene_layout_react/llm_planner.py:75-79`
- `scene_layout_react/react_agent.py:117-129`
- `scene_layout_react/react_agent.py:157-163`

问题：

`_tool_chat()` 解析工具参数失败时返回 `{"type": "tool_error"}`，但 `ReActAgent.run()` 只处理 `final`，否则无条件访问 `decision["calls"]`。

影响：

模型返回非法 tool arguments 时，agent 主循环会 KeyError。

建议：

- `run()` 明确处理 `tool_error`、`json_error`、unknown decision type。
- 将 planner 错误变成 `ToolResult(ok=False, error=...)` 或直接进入 reflection。

### 16. LLM 调用没有 timeout、retry 和异常边界

位置：

- `scene_layout_react/llm_planner.py:23-37`
- `scene_layout_react/llm_planner.py:50-63`

问题：

OpenAI client 调用没有 timeout/retry 配置，也没有捕获网络异常。

影响：

本地服务不可用、模型超时、vLLM 参数不兼容时，主流程直接崩溃。

建议：

- 初始化 client 时配置 timeout。
- 对 API 调用捕获异常并返回结构化 planner error。
- `extra_body={"chat_template_kwargs": {"enable_thinking": True}}` 应该做成 Qwen/vLLM 专用配置，不应硬编码到所有 OpenAI-compatible 后端。

### 17. Agent 返回值不可直接序列化

位置：

- `scene_layout_react/react_agent.py:119-124`
- `scene_layout_react/react_agent.py:180-184`
- `scene_layout_react/react_agent.py:23-32`

问题：

返回的 `steps` 是 `AgentStep` dataclass 列表，内部包含 `ToolResult` 和 `Observation` 对象，不是纯 dict。

影响：

调用方无法直接 `json.dumps(record)`，也无法稳定保存运行轨迹。

建议：

- 给 `AgentStep` 增加 `to_dict()`。
- `run()` 返回纯 JSON-compatible dict。
- 补一个 `save_run(record, path)` 或在 `ReActAgent` 增加 `save()`。

### 18. 日志目录没有确保存在

位置：

- `scene_layout_react/react_agent.py:67-68`

问题：

`logging.FileHandler(log_filename)` 前没有 `config.output_dir.mkdir(...)`。

影响：

如果 outputs 目录不存在，agent 初始化直接失败。

建议：

- 初始化 logger 前执行 `Path(config.output_dir).mkdir(parents=True, exist_ok=True)`。

### 19. Tool 层吞掉所有异常，丢失可调试上下文

位置：

- `scene_layout_react/tools/base.py:39-46`

问题：

`Tool.__call__` 捕获所有 Exception，只返回 `str(exc)`，没有异常类型、trace id 或 traceback。

影响：

LLM 能看到错误字符串，但开发者定位问题困难。

建议：

- `ToolResult` 增加 `error_type`、`debug` 字段。
- debug 信息只写日志，不直接暴露给 LLM。
- 对可预期错误显式返回，避免大范围 catch all 掩盖 bug。

### 20. jsonschema 校验行为与测试期望不一致

位置：

- `scene_layout_react/tools/base.py:31-37`
- `scene_layout_react/test/test_tool_schema.py:22-27`

问题：

当前 `Tool.validate()` 直接返回 jsonschema 的 `exc.message`，例如 required 字段缺失时通常是 `"'query' is a required property"`。测试却期望 `"missing required field: query"` 和 `"unknown fields: ['extra']"`。

影响：

测试与实现已经漂移。

建议：

- 要么更新测试为 jsonschema 原生错误。
- 要么封装错误格式，稳定对 LLM 的错误提示。

### 21. `retrieve_tool` 输出字段不一致

位置：

- `scene_layout_react/tools/retrieve_assets.py:55-65`
- `scene_layout_react/asset_loader.py:110-117`

问题：

Markdown ingestion 写入的是 `detail_level`，工具输出读取的是 `template_detail` 和 `scene_name`。

影响：

scene_template 检索结果会丢失 detail 信息或返回 None 字段。

建议：

- 字段名统一为 `detail_level`。
- 为 asset/template 输出定义 TypedDict 或 dataclass。

### 22. Markdown 文件名解析过于脆弱

位置：

- `scene_layout_react/asset_loader.py:101-102`

问题：

`scene_id, detail = stem.split("-", 1)` 假设文件名一定包含 `-`。

影响：

新增一个不含连字符的 md 文件会直接崩溃。

建议：

- 检查 `if "-" not in stem` 并返回明确错误或默认 detail。

### 23. CSV ingestion 对坏 bbox 和缺 bbox 不健壮

位置：

- `scene_layout_react/asset_loader.py:48-77`

问题：

- `ast.literal_eval()` 没有异常边界。
- bbox 缺失时 `content` 和 `metadata` 不会赋值，但后面无条件使用。
- size 没有校验为正数。

影响：

单行坏数据会中断整个 ingest。

建议：

- 对每一行做 try/except，并记录 bad row。
- 缺 bbox 时要么跳过，要么写入默认 bbox 并标记质量。
- 校验 bbox 长度和 size 正数。

### 24. `SceneStateManager.add_instance` 会静默覆盖实例

位置：

- `scene_layout_react/scene_state.py:15-17`

问题：

`add_instance()` 不检查 ID 是否存在，直接覆盖。

影响：

绕过 `place_instance` 或未来新增工具时，可能静默丢失实例。

建议：

- 在 manager 层统一拒绝重复 ID。
- 或提供明确的 `replace_instance()`。

### 25. Config 不是可移植配置

位置：

- `scene_layout_react/config.py:6`
- `scene_layout_react/config.py:18-20`
- `scene_layout_react/config.py:24-34`

问题：

硬编码了个人目录、`cuda:1`、模型名、本地 LLM 地址、Isaac 路径。`isaac_worker_path` 标注为 `Optional[Path]`，实际默认是字符串。

影响：

代码只能在当前机器假设下运行。

建议：

- 默认路径基于 repo root 推导。
- GPU、LLM、Isaac 配置从 env 或 CLI 参数读取。
- 修正 `isaac_worker_path` 类型。
- `model` 添加类型注解，保持 dataclass 字段一致。

### 26. 依赖不可复现且 GPU 绑定重

位置：

- `requirements.txt:1-11`

问题：

依赖只有下限，没有锁定；`faiss-gpu`、`bitsandbytes`、`torch` 等依赖对 CUDA/Python 平台高度敏感。当前环境已经缺 `openai`、`faiss`、`pytest`。

影响：

任何新环境安装结果都不确定。

建议：

- 分拆 `requirements.txt`、`requirements-dev.txt`、`requirements-physics.txt`。
- 提供 CPU-only fallback，例如 `faiss-cpu`。
- 使用 lockfile 或 Docker/uv/conda env 文件固定版本。

## Physics-Specific Issues

### 27. Isaac bridge 不处理 missing executable

位置：

- `scene_layout_react/physics/isaac_bridge.py:55-84`

问题：

`subprocess.run()` 可能抛 `FileNotFoundError`，当前只捕获 `TimeoutExpired`。

影响：

物理工具直接走 `Tool.__call__` 的 catch all，错误信息不结构化；`run_isaac_physics_feedback()` 也只捕获 `IsaacBridgeError`。

建议：

- 调用前检查 `isaac_python.exists()`、`worker_path.exists()`。
- 将 OSError 包装为 `IsaacBridgeError`。

### 28. Isaac worker 产生临时 stage 但不清理

位置：

- `scene_layout_react/physics/worker.py:101-103`
- `scene_layout_react/physics/worker.py:468-478`

问题：

每次操作创建一个 USD stage，并把路径返回，但 finally 不删除。

影响：

长时间运行会填满 `/tmp/scene_synthesis_isaac`。

建议：

- 增加 `keep_stage` debug 开关。
- 默认清理临时 stage。

### 29. 物理稳定性判定过于简化

位置：

- `scene_layout_react/physics/worker.py:455-473`

问题：

`stable` 只看 `position[2]` 是否下降超过 0.05，不检查碰撞、倾倒、旋转、横向漂移、穿透或 contact 状态。

影响：

`simulate_step` 返回的 stable 不能代表真实稳定。

建议：

- 引入 pose delta、contact pairs、collision pairs、support constraints。
- 将 stable 拆成 `height_stable`、`collision_free`、`support_valid`。

### 30. Physics tools 没有 respect `physics_enabled`

位置：

- `scene_layout_react/tools/check_collision.py:54-60`
- `scene_layout_react/tools/check_support.py:39-45`
- `scene_layout_react/tools/simulate_step.py:52-58`

问题：

即使 `ToolContext.physics_enabled=False`，这些工具仍会直接调用 Isaac。

影响：

用户关闭 physics 仍可能被模型调用物理工具触发 Isaac。

建议：

- 在工具入口检查 `context.physics_enabled`。
- 关闭时返回清晰错误或 fallback 到本地 AABB/support 检查。

## Test and Tooling Issues

### 31. 没有项目元数据和测试配置

位置：

- 仓库根目录缺少 `pyproject.toml`、`setup.py`、`pytest.ini`、CI 配置。

问题：

当前只有 `requirements.txt`，没有包安装入口、console script、lint、format、pytest 配置。

影响：

团队协作和 CI 不可控。

建议：

- 增加 `pyproject.toml`。
- 定义包名、Python 版本、依赖 extras、pytest 配置。
- 增加最小 CI：import check、unit tests、ruff/format。

### 32. `.gitignore` 为空，产物已经进入工作区

位置：

- `.gitignore`
- `scene_layout_react/**/__pycache__`
- `outputs/*.log`
- `data/indexes/*.faiss`
- `data/indexes/corpus.jsonl`

问题：

`.gitignore` 是空文件，当前 git status 已经显示大量 `__pycache__` 修改和运行日志。

影响：

代码 review 被产物噪音淹没；二进制缓存会污染提交。

建议：

- 忽略 `__pycache__/`、`*.pyc`、`.pytest_cache/`、`outputs/*.log`。
- 明确决定 `data/indexes` 是否版本化；如果保留，应有重建流程和 checksum。

### 33. 测试和脚本混在 `scene_layout_react/test`

位置：

- `scene_layout_react/test/test.py`
- `scene_layout_react/test/testtool.py`
- `scene_layout_react/test/test_tool_use.py`
- `scene_layout_react/test/test_tool_place.py`

问题：

这些文件既有 pytest 风格函数，又有顶层执行脚本和远程 LLM 调用。

影响：

无法区分自动测试、手动 smoke、实验脚本。

建议：

- `tests/unit/` 放纯单元测试。
- `tests/integration/` 放需要服务的测试，并用 marker 控制。
- `scripts/smoke/` 放手动 LLM/Isaac 工作流。

## Data Processing Issues

### 34. 数据处理脚本存在 import-time 副作用

位置：

- `dataprocess/bbox.py:4-7`
- `dataprocess/assetprocess/render_topdown_scene.py:19-65`

问题：

`bbox.py` 在 import 时设置 GPU 并启动 Isaac Sim。`render_topdown_scene.py` 在模块顶层 parse args 并启动 SimulationApp。

影响：

无法被安全导入、测试或复用。

建议：

- 所有 CLI 行为放入 `main()`。
- import 阶段只定义函数和类。

### 35. `render_topdown_scene.py` 默认 renderer 不在 choices 中

位置：

- `dataprocess/assetprocess/render_topdown_scene.py:57-61`

问题：

默认值是 `"RayTracing"`，choices 是 `["PathTracing", "Iray", "rtx"]`。

影响：

不传 `--renderer` 时 argparse 会报默认值不合法。

建议：

- 将 choices 加入 `"RayTracing"`，或默认改为 `"rtx"`。

### 36. 数据处理脚本硬编码个人路径

位置：

- `dataprocess/xlsx2csv.py:112-114`
- `dataprocess/bbox.py:116-118`
- `dataprocess/usd2scale.py:8-35`

问题：

脚本默认路径依赖 `/home/simple/Desktop/...`、`/home/simple/isaacsim` 等个人目录。

影响：

脚本不可移植，不适合团队或 CI。

建议：

- 所有输入输出路径都通过 CLI 参数传入。
- 默认路径基于当前项目根目录或不提供默认值。

### 37. `usd2md` 使用 cwd-dependent import

位置：

- `dataprocess/usd2md/main.py:2`
- `dataprocess/usd2md/generator.py:5-6`

问题：

使用 `from generator import ...`、`import extractor`、`import formatter`，依赖当前工作目录。

影响：

从 repo root 以包方式运行时容易失败。

建议：

- 改为包相对导入：`from .generator import ...`、`from . import extractor, formatter`。
- 使用 `python -m dataprocess.usd2md.main` 作为入口。

### 38. `usd2md/main.py` 捕获异常但返回成功状态

位置：

- `dataprocess/usd2md/main.py:29-35`

问题：

异常只打印，不 `raise` 或返回非零退出码。

影响：

批处理或 CI 会把失败任务误判为成功。

建议：

- `main() -> int`，失败返回 1。
- 或异常后重新抛出。

## Architecture Review

### 39. 分层边界不清晰

问题：

当前 `ToolContext`、`AssetRAG`、`LLMPlanner`、`Observer`、`IsaacBridge` 互相直接导入；测试也依赖真实 RAG、真实 OpenAI、真实 Isaac 配置。

影响：

- 难以单测。
- 难以替换模型后端和物理后端。
- 导入成本高，失败点多。

建议：

- 定义接口：
  - `RetrieverProtocol`
  - `PlannerProtocol`
  - `PhysicsBackendProtocol`
  - `SceneValidator`
- Agent 只依赖接口，不依赖具体实现。

### 40. 配置体系缺少环境隔离

问题：

配置同时包含数据路径、模型路径、LLM 服务、物理后端、输出路径，但没有环境层级和 override 机制。

建议：

- 使用 dataclass 分组：`DataConfig`、`ModelConfig`、`PhysicsConfig`、`RuntimeConfig`。
- 支持 env var 和 CLI override。
- 将默认配置设为 CPU/minimal/offline 可运行。

### 41. 工具 schema、工具实现、测试夹杂手工约定

问题：

工具 schema 手写，测试期望另一套 helper；字段名也有 `retrieve_assets`、`retrieve_tool`、`doc_id`、`asset_doc_id` 的漂移。

建议：

- 建一个单一 schema helper。
- 每个工具必须有：
  - schema 测试
  - 成功路径测试
  - 参数错误测试
  - 状态变更测试

### 42. 运行记录和可观测性不足

问题：

Agent 日志写文本，但返回值不是可序列化运行记录；没有 run id、版本信息、配置快照、工具耗时、物理后端耗时。

建议：

- 定义 `RunRecord`、`StepRecord`。
- 所有步骤记录 JSONL。
- 日志和状态快照分开保存。

## Suggested Fix Order

1. 修复导入边界：让 `import scene_layout_react.config`、`data_models`、`tools.base` 不依赖 OpenAI/FAISS/SentenceTransformer。
2. 让最小无物理端到端可跑：`physics_enabled=False` 默认值，mock planner 或脚本化 planner 测通 retrieve/place/query。
3. 修复 `place_instance` 和 scene instance ID 生成。
4. 修复 `AssetRAG.retrieve()` 的 `retrieval_top_k`、`doc_type`、未知类型处理。
5. 拆分测试目录，先建立 10 个纯单元测试覆盖 SceneStateManager、asset_loader、retrieve、place、support、observer。
6. 修复 Isaac worker 的确定性错误，并为 worker 纯函数补单测。
7. 整理 `.gitignore`、依赖分组、pyproject、CI。
8. 再考虑把 physics 工具接回默认 Agent 流程。

## Minimum Acceptance Criteria Before More Features

- `python -c "from scene_layout_react.config import ProjectConfig"` 在无 OpenAI/FAISS 环境下成功。
- `pytest --collect-only` 不访问网络、不启动 Isaac、不加载大模型。
- 无物理模式下能用 fake planner 放置两个同一资产实例。
- `AssetRAG.retrieve(..., doc_type="missing")` 有明确、可测试行为。
- `ReActAgent.run()` 返回纯 JSON-compatible dict。
- `physics_enabled=True` 时，worker 对空场景、单对象场景、两个重叠对象、box-on-pallet 场景都有自动测试。
