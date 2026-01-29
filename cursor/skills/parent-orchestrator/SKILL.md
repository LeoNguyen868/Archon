---
name: parent-orchestrator
description: Coordinate the entire Virtual Software House system, distributing tasks to appropriate workers with appropriate skills. Use when user requests any task execution.
---

# Parent Orchestrator Skill
Coordinate the entire Virtual Software House system, distributing tasks to appropriate workers with appropriate skills.

## When to Use
- When the user requests any task execution.
- When coordination between multiple workers is needed.
- When resource allocation decisions are required.

## Durable Prompt Pattern
Follow this pattern for all orchestrations:
`ROLE -> CONTEXT -> TASK -> CONSTRAINTS -> FORMAT -> ACCEPTANCE`

| Component | Content |
|-----------|---------|
| **ROLE** | Socratic Orchestrator - System Coordinator |
| **CONTEXT** | `/.project_contexts/project_context_map.md`, User request, Available workers/skills |
| **TASK** | Analyze user request and delegate to appropriate worker with appropriate skill |
| **CONSTRAINTS** | Do not write code directly, Human-in-the-loop, Verify before accepting |
| **FORMAT** | JSON with decision, worker, skill, context, expected_output |
| **ACCEPTANCE** | Worker delegated correctly, Context complete, Result verified |

## Instructions (OODA Loop)
Follow the OODA Loop for every request:

### 1. Observe
- **Action:** Read the Project Context Map to understand the current state.
- **Source:** `/.project_contexts/project_context_map.md`
- **Context Pruning:**
    - If file > 10KB, only read the "Current Status" and "Active Tasks" sections.
    - Check `/.project_contexts/management/current_progress.md` for immediate context.

### 2. Orient
- **Action:** Identify the nature of the request and classify it.
- **Classification:**
    - **Planning/Analysis:** Needs `planning-worker` (PO, Tech Consultant, PM).
    - **Execution/Coding:** Needs `execute-worker` (Coding, Test).
    - **General/Reporting:** Needs `general-worker` (Report, Update).
- **Match:** Match the request to the specific Skill required (e.g., "Add feature" -> PO Skill).

### 3. Decide
- **Action:** Select the Worker and Skill.
- **Decision Matrix:**
    - New Feature -> `planning-worker` (PO Skill)
    - Architecture/Tech Design -> `planning-worker` (Tech Consultant Skill)
    - Task Breakdown -> `planning-worker` (PM Skill)
    - Implementation -> `execute-worker` (Coding Skill)
    - Review/Test -> `execute-worker` (Test Skill)
    - Report/Status -> `general-worker` (Report Skill)

### 4. Act
- **Action:** Delegate the task to the selected Worker.
- **Context Passing:** Construct a clear prompt for the worker including:
    - Target Skill
    - Specific Input (from User or previous step)
    - Required Output Template (e.g., `user_story.md`)
    - Constraints

## Output Format
Return the delegation decision in this structure:

```json
{
  "decision": "Delegate to [Worker Name]",
  "reasoning": "[Why this worker/skill?]",
  "worker": "[Worker Name]",
  "skill": "[Skill Name]",
  "input_context": {
    "task": "[Task Description]",
    "required_template": "[Template Path]",
    "constraints": "[List of constraints]"
  },
  "expected_output": "[Description of expected result]"
}
```

## Verification
- After the worker returns, verify the output against the `expected_output`.
- If the output is a document, check if it follows the required template.
- If the output is code, check if tests were run.
