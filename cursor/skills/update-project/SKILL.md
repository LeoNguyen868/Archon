---
name: update-project
description: Guide orchestrator to coordinate project updates, maintenance, and context synchronization. Use when project structure needs updates.
---

# Update Project Skill

Skill for orchestrator understand project update intent and coordinate workers to maintain and synchronize project structure and context.

## When to Use
- **ONLY** when `.project_contexts/` directory already exists in the project
- When user requests project structure updates or maintenance
- When project context needs to be synchronized with actual codebase
- When templates need to be refreshed or updated
- **NEVER** use for brand new projects - use initialization skill instead

## Orchestrator Instructions

### Step 1: Understand Update Intent
Read this skill to understand that project updates require:
- Analyzing current project state
- Determining type of update needed
- Coordinating appropriate workers for specific tasks

### Step 2: Determine Update Type
Classify the user's request:
- **Structure Update:** Missing directories, file organization changes
- **Context Refresh:** Project information needs updating
- **Template Sync:** Templates need to be synchronized
- **Maintenance:** General project upkeep tasks

### Step 3: Delegate Based on Update Type

#### For Structure Updates:
**Delegation Format:**
- **Role:** General Worker
- **Required Skill:** update-project
- **Task:** Create missing directories and organize project structure
- **Context:** Current project structure analysis
- **Constraints:** Follow established directory naming conventions

#### For Context Refresh:
**Delegation Format:**
- **Role:** General Worker
- **Required Skill:** research
- **Task:** Analyze current codebase and extract updated project context
- **Context:** Source code, recent changes, new features
- **Output Requirements:**
  - Updated project objectives
  - New technology stack changes
  - Modified architecture overview
  - Current progress status

Followed by:
- **Role:** General Worker
- **Required Skill:** update-project
- **Task:** Update project_context_map.md with current project information
- **Context:** Research findings from previous step
- **Constraints:** Use current project data, reflect recent changes

#### For Template Sync:
**Delegation Format:**
- **Role:** General Worker
- **Required Skill:** update-project
- **Task:** Synchronize templates with current project structure
- **Context:** Template assets directory and current project needs
- **Constraints:** Maintain backward compatibility with existing files

#### For General Maintenance:
**Delegation Format:**
- **Role:** General Worker
- **Required Skill:** update-project
- **Task:** Perform general project maintenance and cleanup
- **Context:** Project maintenance requirements
- **Constraints:** Do not delete files without explicit user approval

### Step 4: Review Worker Results
Verify that:
- Structure updates follow project conventions
- Context refresh reflects actual project state
- Template synchronization maintains compatibility
- Maintenance tasks preserve important data

### Step 5: Final Verification and Integration
- Verify all updates are consistent across project files
- Ensure project_context_map.md accurately reflects current state
- Confirm current_progress.md is updated with latest changes
- Present update results to user

## Expected Worker Outputs

### From Structure Updates:
- All required directories present and properly organized
- File structure follows established conventions
- No orphaned files or broken references

### From Context Refresh:
- Updated project_context_map.md with current project information
- Refreshed current_progress.md reflecting latest status
- Accurate technology stack and architecture documentation

### From Template Sync:
- All templates synchronized with current project needs
- Template references updated in documentation
- Backward compatibility maintained

### From General Maintenance:
- Clean and organized project structure
- Updated documentation and references
- Maintained project integrity

## Decision Flow
```
User requests project update
     ↓
Orchestrator reads update-project skill
     ↓
Determine update type (structure/context/template/maintenance)
     ↓
Delegate appropriate worker(s) with specific tasks
     ↓
Review worker results
     ↓
Verify integration and consistency
     ↓
Present results to user
```

## Update Type Matrix

| User Request | Update Type | Worker | Skill | Output |
|--------------|-------------|--------|-------|--------|
| "Create missing directories" | Structure | General Worker | update-project | Directory structure |
| "Update project info" | Context | General Worker | research + update-project | Updated context files |
| "Sync templates" | Template | General Worker | update-project | Synchronized templates |
| "Clean up project" | Maintenance | General Worker | update-project | Organized structure |

## Notes
- **Orchestrator Role:** This skill guides orchestrator on how to coordinate updates, not for direct execution
- **Worker Coordination:** Orchestrator must analyze request type and delegate to appropriate workers
- **Context Awareness:** Updates must reflect actual project state, not generic changes
- **Verification:** Orchestrator must verify worker outputs meet user's specific update requirements
- **Incremental Updates:** Prefer small, specific updates over large, sweeping changes
