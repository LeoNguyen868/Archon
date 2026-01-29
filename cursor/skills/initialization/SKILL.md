---
name: initialization
description: Initialize project structure and templates. Use for setting up new projects.
---

# Initialization Skill
Skill for initializing project structure and template files.

## When to Use
- When starting a new project (Inception Phase).
- When the project structure is missing or needs a reset.
- When templates need updates.

## Instructions
- **Action:** Run the `init_project.py` script to create the `/.project_contexts/` structure and template files.
- **Verification:** Check for the existence of directories and files after running.
- **Note:** The script handles creating `/.project_contexts/pm`, `arch`, `dev`, `management`, and `shared`.

## Usage
Run Python script: `python ~/.cursor/skills/initialization/scripts/init_project.py`
or with root parameter:
`python ~/.cursor/skills/initialization/scripts/init_project.py --root /path/to/project`

## Notes
- Script must be executed from the skill's root directory
- Ensure Python dependencies are installed
- Script will create directory structure and template files
