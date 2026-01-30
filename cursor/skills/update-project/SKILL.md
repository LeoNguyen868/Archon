---
name: update-project
description: Update project structure, documentation, and context files. Use for project maintenance tasks.
---

# Update Project Skill
Skill for updating project structure, templates, and context documentation.

## When to Use
- **ONLY** when `.project_contexts/` directory already exists in the project
- When project structure needs updates after initial setup
- When templates need modifications or refresh
- When context files need synchronization
- When configuration files need updates
- **NEVER** use for brand new projects - use `initialization` skill instead

## Decision Flow
```
1. Check if .project_contexts/ exists in target project
   - NO → Use initialization skill, NOT update-project
   - YES → Continue with update-project

2. Determine what needs updating:
   - Missing directories → Create them
   - Outdated context files → Refresh them
   - Template changes → Sync them
```

## Instructions

### 1. Analyze Current Project Structure
Review the existing project organization:

**Required Directories Check:**
- `/.project_contexts/pm/user_stories/` - Product requirements
- `/.project_contexts/pm/prds/` - Product requirement documents
- `/.project_contexts/pm/acceptance_criteria/` - Acceptance criteria
- `/.project_contexts/arch/tech_specs/` - Technical specifications
- `/.project_contexts/arch/adrs/` - Architecture decision records
- `/.project_contexts/arch/diagrams/` - Architecture diagrams
- `/.project_contexts/arch/reviews/` - Architecture reviews
- `/.project_contexts/dev/change_logs/` - Development change logs
- `/.project_contexts/dev/documentations/` - Development documentation
- `/.project_contexts/dev/current_blockings/` - Current blocking issues
- `/.project_contexts/dev/reviews/` - Code reviews
- `/.project_contexts/shared/definitions/` - Shared definitions
- `/.project_contexts/management/backlogs/` - Task backlogs
- `/.project_contexts/management/roadmaps/` - Project roadmaps
- `/.project_contexts/management/progress_reports/` - Progress reports

### 2. Create Missing Directories
Create any missing directories following the established structure:

**Directory Creation Process:**
1. Identify missing required directories
2. Create directories using appropriate permissions
3. Log directory creation for documentation
4. Verify directory creation was successful

### 3. Update Context Files

**Project Context Map Updates:**
- Update `/.project_contexts/project_context_map.md` with current structure
- Refresh "Last Updated" timestamp to current date
- Ensure all sections reflect current project state
- Add new categories or sections as needed

**Current Progress Updates:**
- Update `/.project_contexts/management/current_progress.md`
- Reflect latest completed tasks and achievements
- Update active work streams
- Refresh timeline and milestone information

### 4. Template Synchronization

**Template Management:**
- Review templates in `cursor/templates/` for updates
- Copy new templates to appropriate project locations
- Ensure backward compatibility with existing files
- Update template references in documentation

**Key Templates:**
- `project_context_map.md` → `/.project_contexts/project_context_map.md`
- `current_progress.md` → `/.project_contexts/management/current_progress.md`

### 5. File Organization and Cleanup

**Archive Completed Items:**
- Move completed tasks from active backlogs to archives
- Update status indicators appropriately
- Maintain historical records for reference

**File Structure Validation:**
- Ensure consistent naming conventions
- Verify file permissions are appropriate
- Check for orphaned files that should be moved or deleted

### 6. Documentation Updates

**Update Documentation:**
- Refresh README files with current structure
- Update architecture documentation if structure changed
- Ensure all file references are current and accurate

### 7. Verification and Validation

**Post-Update Checks:**
- Verify all required directories exist
- Confirm file permissions are correct
- Test that context files are readable and properly formatted
- Validate that no critical files were accidentally modified

## Output Format

Report updates in clear, structured format:

```markdown
## Project Structure Update Complete

## Summary
Successfully updated project structure and context files

## Directories Created
- /.project_contexts/new_directory/
- /.project_contexts/another_directory/

## Files Updated
- /.project_contexts/project_context_map.md (refreshed timestamp)
- /.project_contexts/management/current_progress.md (updated status)

## Templates Synchronized
- project_context_map.md → /.project_contexts/project_context_map.md
- current_progress.md → /.project_contexts/management/current_progress.md

## Verification Results
- All required directories present: ✓
- File permissions correct: ✓
- Context files readable: ✓

## Next Steps
Project structure is now up to date and ready for continued development.
```

## Usage Examples

**Complete Project Sync:**
```
/update-project sync entire project structure
```

**Create Missing Directories:**
```
/update-project create required directories
```

**Update Context Files:**
```
/update-project refresh context files and timestamps
```

**Template Synchronization:**
```
/update-project sync templates to project locations
```

## Constraints
- **No Deletions Without Approval**: Never delete existing files or directories without explicit user approval
- **Backup Critical Files**: Always preserve backups of important context files before major updates
- **Maintain Compatibility**: Ensure all changes maintain backward compatibility
- **Document Changes**: Log all structural changes for future reference
- **Permission Awareness**: Respect file system permissions and access controls

## Notes
- Always read current project context before making changes
- Follow established naming conventions and file organization patterns
- Test changes in development environment before production updates
- Keep detailed logs of all structural modifications
