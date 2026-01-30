---
name: delegation
description: Guide orchestrator to delegate tasks to appropriate workers with clear context and instructions. Use for distributing work to specialized workers.
---

# Delegation Skill

Skill for orchestrator to understand how to delegate tasks to specialized workers with clear context and instructions.

## Role Rules (Strict Permissions)
- **Primary Permissions:** Task initiation, context preparation, worker selection.
- **Requirement:** Must follow the strict instruction format for all handoffs.
- **Instruction Format:** Every delegation MUST include:
    - **Role:** The specific role the agent should assume.
    - **Required Skill:** The primary skill the agent must use.
    - **Task:** A detailed description of the task.
    - **Context:** List of files and directories the agent needs access to.
    - **Constraints:** Any rules the agent must follow.

## When to Use
- When orchestrator needs to delegate tasks to specialized workers.
- When work needs to be broken down for specialized agents.
- When the current context is too large and needs isolation.

## Orchestrator Instructions

### Step 1: Identify Worker Type
Based on task requirements:
- **Planning Worker:** For analysis, design, and planning tasks
- **Execute Worker:** For coding, testing, and implementation tasks  
- **General Worker:** For research, reporting, and maintenance tasks

### Step 2: Select Appropriate Worker Skill
Based on worker type and task nature:

#### For Planning Worker:
- **PO Product Owner Skill:** Requirements analysis, user stories, acceptance criteria
- **PM Project Manager Skill:** Task breakdown, planning, backlog management
- **Tech Consultant Skill:** Architecture design, technical specifications, ADRs

#### For Execute Worker:
- **Coding Skill:** Implementation, feature development
- **Test Skill:** Testing, quality assurance, validation
- **Debug Skill:** Troubleshooting, bug fixing
- **Code Analysis Skill:** Code review, analysis, optimization
- **Frontend Design Skill:** UI/UX design, frontend implementation

#### For General Worker:
- **Research Skill:** Information gathering, analysis, documentation
- **Report Skill:** Progress reporting, status updates
- **Update-Project Skill:** Project maintenance, structure updates
- **Review Skill:** Review and validation tasks

### Step 3: Construct Delegation Instruction
Use the strict format:

```
Role: [Planning/Execute/General Worker]
Required Skill: [Specific Skill Name]
Task: [Detailed task description with clear objectives]
Context: [List of required files, directories, and information]
Constraints: [Specific rules, limitations, and requirements]
```

### Step 4: Examples

#### Example 1: Feature Analysis
```
Role: Planning Worker
Required Skill: po-product-owner
Task: Analyze user request for "user authentication feature" and create comprehensive user story with acceptance criteria
Context: User request text, existing project_context_map.md, current_progress.md
Constraints: Focus on WHAT and WHY, do not specify implementation details, use standard user story template
```

#### Example 2: Technical Design
```
Role: Planning Worker  
Required Skill: tech-consultant
Task: Design technical architecture for user authentication system including API endpoints, data models, and security considerations
Context: User story from PO, existing architecture documentation, technology stack
Constraints: Consider security best practices, ensure scalability, create ADRs for major decisions
```

#### Example 3: Implementation
```
Role: Execute Worker
Required Skill: coding
Task: Implement user authentication API endpoints based on technical specifications
Context: Tech spec document, user story, existing codebase structure
Constraints: Follow coding standards, include unit tests, update changelog
```

#### Example 4: Research
```
Role: General Worker
Required Skill: research
Task: Research existing authentication libraries and frameworks compatible with current tech stack
Context: Technology stack documentation, project requirements, existing dependencies
Constraints: Focus on open-source solutions, consider licensing and maintenance
```

## Notes
- **Orchestrator Role:** This skill guides orchestrator on how to delegate, not for workers to use
- **Worker Selection:** Choose worker based on task nature, not convenience
- **Skill Matching:** Ensure worker has access to required skill
- **Context Preparation:** Provide sufficient context for worker to succeed
- **Verification:** Orchestrator must verify worker outputs match expectations
