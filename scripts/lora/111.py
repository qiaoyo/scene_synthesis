from transformers import AutoTokenizer

MODEL_PATH = "/media/simple/another_software/cache/huggingface/hub/models--Qwen--Qwen3.5-27B"

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    trust_remote_code=True,
)

print("=" * 80)
print("CHAT TEMPLATE")
print("=" * 80)
print(tokenizer.chat_template)
print("=" * 80)