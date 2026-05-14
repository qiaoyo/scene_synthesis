import json
from openai import OpenAI
import sys
from pathlib import Path

# =====================================================
# Import ALL Tools
# =====================================================

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import scene_layout_rag.tools

from scene_layout_rag.config import ProjectConfig
from scene_layout_rag.scene_state import SceneStateManager
from scene_layout_rag.rag import AssetRAG

from scene_layout_rag.tools.base import (
    TOOL_REGISTRY,
    ToolContext,
    list_openai_tools,
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
cfg.enable_faiss = False

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
            "Retrieve an indoor AGV and place it "
            "at [1.0, 2.0, 0.0]"
        ),
    }
]

# =====================================================
# Multi-turn Tool Calling Loop
# =====================================================

MAX_ITER = 10

for step in range(MAX_ITER):

    print(f"\n================ STEP {step} ================\n")

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=list_openai_tools(),
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