# react_agent.py
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from .config import ProjectConfig
from .llm_planner import LLMPlanner,ToolDecision,ReflectionResult
from .observer import Observer
from .rag import AssetRAG
from .scene_state import SceneStateManager
from .tools.base import (
    TOOL_REGISTRY,
    ToolContext,
    ToolResult,
)
# =========================================================
# Runtime State
# =========================================================
@dataclass
class AgentStep:
    step: int
    strategy: Optional[Dict[str, Any]] = None
    tool_decision: Optional[ToolDecision] = None
    tool_results: List[ToolResult] = field(
        default_factory=list
    )
    observation: Optional[Dict[str, Any]] = None
    reflection: Optional[ReflectionResult] = None
# =========================================================
# ReAct Agent
# =========================================================
class ReActAgent:
    def __init__(self,config: ProjectConfig,rag: AssetRAG,):
        self.config = config
        self.rag = rag
        self.scene = SceneStateManager()
        self.planner = LLMPlanner(config)
        self.observer = Observer(self.scene)
        self.tool_context = ToolContext(
            scene=self.scene,
            rag=self.rag,
            physics_enabled=self.config.physics_enabled,
            extras={},
        )
        self.toot_specs = [tool.schema for tool in TOOL_REGISTRY.values()]
        self.lessons: List[Dict[str, Any]] = []
        self.reflections: List[Dict[str, Any]] = []
        self.observations: List[Dict[str, Any]] = []
    # =====================================================
    # Main Loop
    # =====================================================
    def run(self, command: str, max_steps: int = 10,) -> Dict[str, Any]:
        strategy: Optional[str] = None
        last_observation: Optional[Dict[str, Any]] = None
        history: List[AgentStep] = []
        for step_idx in range(max_steps):
            print("step",step_idx)
            runtime = AgentStep(step=step_idx)
            # -------------------------------------------------
            # 1. Reasoning / Strategy
            # -------------------------------------------------
            print("think")
            strategy_result = self.planner.reason(
                command=command,
                scene_summary=self.scene.to_dict(),
                recent_observations=self.observations[-5:],
                recent_reflections=self.reflections[-5:],
                lessons=self.lessons[-10:],
                strategy=strategy,
                step=step_idx,
                max_steps=max_steps,
            )
            runtime.strategy = strategy_result
            strategy = (strategy_result.get("next_strategy"))
            # -------------------------------------------------
            # 2. Tool Decision
            # -------------------------------------------------
            print("act")
            decision = self.planner.decide_action(
                command=command,
                strategy=strategy_result,
                scene_summary=self.scene.to_dict(),
                tool_specs=self.toot_specs,
                step=step_idx,
                max_steps=max_steps,
            )
            runtime.tool_decision = decision
            decision_type = decision["type"]
            # -------------------------------------------------
            # 3. Final Answer
            # -------------------------------------------------
            if decision_type == "final":
                return {
                    "ok": True,
                    "type": "final",
                    "response": decision["content"],
                    "steps": history,
                }
            # -------------------------------------------------
            # 4. Execute Tools
            # -------------------------------------------------
            tool_results: List[ToolResult] = []
            for call in decision["calls"]:
                tool_name = call["name"]
                tool_args = call["arguments"]
                tool = TOOL_REGISTRY.get(tool_name)
                if tool is None:
                    result = ToolResult(
                        ok=False,
                        error=f"unknown tool: {tool_name}",
                    )
                else:
                    result = tool(self.tool_context,**tool_args,)
                tool_results.append(result)
            runtime.tool_results = tool_results
            # -------------------------------------------------
            # 5. Observation
            # -------------------------------------------------
            print("observation")
            observation = self.observer.observe(
                command=command,
                tool_results=[
                    r.to_dict()
                    for r in tool_results
                ],
                previous_state=last_observation,
            )
            runtime.observation = observation
            self.observations.append(observation)
            last_observation = observation.to_dict()
            # -------------------------------------------------
            # 6. Reflection
            # -------------------------------------------------
            print("reflection")
            reflection = self.planner.reflect(
                command=command,
                strategy=strategy_result,
                tool_calls=decision["calls"],
                observation=observation.to_dict(),
            )
            runtime.reflection = reflection
            self.reflections.append(reflection)
            # -------------------------------------------------
            # 7. Lesson Update
            # -------------------------------------------------
            lesson = reflection.get("lesson")
            if lesson:
                self.lessons.append({
                    "lesson": lesson,
                })
            history.append(runtime)
        return {
            "ok": False,
            "error": "max steps exceeded",
            "steps": history,
        }