---
name: delegation
description: Delegate tasks to subagents with clear context and instructions. Use when distributing work.
---

# Delegation Skill
Skill for delegating tasks to subagents (workers) with clear context and instructions.

## Role Rules (Strict Permissions)
- **Primary Permissions:** Task initiation, context preparation, worker selection.
- **Requirement:** Must follow the strict instruction format for all handoffs.
- **Instruction Format:** Every delegation MUST include:
    - **Role:** The specific role the agent should assume.
    - **Required Skill:** The primary skill the agent must use.
    - **Task:** A detailed description of the task.
    - **Context:** List of files and directories the agent needs access to.
    - **Constraints:** Any rules the agent must follow.

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
- **Construct Instruction:** Create a clear prompt/task description using the strict format:
    ```
    Role: [Agent Role]
    Required Skill: [Skill Name]
    Task: [Detailed Task Description]
    Context: [Paths]
    Constraints: [Rules]
    ```
- **Isolate:** Ensure the worker receives only necessary context to avoid pollution.
- **Handoff:** Transfer the task using the `Task` tool.
