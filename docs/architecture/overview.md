# Architecture Overview

Archon is a skills-centric AI orchestration system that supercharges IDEs using the OODA Loop and Socratic method.

## Core Concepts

### Skills-Centric Architecture

Archon revolves around **Skills** - domain-specific knowledge modules that encapsulate best practices and capabilities:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Product Owner │    │  Tech Consultant │    │    Developer    │
│     Skills      │    │     Skills       │    │     Skills      │
├─────────────────┤    ├─────────────────┤    ├─────────────────┤
│ • Requirements  │    │ • Architecture   │    │ • Coding        │
│ • User Stories  │    │ • Tech Specs     │    │ • Testing       │
│ • Acceptance    │    │ • ADRs          │    │ • Debugging     │
│   Criteria      │    │ • Trade-offs    │    │ • Reviews       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### OODA Loop Decision Making

All decisions follow the **OODA Loop**:

```
Observe → Orient → Decide → Act
```

- **Observe**: Analyze current state and context
- **Orient**: Classify request and identify approach
- **Decide**: Select appropriate worker and skills
- **Act**: Execute and verify results

### Socratic Questioning

Archon asks "Is that true?" and "What is the real problem?" to ensure:
- Requirements are well understood
- Solutions are appropriate
- Decisions are well-reasoned

## System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Cursor IDE                               │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Agent Orchestrator                    │    │
│  │  ┌─────────────────────────────────────────────────┐ │    │
│  │  │              OODA Loop                          │ │    │
│  │  └─────────────────────────────────────────────────┘ │    │
│  └─────────────────────────────────────────────────────┘    │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐  │
│  │ Planning Worker │  │ Execute Worker  │  │ General     │  │
│  │                 │  │                 │  │ Worker      │  │
│  │ • PO Skills     │  │ • Coding Skills │  │ • Report    │  │
│  │ • Tech Skills   │  │ • Test Skills   │  │   Skills    │  │
│  │ • PM Skills     │  │ • Debug Skills  │  │ • Research  │  │
│  └─────────────────┘  └─────────────────┘  └─────────────┘  │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐    │
│  │            Context Management System               │    │
│  │  ┌─────────────────────────────────────────────────┐ │    │
│  │  │         .project_contexts/                     │ │    │
│  │  │  • Single Source of Truth                      │ │    │
│  │  │  • Domain Separation                          │ │    │
│  │  │  • Context Pruning                            │ │    │
│  │  └─────────────────────────────────────────────────┘ │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## Component Details

### Agent Orchestrator

**Role**: System coordinator and decision maker

**Responsibilities**:
- Request analysis and classification
- Worker selection and delegation
- Context management and pruning
- Result verification and integration

**Key Features**:
- OODA Loop implementation
- Socratic questioning methodology
- Human-in-the-loop verification
- Isolated context windows for workers

### Workers

Archon uses three specialized worker types:

#### 1. Planning Worker
- **Purpose**: Analysis, design, and planning
- **Skills**: PO, Tech Consultant, PM
- **Use Cases**: Requirements analysis, architecture design, task breakdown

#### 2. Execute Worker
- **Purpose**: Implementation and validation
- **Skills**: Coding, Testing, Frontend Design, Debugging
- **Use Cases**: Code implementation, testing, bug fixes

#### 3. General Worker
- **Purpose**: Research, reporting, and maintenance
- **Skills**: Report, Research, Update Project
- **Use Cases**: Documentation, research, project maintenance

### Skills Library

**15 Core Skills** organized by category:

#### High-Level Skills (4)
1. **agent-orchestrator**: System coordination
2. **po-product-owner**: Requirements and user stories
3. **tech-consultant**: Technical design and ADRs
4. **pm-project-manager**: Task breakdown and planning

#### Technical Skills (6)
1. **coding**: Production code implementation
2. **code-analysis**: Code pattern analysis
3. **debug**: Error analysis and fixes
4. **test**: Test creation and execution
5. **review**: Code and document review
6. **frontend-design**: UI/UX implementation

#### Support Skills (5)
1. **delegation**: Task distribution
2. **initialization**: Project setup
3. **update-project**: Project maintenance
4. **report**: Progress reporting
5. **research**: Information gathering

### Context Management System

**Single Source of Truth**: `.project_contexts/project_context_map.md`

**Domain Separation**:
- `pm/`: Product Owner domain (WHAT & WHY)
- `arch/`: Architecture domain (HOW - high-level)
- `dev/`: Development domain (HOW - low-level)
- `management/`: Project management
- `shared/`: Cross-domain artifacts

**Context Pruning Strategies**:
1. **File Size Threshold**: Files > 10KB load summary sections only
2. **Active-First Loading**: Prioritize active tasks
3. **Progressive Loading**: Basic context first, details on-demand

## Orchestration Patterns

### 1. Conductor Pattern (LLM-Based)
- **Use**: Dynamic decision-making, context-dependent tasks
- **Flow**: Analyze → Identify specialists → Plan order → Delegate → Integrate → Verify
- **Example**: Parent orchestrator coordinating complex feature development

### 2. Assembly Line Pattern (Sequential)
- **Use**: Strict order, dependencies between steps
- **Flow**: Step 1 → Step 2 → Step 3 → Verification
- **Example**: Requirements → Design → Implementation → Testing

### 3. Task Force Pattern (Parallel)
- **Use**: Independent tasks, speed critical
- **Flow**: Split → Execute in parallel → Integrate
- **Example**: Parallel analysis of API, database, and UI components

### 4. Refinement Cycle Pattern (Iterative)
- **Use**: Iterative improvement, feedback loops
- **Flow**: Implement → Test → Review → Refine → Repeat
- **Example**: Code review and improvement cycles

## Data Flow

### Request Processing

```
User Request
    ↓
Agent Orchestrator (Observe)
    ↓
Context Analysis & Pruning
    ↓
Request Classification (Orient)
    ↓
Worker & Skill Selection (Decide)
    ↓
Task Delegation (Act)
    ↓
Worker Execution (Isolated Context)
    ↓
Result Integration & Verification
    ↓
Response to User
```

### Context Updates

```
Worker Execution
    ↓
Result Generation
    ↓
Context File Updates
    ↓
Project Context Map Sync
    ↓
Progress Tracking
    ↓
Next Task Preparation
```

## Security and Safety

### Context Isolation
- Workers operate in isolated context windows
- Sensitive information protected through access controls
- Git integration with selective file access

### Validation Mechanisms
- Human-in-the-loop for critical decisions
- Socratic questioning for requirement validation
- Automated verification of worker outputs
- Context integrity checks

## Integration Points

### Cursor IDE Integration
- Skills loaded via migration script
- Context files accessed through `.cursorignore`
- Commands available via command palette

### Git Integration
- `.project_contexts/` excluded from version control
- Selective access via `.cursorignore` overrides
- Change tracking and history management

### Automation Scripts
- Project initialization and maintenance
- Context updates and synchronization
- Report generation and progress tracking

## Performance Characteristics

### Latency Optimization
- Context pruning for large files
- Parallel worker execution when possible
- Progressive loading strategies
- Caching of frequently accessed context

### Scalability Considerations
- Modular skill architecture
- Domain separation in context management
- Configurable worker isolation
- Extensible orchestration patterns

## Extensibility

### Adding New Skills
- Create skill definition in `cursor/skills/`
- Follow established SKILL.md format
- Add assets and scripts as needed
- Test integration with existing workers

### Adding New Workers
- Define worker configuration in `cursor/agents/`
- Specify skills and capabilities
- Configure execution parameters
- Test orchestration integration

### Custom Orchestration Patterns
- Extend agent orchestrator logic
- Implement new decision-making flows
- Add custom context management strategies

This architecture provides a solid foundation for AI-driven software development while maintaining flexibility, safety, and extensibility.