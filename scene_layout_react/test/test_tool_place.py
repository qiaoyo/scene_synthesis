import json
from openai import OpenAI
import sys
from pathlib import Path
import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
# =====================================================
# Import ALL Tools
# =====================================================
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scene_layout_react.config import ProjectConfig
from scene_layout_react.scene_state import SceneStateManager
from scene_layout_react.rag import AssetRAG
from scene_layout_react.tools.base import (
    TOOL_REGISTRY,
    ToolContext,
)
# =====================================================
# OpenAI Client
# =====================================================
client = OpenAI(
    api_key="EMPTY",
    base_url="http://127.0.0.1:8000/v1"
)

MODEL_NAME = "Qwen/Qwen3-32B-AWQ"

# =====================================================
# Context
# =====================================================

cfg = ProjectConfig()
cfg.enable_faiss = True

rag = AssetRAG(cfg)
if (cfg.index_dir / "corpus.jsonl").exists():
    rag.load()
else:
    rag.build(save=True)

context = ToolContext(
    scene=SceneStateManager(),
    rag=rag,
)

# =====================================================
# Messages
# =====================================================

messages = [
    {
        "role": "system",
        "content": (
            "You are an industrial scenario layout assistant.\n"
            "You should:\n"
            "1. retrieve assets first\n"
            "2. then place instances into scene\n"
        ),
    },
    {
        "role": "user",
        "content": (
    """Retrieve a workbench and place it at [1.0, 2.0, 0.0], then retrieve a robot and place it at [10,10,10], then retrieve a conveyor and place it at [0,0,0], Finally, save the usd.
    """
        ),
    }
]

# =====================================================
# Multi-turn Tool Calling Loop
# =====================================================

MAX_ITER = 10
tool_specs = [tool.schema for tool in TOOL_REGISTRY.values()]
for step in range(MAX_ITER):

    print(f"\n================ STEP {step} ================\n")

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=tool_specs,
        tool_choice="auto",
    )

    message = response.choices[0].message

    print("===== ASSISTANT MESSAGE =====")
    print(message)

    # =================================================
    # Append assistant message
    # =================================================

    messages.append({
        "role": "assistant",
        "content": message.content,
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

        arguments = json.loads(
            tool_call.function.arguments
        )

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
        print(result_dict)

        # =============================================
        # Append Tool Result
        # =============================================

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": tool_name,
            "content": json.dumps(result_dict, ensure_ascii=False),
        })

else:

    print("\nReached MAX_ITER")