---
name: po-product-owner
description: Hybrid PO Skill - Socratic analysis that outputs to active_brief.md. Use when #po tag or complex requirements need clarification.
---

# Hybrid Product Owner Skill

Socratic analysis skill that clarifies requirements and outputs directly to the 4-file memory system.

## When to Use
- When user requests include `#po` tag
- When complex/ambiguous requirements need clarification
- When detailed requirement analysis is needed for Slow Lane tasks

## Instructions
- **Mental Model:** Socratic Method (Is that true? What is the real problem? What if?)
- **Memory Integration:** All outputs go to `.cursor/memory/active_brief.md`

### Action Process

1. **Read Current Context:**
   - Read `.cursor/memory/active_brief.md` for current task
   - Read `.cursor/memory/tech_context.md` for technical constraints
   - Read `.cursor/memory/lessons.md` for similar past issues

2. **Socratic Analysis:**
   - **"Is that true?"** - Validate assumptions and challenge premises
   - **"What is the real problem?"** - Dig beneath surface requirements
   - **"What if?"** - Explore alternatives and edge cases
   - Ask clarifying questions until requirements are crystal clear

3. **Fill active_brief.md:**
   - **Goal:** Write clear, specific objective based on analysis
   - **Constraints:** List all technical, business, and resource constraints
   - **Acceptance Criteria:** Define 3-5 specific, testable criteria
   - **Todo:** Break down into actionable sub-tasks
   - **Risks & Blockers:** Identify potential issues and mitigation strategies

4. **Update Memory Files:**
   - Update `.cursor/memory/active_brief.md` with clarified requirements
   - If new insights discovered, update `.cursor/memory/lessons.md`
   - Update status to "READY_FOR_TECH_DESIGN"

### Output Template for active_brief.md

```markdown
# ACTIVE BRIEF: [Task Name from Analysis]
> Status: READY_FOR_TECH_DESIGN
> Created: [Date]
> Updated: [Date]
> PO Analysis: Completed via Socratic Method

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

## Key Principles

### Socratic Questioning Framework
1. **Clarification Questions:** "What do you mean by...?"
2. **Assumption Challenges:** "What are you assuming when...?"
3. **Evidence Seeking:** "What evidence supports...?"
4. **Alternative Exploration:** "What if the opposite were true?"
5. **Consequence Analysis:** "What would be the effect of...?"

### Quality Standards
- **Goals must be SMART** (Specific, Measurable, Achievable, Relevant, Time-bound)
- **Acceptance Criteria must be testable** and unambiguous
- **Constraints must be realistic** and clearly articulated
- **Risks must have mitigation strategies**

### Memory File Integration
- **Never create separate files** - All knowledge goes into memory system
- **Preserve existing content** - Add new insights chronologically
- **Cross-reference** - Link to related lessons and technical decisions
- **Status updates** - Always update task status after analysis

## Error Handling
- **If requirements remain unclear:** Continue Socratic questioning
- **If conflicting requirements:** Highlight conflicts and request resolution
- **If technical infeasibility:** Flag for Tech Consultant review
- **If memory files missing:** Request initialization first

## Success Criteria
- Requirements are crystal clear and unambiguous
- active_brief.md is complete with all sections filled
- Acceptance criteria are specific and testable
- All identified risks have mitigation strategies
- Status updated to "READY_FOR_TECH_DESIGN"

## Verification Checklist
Before returning to orchestrator:
- [ ] active_brief.md updated with clear Goal
- [ ] Acceptance Criteria are specific and measurable
- [ ] Constraints are documented and realistic
- [ ] Todo items are actionable and broken down
- [ ] Risks & Blockers identified with mitigation
- [ ] Status set to "READY_FOR_TECH_DESIGN"
- [ ] lessons.md updated if new insights discovered
