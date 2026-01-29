# Skills Reference Guide

This guide provides comprehensive reference for all Archon skills, organized by category and usage.

## Skills Overview

Archon includes **15 core skills** organized into three categories:

- **High-Level Skills** (4): Strategic decision making and coordination
- **Technical Skills** (6): Implementation and analysis
- **Support Skills** (5): Infrastructure and maintenance

## High-Level Skills

### 1. Parent Orchestrator

**Purpose**: System coordinator using OODA Loop and Socratic method

**When to Use**:
- Complex multi-step tasks requiring coordination
- Tasks needing analysis before execution
- Projects requiring multiple specialized workers
- Any task execution in Archon system

**Key Features**:
- OODA Loop decision making (Observe → Orient → Decide → Act)
- Socratic questioning methodology
- Human-in-the-loop verification
- Isolated context windows for workers

**Usage**:
```
/parent-orchestrator [task description]
```

**Example**:
```
/parent-orchestrator create a user authentication system for my web app
```

### 2. Product Owner (PO)

**Purpose**: Requirements analysis and user story creation

**When to Use**:
- Defining user requirements
- Creating user stories and acceptance criteria
- Analyzing business needs
- Validating feature requests

**Key Features**:
- Socratic questioning for requirement validation
- User story creation with INVEST criteria
- Acceptance criteria definition
- Business value assessment

**Output**: User story files in `.project_contexts/pm/user_stories/`

**Usage**:
```
/po-product-owner analyze requirements for [feature]
```

### 3. Tech Consultant

**Purpose**: Technical design, architecture decisions, and trade-off analysis

**When to Use**:
- Making architectural decisions
- Evaluating technical trade-offs
- Creating technical specifications
- Designing system components

**Key Features**:
- Architecture Decision Records (ADRs)
- Technical specification creation
- Security-first approach
- Trade-off analysis with pros/cons

**Output**:
- Tech specs in `.project_contexts/arch/tech_specs/`
- ADRs in `.project_contexts/arch/adrs/`

**Usage**:
```
/tech-consultant design solution for [requirement]
```

### 4. Project Manager (PM)

**Purpose**: Task breakdown, backlog management, and dependency tracking

**When to Use**:
- Breaking down large features into tasks
- Managing project backlogs
- Tracking dependencies and blockers
- Planning sprints or iterations

**Key Features**:
- Task decomposition using appropriate strategies
- Dependency identification and management
- Progress tracking and reporting
- Risk assessment and mitigation

**Output**: Implementation tickets in `.project_contexts/management/backlogs/`

**Usage**:
```
/pm-project-manager break down [feature] into tasks
```

## Technical Skills

### 5. Coding

**Purpose**: Production code implementation according to specifications

**When to Use**:
- Implementing new features
- Writing production code
- Following established patterns and best practices
- Code generation from specifications

**Key Features**:
- Production-ready code generation
- Best practices adherence
- Error handling and edge cases
- Documentation and comments

**Languages Supported**: JavaScript, TypeScript, Python, Java, Go, Rust, etc.

**Usage**:
```
/coding implement [feature] according to [tech spec]
```

### 6. Code Analysis

**Purpose**: Analyzing existing code for patterns, dependencies, and structure

**When to Use**:
- Understanding unfamiliar codebases
- Identifying code patterns and anti-patterns
- Analyzing dependencies and relationships
- Code review preparation

**Key Features**:
- Pattern recognition and analysis
- Dependency mapping
- Code quality assessment
- Refactoring recommendations

**Usage**:
```
/code-analysis analyze [code/file/directory] for [purpose]
```

### 7. Debug

**Purpose**: Error analysis, root cause identification, and fix implementation

**When to Use**:
- Code is failing or behaving unexpectedly
- Need to identify root causes of issues
- Debugging complex problems
- Analyzing error logs and stack traces

**Key Features**:
- Systematic debugging methodology
- Root cause analysis
- Fix implementation and testing
- Prevention recommendations

**Usage**:
```
/debug [describe the problem or error]
```

### 8. Test

**Purpose**: Test creation, execution, and validation

**When to Use**:
- Writing unit tests, integration tests, or E2E tests
- Validating code functionality
- Ensuring code quality and preventing regressions
- Test-driven development

**Key Features**:
- Multiple test types (unit, integration, e2e)
- Test framework integration
- Coverage analysis
- Test best practices

**Usage**:
```
/test create tests for [feature/component]
```

### 9. Review

**Purpose**: Code and document review for quality, security, and performance

**When to Use**:
- Reviewing code changes before merge
- Security vulnerability assessment
- Performance optimization review
- Documentation quality checks

**Key Features**:
- Comprehensive review checklists
- Security vulnerability detection
- Performance analysis
- Best practice validation

**Usage**:
```
/review check [code/docs] for [quality/security/performance]
```

### 10. Frontend Design

**Purpose**: UI/UX design and implementation

**When to Use**:
- Creating user interfaces
- Designing user experiences
- Implementing responsive designs
- Accessibility compliance

**Key Features**:
- Modern UI frameworks support
- Responsive design principles
- Accessibility best practices (WCAG)
- User experience optimization

**Supported Frameworks**: React, Vue, Angular, HTML/CSS, etc.

**Usage**:
```
/frontend-design create UI for [feature] with [requirements]
```

## Support Skills

### 11. Delegation

**Purpose**: Task distribution and coordination between workers

**When to Use**:
- Distributing work across multiple workers
- Coordinating parallel tasks
- Managing worker assignments
- Optimizing resource utilization

**Key Features**:
- Task analysis and distribution
- Worker capability matching
- Progress coordination
- Conflict resolution

**Usage**:
```
/delegation distribute [tasks] across [workers]
```

### 12. Initialization

**Purpose**: Project structure setup and template initialization

**When to Use**:
- Setting up new projects
- Creating directory structures
- Initializing configuration files
- Bootstrapping development environments

**Key Features**:
- Automated project structure creation
- Template copying and customization
- Configuration file generation
- Environment setup validation

**Usage**:
```
/initialization setup project with [structure/templates]
```

### 13. Update Project

**Purpose**: Project maintenance, context updates, and synchronization

**When to Use**:
- Updating project structure
- Synchronizing templates and contexts
- Maintaining project documentation
- Updating project metadata

**Key Features**:
- Structure validation and updates
- Template synchronization
- Context map maintenance
- Progress tracking updates

**Usage**:
```
/update-project [sync/update/maintain] project [components]
```

### 14. Report

**Purpose**: Progress reporting, status updates, and documentation generation

**When to Use**:
- Generating progress reports
- Creating status summaries
- Documenting project state
- Communicating with stakeholders

**Key Features**:
- Multiple report formats (markdown, JSON, HTML)
- Automated data collection
- Progress visualization
- Stakeholder communication templates

**Usage**:
```
/report generate [type] report for [scope]
```

### 15. Research

**Purpose**: Information gathering, documentation research, and knowledge synthesis

**When to Use**:
- Researching technologies or libraries
- Gathering requirements information
- Analyzing external documentation
- Synthesizing knowledge from multiple sources

**Key Features**:
- Multi-source information gathering
- Knowledge synthesis and summarization
- Source validation and credibility assessment
- Research methodology application

**Usage**:
```
/research investigate [topic/technology/library] for [purpose]
```

## Skill Usage Patterns

### Basic Usage

Most skills follow this pattern:
```
/skill-name [action] [target] [context]
```

### Advanced Usage

#### Chaining Skills
Skills can be used sequentially:
```
/po-product-owner analyze user authentication requirements
/tech-consultant design authentication architecture
/coding implement authentication system
/test create authentication tests
```

#### Context-Aware Usage
Skills automatically access relevant context:
```
/coding implement feature (reads from .project_contexts/arch/tech_specs/)
/test create tests (reads from implementation context)
```

#### Orchestrated Usage
Parent orchestrator handles complex coordination:
```
/parent-orchestrator build complete e-commerce checkout flow
```

## Skill Configuration

### Skill Metadata

Each skill includes:
- **Name**: Unique identifier
- **Description**: What the skill does
- **Category**: High-level, Technical, or Support
- **Dependencies**: Required context or prerequisites

### Customization

Skills can be customized by:
- Modifying SKILL.md instructions
- Adding custom templates in `assets/`
- Creating automation scripts in `scripts/`
- Updating worker configurations

## Error Handling

### Common Issues

- **Context Not Found**: Ensure `.project_contexts/` is initialized
- **Skill Not Available**: Check if skill is loaded in Cursor
- **Permission Denied**: Verify file permissions for context updates
- **Invalid Input**: Provide clear, specific instructions

### Troubleshooting

1. **Restart Cursor** to reload skills
2. **Check context files** for proper initialization
3. **Verify skill syntax** in SKILL.md files
4. **Review error messages** in context logs

## Best Practices

### Skill Selection
- Choose the most specific skill for your task
- Use high-level skills for complex coordination
- Combine skills for comprehensive solutions

### Context Management
- Keep context files current and accurate
- Use domain separation appropriately
- Regularly clean up obsolete context

### Performance Optimization
- Provide clear, concise instructions
- Include relevant context upfront
- Use appropriate skill combinations

This reference provides the foundation for effectively using Archon's skills. Experiment with different combinations to find what works best for your development workflow.