"""LoRA fine-tuning script for layout planning instructions."""
from __future__ import annotations

import argparse
from pathlib import Path
from random import sample

import torch
from datasets import Dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments

from scene_layout_rag import ProjectConfig, SceneLayoutRAG


def build_instruction_dataset(pipeline: SceneLayoutRAG, max_examples: int = 2000) -> Dataset:
    docs = pipeline.documents
    if max_examples and len(docs) > max_examples:
        docs_subset = sample(docs, max_examples)
    else:
        docs_subset = docs
    records = []
    for doc in docs_subset:
        asset_name = doc.metadata.get("asset_category", doc.doc_id)
        usd_path = doc.metadata.get("usd_path", "未知路径")
        prompt = (
            "你是一个工业场景规划助手。根据以下资产描述，"
            "生成该物体应放置在仓库或车间中的建议位置和理由。\n\n"
            f"资产: {asset_name}\nUSD: {usd_path}\n描述:\n{doc.content}\n"
        )
        response = (
            f"物体: {asset_name} \n位置: 依据功能需求靠近{asset_name}相关区域。"
            f"\nUSD引用: {usd_path}\n rationale: {doc.metadata.get('source', '资产库')}"
        )
        records.append({"prompt": prompt, "response": response})
    return Dataset.from_list(records)


def tokenize_dataset(dataset: Dataset, tokenizer: AutoTokenizer) -> Dataset:
    def preprocess(batch):
        model_inputs = tokenizer(batch["prompt"], truncation=True, padding="max_length")
        labels = tokenizer(text_target=batch["response"], truncation=True, padding="max_length")
        model_inputs["labels"] = labels["input_ids"]
        return model_inputs

    return dataset.map(preprocess, batched=True, remove_columns=dataset.column_names)


def create_model(cfg: ProjectConfig) -> AutoModelForCausalLM:
    kwargs = {
        "device_map": "auto",
    }
    if cfg.model.use_8bit:
        kwargs["load_in_8bit"] = True
    if cfg.model.load_in_4bit:
        kwargs["load_in_4bit"] = True
    model = AutoModelForCausalLM.from_pretrained(cfg.model.llm_name_or_path, **kwargs)
    model = prepare_model_for_kbit_training(model)
    lora_cfg = LoraConfig(
        r=cfg.model.lora_rank,
        lora_alpha=cfg.model.lora_alpha,
        target_modules=["q_proj", "v_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )
    return get_peft_model(model, lora_cfg)


def main() -> None:
    parser = argparse.ArgumentParser(description="Fine-tune the layout LLM using LoRA")
    parser.add_argument("--model", default="mistralai/Mistral-7B-Instruct-v0.2", help="Base model name")
    parser.add_argument("--output", type=Path, default=Path("./outputs/lora-layout"))
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--max-examples", type=int, default=2000)
    args = parser.parse_args()

    cfg = ProjectConfig()
    cfg.model.llm_name_or_path = args.model
    pipeline = SceneLayoutRAG(cfg)
    dataset = build_instruction_dataset(pipeline, max_examples=args.max_examples)

    tokenizer = AutoTokenizer.from_pretrained(args.model, use_fast=False)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenized = tokenize_dataset(dataset, tokenizer)

    model = create_model(cfg)
    training_args = TrainingArguments(
        output_dir=str(args.output),
        per_device_train_batch_size=1,
        gradient_accumulation_steps=16,
        num_train_epochs=args.epochs,
        learning_rate=2e-4,
        fp16=torch.cuda.is_available(),
        save_strategy="epoch",
        logging_steps=10,
        optim="adamw_torch",
    )
    trainer = Trainer(model=model, args=training_args, train_dataset=tokenized, tokenizer=tokenizer)
    trainer.train()
    model.save_pretrained(args.output)
    tokenizer.save_pretrained(args.output)


if __name__ == "__main__":
    main()
