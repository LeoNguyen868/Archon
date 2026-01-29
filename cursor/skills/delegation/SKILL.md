---
name: delegation
description: Delegate tasks to subagents with clear context and instructions. Use when distributing work.
---

# Delegation Skill
Skill for delegating tasks to subagents (workers) with clear context and instructions.

## When to Use
- When the Parent Agent needs to distribute tasks.
- When work needs to be broken down for specialized agents.
- When the current context is too large and needs isolation.

## Instructions
- **Prepare Context:**
    - Identify required inputs (files, requirements).
    - Identify required outputs (expected artifacts).
    - Identify constraints.
- **Select Worker:** Choose the suitable worker based on skill set (e.g., Planning Worker for planning, Execute Worker for coding).
- **Construct Instruction:** Create a clear prompt/task description.
- **Isolate:** Ensure the worker receives only necessary context to avoid pollution.
- **Handoff:** Transfer the task and wait for results (or run in background).
