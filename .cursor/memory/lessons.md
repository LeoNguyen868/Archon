# Lessons Learned

## Best Practices

### Memory Management
- Keep memory files under 10KB for optimal performance
- Always preserve existing content when updating
- Use consistent formatting and timestamps
- Add new entries chronologically

### Task Classification
- Fast Lane: Simple, well-defined tasks (bug fixes, small updates)
- Slow Lane: Complex, ambiguous tasks (new features, architecture)
- When in doubt, default to Slow Lane for quality

### Execution Patterns
- Fast Lane: Update active_brief.md → Execute → Update lessons.md
- Slow Lane: PO Skill → Tech Consultant → PM Skill → Execute
- Always verify and update memory files after completion

## Anti-Patterns
- Don't write to `.project_contexts/` (deprecated)
- Don't parallelize tasks that modify the same files
- Don't skip memory file updates after task completion

## Common Issues and Solutions

### Issue: Memory file missing
**Solution:** Run initialization script to create all required files

### Issue: Classification uncertainty
**Solution:** Default to Slow Lane for better quality assurance

## Classification Keywords

### Fast Lane Triggers
- Explicit tags: "#fast", "#quick" (highest priority, force Fast Lane)
- Keywords: "fix", "bug", "error", "update", "change", "modify"
- Task types: "add button", "add component", "small task", "quick fix"
- File scope: Tasks affecting less than 2 files typically qualify
- Time estimate: Tasks expected to complete in under 15 minutes

### Slow Lane Triggers
- Explicit tags: "#slow", "#po", "#architect", "#pm" (highest priority, force Slow Lane)
- Keywords: "feature", "new feature", "implement", "architecture", "design", "system"
- Task types: "refactor", "restructure", "plan", "break down", "decompose"
- Complexity indicators: Ambiguous requirements, novel problems, architectural changes
- Time estimate: Tasks expected to take more than 1 hour

### Classification Priority Order
1. Explicit tags (highest priority - always respected)
2. Keyword analysis (medium priority)
3. Complexity assessment (low priority - default to Slow Lane if uncertain)

## Skill Interaction Patterns

### PO Skill Workflow
- Trigger: Complex requirements, ambiguous tasks, "#po" tag
- Process: Socratic method questions ("Is that true?", "What is the real problem?", "What if?")
- Output: Fills active_brief.md with clarified requirements, goals, acceptance criteria
- No file creation: Does not create separate user story files
- Memory update: Only updates active_brief.md

### Tech Consultant Workflow
- Trigger: Technical complexity, "#architect" tag, Slow Lane tasks
- Process: Trade-off analysis, security implications, performance impact
- Output: Creates ADRs in tech_context.md, adds technical notes to active_brief.md
- No file creation: Does not create separate ADR or tech spec files
- Memory update: Updates tech_context.md and active_brief.md

### PM Skill Workflow
- Trigger: Large features requiring decomposition, tasks over 8 hours
- Process: Task breakdown, dependency management
- Output: Creates multiple active_brief-XXX.md files if needed, updates roadmap.md
- Memory update: Updates roadmap.md with detailed planning

### Execute Worker Workflow
- Trigger: active_brief.md contains complete information
- Process: Read all memory files, implement code, handle errors
- Output: Code implementation, updates to lessons.md for new bugs/fixes
- Memory update: Marks task complete in active_brief.md, adds learnings to lessons.md

## Memory File Operations

### Reading Strategy
- Always read active_brief.md first to understand current task
- Check lessons.md for similar past issues before starting
- Reference tech_context.md for technical constraints and patterns
- Review roadmap.md for project vision alignment

### Writing Strategy
- Preserve all existing content when updating
- Add new entries chronologically with timestamps
- Use consistent markdown formatting
- Keep files under 10KB - archive old content if needed
- Update status fields immediately when task state changes

### File Size Management
- If file exceeds 10KB, archive old entries to separate archive files
- Keep recent entries (last 30 days) in main file
- Reference archived content when needed
- Consider summarization for very old lessons

### Conflict Resolution
- If multiple skills update same file, prioritize most recent update
- For conflicting technical decisions, create ADR in tech_context.md
- Document resolution process in lessons.md for future reference

## Workflow Patterns

### Fast Lane Pattern (15 minutes target)
1. User request received
2. Update active_brief.md with task details
3. Read lessons.md for similar issues
4. Execute task immediately
5. Update lessons.md if new insights
6. Mark task complete in active_brief.md

### Slow Lane Pattern (1 hour target)
1. User request received
2. Classify as Slow Lane
3. Call PO Skill for requirement clarification
4. PO Skill updates active_brief.md
5. Call Tech Consultant for technical design
6. Tech Consultant updates tech_context.md and active_brief.md
7. Call PM Skill if decomposition needed (optional)
8. PM Skill updates roadmap.md if needed
9. Execute Worker implements solution
10. Update lessons.md with learnings
11. Mark task complete in active_brief.md

### Parallel Execution Rules
- Only parallelize independent tasks
- Never parallelize tasks modifying same files
- Ensure read-only operations don't conflict with writes
- Use sequential execution if any doubt about conflicts
- Create separate active_brief-XXX.md files for parallel tasks

## Performance Optimization

### Context Pruning
- If memory files exceed 10KB, read only key sections
- Focus on active_brief.md status and recent lessons.md entries
- Skip archived content unless specifically needed
- Use file size checks before reading large files

### Speed Optimization
- Fast Lane tasks should complete in under 15 minutes
- Slow Lane tasks should complete in under 1 hour
- Avoid unnecessary skill calls for simple tasks
- Cache frequently accessed information in active_brief.md

### Quality Optimization
- Always use Slow Lane for uncertain classifications
- Complete requirement clarification before implementation
- Document all technical decisions in tech_context.md
- Learn from mistakes and document in lessons.md

## Error Prevention

### Common Mistakes
- Skipping memory file updates after task completion
- Classifying complex tasks as Fast Lane incorrectly
- Creating separate files instead of updating memory files
- Not checking lessons.md before starting similar tasks
- Parallelizing tasks that modify same files

### Prevention Strategies
- Always update memory files as last step
- When uncertain, default to Slow Lane
- Check lessons.md for similar past issues
- Verify file dependencies before parallel execution
- Use explicit tags (#fast, #slow) to override classification

### Recovery Procedures
- If memory file corrupted, restore from version control
- If classification error detected, restart with correct lane
- If skill conflict occurs, resolve manually and document in lessons.md
- If task fails, document error in lessons.md before retry

## Quality Assurance

### Verification Checklist
After each task completion:
- active_brief.md updated with completion status
- lessons.md updated with new learnings (if any)
- tech_context.md updated with ADRs (if any)
- roadmap.md updated with progress (if milestone)
- All memory files are consistent
- User notified of completion

### Consistency Checks
- Verify active_brief.md status matches actual task state
- Ensure tech_context.md ADRs align with implementation
- Check lessons.md entries match actual bugs encountered
- Confirm roadmap.md reflects current project state

## Advanced Patterns

### Multi-Task Coordination
- For related tasks, create single active_brief.md with multiple sections
- Update roadmap.md to track dependencies
- Use lessons.md to share learnings across related tasks
- Coordinate through active_brief.md status updates

### Knowledge Transfer
- Document patterns in lessons.md for reuse
- Create ADRs in tech_context.md for architectural decisions
- Update roadmap.md to track feature evolution
- Reference past active_brief.md entries for similar tasks

### Maintenance Procedures
- Regularly review and archive old lessons.md entries
- Consolidate similar ADRs in tech_context.md
- Update roadmap.md as project evolves
- Clean up completed tasks from active_brief.md periodically

## Notes
- This file accumulates knowledge over time
- Document bugs, fixes, and patterns here
- Reference this file for similar past issues
- Update this file whenever new patterns or issues are discovered
- Keep entries concise but informative
- Use consistent formatting for easy scanning

## 2026-02-01

### Fast Lane milestone execution
- A valid Fast Lane task can be a “memory-only” maintenance action: update `active_brief.md` → change one project-tracking artifact (e.g. `roadmap.md`) → add a short lesson → mark the brief completed.
- Keep milestone updates small to avoid memory file bloat; prefer one concise entry over verbose logs.

### Memory system validation
- Validate existence + size budget early (all memory files < 10KB) to prevent context bloat.
- Enforce constraints consistently across all memory artifacts (e.g., remove emojis from `roadmap.md` if the project standard is “no emojis”).
