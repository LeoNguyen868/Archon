---
name: report
description: Generate progress reports, summaries, and status updates. Use when reporting to user.
---

# Report Skill
Skill for synthesizing information, creating progress reports, and status updates.

## When to Use
- When the user requests a "Progress Report".
- At the end of each Phase.
- When facing blockers that need escalation.

## Instructions
- **Gather Data:**
    - Run `python ~/.cursor/skills/report/scripts/generate_report.py --format markdown --output [path]`
    - Read `current_progress.md`.
    - Read `active_tasks`.
    - Read `change_logs`.
- **Synthesize:** Synthesize information consistently and concisely (80/20).
- **Format:** Use status report templates or Markdown tables.
- **Output:** Report containing:
    - Status (Green/Yellow/Red).
    - Completed items.
    - Ongoing items.
    - Blockers/Risks.
    - Decisions needed.

## Usage
Run Python script to generate report:
`python ~/.cursor/skills/report/scripts/generate_report.py --format markdown --output report.md`

## Notes
- Script must be executed from the skill's root directory
- Ensure read permissions to context files in `/.project_contexts/`
- Output will be written to file or stdout if no output specified
