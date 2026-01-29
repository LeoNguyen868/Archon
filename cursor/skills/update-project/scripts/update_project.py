#!/usr/bin/env python3
"""
update_project.py
Purpose: Update project structure and templates for Archon
Usage: python update_project.py [--action ACTION] [--target TARGET]
Arguments:
  --action: update_structure|update_templates|update_context_map|sync_all
  --target: Target to update (optional)
Output: Project updated status
"""

import os
import sys
import logging
import argparse
from datetime import datetime
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration
PROJECT_ROOT = ".project_contexts"
REQUIRED_DIRECTORIES = [
    f"{PROJECT_ROOT}/pm/user_stories",
    f"{PROJECT_ROOT}/pm/prds",
    f"{PROJECT_ROOT}/pm/acceptance_criteria",
    f"{PROJECT_ROOT}/arch/tech_specs",
    f"{PROJECT_ROOT}/arch/adrs",
    f"{PROJECT_ROOT}/arch/diagrams",
    f"{PROJECT_ROOT}/arch/reviews",
    f"{PROJECT_ROOT}/dev/change_logs",
    f"{PROJECT_ROOT}/dev/documentations",
    f"{PROJECT_ROOT}/dev/current_blockings",
    f"{PROJECT_ROOT}/dev/reviews",
    f"{PROJECT_ROOT}/shared/definitions",
    f"{PROJECT_ROOT}/management/backlogs",
    f"{PROJECT_ROOT}/management/roadmaps",
    f"{PROJECT_ROOT}/management/progress_reports",
]


def main():
    """Main execution function."""
    try:
        args = parse_arguments()
        
        logger.info(f"Updating project: {args['action']}")
        
        # Execute action
        if args['action'] == 'update_structure':
            result = update_structure()
        elif args['action'] == 'update_templates':
            result = update_templates()
        elif args['action'] == 'update_context_map':
            result = update_context_map()
        elif args['action'] == 'sync_all':
            result = sync_all()
        else:
            raise ValueError(f"Unknown action: {args['action']}")
        
        logger.info("Project update complete!")
        print(f"\nResult: {result}")
        return result
        
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)


def parse_arguments() -> Dict[str, Any]:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Update project structure')
    parser.add_argument('--action', type=str, required=True,
                       choices=['update_structure', 'update_templates', 'update_context_map', 'sync_all'],
                       help='Action to perform')
    parser.add_argument('--target', type=str, help='Target to update')
    
    return vars(parser.parse_args())


def update_structure() -> Dict[str, Any]:
    """Update project structure by ensuring all directories exist."""
    created = []
    existing = []
    
    for directory in REQUIRED_DIRECTORIES:
        if not os.path.exists(directory):
            os.makedirs(directory)
            created.append(directory)
            logger.info(f"Created directory: {directory}")
        else:
            existing.append(directory)
    
    return {
        "status": "success",
        "action": "update_structure",
        "created": len(created),
        "existing": len(existing),
        "details": {
            "created_dirs": created,
            "existing_dirs": existing
        }
    }


def update_templates() -> Dict[str, Any]:
    """Update templates from cursor/templates to project contexts."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(os.path.dirname(script_dir), "templates")
    
    if not os.path.exists(templates_dir):
        return {
            "status": "error",
            "message": f"Templates directory not found: {templates_dir}"
        }
    
    updated = []
    skipped = []
    
    # Define template mappings (source -> destination)
    template_mappings = {
        "project_context_map.md": f"{PROJECT_ROOT}/project_context_map.md",
        "current_progress.md": f"{PROJECT_ROOT}/management/current_progress.md",
    }
    
    for template_name, dest_path in template_mappings.items():
        template_src = os.path.join(templates_dir, template_name)
        
        if os.path.exists(template_src):
            # Only update if destination doesn't exist (preserve existing)
            if not os.path.exists(dest_path):
                with open(template_src, 'r') as f:
                    content = f.read()
                with open(dest_path, 'w') as f:
                    f.write(content)
                updated.append(dest_path)
                logger.info(f"Created from template: {dest_path}")
            else:
                skipped.append(dest_path)
                logger.info(f"Skipped (exists): {dest_path}")
        else:
            logger.warning(f"Template not found: {template_src}")
    
    return {
        "status": "success",
        "action": "update_templates",
        "updated": updated,
        "skipped": skipped
    }


def update_context_map() -> Dict[str, Any]:
    """Update project context map with current date."""
    context_map_path = f"{PROJECT_ROOT}/project_context_map.md"
    
    if not os.path.exists(context_map_path):
        return {
            "status": "error",
            "message": f"Context map not found: {context_map_path}"
        }
    
    # Read current content
    with open(context_map_path, 'r') as f:
        content = f.read()
    
    # Update last updated date
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Simple pattern replacement for date
    if "> Last Updated:" in content:
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if "> Last Updated:" in line:
                lines[i] = f"> Last Updated: {current_date}"
                break
        content = '\n'.join(lines)
        
        with open(context_map_path, 'w') as f:
            f.write(content)
        
        logger.info(f"Updated context map date to: {current_date}")
    
    return {
        "status": "success",
        "action": "update_context_map",
        "updated_date": current_date
    }


def sync_all() -> Dict[str, Any]:
    """Perform all update operations."""
    results = {
        "structure": update_structure(),
        "templates": update_templates(),
        "context_map": update_context_map()
    }
    
    return {
        "status": "success",
        "action": "sync_all",
        "results": results
    }


if __name__ == "__main__":
    main()
