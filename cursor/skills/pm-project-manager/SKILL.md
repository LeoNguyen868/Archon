---
name: pm-project-manager
description: Manage project progress, break down tasks, create backlogs, and track dependencies. Use for planning and tracking.
---

# Project Manager Skill
Skill for managing progress, breaking down tasks, creating backlogs, and tracking dependencies.

## When to Use
- When a Tech Spec is available.
- When implementation planning is needed (Sprint Planning).
- When tracking progress and reporting.
- When managing the backlog.

## Instructions
- **Mental Model:** Decomposition, Critical Path, Risk Management.
- **Action:**
    1.  **Decompose:** Break down the Tech Spec into small, manageable tasks (implementation tickets).
    2.  **Estimate:** Estimate complexity/time for each task.
    3.  **Dependencies:** Identify dependencies between tasks.
    4.  **Backlog:** Create/Update Sprint Backlog at `/.project_contexts/management/backlogs/`.
    5.  **Ticket:** Create an Implementation Ticket for the active task using `cursor/templates/implementation_ticket.md`.
    6.  **Roadmap:** Update the Roadmap.
    7.  **Update Changelog:** MANDATORY - After completing the task, update changelog at `/.project_contexts/dev/change_logs/[YYYY-MM-DD].md` with entry describing the planning work completed.
    8.  **Update Progress:** MANDATORY - Update `/.project_contexts/management/current_progress.md` to reflect completed planning work.
- **Outputs:**
    - Sprint Backlog
    - Implementation Tickets
    - Roadmap updates
    - Changelog entry (MANDATORY)
    - Progress update (MANDATORY)
- **Constraints:**
    - Ensure tasks are small enough for Devs to complete in a short time.
    - Ensure tasks have clear Acceptance Criteria (from PO).
- **Post-Task Requirements:** Before returning to orchestrator, ensure changelog and progress files are updated.
