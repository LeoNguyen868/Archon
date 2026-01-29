---
name: tech-consultant
description: Design technical solutions, create Tech Specs, ADRs, and diagrams. Use when technical architecture or design is needed.
---

# Tech Consultant Skill
Skill for designing technical solutions, creating Tech Specs, ADRs, and diagrams.

## When to Use
- When clear User Stories/Requirements are available.
- When system architecture decisions are needed.
- When technical trade-offs analysis is required.
- When data structures and API contracts need to be defined.

## Instructions
- **Mental Model:** Trade-off Analysis (Pros/Cons), Security First, KISS, YAGNI.
- **Action:**
    1.  **Analyze:** Read User Story and requirements.
    2.  **Design:** Design data structures, API contracts, and modules.
    3.  **Trade-offs:** Evaluate options (Why this? Why not that?).
    4.  **ADR:** Record key architectural decisions in `/.project_contexts/arch/adrs/` using `cursor/templates/adr.md`.
    5.  **Tech Spec:** Create detailed technical documentation in `/.project_contexts/arch/tech_specs/` using `cursor/templates/tech_spec.md`.
    6.  **Diagram:** Draw diagrams (C4 model) in `/.project_contexts/arch/diagrams/` (using Mermaid).
    7.  **Update Changelog:** MANDATORY - After completing the task, update changelog at `/.project_contexts/dev/change_logs/[YYYY-MM-DD].md` with entry describing the architecture work completed.
    8.  **Update Progress:** MANDATORY - Update `/.project_contexts/management/current_progress.md` to reflect completed architecture work.
- **Outputs:**
    - Tech Specs
    - ADRs (Architecture Decision Records)
    - Architecture Diagrams
    - Changelog entry (MANDATORY)
    - Progress update (MANDATORY)
- **Constraints:**
    - Ensure feasibility for implementation.
    - Do not write production code (only prototypes if needed to prove a concept).
    - Always consider Security.
- **Post-Task Requirements:** Before returning to orchestrator, ensure changelog and progress files are updated.
