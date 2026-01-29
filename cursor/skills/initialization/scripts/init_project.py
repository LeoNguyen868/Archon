#!/usr/bin/env python3
import os
import argparse
import sys

CURSORIGNORE_TEMPLATE = """# Allow AI to access project context files despite gitignore
# This overrides git's ignore rules for Cursor AI operations
!.project_contexts/

# Still ignore generated/sensitive content within project_contexts
.project_contexts/**/temp/
.project_contexts/**/cache/
.project_contexts/**/*.log
"""

def create_directory(path):
    if not os.path.exists(path):
        try:
            os.makedirs(path)
            print(f"Created directory: {path}")
        except OSError as e:
            print(f"Error creating directory {path}: {e}")
            sys.exit(1)
    else:
        print(f"Directory already exists: {path}")

def create_file(path, content):
    if not os.path.exists(path):
        try:
            with open(path, 'w') as f:
                f.write(content)
            print(f"Created file: {path}")
        except OSError as e:
            print(f"Error creating file {path}: {e}")
            sys.exit(1)
    else:
        print(f"File already exists: {path}")

def read_template(template_path):
    try:
        with open(template_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Template not found: {template_path}")
        return ""

def main():
    parser = argparse.ArgumentParser(description="Initialize Archon Project Structure")
    parser.add_argument("--root", default=".", help="Root directory for the project")
    args = parser.parse_args()

    root_dir = args.root
    project_contexts_dir = os.path.join(root_dir, ".project_contexts")

    # Define directory structure
    dirs = [
        os.path.join(project_contexts_dir, "pm", "user_stories"),
        os.path.join(project_contexts_dir, "pm", "prds"),
        os.path.join(project_contexts_dir, "pm", "acceptance_criteria"),
        os.path.join(project_contexts_dir, "arch", "tech_specs"),
        os.path.join(project_contexts_dir, "arch", "adrs"),
        os.path.join(project_contexts_dir, "arch", "diagrams"),
        os.path.join(project_contexts_dir, "arch", "reviews"),
        os.path.join(project_contexts_dir, "dev", "change_logs"),
        os.path.join(project_contexts_dir, "dev", "documentations"),
        os.path.join(project_contexts_dir, "dev", "current_blockings"),
        os.path.join(project_contexts_dir, "dev", "reviews"),
        os.path.join(project_contexts_dir, "management", "backlogs"),
        os.path.join(project_contexts_dir, "management", "roadmaps"),
        os.path.join(project_contexts_dir, "management", "progress_reports"),
        os.path.join(project_contexts_dir, "shared", "definitions"),
        os.path.join(root_dir, ".cursor", "rules"),
    ]

    print("Initializing project structure...")
    for d in dirs:
        create_directory(d)

    # Define templates mapping
    # Format: (skill_name, template_filename, destination_path)
    templates_mapping = [
        ("update-project", "project_context_map.md", os.path.join(project_contexts_dir, "project_context_map.md")),
        ("update-project", "current_progress.md", os.path.join(project_contexts_dir, "management", "current_progress.md")),
        ("pm-project-manager", "implementation_ticket.md", os.path.join(project_contexts_dir, "management", "backlogs", "active.md")),
        ("update-project", "communication_rules.mdc", os.path.join(root_dir, ".cursor", "rules", "communication_rules.mdc")),
    ]
    
    # Skills root directory relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # script is in cursor/skills/initialization/scripts
    # skills is in cursor/skills
    skills_root = os.path.dirname(os.path.dirname(script_dir))

    print("Creating template files...")
    for skill, template_name, dest_path in templates_mapping:
        # Template path: cursor/skills/<skill>/assets/<template_name>
        template_src = os.path.join(skills_root, skill, "assets", template_name)
        content = read_template(template_src)
        if content:
            create_file(dest_path, content)
        else:
            print(f"Skipping {dest_path} due to missing template at {template_src}.")
    
    # Create .cursorignore
    create_file(os.path.join(root_dir, ".cursorignore"), CURSORIGNORE_TEMPLATE)
    
    # Manual creation for some files if templates don't exist yet or need dynamic content
    # For now, we assume templates will be created.

    print("Project initialization complete.")

if __name__ == "__main__":
    main()
