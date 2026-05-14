import json
from openai import OpenAI

# =====================================================
# vLLM OpenAI-Compatible API
# =====================================================

client = OpenAI(
    api_key="EMPTY",
    base_url="http://localhost:8000/v1"
)

MODEL_NAME = "Qwen/Qwen3-32B-AWQ"

# =====================================================
# Tool Schema (给LLM看的)
# =====================================================

retrieve_assets_tool = {
    "type": "function",
    "function": {
        "name": "retrieve_assets",
        "description": "检索资产",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "检索需求"
                }
            },
            "required": ["query"]
        }
    }
}

# =====================================================
# Python Tool Function (真正执行)
# =====================================================

def retrieve_assets(query):

    print("\n===== TOOL EXECUTED =====")
    print("query =", query)

    return {
        "result": "office_plant.usd"
    }

# =====================================================
# Tool Registry
#tools=[...]  LLM告诉模型有哪些工具
#TOOLS={...}   真正执行函数
# =====================================================

TOOLS = {
    "retrieve_assets": retrieve_assets
}

# =====================================================
# First LLM Call
# =====================================================

response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {
            "role": "user",
            "content": "帮我找一个办公室植物资产"
        }
    ],
    tools=[retrieve_assets_tool],
    tool_choice="auto"
)

# =====================================================
# Parse Tool Call
# =====================================================

message = response.choices[0].message

print("\n===== RAW MODEL RESPONSE =====")
print(message)

# =====================================================
# Check Tool Calls
# =====================================================

if message.tool_calls:

    tool_call = message.tool_calls[0]

    tool_name = tool_call.function.name

    arguments = json.loads(
        tool_call.function.arguments
    )

    print("\n===== TOOL CALL =====")
    print("tool_name =", tool_name)
    print("arguments =", arguments)

    # =================================================
    # Execute Tool
    # =================================================

    tool_result = TOOLS[tool_name](**arguments)

    print("\n===== TOOL RESULT =====")
    print(tool_result)

else:

    print("\n模型没有调用工具")
    print("模型回复：")
    print(message.content)