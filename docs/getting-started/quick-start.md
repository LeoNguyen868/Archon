# Quick Start Guide

Get up and running with Archon in under 10 minutes.

## Prerequisites

- **Cursor IDE** (recommended) or VS Code
- **Git** for version control
- **Python 3.8+** (for automation scripts)
- Basic understanding of AI-assisted development

## Installation

### Step 1: Clone and Setup

```bash
# Clone the repository
git clone https://github.com/LeoNguyen868/archon.git
cd archon

# Sync to Cursor (recommended setup)
./migration_to_cursor.sh --setup-alias

# Restart Cursor IDE
```

The migration script will:
- Copy skills and agents to your Cursor configuration
- Create convenient aliases for future syncs
- Set up development environment

### Step 2: Verify Installation

Open Cursor and check that Archon is loaded:
1. Open Command Palette (`Cmd/Ctrl + Shift + P`)
2. Type "Archon" to see available commands
3. You should see parent-orchestrator and other skills

## Your First Project

### Initialize a New Project

Create a new project directory and initialize Archon:

```bash
# Create new project
mkdir my-awesome-project
cd my-awesome-project

# Initialize with Archon
archon-init
```

This creates the `.project_contexts/` directory structure for context management.

### First Task: Create a Simple Feature

Let's create a simple todo application:

1. **Start with Parent Orchestrator:**
   ```
   /parent-orchestrator I want to create a simple todo app with React
   ```

2. **Archon will:**
   - Analyze your requirements
   - Break down the task
   - Delegate to appropriate workers
   - Create implementation plan

3. **Review the plan:**
   - Check `.project_contexts/pm/user_stories/` for requirements
   - Review `.project_contexts/arch/tech_specs/` for technical design
   - Examine `.project_contexts/management/backlogs/` for tasks

### Implement the Feature

Archon will guide you through implementation:

```bash
# Execute the implementation plan
/execute-worker implement the todo app according to the tech spec
```

## Understanding the Workflow

### OODA Loop Process

Archon uses the **OODA Loop** for decision making:

1. **Observe** - Analyze current state and requirements
2. **Orient** - Classify request and identify approach
3. **Decide** - Select appropriate worker and skills
4. **Act** - Execute the plan and verify results

### Key Concepts

- **Skills**: Domain-specific capabilities (coding, testing, design, etc.)
- **Workers**: AI agents that execute tasks using skills
- **Context**: Project state stored in `.project_contexts/`
- **Orchestration**: Parent orchestrator coordinates all activities

## Example Workflows

### Feature Development

```
/parent-orchestrator Add user authentication to my app
```

Archon will:
1. Analyze requirements with PO skill
2. Design solution with Tech Consultant skill
3. Break down tasks with PM skill
4. Implement with Execute Worker
5. Test and review the implementation

### Code Review

```
/review check this authentication implementation for security issues
```

### Bug Fixing

```
/debug why is the login form not submitting?
```

### Documentation

```
/report generate a progress report for this sprint
```

## Project Context Management

Archon maintains project state in `.project_contexts/`:

```
.project_contexts/
├── project_context_map.md      # Project overview
├── pm/                         # Product requirements
├── arch/                       # Architecture decisions
├── dev/                        # Development artifacts
├── management/                 # Project management
└── shared/                     # Cross-domain items
```

### Key Files

- **`project_context_map.md`**: Single source of truth
- **`current_progress.md`**: Current status
- **`active.md`**: Active tasks
- **Domain folders**: Organized by concern

## Advanced Usage

### Custom Skills

Create domain-specific skills:

```bash
# Create new skill directory
mkdir cursor/skills/my-custom-skill

# Create skill definition
cat > cursor/skills/my-custom-skill/SKILL.md << 'EOF'
# My Custom Skill

Description of what this skill does.

## When to Use
- Condition for using this skill

## Instructions
Implementation steps...
EOF
```

### Custom Workers

Define specialized workers in `cursor/agents/`.

### Integration with CI/CD

```bash
# Update project context after CI
python cursor/skills/update-project/scripts/update_project.py

# Generate reports
python cursor/skills/report/scripts/generate_report.py
```

## Troubleshooting

### Common Issues

**Skills not loading:**
- Restart Cursor IDE
- Run migration script again
- Check Cursor logs for errors

**Context not updating:**
- Ensure `.project_contexts/` is writable
- Check file permissions
- Verify `.cursorignore` configuration

**Workers failing:**
- Check worker configuration in YAML frontmatter
- Verify required skills are available
- Review error messages in context files

### Getting Help

- Check existing [issues](https://github.com/LeoNguyen868/archon/issues)
- Review [documentation](../README.md)
- Create a new issue with detailed reproduction steps

## Next Steps

Now that you're set up:

1. **Explore examples** in `docs/examples/`
2. **Read the architecture docs** in `docs/architecture/`
3. **Contribute** by checking the [contributing guide](../contributing/CONTRIBUTING.md)
4. **Join the community** on GitHub Discussions

Happy coding with Archon! 🚀