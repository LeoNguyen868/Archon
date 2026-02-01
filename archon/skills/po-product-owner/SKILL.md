---
name: po-product-owner
description: Hybrid PO/PM Skill - Socratic analysis with task decomposition and roadmap management using memory system. Use when #po tag or complex requirements need clarification.
---

# Hybrid Product Owner Skill

Socratic analysis with task decomposition and roadmap management skill that clarifies requirements, breaks down large features, and outputs directly to the 4-file memory system.

## When to Use
- When user requests include `#po` tag
- When complex/ambiguous requirements need clarification
- When detailed requirement analysis is needed for Slow Lane tasks
- When large features need to be broken down into smaller tasks
- When complex projects require implementation planning
- When roadmap and progress tracking is needed

## Instructions
- **Mental Model:** Socratic Method + Task Decomposition (Is that true? What is the real problem? What if?)
- **Memory Integration:** All outputs go to `.cursor/memory/` files

### Action Process

1. **Read Current Context:**
   - Read `.cursor/memory/active_brief.md` for current task
   - Read `.cursor/memory/tech_context.md` for technical constraints
   - Read `.cursor/memory/lessons.md` for similar past issues
   - Read `.cursor/memory/roadmap.md` for current project vision

2. **Socratic Analysis:**
   - **"Is that true?"** - Validate assumptions and challenge premises
   - **"What is the real problem?"** - Dig beneath surface requirements
   - **"What if?"** - Explore alternatives and edge cases
   - Ask clarifying questions until requirements are crystal clear

3. **Task Decomposition (for large features):**
   - **Break Down:** Split large features into small, manageable tasks (2-4 hours each)
   - **Estimate Complexity:** Assess effort for each sub-task
   - **Identify Dependencies:** Map task relationships and critical path
   - **Risk Assessment:** Identify potential blockers and mitigation strategies
   - **Create Multiple Briefs:** For complex features, create `active_brief-XXX.md` files

4. **Fill Memory Files:**
   - **Update active_brief.md:** Fill with clarified requirements and task breakdown
   - **Update roadmap.md:** Add detailed breakdown and progress tracking
   - **Create sub-briefs:** If complexity requires, create numbered briefs
   - **Update status:** Set to "READY_FOR_TECH_DESIGN"

### Output Template for active_brief.md

```markdown
# ACTIVE BRIEF: [Task Name from Analysis]
> Status: READY_FOR_TECH_DESIGN
> Created: [Date]
> Updated: [Date]
> PO/PM Analysis: Completed via Socratic Method + Task Decomposition

## Goal
[Clear, specific goal based on Socratic analysis]

## Constraints
- [Technical constraints from tech_context.md]
- [Business constraints discovered during analysis]
- [Resource or time constraints]

## Acceptance Criteria
- [ ] [Specific, measurable criteria 1]
- [ ] [Specific, measurable criteria 2]
- [ ] [Specific, measurable criteria 3]

## Task Decomposition (for large features)
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

## Todo
- [ ] [Sub-task 1]
- [ ] [Sub-task 2]
- [ ] [Sub-task 3]

## Technical Notes
[Technical considerations for Tech Consultant]

## Risks & Blockers
- [Risk 1]: [Mitigation strategy]
- [Blocker 1]: [Workaround plan]
```

### Multiple Briefs Template (for complex features)

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

### Socratic Questioning Framework
1. **Clarification Questions:** "What do you mean by...?"
2. **Assumption Challenges:** "What are you assuming when...?"
3. **Evidence Seeking:** "What evidence supports...?"
4. **Alternative Exploration:** "What if the opposite were true?"
5. **Consequence Analysis:** "What would be the effect of...?"

### Task Decomposition Framework
1. **Identify Main Components:** Break feature into logical parts
2. **Create Task Hierarchy:** Main task → Sub-tasks → Sub-sub-tasks
3. **Estimate Realistically:** Consider complexity and dependencies
4. **Define Completion:** Clear "done" criteria for each task
5. **Sequence Properly:** Order tasks by dependency and priority

### Quality Standards
- **Goals must be SMART** (Specific, Measurable, Achievable, Relevant, Time-bound)
- **Acceptance Criteria must be testable** and unambiguous
- **Constraints must be realistic** and clearly articulated
- **Risks must have mitigation strategies**
- **Task Size:** Each task should be completable in 2-4 hours
- **Clear Dependencies:** No circular dependencies
- **Testable Outcomes:** Each task has verifiable results

### Memory File Integration
- **Never create separate files** - All knowledge goes into memory system
- **Multiple Briefs:** For complex features, use numbered briefs (active_brief-001.md)
- **Cross-Reference:** Link briefs to roadmap items
- **Progress Tracking:** Update roadmap as tasks complete
- **Preserve existing content** - Add new insights chronologically
- **Status updates** - Always update task status after analysis

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
- **If requirements remain unclear:** Continue Socratic questioning
- **If conflicting requirements:** Highlight conflicts and request resolution
- **If technical infeasibility:** Flag for Tech Consultant review
- **If memory files missing:** Request initialization first
- **If tasks too large:** Break down further into sub-briefs
- **If dependencies unclear:** Request clarification from Tech Consultant
- **If effort estimation difficult:** Use relative sizing (S/M/L)
- **If risks unidentified:** Conduct risk assessment workshop

## Success Criteria
- Requirements are crystal clear and unambiguous
- active_brief.md is complete with all sections filled
- Acceptance criteria are specific and testable
- All identified risks have mitigation strategies
- Status updated to "READY_FOR_TECH_DESIGN"
- Large feature broken into manageable 2-4 hour tasks (if applicable)
- All dependencies identified and sequenced (if applicable)
- Roadmap updated with detailed progress tracking (if applicable)
- Multiple briefs created if complexity requires (if applicable)

## Verification Checklist
Before returning to orchestrator:
- [ ] active_brief.md updated with clear Goal
- [ ] Acceptance Criteria are specific and measurable
- [ ] Constraints are documented and realistic
- [ ] Todo items are actionable and broken down
- [ ] Risks & Blockers identified with mitigation
- [ ] Status set to "READY_FOR_TECH_DESIGN"
- [ ] lessons.md updated if new insights discovered
- [ ] Task decomposition completed for large features
- [ ] Sub-tasks sized appropriately (2-4 hours each)
- [ ] Dependencies identified and sequenced
- [ ] roadmap.md updated with detailed progress tracking
- [ ] Multiple briefs created if complexity requires
- [ ] Risk assessment completed with mitigations
