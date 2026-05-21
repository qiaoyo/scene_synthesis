from __future__ import annotations
import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
import json
import re
import sys
from pathlib import Path

from openai import OpenAI

# =====================================================
# Import Project
# =====================================================

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scene_layout_react.config import ProjectConfig
from scene_layout_react.rag import AssetRAG
from scene_layout_react.scene_state import SceneStateManager

from scene_layout_react.tools.base import (
    TOOL_REGISTRY,
    ToolContext,
)

# =====================================================
# Constants
# =====================================================

MAX_ITER = 20

TEST_TOOL_NAMES = [
    "retrieve_tool",
    "place_instance",
    "query_scene",
    "set_support",
    "check_collision",
    "check_support",
    "simulate_step",
]

# =====================================================
# OpenAI Client
# =====================================================

cfg = ProjectConfig()

client = OpenAI(
    api_key=cfg.llm_api_key,
    base_url=cfg.llm_api_base_url,
)

# =====================================================
# RAG
# =====================================================

rag = AssetRAG(cfg)

if (cfg.index_dir / "corpus.jsonl").exists():
    rag.load()
else:
    rag.build(save=True)

# =====================================================
# Context
# =====================================================

cfg.isaac_worker_path = (
    Path(__file__).resolve().parents[2]
    / "scene_layout_react"
    / "physics"
    / "worker.py"
)

context = ToolContext(
    scene=SceneStateManager(),
    rag=rag,
    config=cfg,
    physics_enabled=True,
)

# =====================================================
# Tools
# =====================================================

tools = [
    TOOL_REGISTRY[name].schema
    for name in TEST_TOOL_NAMES
]

# =====================================================
# Messages
# =====================================================

messages = [
    {
        "role": "system",
        "content": """
            You are an industrial scene planning assistant.

            Strict Rules:
            1. Use tools as the only execution method.
            2. Never fabricate ids or physics results.
            3. Use exactly the values returned by tools.
            4. One tool call per step.
            5. Prefer short responses.
            6. Complete the following workflow in order:
            - retrieve pallet
            - retrieve box
            - place pallet
            - place box on pallet
            - set support
            - query scene
            - check collision
            - check support
            - simulate_step
            7. simulate_step arguments:
            duration=1.0
            dt=0.01
            write_back=true
            8. Final response should summarize all tool results.
            """,
                },
                {
                    "role": "user",
                    "content": """
            Run a full physics workflow smoke test.
            Steps:
            1. Retrieve one Pallet.
            2. Retrieve one Box.
            3. Place the Pallet.
            4. Place the Box on top of the Pallet.
            5. Set support relation.
            6. Query scene.
            7. Check collision.
            8. Check support.
            9. Run simulate_step.
            10. Return final report.
            """,
    },
]

# =====================================================
# Tool Calling Loop
# =====================================================

for step in range(MAX_ITER):

    print(f"\n================ STEP {step} ================\n")

    # =================================================
    # LLM Request
    # =================================================

    response = client.chat.completions.create(
        model=cfg.model,
        messages=messages,
        tools=tools,
        tool_choice="auto",
        temperature=0.2,
    )

    message = response.choices[0].message

    # =================================================
    # Assistant Message
    # =================================================

    clean_content = re.sub(
        r"<think>.*?</think>",
        "",
        message.content or "",
        flags=re.DOTALL | re.IGNORECASE,
    ).strip()

    print("===== ASSISTANT MESSAGE =====")
    print(clean_content)

    messages.append({
        "role": "assistant",
        "content": clean_content,
        "tool_calls": message.tool_calls,
    })

    # =================================================
    # Finish
    # =================================================

    if not message.tool_calls:

        print("\n===== FINAL RESPONSE =====")
        print(clean_content)
        break

    # =================================================
    # Execute Tool
    # =================================================

    for tool_call in message.tool_calls:

        tool_name = tool_call.function.name
        arguments = json.loads(
            tool_call.function.arguments or "{}"
        )

        print("\n===== TOOL CALL =====")
        print("tool_name =", tool_name)
        print("arguments =")
        print(json.dumps(arguments, ensure_ascii=False, indent=2))

        # =============================================
        # Execute
        # =============================================

        tool = TOOL_REGISTRY[tool_name]

        result = tool(
            context=context,
            **arguments,
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
            "content": json.dumps(
                result_dict,
                ensure_ascii=False,
                indent=2,
            ),
        })

else:
    print("\nReached MAX_ITER")

    print("\n===== FINAL SCENE =====")
    print(json.dumps(
        context.scene.to_dict(),
        ensure_ascii=False,
        indent=2,
    ))