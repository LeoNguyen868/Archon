# Workers Reference Guide

This guide explains Archon's worker system, how workers use skills, and how to leverage them effectively.

## Workers Overview

Archon uses **three specialized worker types** that operate in isolated context windows:

- **Planning Worker**: Analysis, design, and planning
- **Execute Worker**: Implementation and validation
- **General Worker**: Research, reporting, and maintenance

## Worker Architecture

### Context Isolation Model

```
Parent Orchestrator
        ↓
   Task Delegation
        ↓
┌─────────────────┐
│  Isolated       │ ← Worker operates here
│  Context        │    - Limited context access
│  Window         │    - Skill-specific execution
│                 │    - Result-only communication
└─────────────────┘
        ↓
  Result Integration
        ↓
Parent Orchestrator
```

**Key Benefits**:
- Clean separation of concerns
- Focused execution context
- Security through isolation
- Predictable communication

## Planning Worker

**Configuration**:
```yaml
name: planning-worker
description: Planning, analysis, design, and requirements
model: inherit
readonly: false
is_background: false
```

### Capabilities

**Primary Skills**:
- `po-product-owner`: Requirements analysis
- `tech-consultant`: Technical design
- `pm-project-manager`: Task breakdown

### Use Cases

#### 1. Requirements Analysis
```
/planning-worker analyze requirements for user authentication
```
**Process**:
- Creates user stories with INVEST criteria
- Defines acceptance criteria
- Identifies business value and priorities

**Output**: `.project_contexts/pm/user_stories/`

#### 2. Technical Design
```
/planning-worker design architecture for payment processing
```
**Process**:
- Evaluates technical trade-offs
- Creates Architecture Decision Records (ADRs)
- Produces technical specifications

**Output**: `.project_contexts/arch/tech_specs/` and `adrs/`

#### 3. Task Breakdown
```
/planning-worker break down e-commerce feature into tasks
```
**Process**:
- Decomposes features into manageable tasks
- Identifies dependencies and blockers
- Creates implementation roadmap

**Output**: `.project_contexts/management/backlogs/`

### Best Practices

- **Start with PO** for unclear requirements
- **Use Tech Consultant** for complex architecture decisions
- **Apply PM** for large feature decomposition
- **Chain skills** for comprehensive analysis

## Execute Worker

**Configuration**:
```yaml
name: execute-worker
description: Implementation, testing, and validation
model: auto
readonly: false
is_background: false
```

### Capabilities

**Primary Skills**:
- `coding`: Production code implementation
- `test`: Test creation and execution
- `frontend-design`: UI/UX implementation
- `debug`: Error analysis and fixes
- `review`: Code quality assessment

### Use Cases

#### 1. Feature Implementation
```
/execute-worker implement user login according to tech spec
```
**Process**:
- Reads technical specifications
- Generates production-ready code
- Includes error handling and documentation
- Follows established patterns

**Output**: Source code files, updated documentation

#### 2. Testing Implementation
```
/execute-worker create comprehensive tests for authentication
```
**Process**:
- Analyzes code structure
- Creates unit, integration, and E2E tests
- Ensures adequate coverage
- Validates edge cases

**Output**: Test files and coverage reports

#### 3. Bug Fixing
```
/execute-worker fix the null pointer exception in user service
```
**Process**:
- Analyzes error logs and stack traces
- Identifies root cause
- Implements and tests fix
- Documents solution

**Output**: Fixed code, test updates

#### 4. Code Review
```
/execute-worker review authentication implementation for security
```
**Process**:
- Analyzes code against security checklists
- Identifies vulnerabilities and issues
- Provides remediation recommendations
- Validates fixes

**Output**: Review reports and recommendations

### Best Practices

- **Provide clear specifications** before implementation
- **Include context** about existing codebase
- **Specify requirements** (performance, security, etc.)
- **Request reviews** for critical components

## General Worker

**Configuration**:
```yaml
name: general-worker
description: Research, reporting, and project maintenance
model: auto
readonly: true
is_background: true
```

### Capabilities

**Primary Skills**:
- `report`: Progress reporting and documentation
- `research`: Information gathering and analysis
- `update-project`: Project maintenance and synchronization

### Use Cases

#### 1. Progress Reporting
```
/general-worker generate sprint progress report
```
**Process**:
- Collects data from project contexts
- Analyzes progress and blockers
- Generates comprehensive reports
- Identifies trends and recommendations

**Output**: Markdown/HTML reports

#### 2. Research Tasks
```
/general-worker research best practices for API authentication
```
**Process**:
- Searches multiple sources and documentation
- Synthesizes information and recommendations
- Validates credibility of sources
- Provides actionable insights

**Output**: Research summaries and recommendations

#### 3. Project Maintenance
```
/general-worker update project structure and sync templates
```
**Process**:
- Validates current project structure
- Updates templates and configurations
- Synchronizes context files
- Maintains project metadata

**Output**: Updated project files and contexts

### Best Practices

- **Specify report formats** (markdown, HTML)
- **Define research scope** clearly
- **Include timelines** for maintenance tasks
- **Request specific outputs** for research

## Orchestration Patterns

### 1. Sequential Execution (Assembly Line)

```
Planning Worker → Execute Worker → General Worker
     ↓                ↓                ↓
  Design →       Implement →       Document
```

**Example**:
```
/planning-worker design user dashboard
/execute-worker implement dashboard
/general-worker document dashboard API
```

### 2. Parallel Execution (Task Force)

```
Planning Worker
     ↓
┌────┴────┐
Execute   Execute
Worker    Worker
  ↓        ↓
General  General
Worker   Worker
```

**Example**: Parallel implementation of microservices

### 3. Iterative Refinement (Feedback Loop)

```
Execute Worker → General Worker → Planning Worker
     ↓                ↓                ↓
Implement →      Review →        Refine
     ↑                ↑                ↑
     └────────────────────────────────┘
```

**Example**: Code review and improvement cycles

## Worker Communication

### Input Format

Workers expect structured input following the **Durable Prompt Pattern**:

```
ROLE → CONTEXT → TASK → CONSTRAINTS → FORMAT → ACCEPTANCE
```

### Context Access

Workers access context through:

1. **Explicit Parameters**: Provided in the request
2. **Project Context**: `.project_contexts/` files
3. **Skill Assets**: Templates and resources
4. **Previous Results**: Chain of execution history

### Output Structure

Workers return structured results in human-readable format:

```markdown
## Status
success

## Summary
Brief description of outcome

## Artifacts
- /path/to/file1.md
- /path/to/file2.py

## Next Steps
Recommended follow-up actions
```

## Configuration and Customization

### Worker Configuration

Workers are configured via YAML frontmatter in their definition files:

```yaml
---
name: custom-worker
description: Specialized worker for specific domain
model: fast|balanced|accurate  # Model selection
readonly: true|false          # Write permissions
is_background: true|false     # Execution mode
---
```

### Model Selection

- **inherit**: Use same model as parent orchestrator
- **auto**: Automatic model selection based on task
- **specific**: Force use of particular model

### Permission Modes

- **readonly: true**: Can only read and analyze
- **readonly: false**: Can create and modify files

### Execution Modes

- **is_background: false**: Synchronous execution
- **is_background: true**: Asynchronous background execution

## Error Handling and Recovery

### Common Issues

#### Context Access Errors
- **Symptom**: "Context file not found"
- **Solution**: Initialize project with `/initialization`

#### Skill Loading Errors
- **Symptom**: "Skill not available"
- **Solution**: Restart Cursor, re-run migration script

#### Permission Errors
- **Symptom**: "Cannot write to file"
- **Solution**: Check file permissions, run as appropriate user

#### Model Errors
- **Symptom**: "Model not available"
- **Solution**: Check model configuration, use fallback

### Recovery Strategies

1. **Restart Worker**: Re-run the command
2. **Check Context**: Verify `.project_contexts/` state
3. **Simplify Request**: Break complex requests into smaller tasks
4. **Manual Intervention**: Fix context files manually if needed

## Performance Optimization

### Context Pruning

Workers use context pruning to manage large codebases:

- **File Size Threshold**: >10KB files load summaries only
- **Active-First Loading**: Prioritize current tasks
- **Progressive Loading**: Load basic context first

### Parallel Execution

When possible, use multiple workers in parallel:

```bash
# Parallel research and design
/general-worker research authentication libraries &
/planning-worker design authentication architecture &
```

### Background Processing

Use background workers for long-running tasks:

```yaml
is_background: true  # For research, reporting, maintenance
```

## Best Practices

### Task Assignment
- **Match complexity to worker**: Simple tasks to execute worker, complex analysis to planning worker
- **Consider dependencies**: Sequential tasks need careful ordering
- **Balance workload**: Distribute across workers when possible

### Context Management
- **Keep context current**: Regular updates via general worker
- **Use domain separation**: Store information in appropriate domains
- **Clean obsolete context**: Remove outdated or irrelevant information

### Error Prevention
- **Validate inputs**: Ensure clear, specific requests
- **Check prerequisites**: Verify required context exists
- **Test integrations**: Validate worker-skill combinations

### Monitoring and Maintenance
- **Track performance**: Monitor execution times and success rates
- **Update configurations**: Adjust worker settings based on usage patterns
- **Maintain skills**: Keep skill definitions current with best practices

This guide provides the foundation for effectively leveraging Archon's worker system. The key is understanding each worker's strengths and using appropriate orchestration patterns for your development workflow.