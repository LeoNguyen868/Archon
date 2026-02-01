---
name: coding
description: Write production code according to tech specs and implementation tickets. Use when code implementation is needed.
---

# Coding Skill
Skill for writing production code according to technical specifications and implementation tickets.

## When to Use
- When an Implementation Ticket is assigned.
- When a Tech Spec is available and ready for implementation.
- When bug fixes require code changes.
- When refactoring is needed.

## Instructions
- **Preparation:**
    1. Read the Implementation Ticket from `/.project_contexts/management/backlogs/active.md`.
    2. Read the related Tech Spec from `/.project_contexts/arch/tech_specs/`.
    3. Understand acceptance criteria before coding.
- **Implementation:**
    1. Follow coding best practices (Clean Code, DRY, KISS).
    2. Write self-documenting code with meaningful names.
    3. Add comments for complex logic.
    4. Handle edge cases and errors gracefully.
- **Quality:**
    1. Write unit tests alongside code (or use TDD).
    2. Run linting and formatting tools.
    3. Ensure no secrets or sensitive data in code.
- **Documentation:**
    1. **Update Changelog:** MANDATORY - Update changelog at `/.project_contexts/dev/change_logs/[YYYY-MM-DD].md` with detailed entry describing code changes, files modified, and impact.
    2. Update documentation if API changes.
    3. **Update Progress:** MANDATORY - Update `/.project_contexts/management/current_progress.md` to reflect completed implementation work.
- **Output:**
    - Working code files
    - Unit tests
    - Changelog entry (MANDATORY)
    - Progress update (MANDATORY)
- **Constraints:**
    - Follow the Tech Spec exactly. If changes are needed, escalate to Tech Consultant first.
    - Report blockers immediately to Parent Agent.
    - Do not merge/commit without review approval.
- **Post-Task Requirements:** Before returning to orchestrator, ensure changelog and progress files are updated. Changelog must include: date, task description, files changed, and impact summary.
