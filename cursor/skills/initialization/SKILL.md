---
name: initialization
description: Initialize project structure and templates. Use for setting up new projects.
---

# Initialization Skill

Skill for initializing project structure and template files.

## When to Use
- **ONLY** when starting a completely new project (Inception Phase)
- **ONLY** when `.project_contexts/` directory does NOT exist in the target project
- **NEVER** use when project structure already exists - use `update-project` skill instead

## Decision Flow
```
1. Check if .project_contexts/ exists in target project
   - YES → Use update-project skill, NOT initialization
   - NO → Continue with initialization

2. Run init script from ~/.cursor/ to target project directory
   - Script creates .project_contexts/ structure in user's project
   - Script copies templates from skill assets
   - Script creates .cursorignore
```

## Instructions
- **Action:** Run the `init_project.py` script to create the `/.project_contexts/` structure and template files.
- **Source:** Script must be called from `~/.cursor/skills/initialization/scripts/init_project.py`
- **Target:** Initialize project structure in user's current working directory
- **Verification:** Check for the existence of directories and files after running.
- **Critical:** This skill should ONLY be used once per project lifecycle

## Usage
Run Python script from user's project directory:
`python ~/.cursor/skills/initialization/scripts/init_project.py --root .`
or from any location:
`python ~/.cursor/skills/initialization/scripts/init_project.py --root /path/to/user/project`

## Notes
- **Script Location:** `~/.cursor/skills/initialization/scripts/init_project.py`
- **Target Directory:** User's project directory (NOT ~/.cursor/)
- **One-time Use:** Only run once when project is first created
- **Template Source:** Templates are copied from `cursor/skills/<skill>/assets/`
- **Creates:** Complete `.project_contexts/` structure with pm, arch, dev, management, shared folders
- **Conflict Resolution:** If files already exist, script will skip them (no overwrite)
