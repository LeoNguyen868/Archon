# Archon

**The Socratic Orchestrator for AI Development Teams.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Cursor](https://img.shields.io/badge/IDE-Cursor-blue)](https://cursor.sh/)

Archon transforms your IDE into a specialized AI orchestration environment. It utilizes the OODA Loop model and the Socratic method to coordinate AI Sub-agents (Product Owner, Architect, Developer) through a skills-centric architecture.

## Overview

Archon is designed to bring order and structure to AI-driven development. By acting as a Agent Orchestrator, it ensures that every task is properly analyzed, planned, and reviewed before execution.

### Key Features

- **Skills-Centric Architecture:** Agents are augmented with specialized "knowledge modules" (Skills) that define domain-specific best practices.
- **Sub-agent Delegation:** Tasks are delegated to specialized workers (Planning, Execution, General) operating in isolated context windows.
- **OODA Loop Decision Making:** Every request follows an Observe-Orient-Decide-Act cycle.
- **Socratic Questioning:** Archon doesn't just execute; it asks "Is that true?" and "What is the real problem?" to ensure alignment and quality.
- **Single Source of Truth:** Maintains project state in a structured `.project_contexts/` directory.
- **Open Source:** Fully open source with comprehensive documentation and contributor guidelines.

## Getting Started

Archon is designed to work seamlessly within Cursor IDE.

### Prerequisites

- **Cursor IDE** (recommended) or VS Code with Cursor extensions
- **Git** for version control
- **Python 3.8+** (for automation scripts)
- Basic understanding of AI-assisted development

### Quick Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/LeoNguyen868/archon.git
   cd archon
   ```

2. **Sync to Cursor:**
   ```bash
   # Basic sync (recommended for most users)
   ./migration_to_cursor.sh

   # Or setup convenient alias for future syncs
   ./migration_to_cursor.sh --setup-alias

   # Or create automatic watch mode for development
   ./migration_to_cursor.sh --setup-alias --create-watch
   ```

3. **Restart Cursor IDE** to load the new configuration.

### First Project Setup

```bash
# Create new project
mkdir my-awesome-project
cd my-awesome-project

# Initialize with Archon
archon-init
```

This creates the `.project_contexts/` directory structure for context management.

### Your First Task

Try the agent orchestrator:
```
/agent-orchestrator create a simple todo app with React
```

Archon will analyze requirements, design the solution, break it down into tasks, and guide implementation.

## Repository Structure

```text
archon/
├── .cursor/                    # Cursor IDE configuration
│   ├── skills/                 # Skills library (15 skills)
│   │   ├── agent-orchestrator/
│   │   ├── po-product-owner/
│   │   ├── tech-consultant/
│   │   ├── pm-project-manager/
│   │   ├── coding/
│   │   ├── code-analysis/
│   │   ├── debug/
│   │   ├── test/
│   │   ├── review/
│   │   ├── frontend-design/
│   │   ├── delegation/
│   │   ├── initialization/
│   │   ├── update-project/
│   │   ├── report/
│   │   └── research/
│   └── rules/                  # Communication protocols
├── cursor/
│   └── agents/                 # Worker definitions (3 workers)
│       ├── planning-worker.md
│       ├── execute-worker.md
│       └── general-worker.md
├── docs/                       # Comprehensive documentation
│   ├── getting-started/
│   │   └── quick-start.md      # Quick start guide
│   ├── user-guide/
│   │   ├── skills-reference.md # Skills reference
│   │   └── workers-reference.md # Workers guide
│   ├── architecture/           # Technical architecture
│   │   ├── overview.md         # System architecture
│   │   ├── skills-architecture.md
│   │   ├── worker-orchestration.md
│   │   ├── ooda-loop.md
│   │   └── context-management.md
│   ├── contributing/           # Contributor documentation
│   │   ├── CONTRIBUTING.md    # Contribution guidelines
│   │   ├── creating-skills.md
│   │   ├── creating-workers.md
│   │   └── code-style.md
│   └── examples/               # Usage examples
├── scripts/                    # Automation scripts
│   ├── migration_to_cursor.sh # IDE integration
│   └── python/                 # Python utilities
├── .project_contexts/          # Single Source of Truth (git-ignored)
├── LICENSE                     # MIT License
└── README.md
```

## Documentation

### 📚 User Guides

- **[Quick Start](docs/getting-started/quick-start.md)** - Get up and running in under 10 minutes
- **[Skills Reference](docs/user-guide/skills-reference.md)** - Complete guide to all 15 skills
- **[Workers Reference](docs/user-guide/workers-reference.md)** - Understanding the worker system

### 🏗️ Architecture

- **[System Overview](docs/architecture/overview.md)** - High-level architecture and concepts
- **[Skills Architecture](docs/architecture/skills-architecture.md)** - Skills-centric design patterns
- **[Worker Orchestration](docs/architecture/worker-orchestration.md)** - Orchestration patterns and flows
- **[OODA Loop](docs/architecture/ooda-loop.md)** - Decision-making framework
- **[Context Management](docs/architecture/context-management.md)** - Project state management

### 🤝 Contributing

- **[Contribution Guide](CONTRIBUTING.md)** - How to contribute to Archon
- **[Creating Skills](docs/contributing/creating-skills.md)** - Add new skills to the library
- **[Creating Workers](docs/contributing/creating-workers.md)** - Extend the worker system
- **[Code Style](docs/contributing/code-style.md)** - Coding standards and guidelines

### 💡 Examples

- **[Basic Workflow](docs/examples/basic-workflow.md)** - Common usage patterns
- **[Custom Skill](docs/examples/custom-skill.md)** - Creating custom skills
- **[Custom Worker](docs/examples/custom-worker.md)** - Extending workers

## Architecture Highlights

### Skills-Centric Design

Archon revolves around **Skills** - domain-specific knowledge modules:

- **High-Level Skills** (4): Strategic coordination and planning
- **Technical Skills** (6): Implementation and analysis
- **Support Skills** (5): Infrastructure and maintenance

### OODA Loop Decision Making

Every task follows the **OODA Loop**:
1. **Observe** - Analyze current state
2. **Orient** - Classify and understand
3. **Decide** - Select appropriate approach
4. **Act** - Execute and verify

### Worker Orchestration

Three specialized workers in isolated contexts:
- **Planning Worker**: Analysis, design, requirements
- **Execute Worker**: Implementation, testing, debugging
- **General Worker**: Research, reporting, maintenance

### Context Management

**Single Source of Truth** in `.project_contexts/`:
- Domain separation (PM, Architecture, Development, Management)
- Context pruning for performance
- Git integration with selective access

## Use Cases

### Feature Development
```
/agent-orchestrator add user authentication to my web app
```

### Code Analysis
```
/code-analysis analyze this legacy codebase for modernization opportunities
```

### Bug Investigation
```
/debug why is the API returning 500 errors?
```

### Technical Design
```
/tech-consultant design microservices architecture for e-commerce platform
```

### Testing
```
/test create comprehensive test suite for payment processing
```

## Author

**Nguyen Van Hieu (LeoNguyen868)**
- GitHub: [https://github.com/LeoNguyen868](https://github.com/LeoNguyen868)
- LinkedIn: [Your LinkedIn if applicable]

## Contributing

We welcome contributions! See our [Contribution Guide](CONTRIBUTING.md) for details.

**Quick Start for Contributors:**
1. Fork the repository
2. Read the [Contributing Guide](CONTRIBUTING.md)
3. Check [Creating Skills](docs/contributing/creating-skills.md) or [Creating Workers](docs/contributing/creating-workers.md)
4. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **OODA Loop** concept by John Boyd
- **Socratic Method** inspiration from classical philosophy
- **Cursor IDE** for the excellent AI-assisted development platform
- Open source community for inspiration and collaboration

---

*Supercharge your development with Archon!* 🚀
