---
name: report
description: Generate progress reports, summaries, and status updates. Use when reporting to user.
---

# Report Skill
Skill for synthesizing information, creating progress reports, and status updates.

## When to Use
- When the user requests a "Progress Report".
- At the end of each Phase.
- When facing blockers that need escalation.

## Instructions

### 1. Gather Data
Read and analyze all relevant context files:

**Project Status Files:**
- `/.project_contexts/project_context_map.md` - Overall project overview
- `/.project_contexts/management/current_progress.md` - Current progress status
- `/.project_contexts/management/backlogs/active.md` - Active tasks and backlogs
- `/.project_contexts/management/backlogs/sprint_backlog.md` - Current sprint items

**Change Tracking:**
- `/.project_contexts/dev/change_logs/` - Recent changes and updates
- `/.project_contexts/dev/current_blockings/` - Current blockers and issues

### 2. Analyze Project Health
Evaluate project status using these criteria:

**Status Assessment:**
- **Green**: No blockers, all tasks progressing, timelines met
- **Yellow**: Minor issues, some delays, manageable blockers
- **Red**: Major blockers, significant delays, critical issues

**Key Metrics:**
- Task completion rate
- Blocker count and severity
- Timeline adherence
- Resource utilization

### 3. Synthesize Information (80/20 Rule)
Focus on the most important 20% of information that drives 80% of decisions:

**Critical Information:**
- Current blockers and their impact
- Next critical milestones
- Resource constraints
- Risk factors

**Secondary Information:**
- Completed tasks (summary only)
- Minor issues
- Detailed metrics

### 4. Generate Comprehensive Report

**Report Structure:**
```markdown
# Progress Report
**Generated:** [Current Date/Time]
**Status:** [Green/Yellow/Red]

## Executive Summary
[2-3 sentence overview of project health and key achievements]

## Current Status
- **Overall Progress:** [Percentage or qualitative assessment]
- **Active Tasks:** [Count and brief descriptions]
- **Completed This Period:** [Key achievements]
- **Upcoming Milestones:** [Next 1-2 weeks]

## Blockers & Risks
[List of current blockers with severity and impact]
- **Critical:** [High-impact issues requiring immediate attention]
- **High:** [Important issues affecting progress]
- **Medium:** [Issues to monitor]

## Active Work Streams
[Current active tasks categorized by priority/phase]

## Recent Changes
[Summary of major changes in last 1-2 weeks]
- [Change 1]: [Impact]
- [Change 2]: [Impact]

## Recommendations
[Specific actionable recommendations]
- [Immediate actions needed]
- [Strategic suggestions]

## Next Steps
[Concrete next actions with owners/timelines]
```

### 5. Validation
Before finalizing the report:
- Verify all data sources are current
- Cross-reference information across files
- Ensure recommendations are actionable
- Confirm status assessment is accurate

## Output Format
Reports should be written to appropriate locations:
- `/.project_contexts/management/progress_reports/` - For regular progress reports
- Direct output to user - For ad-hoc status requests

## Usage Examples

**Regular Progress Report:**
```
/report create weekly progress report
```

**Status Check:**
```
/report check current project status
```

**Blocker Escalation:**
```
/report identify and report critical blockers
```

## Notes
- Always read the most current versions of context files
- Focus on actionable insights over raw data
- Use clear, professional language suitable for stakeholders
- Include specific recommendations with owners where possible
