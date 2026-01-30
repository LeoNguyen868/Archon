---
name: initialization
description: Initialize project structure and analyze existing project context. Use when starting new projects or setting up Archon system.
---

# Initialization Skill

Skill for orchestrator understand project initialization intent and coordinate workers to set up project structure and context.

## When to Use
- **ONLY** when user requests to initialize a new project with Archon system
- **ONLY** when `.project_contexts/` directory does NOT exist in the target project
- **NEVER** use when project structure already exists - use update-project skill instead

## Orchestrator Instructions

### Step 1: Understand Initialization Intent
Read this skill to understand that initialization requires:
- Creating project structure
- Analyzing existing project context
- Setting up initial documentation

### Step 2 & 3: Parallel Delegation (SAFE Parallel Option)
**For faster initialization, orchestrator can run these in parallel with SAFE constraints:**

**Parallel Delegation Format:**
```
Delegate simultaneously:
- Role: General Worker | Required Skill: update-project | Task: Create .project_contexts/ directories ONLY (no files)
- Role: General Worker | Required Skill: research | Task: Analyze existing project context (read-only)
Constraints: 
- Structure worker: Create directories ONLY, skip file creation
- Research worker: Read-only analysis, no file modifications
- Both workers must complete before context writing
```

**Sequential Alternative (SAFEST):**
- Step 2: Delegate General Worker (update-project) → Create complete structure
- Step 3: Delegate General Worker (research) → Analyze project
- Step 4: Review both results
- Step 5: Delegate General Worker (update-project) → Write context

### Step 4: Review Worker Results
Verify that:
- Directory structure was created successfully
- Research findings are comprehensive and accurate
- All required information was extracted

### Step 5: Delegate to General Worker (update-project skill)
**Delegation Format:**
- **Role:** General Worker
- **Required Skill:** update-project
- **Task:** Write project_context_map.md with real project information
- **Context:** Research findings + created directory structure
- **Constraints:** Use real project data, not generic placeholders

### Step 6: Final Verification
- Verify project_context_map.md contains meaningful project information
- Confirm all directories are properly structured
- Ensure .cursorignore was created
- Present initialization results to user

## Expected Worker Outputs

### From Step 2 (update-project):
- Complete .project_contexts/ directory structure
- All required subdirectories created
- .cursorignore file created

### From Step 3 (research):
- Project analysis document with:
  - Project name and description
  - Technology stack identification
  - Key objectives extracted from README/docs
  - Architecture overview

### From Step 5 (update-project):
- Rich project_context_map.md with real project information
- Updated current_progress.md with initialization status
- All template files populated with project-specific content

## Decision Flow
```
User requests "Initialize project"
     ↓
Orchestrator reads initialization skill
     ↓
SAFE Parallel Option:
     ├─ General Worker (update-project) → Create directories ONLY
     └─ General Worker (research) → Read-only analysis
     ↓
Wait for both workers to complete
     ↓
Review both results
     ↓
Delegate General Worker (update-project) → Write context files
     ↓
Verify and present to user

OR SAFEST Sequential Option:
     ↓
Delegate General Worker (update-project) → Create complete structure
     ↓
Delegate General Worker (research) → Analyze project
     ↓
Review results
     ↓
Delegate General Worker (update-project) → Write context
     ↓
Verify and present to user
```

## Parallel Safety Rules
- **Rule 1:** Structure creation must be directories-only during parallel phase
- **Rule 2:** Research must be read-only during parallel phase
- **Rule 3:** Context writing happens only after both complete
- **Rule 4:** Use sequential if any doubt about file conflicts
- **Rule 5:** Always verify directory creation before file writing

## Notes
- **Orchestrator Role:** This skill guides orchestrator on how to coordinate initialization, not for direct execution
- **Worker Coordination:** Orchestrator must delegate specific tasks to appropriate workers
- **Context Analysis:** Critical step - initialization must understand existing project, not just create empty structure
- **Verification:** Orchestrator must verify each worker's output before proceeding to next step

