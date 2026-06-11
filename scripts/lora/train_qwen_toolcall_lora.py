from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import torch
from datasets import Dataset
from peft import LoraConfig, TaskType, get_peft_model, prepare_model_for_kbit_training
from torch.nn.utils.rnn import pad_sequence
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    Trainer,
    TrainingArguments,
)


IGNORE_INDEX = -100


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Train a Qwen tool-call LoRA adapter for scene_layout_react."
    )
    parser.add_argument(
        "--data-path",
        type=Path,
        default=Path("data/lora/toolcall_sft_sample.json"),
        help="JSON or JSONL file containing messages and assistant tool-call targets.",
    )
    parser.add_argument(
        "--model-name-or-path",
        type=str,
        default="Qwen/Qwen3.5-27B",
        help="Base Qwen model path or Hugging Face model id.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs/lora/qwen_toolcall_lora"),
        help="Directory for LoRA checkpoints and final adapter.",
    )
    parser.add_argument("--max-length", type=int, default=4096)
    parser.add_argument("--epochs", type=float, default=3.0)
    parser.add_argument("--learning-rate", type=float, default=2e-4)
    parser.add_argument("--batch-size", type=int, default=1)
    parser.add_argument("--gradient-accumulation-steps", type=int, default=8)
    parser.add_argument("--warmup-ratio", type=float, default=0.03)
    parser.add_argument("--logging-steps", type=int, default=1)
    parser.add_argument("--save-steps", type=int, default=20)
    parser.add_argument("--no-4bit", action="store_true", help="Disable QLoRA 4-bit loading.")
    parser.add_argument("--bf16", action="store_true", help="Use bf16 training.")
    parser.add_argument("--fp16", action="store_true", help="Use fp16 training.")
    parser.add_argument(
        "--gradient-checkpointing",
        action="store_true",
        help="Enable gradient checkpointing to reduce memory use.",
    )
    return parser.parse_args()


def load_records(path: Path) -> list[dict[str, Any]]:
    path = path.expanduser()
    if path.suffix == ".jsonl":
        records = []
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                records.append(json.loads(line))
        return records

    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and isinstance(payload.get("samples"), list):
        return payload["samples"]
    if isinstance(payload, dict) and isinstance(payload.get("messages"), list):
        return [payload]
    raise ValueError(f"Unsupported dataset format: {path}")


def normalize_record(record: dict[str, Any]) -> dict[str, Any]:
    messages = record.get("messages")
    if not isinstance(messages, list) or len(messages) < 2:
        raise ValueError("Each record must contain a messages list.")
    if messages[-1].get("role") != "assistant":
        raise ValueError("The last message must be the assistant target.")
    if not isinstance(messages[-1].get("content"), str):
        target = record.get("expected_output")
        if target is None:
            raise ValueError("Assistant target must be content string or expected_output.")
        messages = [dict(item) for item in messages]
        messages[-1]["content"] = json.dumps(target, ensure_ascii=False, separators=(",", ":"))
    return {"messages": messages}


def render_chat(tokenizer: Any, messages: list[dict[str, str]], add_generation_prompt: bool) -> str:
    if tokenizer.chat_template:
        return tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=add_generation_prompt,
        )

    chunks = []
    for message in messages:
        role = message["role"]
        content = message["content"]
        chunks.append(f"<|{role}|>\n{content}\n")
    if add_generation_prompt:
        chunks.append("<|assistant|>\n")
    return "".join(chunks)


def tokenize_record(
    record: dict[str, Any],
    tokenizer: Any,
    max_length: int,
) -> dict[str, list[int]]:
    messages = record["messages"]
    prompt_text = render_chat(tokenizer, messages[:-1], add_generation_prompt=True)
    full_text = render_chat(tokenizer, messages, add_generation_prompt=False)

    prompt_ids = tokenizer(prompt_text, add_special_tokens=False)["input_ids"]
    full_ids = tokenizer(full_text, add_special_tokens=False)["input_ids"]

    if tokenizer.eos_token_id is not None:
        full_ids = full_ids + [tokenizer.eos_token_id]

    labels = list(full_ids)
    prompt_len = min(len(prompt_ids), len(labels))
    labels[:prompt_len] = [IGNORE_INDEX] * prompt_len

    if len(full_ids) > max_length:
        full_ids = full_ids[-max_length:]
        labels = labels[-max_length:]
        if all(label == IGNORE_INDEX for label in labels):
            raise ValueError(
                "max_length truncated away the assistant target. Increase --max-length."
            )

    return {
        "input_ids": full_ids,
        "attention_mask": [1] * len(full_ids),
        "labels": labels,
    }


@dataclass
class DataCollatorForAssistantOnlyLM:
    tokenizer: Any

    def __call__(self, features: list[dict[str, list[int]]]) -> dict[str, torch.Tensor]:
        input_ids = [
            torch.tensor(feature["input_ids"], dtype=torch.long)
            for feature in features
        ]
        attention_mask = [
            torch.tensor(feature["attention_mask"], dtype=torch.long)
            for feature in features
        ]
        labels = [
            torch.tensor(feature["labels"], dtype=torch.long)
            for feature in features
        ]

        return {
            "input_ids": pad_sequence(
                input_ids,
                batch_first=True,
                padding_value=self.tokenizer.pad_token_id,
            ),
            "attention_mask": pad_sequence(
                attention_mask,
                batch_first=True,
                padding_value=0,
            ),
            "labels": pad_sequence(
                labels,
                batch_first=True,
                padding_value=IGNORE_INDEX,
            ),
        }


def main() -> int:
    args = parse_args()

    tokenizer = AutoTokenizer.from_pretrained(
        args.model_name_or_path,
        trust_remote_code=True,
        use_fast=True,
    )
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token

    records = [normalize_record(record) for record in load_records(args.data_path)]
    tokenized_records = [
        tokenize_record(record, tokenizer, max_length=args.max_length)
        for record in records
    ]
    dataset = Dataset.from_list(tokenized_records)

    quantization_config = None
    if not args.no_4bit:
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=torch.bfloat16 if args.bf16 else torch.float16,
        )

    model = AutoModelForCausalLM.from_pretrained(
        args.model_name_or_path,
        trust_remote_code=True,
        device_map="auto",
        quantization_config=quantization_config,
        torch_dtype=torch.bfloat16 if args.bf16 else torch.float16,
    )
    model.config.use_cache = False

    if not args.no_4bit:
        model = prepare_model_for_kbit_training(model)
    if args.gradient_checkpointing:
        model.gradient_checkpointing_enable()

    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        bias="none",
        target_modules=[
            "q_proj",
            "k_proj",
            "v_proj",
            "o_proj",
            "gate_proj",
            "up_proj",
            "down_proj",
        ],
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    training_args = TrainingArguments(
        output_dir=str(args.output_dir),
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        learning_rate=args.learning_rate,
        warmup_ratio=args.warmup_ratio,
        logging_steps=args.logging_steps,
        save_steps=args.save_steps,
        save_total_limit=3,
        bf16=args.bf16,
        fp16=args.fp16,
        optim="paged_adamw_8bit" if not args.no_4bit else "adamw_torch",
        lr_scheduler_type="cosine",
        report_to="none",
        remove_unused_columns=False,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        data_collator=DataCollatorForAssistantOnlyLM(tokenizer),
    )
    trainer.train()
    trainer.save_model(str(args.output_dir))
    tokenizer.save_pretrained(str(args.output_dir))

    print(f"[lora] saved adapter to {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())