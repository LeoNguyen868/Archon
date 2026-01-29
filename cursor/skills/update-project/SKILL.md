---
name: update-project
description: Update project structure, documentation, and context files. Use for project maintenance tasks.
---

# Update Project Skill
Skill for updating project structure, templates, and context documentation.

## When to Use
- When project structure needs updates.
- When templates need modifications.
- When context files need synchronization.
- When configuration files need updates.

## Instructions
- **Structure Updates:**
    1. Add new directories as needed.
    2. Ensure correct file organization.
    3. Follow existing naming conventions.
- **Context Updates:**
    1. Update `project_context_map.md` after major changes.
    2. Update `current_progress.md` with latest status.
    3. Archive completed items appropriately.
- **Template Updates:**
    1. Update templates in `cursor/templates/` if format changes are needed.
    2. Ensure backward compatibility.
- **Scripts:**
    1. Use `python ~/.cursor/skills/update-project/scripts/update_project.py --action [action]` for automated updates.
    2. Verify changes after script execution.
- **Output:**
    - Updated directory structure
    - Updated context files
    - Updated templates
- **Constraints:**
    - Do not delete existing files without explicit approval.
    - Back up important files before major changes.
    - Document all structural changes.

## Usage
Run Python script with specific action:
`python ~/.cursor/skills/update-project/scripts/update_project.py --action update_structure`
or:
`python ~/.cursor/skills/update-project/scripts/update_project.py --action update_templates`
or:
`python ~/.cursor/skills/update-project/scripts/update_project.py --action update_context_map`

## Notes
- Script must be executed from the skill's root directory
- Ensure write permissions to files that need updating
- Always backup before running script
