import json
from openai import OpenAI
import sys
from pathlib import Path
import re
# =====================================================
# Import ALL Tools
# =====================================================
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scene_layout_rag.config import ProjectConfig
from scene_layout_rag.scene_state import SceneStateManager
from scene_layout_rag.rag import AssetRAG

from scene_layout_rag.tools.base import (
    TOOL_REGISTRY,
    ToolContext,
)

# =====================================================
# OpenAI Client
# =====================================================

client = OpenAI(
    api_key="EMPTY",
    base_url="http://localhost:8000/v1"
)

MODEL_NAME = "Qwen/Qwen3-32B-AWQ"

# =====================================================
# Context
# =====================================================

cfg = ProjectConfig()
rag = AssetRAG(cfg)
#rag.build(save=True)  # 先构建不保存，后面根据情况决定是否保存
if (cfg.index_dir / "corpus.jsonl").exists():
    rag.load()
else:
    rag.build(save=True)

context = ToolContext(
    scene=SceneStateManager(),
    rag=rag,
)

# =====================================================
# Constants
# =====================================================

MAX_ITER = 20
# =====================================================
# Messages
# =====================================================
messages = [
    {
        "role": "system",
        "content": ("""
            You are an industrial scene planning assistant.
            Strict Rules:
            1. First formulate a clear execution plan, then execute step by step in strict accordance with the plan. Do not skip any steps.
            2. Take tool returned results as the sole source of truth.
            3. Never fabricate or invent any instance IDs.
            4. Keep internal reasoning concise and brief.
            5. Prioritize calling tools instead of giving lengthy text explanations.
            6. Complete only one small independent operation with one tool at a time. Do not call multiple tools in a single step.
            7. Check the scene status at appropriate times.
    """),
    },
    {
        "role": "user",
        "content": ("""
            Retrieve an IndustrialRobot, Pallet and a Box, place them at [4.2,0.8,0.0], [4.4,1.0,0.0] and [4.5,1.1,0.0]. Set a supporting relation that the Box is fully supported by the Pallet. Then move the IndustrialRobot to [5.2,0.8,0.0]. Finally delete the Box. And give the final scene status."""
            ),
    },
]

# =====================================================
# Multi-turn Tool Calling Loop
# =====================================================

for step in range(MAX_ITER):

    print(f"\n================ STEP {step} ================\n")
    # =================================================
    # LLM Request
    # =================================================
    tools = [tool.schema for tool in TOOL_REGISTRY.values()]
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=tools,
        tool_choice="auto",
        temperature=0.2,
        # vLLM + Qwen important  不思考直接输出结果
        # extra_body={
        #     "chat_template_kwargs": {
        #         "enable_thinking": False
        #     }
        # }
    )

    message = response.choices[0].message
    
    print("===== ASSISTANT MESSAGE =====")
    print(message)
    clean_content = re.sub(
                    r"<think>.*?</think>",
                     "",
                     message.content or "",
                     flags=re.DOTALL | re.IGNORECASE,
                     ).strip()
    print("===== ASSISTANT MESSAGE (cleaned) =====")
    print(clean_content)

    # =================================================
    # Append assistant message
    # =================================================

    messages.append({
        "role": "assistant",
        "content": clean_content,
        "tool_calls": message.tool_calls,
    })
    # =================================================
    # No Tool Call -> Finish
    # =================================================

    if not message.tool_calls:

        print("\n===== FINAL RESPONSE =====")
        print(message.content)
        break

    # =================================================
    # Execute Tool Calls
    # =================================================

    for tool_call in message.tool_calls:

        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments or "{}")

        print("\n===== TOOL CALL =====")
        print("tool_name =", tool_name)
        print("arguments =", arguments)
        

        # =============================================
        # Find Tool
        # =============================================
        tool = TOOL_REGISTRY[tool_name]
        # =============================================
        # Execute Tool
        # =============================================

        result = tool(
            context=context,
            **arguments
        )

        result_dict = result.to_dict()

        print("\n===== TOOL RESULT =====")
        print(json.dumps(result_dict, ensure_ascii=False, indent=2))

        # =============================================
        # Append Tool Result
        # =============================================

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": tool_name,
            "content": json.dumps(result_dict, ensure_ascii=False, indent=2),
        })
        
        last_tool_name = tool_name
else:
    print("\nReached MAX_ITER")