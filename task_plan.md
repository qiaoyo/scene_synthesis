# Task Plan

Objective: implement a batch LoRA workflow regeneration tool for data/lora/raw/planner_toolcall_sft_preview.json. The tool should build retrieve/place seeds per episode, infer deterministic support relations, run runtime/generate_tool_workflow_messages.py with max_repair_rounds=20, validate fixed workflow outputs, merge only successful LoRA records, and record failures for manual review without second-round replacement.

## Phases

- [x] Inspect raw preview data shape and generator requirements
- [x] Implement runtime/batch_regenerate_tool_workflow_messages.py
- [x] Implement deterministic support extraction and command fallback
- [x] Implement per-episode seed writing and generator invocation
- [x] Implement validation for fixed workflow, recent tool suggestions, and final save preconditions
- [x] Smoke-test seed building and a real generator success/failure path
- [x] Summarize output files, failure behavior, and full-run command

## Constraints

- Do not edit data/lora/planning_data.json or data/lora/correction_data.json.
- Do not edit data/lora/raw/planner_toolcall_sft_preview.json.
- Keep temporary/generated files under runtime/tmp.
- Use /home/simple/isaac_env.
- Do not perform second-round replacement in the batch tool.
- Final save record must use include_physics=false.
