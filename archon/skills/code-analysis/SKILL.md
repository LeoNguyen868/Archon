---
name: code-analysis
description: Analyze existing code for patterns, dependencies, and structure. Use when understanding code is needed.
---

# Code Analysis Skill
Skill for analyzing existing codebase to understand patterns, dependencies, and architecture.

## When to Use
- When starting work on an unfamiliar codebase.
- When planning refactoring efforts.
- When identifying dependencies before changes.
- When looking for similar implementations.

## Instructions
- **Analysis Techniques:**
    1. **Structure Analysis:** Map file/directory organization.
    2. **Dependency Analysis:** Identify imports, packages, and external dependencies.
    3. **Pattern Recognition:** Find design patterns and coding conventions used.
    4. **Hotspot Analysis:** Identify frequently changed or complex files.
- **Tools:**
    - Use `grep`, `find` for text searches.
    - Use `codebase_search` for semantic search.
    - Use static analysis tools if available (linters, type checkers).
- **Output:**
    - Codebase overview document.
    - Dependency graph (if needed).
    - Recommendations for improvements.
- **Constraints:**
    - Read-only analysis. Do not modify code during analysis.
    - Focus on relevant areas to the current task.
    - Document findings clearly for other workers.
