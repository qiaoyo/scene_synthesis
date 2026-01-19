from __future__ import annotations
import argparse, json, math, os, re, sys
from pathlib import Path
from typing import Any, Dict, List

SRC_ROOT = Path(__file__).resolve().parents[1]
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

from scene_layout_rag import ProjectConfig, SceneLayoutRAG

REACT_SYSTEM = """You are a ReAct agent for industrial scene layout planning.
Tools:
- analyze_scene(command: str) -> JSON with scene_type, equipment list, zones, flow
- search_assets(query: str, top_k: int) -> top-K asset snippets (with ids/usd/bbox)
- search_scenes(query: str, top_k: int) -> top-K scene paragraphs (rules/relations)
- plan_layout(command: str, top_k: int) -> final layout plan as JSON (calls RAG+LLM planner)
- llm_reason(prompt: str, max_new_tokens: int) -> free-form explanation (optional)
Format:
    Thought: your reasoning
    Action: tool_name({"arg":"value", "top_k": 6})
    Observation: tool output (provided by system)
    Repeat Thought/Action/Observation for a few steps, then use plan_layout to finalize.
    Only one Action per step.
Workflow (必须遵循):
    1) 先判断场景类型并列出该场景应有的设备清单（使用 analyze_scene）。
    2) 基于场景类型+设备清单检索资产与场景规则（search_assets/search_scenes）。
    3) 结合检索文本进行逐步规划，先粗后细，确保所有设备被规划，并利用LLM给出关系指导。
    4) 避免所有物体堆叠在场景中心，合理分布。
First action MUST be analyze_scene.
"""

ACTION_RE = re.compile(r"Action:\s*([a-zA-Z_][\w]*)\s*\(\s*(\{.*\})\s*\)", re.DOTALL)

class ReactAgent:
    def __init__(self, config: ProjectConfig, top_k: int = 6, max_steps: int = 4):
        self.config = config
        self.top_k = top_k
        self.max_steps = max_steps
        self.pipeline = SceneLayoutRAG(config)
        self._tokenizer = None
        self._model = None
        self._device = config.model.device

    def _ensure_llm(self) -> None:
        if self._model is not None:
            return
        name = self.config.model.llm_name_or_path
        tok = AutoTokenizer.from_pretrained(name, use_fast=False)
        if tok.pad_token is None:
            tok.pad_token = tok.eos_token
        kwargs: Dict[str, Any] = {}
        if self.config.model.load_in_4bit:
            kwargs["load_in_4bit"] = True
            kwargs["device_map"] = "cuda:0"
        elif self.config.model.use_8bit:
            kwargs["load_in_8bit"] = True
            kwargs["device_map"] = "cuda:0"
        else:
            dev = self.config.model.device or ("cuda" if torch.cuda.is_available() else "cpu")
            kwargs["device_map"] = None
            kwargs["torch_dtype"] = torch.float16 if dev.startswith("cuda") and torch.cuda.is_available() else torch.float32
        model = AutoModelForCausalLM.from_pretrained(name, **kwargs)
        if kwargs.get("device_map") is None:
            dev = self.config.model.device or ("cuda" if torch.cuda.is_available() else "cpu")
            model.to(dev)
            self._device = torch.device(dev)
        else:
            self._device = next(model.parameters()).device
        self._tokenizer, self._model = tok, model

    def _gen(self, prompt: str, max_new: int = 256, temperature: float = 0.2) -> str:
        self._ensure_llm()
        inputs = self._tokenizer(prompt, return_tensors="pt")
        inputs = {k: v.to(self._device) for k, v in inputs.items()}
        with torch.no_grad():
            out = self._model.generate(
                **inputs,
                max_new_tokens=max_new,
                temperature=temperature,
                do_sample=temperature > 0,
            )
        gen_ids = out[0][inputs["input_ids"].shape[1]:]
        return self._tokenizer.decode(gen_ids, skip_special_tokens=True).strip()

    # Tool 1: 资产检索
    def _tool_search_assets(self, query: str, top_k: int) -> str:
        hits = self.pipeline.retrieve_assets(query, top_k=top_k)
        lines = []
        for h in hits:
            m = h.document.metadata
            aid = m.get("asset_category", h.document.doc_id)
            usd = m.get("usd_path", "")
            bbox = m.get("bbox")
            lines.append(f"- [{h.score:.3f}] id:{aid} usd:{usd} bbox:{json.dumps(bbox, ensure_ascii=False) if bbox else 'null'}")
        return "\n".join(lines) or "(no assets)"

    # Tool 2: 场景检索
    def _tool_search_scenes(self, query: str, top_k: int) -> str:
        hits = self.pipeline.retrieve_scenes(query, top_k=top_k)
        lines = []
        for h in hits:
            txt = h.document.content.replace("\n", " ").strip()
            if len(txt) > 280:
                txt = txt[:280] + "..."
            src = h.document.metadata.get("source", "")
            lines.append(f"- [{h.score:.3f}] {txt} ({src})")
        return "\n".join(lines) or "(no scenes)"

    # Tool 3: 规划（调用管道的 LLMPlanner）
    def _tool_plan_layout(self, command: str, top_k: int) -> str:
        plan = self.pipeline.generate_layout(command, top_k=top_k)
        #检查是否堆在中心  是则做环形散开
        layout = self._spread_if_center_stacked(plan.summary())
        return json.dumps(layout, ensure_ascii=False, indent=2)

    # 可选：自由推理说明
    def _tool_llm_reason(self, prompt: str, max_new_tokens: int = 256) -> str:
        return self._gen("Thought: " + prompt + "\nAnswer:", max_new=max_new_tokens, temperature=self.config.model.temperature)

    # 场景分析：类型+设备清单
    def _tool_analyze_scene(self, command: str) -> str:
        prompt = (
            "Analyze the requirement and output ONLY valid JSON with keys:\n"
            '{"scene_type": "...", "equipment": ["..."], "zones": ["..."], "flow": "..."}\n'
            "Use short equipment names. No extra text.\n"
            f"Requirement: {command}"
        )
        return self._gen(prompt, max_new=256, temperature=0.2)

    def _safe_json_object(self, text: str) -> Dict[str, Any]:
        if not text:
            return {}
        try:
            data = json.loads(text)
            if isinstance(data, dict):
                return data
        except Exception:
            pass
        match = re.search(r"\{[\s\S]*\}", text)
        if match:
            try:
                data = json.loads(match.group(0))
                if isinstance(data, dict):
                    return data
            except Exception:
                return {}
        return {}

    def _normalize_list(self, raw: Any) -> List[str]:
        if raw is None:
            return []
        if isinstance(raw, list):
            items = raw
        else:
            items = re.split(r"[,\n;/，、]+", str(raw))
        cleaned: List[str] = []
        for item in items:
            text = str(item).strip()
            if text:
                cleaned.append(text)
        return self._dedupe_keep_order(cleaned)

    def _dedupe_keep_order(self, items: List[str]) -> List[str]:
        seen = set()
        result = []
        for item in items:
            key = item.lower()
            if key in seen:
                continue
            seen.add(key)
            result.append(item)
        return result

    def _fallback_scene_type(self, command: str) -> str:
        keywords = [
            ("仓储", "warehouse"),
            ("装配", "assembly"),
            ("码垛", "palletizing"),
            ("分拣", "sorting"),
            ("运输", "transportation")
        ]
        text = command.lower()
        for key, value in keywords:
            if key.lower() in text:
                return value
        return ""

    def _build_asset_queries(self, command: str, scene_type: str, equipment: List[str]) -> List[str]:
        queries = []
        for item in equipment:
            if scene_type:
                queries.append(f"{scene_type} {item}".strip())
            else:
                queries.append(item)
        if not queries:
            queries.append(command)
        return self._dedupe_keep_order(queries)

    def _build_scene_queries(self, command: str, scene_type: str, zones: List[str]) -> List[str]:
        queries = []
        if scene_type:
            queries.append(scene_type)
        for zone in zones:
            if scene_type:
                queries.append(f"{scene_type} {zone}".strip())
            else:
                queries.append(zone)
        if not queries:
            queries.append(command)
        return self._dedupe_keep_order(queries)

    def _cap_queries(self, queries: List[str], cap: int) -> List[str]:
        if cap <= 0 or len(queries) <= cap:
            return queries
        merged = ", ".join(queries[cap - 1 :])
        return queries[: cap - 1] + [merged]

    def _format_retrieval_block(self, title: str, pairs: List[tuple[str, str]]) -> str:
        if not pairs:
            return f"{title}: (none)"
        lines = [f"{title}:"]
        for idx, (query, result) in enumerate(pairs, 1):
            lines.append(f"[{idx}] query: {query}")
            lines.append(result or "(no results)")
        return "\n".join(lines)

    def _generate_guidance(
        self,
        command: str,
        scene_type: str,
        equipment: List[str],
        zones: List[str],
        flow: str,
        asset_block: str,
        scene_block: str,
    ) -> str:
        equipment_text = ", ".join(equipment) if equipment else "unknown"
        zones_text = ", ".join(zones) if zones else "unknown"
        prompt = (
            "You are planning an industrial layout. Provide stepwise placement guidance.\n"
            "- Use numbered steps (1..N).\n"
            "- Include relationships like 'boxes on racks' when relevant.\n"
            "- Cover all equipment.\n"
            "- Avoid putting everything at the scene center; distribute across zones.\n"
            f"Requirement: {command}\n"
            f"Scene type: {scene_type}\n"
            f"Equipment: {equipment_text}\n"
            f"Zones: {zones_text}\n"
            f"Flow: {flow}\n"
            f"{asset_block}\n"
            f"{scene_block}\n"
        )
        return self._tool_llm_reason(prompt, max_new_tokens=384)

    def _generate_item_guidance(
        self,
        command: str,
        scene_type: str,
        equipment: List[str],
        asset_block: str,
        scene_block: str,
    ) -> str:
        if not equipment:
            return ""
        equipment_text = ", ".join(equipment)
        prompt = (
            "Provide per-item placement guidance as a list. Format each line as:\n"
            "<item>: <one short guidance sentence>\n"
            "Focus on inter-object relations when applicable.\n"
            f"Requirement: {command}\n"
            f"Scene type: {scene_type}\n"
            f"Equipment: {equipment_text}\n"
            f"{asset_block}\n"
            f"{scene_block}\n"
        )
        return self._tool_llm_reason(prompt, max_new_tokens=320)

    def _compose_plan_command(
        self,
        command: str,
        scene_type: str,
        equipment: List[str],
        zones: List[str],
        flow: str,
        asset_block: str,
        scene_block: str,
        guidance: str,
    ) -> str:
        parts = [command]
        if scene_type:
            parts.append(f"Scene type: {scene_type}")
        if equipment:
            parts.append(f"Equipment list: {', '.join(equipment)}")
        if zones:
            parts.append(f"Zones: {', '.join(zones)}")
        if flow:
            parts.append(f"Flow: {flow}")
        if asset_block:
            parts.append(asset_block)
        if scene_block:
            parts.append(scene_block)
        if guidance:
            parts.append("Placement guidance:\n" + guidance)
        parts.append(
            "Constraints: distribute items across zones; avoid placing everything at the scene center; "
            "allow logical stacking like box on rack when supported."
        )
        return "\n\n".join(part for part in parts if part)

    def _spread_if_center_stacked(self, layout: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        positions = []
        for entry in layout:
            pos = entry.get("position")
            if isinstance(pos, (list, tuple)) and len(pos) >= 2:
                z = float(pos[2]) if len(pos) > 2 else 0.0
                positions.append((float(pos[0]), float(pos[1]), z))
                continue
            if isinstance(pos, dict):
                positions.append(
                    (
                        float(pos.get("x", 0.0)),
                        float(pos.get("y", 0.0)),
                        float(pos.get("z", 0.0)),
                    )
                )
                continue
            positions.append((0.0, 0.0, 0.0))

        if len(positions) < 2:
            return layout

        center_tol = 0.5
        eps = 1e-3
        all_near_center = all(abs(x) <= center_tol and abs(y) <= center_tol for x, y, _ in positions)
        all_same = all(abs(x - positions[0][0]) <= eps and abs(y - positions[0][1]) <= eps for x, y, _ in positions)
        if not (all_near_center or all_same):
            return layout

        base_x = 0.0 if all_near_center else sum(x for x, _, _ in positions) / len(positions)
        base_y = 0.0 if all_near_center else sum(y for _, y, _ in positions) / len(positions)
        radius = min(6.0, 1.5 + 0.8 * len(positions))
        for idx, entry in enumerate(layout):
            angle = (2 * math.pi * idx) / len(layout)
            x = round(base_x + radius * math.cos(angle), 2)
            y = round(base_y + radius * math.sin(angle), 2)
            z = positions[idx][2]
            pos = entry.get("position")
            if isinstance(pos, list):
                if len(pos) < 3:
                    entry["position"] = [x, y, z]
                else:
                    pos[0], pos[1], pos[2] = x, y, z
            elif isinstance(pos, dict):
                pos["x"], pos["y"], pos["z"] = x, y, z
            else:
                entry["position"] = [x, y, z]
        return layout

    def run(self, command: str) -> str:
        print("Thought: 我需要先分析用户的需求，确定场景类型和设备清单。")
        print(f"Action: analyze_scene({{'command': '{command}'}})")
        analysis_text = self._tool_analyze_scene(command)
        print(f"Observation: {analysis_text}\n")

        analysis = self._safe_json_object(analysis_text)
        scene_type = str(analysis.get("scene_type", "")).strip()
        if not scene_type:
            scene_type = self._fallback_scene_type(command)
        equipment = self._normalize_list(analysis.get("equipment"))
        zones = self._normalize_list(analysis.get("zones"))
        flow = str(analysis.get("flow", "")).strip()

        if not equipment:
            print("Thought: 没有识别出设备清单，尝试从需求中提取。")
            print(f"Action: llm_reason(Extract equipment from: {command})")
            fallback = self._tool_llm_reason(
                "Extract a short equipment list from the requirement. Output only a comma-separated list.\n"
                f"Requirement: {command}",
                max_new_tokens=128,
            )
            print(f"Observation: {fallback}\n")
            equipment = self._normalize_list(fallback)

        asset_queries = self._build_asset_queries(command, scene_type, equipment)
        scene_queries = self._build_scene_queries(command, scene_type, zones)
        asset_queries = self._cap_queries(asset_queries, cap=6)
        scene_queries = self._cap_queries(scene_queries, cap=4)

        asset_pairs = []
        for q in asset_queries:
            print(f"Thought: 检索与设备相关的资产：{q}")
            print(f"Action: search_assets({{'query': '{q}', 'top_k': {self.top_k}}})")
            result = self._tool_search_assets(q, self.top_k)
            print(f"Observation:\n{result}\n")
            asset_pairs.append((q, result))

        scene_pairs = []
        for q in scene_queries:
            print(f"Thought: 检索与场景相关的规则：{q}")
            print(f"Action: search_scenes({{'query': '{q}', 'top_k': {self.top_k}}})")
            result = self._tool_search_scenes(q, self.top_k)
            print(f"Observation:\n{result}\n")
            scene_pairs.append((q, result))

        asset_block = self._format_retrieval_block("Asset retrieval (csv)", asset_pairs)
        scene_block = self._format_retrieval_block("Scene retrieval (md)", scene_pairs)

        print("Thought: 基于检索结果，生成布局建议。")
        print("Action: llm_reason(生成布局指导)")
        guidance = self._generate_guidance(
            command=command,
            scene_type=scene_type,
            equipment=equipment,
            zones=zones,
            flow=flow,
            asset_block=asset_block,
            scene_block=scene_block,
        )
        print(f"Observation:\n{guidance}\n")

        item_guidance = self._generate_item_guidance(
            command=command,
            scene_type=scene_type,
            equipment=equipment,
            asset_block=asset_block,
            scene_block=scene_block,
        )
        if item_guidance:
            print("Thought: 为每个设备生成单独的放置建议。")
            print("Action: llm_reason(生成逐项建议)")
            print(f"Observation:\n{item_guidance}\n")
            guidance += "\n\nPer-item guidance:\n" + item_guidance

        plan_command = self._compose_plan_command(
            command=command,
            scene_type=scene_type,
            equipment=equipment,
            zones=zones,
            flow=flow,
            asset_block=asset_block,
            scene_block=scene_block,
            guidance=guidance,
        )

        print("Thought: 根据所有信息生成最终布局方案。")
        print("Action: plan_layout(...)")
        layout = self._tool_plan_layout(plan_command, self.top_k)
        print(f"Observation:\n{layout}\n")

        return layout


def main() -> None:
    parser = argparse.ArgumentParser(description="Run ReAct agent over SceneLayoutRAG")
    parser.add_argument("command", nargs="+", help="User requirement")
    parser.add_argument("--top-k", type=int, default=6)
    parser.add_argument("--max-steps", type=int, default=4)
    args = parser.parse_args()
    text = " ".join(args.command)
    cfg = ProjectConfig()
    agent = ReactAgent(cfg, top_k=args.top_k, max_steps=args.max_steps)
    print("[Agent] start")
    out = agent.run(text)
    print(out)

if __name__ == "__main__":
    main()
