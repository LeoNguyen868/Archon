---
name: debug
description: Analyze errors, trace root causes, and propose fixes. Use when code fails or behaves unexpectedly.
---

# Debug Skill
Skill for analyzing errors, tracing root causes, and proposing fixes.

## When to Use
- When script/code execution encounters an error.
- When tests fail.
- When behaviors are not as expected.

## Instructions
- **Observe:** Read error logs, stack traces.
- **Reproduce:** Create a minimal reproduction case if needed.
- **Analyze:** Trace back from the error point to find the root cause (Root Cause Analysis).
- **Hypothesize:** Formulate a hypothesis about the cause.
- **Verify:** Test the hypothesis.
- **Fix:** Propose a fix and verify it.
- **Report:** MANDATORY - Record the cause and fix in changelog at `/.project_contexts/dev/change_logs/[YYYY-MM-DD].md`.
- **Update Progress:** MANDATORY - Update `/.project_contexts/management/current_progress.md` to reflect completed debugging work.
- **Post-Task Requirements:** Before returning to orchestrator, ensure changelog and progress files are updated with detailed root cause analysis and fix description.
