import json
from openai import OpenAI
import sys
from pathlib import Path
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
#  Context
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
# LLM Call
# =====================================================

response = client.chat.completions.create(
    model=MODEL_NAME,

    messages=[
        {
            "role": "system",
            "content": "You are an industrial scenario layout generation assistant. First, invoke tools to retrieve assets according to commands.",
        },
        {
            "role": "user",
            "content": """
            Please help me retrieve 1 agv asset:
            """
        }
    ],

    # 自动获取所有工具
    tools=list_openai_tools(),

    tool_choice="auto"
)
print("OpenAI Tools:")
tos = list_openai_tools()
for to in tos:
    print("tool name:", to["function"]["name"])
# =====================================================
# Parse Response
# =====================================================

message = response.choices[0].message

print("\n===== RAW RESPONSE =====")
print(message)

# =====================================================
# Tool Calling
# =====================================================

if message.tool_calls:

    for tool_call in message.tool_calls:

        tool_name = tool_call.function.name

        arguments = json.loads(
            tool_call.function.arguments
        )

        print("\n===== TOOL CALL =====")
        print("tool_name =", tool_name)
        print("arguments =", arguments)

        # =================================================
        # Find Tool
        # =================================================

        tool = TOOL_REGISTRY[tool_name]

        # =================================================
        # Execute Tool
        # =================================================

        result = tool(
            context=context,
            **arguments
        )

        print("\n===== TOOL RESULT =====")
        print(result.to_dict())
        hits = result.data.get("catch", [])
        if hits and len(hits) > 0:
            print(len(hits), "catch found")
            for hit in hits:
                print("scene_id =", hit.get("scene_id"))
                print("doc_id =", hit.get("doc_id"))
        else:
            print("no catch")

else:

    print("\n模型没有调用工具")
    print(message.content)