"""ReAct-style agent for scene planning.

The agent follows a tool-using architecture:
1) infer scene type from natural language
2) choose a matching MD scene template
3) retrieve/select CSV assets
4) plan placements by imitating the MD template anchors
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Tuple

from .data_models import AssetDocument, LayoutElement, LayoutPlan, SceneCommand
from .local_llm import GenerationConfig, LocalCausalLM
from .template_layout import SelectedAsset, TemplateLayoutPlanner


@dataclass
class AgentStep:
    action: str
    action_input: Dict[str, Any]
    observation: str


@dataclass
class AgentTrace:
    steps: List[AgentStep] = field(default_factory=list)

    def add(self, action: str, action_input: Dict[str, Any], observation: str) -> None:
        self.steps.append(AgentStep(action=action, action_input=action_input, observation=observation))

    def to_text(self, max_steps: int = 12) -> str:
        lines: List[str] = []
        for step in self.steps[:max_steps]:
            lines.append(f"- {step.action}({json.dumps(step.action_input, ensure_ascii=False)}) => {step.observation}")
        if len(self.steps) > max_steps:
            lines.append(f"... ({len(self.steps) - max_steps} more steps)")
        return "\n".join(lines)


_SCENE_KEYWORDS: List[Tuple[str, List[str]]] = [
    ("warehouse", ["warehouse", "仓库", "入库", "出库", "货架", "库位", "托盘", "pallet", "rack"]),
    ("assembly", ["assembly", "装配", "工位", "workbench", "机器人", "robot", "franka", "ur10"]),
    ("sorting", ["sorting", "分拣", "sort", "扫码", "scan", "conveyor", "传送带"]),
    ("palletizing", ["palletizing", "码垛", "palletize", "堆叠", "stack"]),
    ("transport", ["transport", "运输", "搬运", "agv", "forklift", "叉车", "vehicle"]),
]


def _base_scene_type(scene_name: str) -> str:
    """Normalize scene template name to a coarse type (warehouse1-brief -> warehouse)."""
    s = scene_name.strip().lower()
    s = s.split("-", 1)[0]
    m = re.match(r"([a-z]+)", s)
    return m.group(1) if m else s


class SceneLayoutReActAgent:
    def __init__(self, rag_pipeline: Any):
        # Avoid importing SceneLayoutRAG directly to keep module load light.
        self.rag = rag_pipeline
        self._llm: LocalCausalLM | None = None

    def _ensure_llm(self) -> LocalCausalLM:
        if self._llm is not None:
            return self._llm
        cfg = getattr(self.rag, "config", None)
        model_cfg = getattr(cfg, "model", None)
        model_name = getattr(model_cfg, "llm_name_or_path", "") if model_cfg is not None else ""
        if not model_name:
            raise ValueError("未配置本地 LLM (config.model.llm_name_or_path)，无法运行 ReAct-LLM 模式")
        self._llm = LocalCausalLM(
            model_name_or_path=model_name,
            device=getattr(model_cfg, "device", None),
            use_8bit=bool(getattr(model_cfg, "use_8bit", False)),
            load_in_4bit=bool(getattr(model_cfg, "load_in_4bit", False)),
            generation=GenerationConfig(
                max_new_tokens=int(getattr(model_cfg, "max_new_tokens", 256)),
                temperature=float(getattr(model_cfg, "temperature", 0.2)),
            ),
        )
        return self._llm

    def _tool_detect_scene_type(self, command: str) -> str:
        text = command.lower()
        best = ("warehouse", 0)
        for scene_type, kws in _SCENE_KEYWORDS:
            score = sum(1 for kw in kws if kw.lower() in text)
            if score > best[1]:
                best = (scene_type, score)
        if best[1] > 0:
            return best[0]

        # Fallback: use nearest MD hit to guess the template family.
        try:
            hits = self.rag.retrieve_scenes(command, top_k=3)
        except Exception:
            hits = []
        for h in hits:
            scene_name = h.document.metadata.get("scene_name")
            if isinstance(scene_name, str) and scene_name:
                return _base_scene_type(scene_name)
        return "warehouse"

    def _tool_choose_template(self, command: str, scene_type: str, top_k: int = 5) -> Tuple[str, List[AssetDocument]]:
        hits = self.rag.retrieve_scenes(f"{scene_type}\n{command}", top_k=max(top_k, 3))
        # Prefer scene_meta docs; else fallback to any doc with a scene_name.
        ranked: List[Tuple[str, float]] = []
        for h in hits:
            scene_name = h.document.metadata.get("scene_name")
            if not isinstance(scene_name, str) or not scene_name:
                continue
            score = float(h.score)
            if _base_scene_type(scene_name) == scene_type:
                score += 0.25
            ranked.append((scene_name, score))
        ranked.sort(key=lambda x: x[1], reverse=True)
        chosen = ranked[0][0] if ranked else (self.rag.get_scene_names()[0] if self.rag.get_scene_names() else "")
        scene_docs = self.rag.get_scene_anchor_documents(chosen) if chosen else []
        return chosen, scene_docs

    def _tool_search_assets(self, command: str, top_k: int = 12) -> List[Tuple[AssetDocument, float]]:
        hits = self.rag.retrieve_assets(command, top_k=top_k)
        return [(h.document, float(h.score)) for h in hits]

    def _tool_pick_assets(
        self,
        command: str,
        scene_type: str,
        asset_doc_scores: Sequence[Tuple[AssetDocument, float]],
        max_assets: int = 8,
    ) -> List[SelectedAsset]:
        # Collapse chunks to unique (asset_category, usd_path) picks.
        best_by_key: Dict[Tuple[str, str], Tuple[AssetDocument, float]] = {}
        for doc, score in asset_doc_scores:
            asset_id = str(doc.metadata.get("asset_category") or doc.doc_id)
            usd_path = str(doc.metadata.get("usd_path") or "")
            if not usd_path:
                continue
            key = (asset_id, usd_path)
            prev = best_by_key.get(key)
            if prev is None or score > prev[1]:
                best_by_key[key] = (doc, score)

        candidates = sorted(best_by_key.values(), key=lambda x: x[1], reverse=True)

        prefer: Dict[str, List[str]] = {
            "warehouse": ["Rack", "Pallet", "Box", "Vehicle", "Conveyor"],
            "assembly": ["Workbench", "Industrial Robot", "Part", "Conveyor"],
            "sorting": ["Conveyor", "Box", "Vehicle", "Rack"],
            "palletizing": ["Industrial Robot", "Pallet", "Box", "Conveyor"],
            "transport": ["Vehicle", "Pallet", "Box", "Conveyor"],
        }
        preferred_categories = prefer.get(scene_type, [])
        selected: List[SelectedAsset] = []

        def to_selected(doc: AssetDocument, score: float) -> SelectedAsset:
            asset_id = str(doc.metadata.get("asset_category") or doc.doc_id)
            usd_path = str(doc.metadata.get("usd_path") or "")
            scale_value = doc.metadata.get("scale")
            scale = [float(scale_value)] * 3 if isinstance(scale_value, (int, float)) else [0.01, 0.01, 0.01]
            desc = doc.content.replace("\n", " ")
            return SelectedAsset(asset_id=asset_id, usd_path=usd_path, scale=scale, score=float(score), description=desc)

        # Pick one per preferred category if possible.
        for cat in preferred_categories:
            if len(selected) >= max_assets:
                break
            for doc, score in candidates:
                if str(doc.metadata.get("asset_category") or "").lower() == cat.lower():
                    picked = to_selected(doc, score)
                    if all(p.usd_path != picked.usd_path for p in selected):
                        selected.append(picked)
                        break

        # Fill remaining slots by relevance.
        for doc, score in candidates:
            if len(selected) >= max_assets:
                break
            picked = to_selected(doc, score)
            if all(p.usd_path != picked.usd_path for p in selected):
                selected.append(picked)

        return selected

    def generate_layout(self, command_text: str, *, top_k_assets: int = 12, max_assets: int = 8) -> LayoutPlan:
        trace = AgentTrace()

        scene_type = self._tool_detect_scene_type(command_text)
        trace.add("detect_scene_type", {"command": command_text}, scene_type)

        template_name, template_anchor_docs = self._tool_choose_template(command_text, scene_type, top_k=5)
        trace.add(
            "choose_template",
            {"command": command_text, "scene_type": scene_type, "top_k": 5},
            f"{template_name} (anchors={len(template_anchor_docs)})",
        )

        asset_doc_scores = self._tool_search_assets(command_text, top_k=top_k_assets)
        trace.add("search_assets", {"command": command_text, "top_k": top_k_assets}, f"hits={len(asset_doc_scores)}")

        selected_assets = self._tool_pick_assets(command_text, scene_type, asset_doc_scores, max_assets=max_assets)
        trace.add(
            "pick_assets",
            {"scene_type": scene_type, "max_assets": max_assets},
            f"selected={len(selected_assets)}",
        )

        planner = TemplateLayoutPlanner(target_radius_xy=8.0)
        elements: List[LayoutElement] = planner.plan(selected_assets, template_anchor_docs)
        trace.add("plan_with_template", {"template": template_name}, f"elements={len(elements)}")

        command = SceneCommand(raw_text=command_text)
        plan = LayoutPlan(
            command=command,
            elements=elements,
            retrieved_docs=[doc for doc, _ in asset_doc_scores] + template_anchor_docs,
            planner_notes=f"scene_type={scene_type}\ntemplate={template_name}\ntrace:\n{trace.to_text()}",
        )
        return plan

    def generate_layout_llm(
        self,
        command_text: str,
        *,
        top_k_assets: int = 12,
        max_assets: int = 8,
        max_steps: int = 6,
    ) -> LayoutPlan:
        """LLM-driven ReAct loop (tools are still executed locally).

        This method is optional: if the LLM output cannot be parsed, it falls back to `generate_layout`.
        """
        trace = AgentTrace()
        state: Dict[str, Any] = {"command": command_text}

        def obs(action: str, action_input: Dict[str, Any], observation: Dict[str, Any]) -> None:
            trace.add(action, action_input, json.dumps(observation, ensure_ascii=False))

        tools = {
            "detect_scene_type": "Infer coarse scene type (warehouse/assembly/sorting/palletizing/transport). Input: {command}",
            "choose_template": "Pick an MD template scene_name and load its anchors. Input: {command, scene_type}",
            "search_assets": "Retrieve CSV assets relevant to the command. Input: {command, top_k_assets}",
            "pick_assets": "Select a small asset set from retrieved candidates. Input: {scene_type, max_assets}",
            "plan_with_template": "Generate placements by imitating template anchors. Input: {} (uses current state)",
        }

        system = (
            "You are a ReAct agent for industrial scene layout planning.\n"
            "You MUST use the provided tools to get information; do not hallucinate asset paths.\n"
            "Output format (no extra text):\n"
            "Action: <tool_name>\n"
            "Action Input: <json object>\n"
            "OR\n"
            "Final: <json object>\n"
            "Available tools:\n"
            + "\n".join([f"- {k}: {v}" for k, v in tools.items()])
        )

        scratchpad = ""
        for _ in range(max_steps):
            state_view = {
                "scene_type": state.get("scene_type"),
                "template": state.get("template"),
                "asset_candidates": len(state.get("asset_doc_scores") or []),
                "selected_assets": len(state.get("selected_assets") or []),
            }
            prompt = (
                f"{system}\n\n"
                f"Command: {command_text}\n"
                f"State: {json.dumps(state_view, ensure_ascii=False)}\n\n"
                f"{scratchpad}"
            )
            try:
                model = self._ensure_llm()
                out = model.generate(prompt, max_new_tokens=256, temperature=0.0)
            except Exception:
                break

            m_final = re.search(r"Final:\\s*(\\{[\\s\\S]*\\})", out)
            if m_final:
                try:
                    final_obj = json.loads(m_final.group(1))
                except Exception:
                    break
                if isinstance(final_obj, dict) and "layout" in final_obj and isinstance(final_obj["layout"], list):
                    # Convert Final.layout into LayoutPlan elements.
                    elements: List[LayoutElement] = []
                    for item in final_obj["layout"]:
                        if not isinstance(item, dict):
                            continue
                        pos = item.get("position") or [0.0, 0.0, 0.0]
                        if isinstance(pos, (list, tuple)) and len(pos) >= 3:
                            x, y, z = float(pos[0]), float(pos[1]), float(pos[2])
                        else:
                            x, y, z = 0.0, 0.0, 0.0
                        scale = item.get("scale")
                        if isinstance(scale, (list, tuple)) and len(scale) >= 3:
                            scale_list = [float(scale[0]), float(scale[1]), float(scale[2])]
                        else:
                            scale_list = [0.01, 0.01, 0.01]
                        elements.append(
                            LayoutElement(
                                asset_id=str(item.get("asset_id") or ""),
                                usd_path=str(item.get("usd_path") or ""),
                                transform={"x": x, "y": y, "z": z},
                                score=float(item.get("score") or 0.0),
                                reasoning=str(item.get("reason") or "ReAct-LLM"),
                                scale=scale_list,
                            )
                        )
                    return LayoutPlan(
                        command=SceneCommand(raw_text=command_text),
                        elements=elements,
                        retrieved_docs=[],
                        planner_notes=f"react_llm_final\ntrace:\n{trace.to_text()}",
                    )
                break

            m_action = re.search(r"Action:\\s*([a-zA-Z_][a-zA-Z0-9_]*)", out)
            m_input = re.search(r"Action Input:\\s*(\\{[\\s\\S]*\\})", out)
            if not m_action or not m_input:
                break
            action = m_action.group(1)
            try:
                action_input = json.loads(m_input.group(1))
            except Exception:
                break

            if action == "detect_scene_type":
                scene_type = self._tool_detect_scene_type(str(action_input.get("command") or command_text))
                state["scene_type"] = scene_type
                obs(action, action_input, {"scene_type": scene_type})
            elif action == "choose_template":
                st = str(action_input.get("scene_type") or state.get("scene_type") or "")
                tmpl, anchors = self._tool_choose_template(command_text, st, top_k=5)
                state["template"] = tmpl
                state["template_anchor_docs"] = anchors
                obs(action, action_input, {"template": tmpl, "anchors": len(anchors)})
            elif action == "search_assets":
                k = int(action_input.get("top_k_assets") or top_k_assets)
                asset_doc_scores = self._tool_search_assets(command_text, top_k=k)
                state["asset_doc_scores"] = asset_doc_scores
                obs(action, action_input, {"hits": len(asset_doc_scores)})
            elif action == "pick_assets":
                st = str(action_input.get("scene_type") or state.get("scene_type") or "")
                ma = int(action_input.get("max_assets") or max_assets)
                selected = self._tool_pick_assets(command_text, st, state.get("asset_doc_scores") or [], max_assets=ma)
                state["selected_assets"] = selected
                obs(action, action_input, {"selected": len(selected), "asset_ids": [a.asset_id for a in selected]})
            elif action == "plan_with_template":
                anchors = state.get("template_anchor_docs") or []
                selected = state.get("selected_assets") or []
                planner = TemplateLayoutPlanner(target_radius_xy=8.0)
                elements = planner.plan(selected, anchors)
                layout = LayoutPlan(
                    command=SceneCommand(raw_text=command_text),
                    elements=elements,
                    retrieved_docs=[],
                    planner_notes=f"react_llm_tools\ntrace:\n{trace.to_text()}",
                )
                # Provide layout back as observation; LLM may wrap it as Final later.
                obs(action, action_input, {"layout": layout.summary(), "template": state.get("template")})
            else:
                break

            scratchpad += f"Action: {action}\nAction Input: {json.dumps(action_input, ensure_ascii=False)}\nObservation: {trace.steps[-1].observation}\n\n"

        # Fallback if LLM loop didn't converge.
        plan = self.generate_layout(command_text, top_k_assets=top_k_assets, max_assets=max_assets)
        plan.planner_notes = (plan.planner_notes or "") + "\n(fallback_from_react_llm)"
        return plan


__all__ = ["SceneLayoutReActAgent", "AgentTrace", "AgentStep"]
