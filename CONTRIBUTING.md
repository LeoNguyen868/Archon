# Contributing to Archon

Thank you for your interest in contributing to Archon! This document provides guidelines and information for contributors.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Workflow](#development-workflow)
- [Creating Skills](#creating-skills)
- [Creating Workers](#creating-workers)
- [Testing](#testing)
- [Documentation](#documentation)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project follows a code of conduct to ensure a welcoming environment for all contributors. Please be respectful and constructive in all interactions.

## Getting Started

### Prerequisites

- Git
- Python 3.8+ (for automation scripts)
- Cursor IDE (recommended)
- Basic understanding of AI orchestration concepts

### Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/LeoNguyen868/archon.git
   cd archon
   ```

2. **Set up Cursor configuration:**
   ```bash
   # Basic sync (recommended)
   ./migration_to_cursor.sh

   # Or setup with convenient alias
   ./migration_to_cursor.sh --setup-alias
   ```

3. **Restart Cursor IDE** to load the new configuration.

### Project Structure

```
archon/
├── .cursor/                 # Cursor IDE configuration
│   ├── skills/             # Skill library (15 skills)
│   └── rules/              # Communication protocols
├── cursor/                  # Core implementation
│   ├── agents/             # Worker definitions (3 workers)
│   └── skills/             # Skill implementations
├── docs/                    # Documentation
├── scripts/                 # Automation scripts
└── .project_contexts/       # Context management (git-ignored)
```

## How to Contribute

### Types of Contributions

- **Bug fixes** - Fix issues in existing code
- **Features** - Add new functionality
- **Documentation** - Improve documentation
- **Skills** - Create new skills for the skill library
- **Workers** - Create new worker types
- **Testing** - Add tests and improve test coverage

### Finding Issues

- Check the [Issues](https://github.com/LeoNguyen868/archon/issues) page
- Look for issues labeled `good first issue` or `help wanted`
- Comment on issues you'd like to work on to avoid duplicate work

## Development Workflow

### 1. Choose an Issue

Select an issue from the [Issues](https://github.com/LeoNguyen868/archon/issues) page or create a new one describing your proposed changes.

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-number-description
```

### 3. Make Changes

- Follow the [code style guidelines](#code-style)
- Write tests for new functionality
- Update documentation as needed
- Ensure all tests pass

### 4. Commit Changes

```bash
git add .
git commit -m "feat: add new skill for X functionality

- Added new skill implementation
- Updated documentation
- Added tests"
```

Follow conventional commit format:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `test:` for test-related changes
- `refactor:` for code refactoring

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub.

## Creating Skills

Skills are the core architectural pattern of Archon. Each skill defines domain-specific capabilities and best practices.

### Skill Structure

Skills are stored in `cursor/skills/` and follow this structure:

```
skill-name/
├── SKILL.md              # Main skill definition
├── assets/               # Templates and resources (optional)
│   └── template.md
└── scripts/              # Automation scripts (optional)
    └── script.py
```

### Skill Definition Format

Each skill must have a `SKILL.md` file with this structure:

```markdown
# Skill Name

Brief description of what this skill does and when to use it.

## When to Use

- Condition 1 for using this skill
- Condition 2 for using this skill

## Instructions

Detailed instructions for how to apply this skill, including:

### Step 1
Description and implementation details.

### Step 2
More implementation steps.

## Output Format

Expected output format or structure.

## Examples

Code examples or usage scenarios.

## Constraints

Any limitations or requirements.
```

### Skill Categories

Skills are categorized into three types:

1. **High-Level Skills** - Strategic decision making
   - `agent-orchestrator`, `po-product-owner`, `tech-consultant`, `pm-project-manager`

2. **Technical Skills** - Implementation and analysis
   - `coding`, `code-analysis`, `debug`, `test`, `review`, `frontend-design`

3. **Support Skills** - Infrastructure and maintenance
   - `delegation`, `initialization`, `update-project`, `report`, `research`

### Creating a New Skill

1. **Choose a category** and create directory: `cursor/skills/your-skill-name/`

2. **Create SKILL.md** following the format above

3. **Add templates/assets** if needed in `assets/` subdirectory

4. **Test the skill** by using it in Cursor

5. **Document usage** in the skill definition

### Skill Best Practices

- **Clear scope**: Each skill should have a focused, well-defined purpose
- **Comprehensive instructions**: Include all necessary context and steps
- **Consistent formatting**: Follow established patterns from existing skills
- **Error handling**: Document potential failure modes and recovery
- **Examples**: Provide practical usage examples
- **Constraints**: Clearly state limitations and requirements

## Creating Workers

Workers are AI agents that execute tasks using skills. There are currently three worker types: planning, execution, and general.

### Worker Structure

Workers are defined in `cursor/agents/` with this format:

```markdown
---
name: worker-name
description: Brief description of when to use this worker
model: inherit|auto|specific-model
readonly: true|false
is_background: true|false
---

# Worker Name

Detailed description and capabilities.

## Capabilities

- Capability 1
- Capability 2

## Use Cases

- Use case 1
- Use case 2

## Skills Used

List of skills this worker can utilize.
```

### Worker Types

1. **Planning Worker** (`planning-worker.md`)
   - Uses: PO, Tech Consultant, PM skills
   - Purpose: Analysis, design, planning

2. **Execute Worker** (`execute-worker.md`)
   - Uses: Coding, Test, Frontend Design skills
   - Purpose: Implementation and testing

3. **General Worker** (`general-worker.md`)
   - Uses: Report, Research, Update Project skills
   - Purpose: Research, reporting, maintenance

### Creating a New Worker

1. **Determine purpose** and required skills

2. **Create worker file** in `cursor/agents/new-worker.md`

3. **Define configuration** in YAML frontmatter

4. **Document capabilities** and use cases

5. **Test integration** with existing skills

## Testing

### Running Tests

```bash
# Run all tests (if test framework is implemented)
npm test

# Or run specific test files
python -m pytest tests/
```

### Test Guidelines

- Write tests for all new functionality
- Include both unit tests and integration tests
- Test error conditions and edge cases
- Ensure tests are automated and run in CI/CD

## Documentation

### Documentation Standards

- All documentation in English
- Use Markdown format
- Include code examples where relevant
- Keep documentation current with code changes
- Use consistent formatting and structure

### Updating Documentation

- Update README.md for significant changes
- Add examples for new features
- Keep API documentation current
- Document breaking changes clearly

## Pull Request Process

### Before Submitting

- [ ] All tests pass
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Commit messages follow conventional format
- [ ] Branch is up to date with main

### Pull Request Template

Please use this template for pull requests:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring
- [ ] Other

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed

## Checklist
- [ ] Code follows project standards
- [ ] Documentation updated
- [ ] No breaking changes
- [ ] Ready for review
```

### Review Process

1. Automated checks run (tests, linting)
2. Code review by maintainers
3. Address review comments
4. Merge when approved

## Getting Help

- **Issues**: Report bugs and request features
- **Discussions**: Ask questions and get community help
- **Documentation**: Check docs/ directory for detailed guides

## Recognition

Contributors will be recognized in:
- GitHub contributor statistics
- CHANGELOG.md for significant contributions
- Release notes

Thank you for contributing to Archon! 🚀