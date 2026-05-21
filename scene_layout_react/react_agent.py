# react_agent.py
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from .config import ProjectConfig
from .llm_planner import LLMPlanner,ToolDecision,ReflectionResult
from .observer import Observer
from .physics.isaac_bridge import run_isaac_physics_feedback
from .rag import AssetRAG
from .scene_state import SceneStateManager
from .tools.base import (
    TOOL_REGISTRY,
    ToolContext,
    ToolResult,
)
import logging
from datetime import datetime
import os
import json
#========================================================
# Runtime State
#========================================================
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
        physics_callable = None
        if self.config.physics_enabled:
            physics_callable =lambda state: run_isaac_physics_feedback(
                    self.config,
                    state,
                )
        self.observer = Observer(self.scene, physics_callable=physics_callable)
        self.tool_context = ToolContext(
            scene=self.scene,
            rag=self.rag,
            config=self.config,
            physics_enabled=self.config.physics_enabled,
            extras={},
        )
        self.tool_specs = [tool.schema for tool in TOOL_REGISTRY.values()]
        #logger
        self.logger = logging.getLogger(f"ReActAgent.{id(self)}")
        self.logger.setLevel(logging.DEBUG)
        if not self.logger.handlers:
            # 控制台 handler（INFO 级别，方便实时观看）
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            ch.setFormatter(logging.Formatter('%(asctime)s | %(message)s', datefmt='%H:%M:%S'))
            self.logger.addHandler(ch)
            # 文件 handler（DEBUG 级别，保存完整细节）
            log_filename = os.path.join(config.output_dir, f"agent_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
            fh = logging.FileHandler(log_filename, encoding='utf-8')
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
            self.logger.addHandler(fh)
    # =====================================================
    # Main Loop
    # =====================================================
    def run(self, command: str, max_steps: int = 10,) -> Dict[str, Any]:
        self.logger.info(f"开始执行命令:{command}")
        history: List[AgentStep] = []
        lessons: List[Dict[str, Any]] = []
        for step_idx in range(max_steps):
            self.logger.info(f"{'='*40} Step {step_idx +1}/{max_steps} {'='*40}")
            runtime = AgentStep(step=step_idx)
            # -------------------------------------------------
            # 1. Reasoning / Strategy
            # -------------------------------------------------
            self.logger.info("Thinking...")
            strategy_result = self.planner.reason(
                command=command,
                scene_summary=self.scene.to_dict(),
                recent_observations=[s.observation.to_dict() for s in history[-5:] if s.observation is not None],
                recent_reflections = [s.reflection for s in history[-5:] if s.reflection is not None],
                tool_results =[[r.to_dict() for r in s.tool_results]  for s in history[-5:]  if s.tool_results],
                lessons=lessons[-10:],
                strategy=[history[-1].strategy if history else None],
                step=step_idx,
                max_steps=max_steps,
            )
            runtime.strategy = strategy_result
            self.logger.debug(f"Strategy: {json.dumps(strategy_result, indent=2, ensure_ascii=False)}")
            # -------------------------------------------------
            # 2. Tool Decision
            # -------------------------------------------------
            self.logger.info(f"Deciding action...")
            decision = self.planner.decide_action(
                command=command,
                strategy=strategy_result,
                scene_summary=self.scene.to_dict(),
                tool_specs=self.tool_specs,
                step=step_idx,
                max_steps=max_steps,
                tool_results =[[r.to_dict() for r in s.tool_results]  for s in history[-5:]  if s.tool_results],
            )
            runtime.tool_decision = decision
            self.logger.debug(f"Decision: {json.dumps(decision, indent=2, ensure_ascii=False)}")
            # -------------------------------------------------
            # 3. Final Answer
            # -------------------------------------------------
            if decision["type"] == "final":
                self.logger.info("Reach the final answer")
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
                self.logger.info(f"Execute tool: {tool_name}, parameter: {tool_args}")
                tool = TOOL_REGISTRY.get(tool_name)
                if tool is None:
                    result = ToolResult(
                        ok=False,
                        error=f"unknown tool: {tool_name}",
                    )
                else:
                    result = tool(self.tool_context,**tool_args,)
                if result.ok:
                    self.logger.info(f"Success: {result.to_dict()}")
                else:
                    self.logger.error(f"Failed: {result.error}")
                tool_results.append(result)
            runtime.tool_results = tool_results
            # -------------------------------------------------
            # 5. Observation
            # -------------------------------------------------
            self.logger.info(f"Observe environment...")
            observation = self.observer.observe()
            self.logger.debug(f"Observation: {json.dumps(observation.to_dict(), indent=2, ensure_ascii=False)}")
            runtime.observation = observation
            # -------------------------------------------------
            # 6. Reflection
            # -------------------------------------------------
            if not observation.ok or not all(r.ok for r in tool_results):
                self.logger.info("Reflect...")
                reflection = self.planner.reflect(
                    command=command,
                    strategy=strategy_result,
                    tool_calls=decision["calls"],
                    observation=observation.to_dict(),
                    tool_results=[
                        r.to_dict()
                        for r in tool_results
                    ],
                )
                runtime.reflection = reflection
            # -------------------------------------------------
            # 7. Lesson Update
            # -------------------------------------------------
                lesson = reflection.get("lesson")
                if lesson:
                    lessons.append({
                        "lesson": lesson,
                    })
                    self.logger.info(f"Lesson learned: {lesson}")
            history.append(runtime)
        return {
            "ok": False,
            "error": "max steps exceeded",
            "steps": history,
        }
