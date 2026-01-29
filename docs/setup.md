# Archon Setup Guide

Follow these steps to set up Archon in your project.

## Prerequisites

- Cursor IDE
- Python 3.8+

## Setup Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/archon.git
   ```

2. **Initialize Project Contexts:**
   Run the initialization script from your project root:
   ```bash
   python3 scripts/init_project.py
   ```
   This will create the `.project_contexts/` directory and basic configuration files.

3. **Configure Cursor:**
   Archon comes with pre-configured rules in `.cursor/rules/`. Make sure Cursor is picking them up.

4. **Define Your Project:**
   Update `.project_contexts/project_context_map.md` with your project name, tagline, and core goals.

## Usage

Start by describing your requirements to the Parent Orchestrator. Archon will then guide you through the OODA loop to analyze, design, plan, and execute your task.
