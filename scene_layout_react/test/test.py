from openai import OpenAI
import json
# =========================================================
# vLLM OpenAI-Compatible Server
# =========================================================
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"

MODEL_NAME = "Qwen/Qwen3-32B-AWQ"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

# =========================================================
# Tool Definition (JSON Schema)
# =========================================================
retrieve_assets_tool = {
    "type": "function",
    "function": {
        "name": "retrieve_assets",
        "description": "检索3D资产",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "用户的资产检索需求"
                },
                "top_k": {
                    "type": "integer",
                    "description": "返回结果数量",
                    "default": 5
                }
            },
            "required": ["query"]
        }
    }
}

# =========================================================
# Actual Python Tool Function
# =========================================================

def retrieve_assets(query: str, top_k: int = 5):

    print("\n================ TOOL EXECUTION ================")
    print(f"执行资产检索:")
    print(f"query = {query}")
    print(f"top_k = {top_k}")

    # 模拟数据库 / 向量检索
    mock_database = [
        {
            "name": "office_plant_small",
            "category": "plant",
            "usd_path": "/assets/plants/office_plant_small.usd",
            "description": "适合办公室桌面的绿色小型植物"
        },
        {
            "name": "modern_office_plant",
            "category": "plant",
            "usd_path": "/assets/plants/modern_office_plant.usd",
            "description": "现代办公室装饰植物"
        }
    ]

    result = {
        "hits": mock_database[:top_k]
    }

    print("Tool Result:")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print("================================================\n")

    return result

# =========================================================
# Tool Registry
# =========================================================

#函数列表
TOOLS = {
    "retrieve_assets": retrieve_assets
}
#工具说明书
AVAILABLE_TOOLS = [
    retrieve_assets_tool
]

# =========================================================
# Initial Messages
# =========================================================

messages = [
    {
        "role": "system",
        "content": (
            "你是一个3D场景资产助手。"
            "当用户需要检索资产时，优先调用工具。"
        )
    },
    {
        "role": "user",
        "content": "请帮我检索一个适合放在办公室里的小型植物的资产。"
    }
]

# =========================================================
# Agent Loop
# =========================================================
MAX_ITERATIONS = 1
for step in range(MAX_ITERATIONS):

    print(f"\n================ LLM STEP {step + 1} ================\n")
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=AVAILABLE_TOOLS,
        tool_choice="auto",
        temperature=0
    )
    message = response.choices[0].message

    print("LLM Response:")
    print(message)
    
    # -----------------------------------------------------
    # Case 1: No Tool Call -> Final Answer
    # -----------------------------------------------------
    
    if not message.tool_calls:

        print("\n================ FINAL ANSWER ================\n")
        print(message.content)
        break
    
    # -----------------------------------------------------
    # Case 2: Tool Calls Exist
    # -----------------------------------------------------

    messages.append({
        "role": "assistant",
        "content": message.content,
        "tool_calls": [
            {
                "id": tc.id,
                "type": tc.type,
                "function": {
                    "name": tc.function.name,
                    "arguments": tc.function.arguments
                }
            }
            for tc in message.tool_calls
        ]
    })
    
    # -----------------------------------------------------
    # Execute All Tools
    # -----------------------------------------------------
    for tool_call in message.tool_calls:

        tool_name = tool_call.function.name

        print(f"\nTool Requested: {tool_name}")

        # -------------------------------------------------
        # Tool Exists?
        # -------------------------------------------------

        if tool_name not in TOOLS:

            tool_result = {
                "error": f"Tool '{tool_name}' not found."
            }

        else:

            try:
                # -----------------------------------------
                # Parse Tool Arguments
                # -----------------------------------------
                # 原始字符串参数
                raw_arguments = tool_call.function.arguments

                print("Raw Arguments:")
                print(raw_arguments)
                
                # 解析成字典参数
                arguments = json.loads(raw_arguments)

                print("Parsed Arguments:")
                print(arguments)

                # -----------------------------------------
                # Execute Tool
                # -----------------------------------------

                tool_function = TOOLS[tool_name]

                tool_result = tool_function(**arguments)

            except Exception as e:

                tool_result = {
                    "error": str(e)
                }

        # -------------------------------------------------
        # Append Tool Result Back To Messages
        # -------------------------------------------------

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": tool_name,
            "content": json.dumps(
                tool_result,
                ensure_ascii=False
            )
        })

# =========================================================
# Debug: Final Full Conversation
# =========================================================

print("\n================ FULL MESSAGE HISTORY ================\n")

for i, msg in enumerate(messages):

    print(f"\n--- Message {i + 1} ---")
    print(json.dumps(msg, indent=2, ensure_ascii=False))