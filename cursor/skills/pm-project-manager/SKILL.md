---
name: pm-project-manager
description: Hybrid PM Skill - Task breakdown and roadmap management using memory system. Use for large features needing decomposition.
---

# Hybrid Project Manager Skill

Task decomposition and roadmap management skill that outputs directly to the 4-file memory system.

## When to Use
- When large features need to be broken down into smaller tasks
- When complex projects require implementation planning
- When roadmap and progress tracking is needed
- When PM is called in Slow Lane workflow for large projects

## Instructions
- **Mental Model:** Decomposition, Critical Path, Risk Management
- **Memory Integration:** All outputs go to `.cursor/memory/` files

### Action Process

1. **Read Current Context:**
   - Read `.cursor/memory/active_brief.md` for requirements and constraints
   - Read `.cursor/memory/tech_context.md` for technical decisions
   - Read `.cursor/memory/roadmap.md` for current project vision
   - Read `.cursor/memory/lessons.md` for past planning insights

2. **Task Decomposition:**
   - **Break Down:** Split large features into small, manageable tasks
   - **Estimate Complexity:** Assess effort for each sub-task
   - **Identify Dependencies:** Map task relationships and critical path
   - **Risk Assessment:** Identify potential blockers and mitigation strategies

3. **Create Multiple Briefs (if needed):**
   - For large features, create multiple `active_brief-XXX.md` files
   - Each brief focuses on one sub-task
   - Maintain clear dependencies between briefs

4. **Update Memory Files:**
   - Update `.cursor/memory/roadmap.md` with detailed breakdown
   - Update `.cursor/memory/active_brief.md` with task decomposition
   - Create sub-task briefs if complexity requires it

### Task Breakdown Template

```markdown
## Task Decomposition
### Main Feature: [Feature Name]
**Estimated Total Effort:** [X hours/days]
**Critical Path:** [Task 1 → Task 3 → Task 5]

#### Sub-Tasks:
1. **Task 1:** [Description] - [Effort] - [Dependencies: None]
2. **Task 2:** [Description] - [Effort] - [Dependencies: Task 1]
3. **Task 3:** [Description] - [Effort] - [Dependencies: Task 1]
4. **Task 4:** [Description] - [Effort] - [Dependencies: Task 2, Task 3]
5. **Task 5:** [Description] - [Effort] - [Dependencies: Task 4]

### Risk Assessment
- **High Risk:** [Risk 1] - [Mitigation]
- **Medium Risk:** [Risk 2] - [Mitigation]
- **Low Risk:** [Risk 3] - [Accept]
```

### Multiple Briefs Template

For complex features, create sequential briefs:

**active_brief-001.md:**
```markdown
# ACTIVE BRIEF: [Feature] - Part 1
> Status: READY_FOR_IMPLEMENTATION
> Part: 1 of 3
> Dependencies: None

## Goal
[First part of feature]

## Acceptance Criteria
- [ ] [Criteria 1]
- [ ] [Criteria 2]

## Next Task
active_brief-002.md (depends on this completion)
```

**active_brief-002.md:**
```markdown
# ACTIVE BRIEF: [Feature] - Part 2
> Status: PLANNING
> Part: 2 of 3
> Dependencies: active_brief-001.md

## Goal
[Second part of feature]

## Acceptance Criteria
- [ ] [Criteria 1]
- [ ] [Criteria 2]

## Next Task
active_brief-003.md (depends on this completion)
```

### Roadmap Update Template

```markdown
## In Progress
- [ ] [Main Feature] - [Priority: High]
  - [ ] [Sub-task 1] - active_brief-001.md
  - [ ] [Sub-task 2] - active_brief-002.md
  - [ ] [Sub-task 3] - active_brief-003.md
```

## Key Principles

### Decomposition Framework
1. **Identify Main Components:** Break feature into logical parts
2. **Create Task Hierarchy:** Main task → Sub-tasks → Sub-sub-tasks
3. **Estimate Realistically:** Consider complexity and dependencies
4. **Define Completion:** Clear "done" criteria for each task
5. **Sequence Properly:** Order tasks by dependency and priority

### Quality Standards
- **Task Size:** Each task should be completable in 2-4 hours
- **Clear Dependencies:** No circular dependencies
- **Testable Outcomes:** Each task has verifiable results
- **Risk Mitigation:** Each identified risk has mitigation strategy

### Memory File Integration
- **Never create separate files** - Use memory system only
- **Multiple Briefs:** For complex features, use numbered briefs
- **Cross-Reference:** Link briefs to roadmap items
- **Progress Tracking:** Update roadmap as tasks complete

## When to Use Multiple Briefs

### Use Single Brief When:
- Feature can be completed in < 4 hours
- Task has no significant dependencies
- Requirements are well-defined and stable

### Use Multiple Briefs When:
- Feature requires > 8 hours total effort
- Task has clear sequential dependencies
- Multiple team members might work in parallel
- Complexity requires focused attention on sub-tasks

## Error Handling
- **If tasks too large:** Break down further into sub-briefs
- **If dependencies unclear:** Request clarification from PO/Tech Consultant
- **If effort estimation difficult:** Use relative sizing (S/M/L)
- **If risks unidentified:** Conduct risk assessment workshop

## Success Criteria
- Large feature broken into manageable 2-4 hour tasks
- All dependencies identified and sequenced
- Risks assessed with mitigation strategies
- Roadmap updated with clear progress tracking
- Memory files contain complete decomposition

## Verification Checklist
Before returning to orchestrator:
- [ ] active_brief.md updated with task breakdown
- [ ] Sub-tasks sized appropriately (2-4 hours each)
- [ ] Dependencies identified and sequenced
- [ ] roadmap.md updated with detailed progress tracking
- [ ] Multiple briefs created if complexity requires
- [ ] Risk assessment completed with mitigations
- [ ] lessons.md updated if new planning insights discovered
