#!/usr/bin/env python3
"""
generate_report.py
Purpose: Generate progress reports for Archon
Usage: python generate_report.py [--format FORMAT] [--output OUTPUT]
Arguments:
  --format: markdown|json|html (default: markdown)
  --output: Output file path (optional, defaults to stdout)
Output: Progress report in specified format
"""

import os
import sys
import json
import logging
import argparse
from datetime import datetime
from typing import Dict, Any, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration
PROJECT_ROOT = ".project_contexts"


def main():
    """Main execution function."""
    try:
        args = parse_arguments()
        
        logger.info(f"Generating progress report in {args['format']} format...")
        
        # Read project state
        project_state = read_project_state()
        
        # Generate report
        report = generate_report(project_state, args['format'])
        
        # Output report
        if args['output']:
            save_report(report, args['output'])
            logger.info(f"Report saved to: {args['output']}")
        else:
            print(report)
        
        logger.info("Report generated successfully!")
        return {"status": "success", "format": args['format']}
        
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)


def parse_arguments() -> Dict[str, Any]:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Generate progress report')
    parser.add_argument('--format', type=str, default='markdown',
                       choices=['markdown', 'json', 'html'],
                       help='Output format')
    parser.add_argument('--output', type=str, help='Output file path')
    
    return vars(parser.parse_args())


def read_file_safe(path: str) -> Optional[str]:
    """Safely read a file, returning None if it doesn't exist."""
    try:
        if os.path.exists(path):
            with open(path, 'r') as f:
                return f.read()
    except Exception as e:
        logger.warning(f"Could not read {path}: {e}")
    return None


def read_project_state() -> Dict[str, Any]:
    """Read project state from files."""
    state = {
        "timestamp": datetime.now().isoformat(),
        "project_context_map": None,
        "current_progress": None,
        "active_tasks": None,
        "sprint_backlog": None,
        "blockers": [],
        "change_logs": []
    }
    
    # Read main context files
    state["project_context_map"] = read_file_safe(f"{PROJECT_ROOT}/project_context_map.md")
    state["current_progress"] = read_file_safe(f"{PROJECT_ROOT}/management/current_progress.md")
    state["active_tasks"] = read_file_safe(f"{PROJECT_ROOT}/management/backlogs/active.md")
    state["sprint_backlog"] = read_file_safe(f"{PROJECT_ROOT}/management/backlogs/sprint_backlog.md")
    
    # Read blockers
    blockers_dir = f"{PROJECT_ROOT}/dev/current_blockings"
    if os.path.exists(blockers_dir):
        for file in os.listdir(blockers_dir):
            if file.endswith('.md'):
                content = read_file_safe(os.path.join(blockers_dir, file))
                if content:
                    state["blockers"].append({"file": file, "content": content})
    
    # Read recent change logs
    logs_dir = f"{PROJECT_ROOT}/dev/change_logs"
    if os.path.exists(logs_dir):
        for file in sorted(os.listdir(logs_dir), reverse=True)[:5]:  # Last 5 logs
            if file.endswith('.md'):
                content = read_file_safe(os.path.join(logs_dir, file))
                if content:
                    state["change_logs"].append({"file": file, "content": content})
    
    return state


def generate_report(state: Dict[str, Any], format: str) -> str:
    """Generate report in specified format."""
    if format == 'markdown':
        return generate_markdown_report(state)
    elif format == 'json':
        return generate_json_report(state)
    elif format == 'html':
        return generate_html_report(state)
    else:
        raise ValueError(f"Unknown format: {format}")


def generate_markdown_report(state: Dict[str, Any]) -> str:
    """Generate Markdown progress report."""
    report = []
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    report.append("# Progress Report")
    report.append(f"\n**Generated:** {current_date}\n")
    
    # Overall Status
    report.append("## Status Overview\n")
    
    blocker_count = len(state.get("blockers", []))
    if blocker_count > 0:
        report.append(f"- **Overall Status:** [!] At Risk ({blocker_count} blocker(s))")
    else:
        report.append("- **Overall Status:** [OK] On Track")
    
    # Active Tasks
    report.append("\n## Active Tasks\n")
    if state.get("active_tasks"):
        report.append(state["active_tasks"])
    else:
        report.append("*No active tasks found.*")
    
    # Sprint Backlog Summary
    report.append("\n## Sprint Backlog\n")
    if state.get("sprint_backlog"):
        # Extract just the task list from backlog
        report.append(state["sprint_backlog"])
    else:
        report.append("*No sprint backlog found.*")
    
    # Blockers
    report.append("\n## Blockers & Risks\n")
    if state.get("blockers"):
        for blocker in state["blockers"]:
            report.append(f"### {blocker['file']}\n")
            report.append(blocker["content"])
    else:
        report.append("*No blockers reported.*")
    
    # Recent Changes
    report.append("\n## Recent Changes\n")
    if state.get("change_logs"):
        for log in state["change_logs"][:3]:  # Show last 3
            report.append(f"### {log['file']}\n")
            # Show first 10 lines of each log
            lines = log["content"].split('\n')[:10]
            report.append('\n'.join(lines))
            if len(log["content"].split('\n')) > 10:
                report.append("\n*... (truncated)*")
    else:
        report.append("*No change logs found.*")
    
    return '\n'.join(report)


def generate_json_report(state: Dict[str, Any]) -> str:
    """Generate JSON progress report."""
    report = {
        "generated_at": datetime.now().isoformat(),
        "status": "on_track" if len(state.get("blockers", [])) == 0 else "at_risk",
        "blocker_count": len(state.get("blockers", [])),
        "has_active_tasks": state.get("active_tasks") is not None,
        "has_sprint_backlog": state.get("sprint_backlog") is not None,
        "recent_changes_count": len(state.get("change_logs", [])),
        "blockers": [b["file"] for b in state.get("blockers", [])],
    }
    return json.dumps(report, indent=2)


def generate_html_report(state: Dict[str, Any]) -> str:
    """Generate HTML progress report."""
    markdown_content = generate_markdown_report(state)
    
    # Basic HTML wrapper
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Progress Report</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 40px; }}
        h1 {{ color: #333; }}
        h2 {{ color: #555; border-bottom: 1px solid #ddd; padding-bottom: 5px; }}
        pre {{ background: #f4f4f4; padding: 10px; overflow-x: auto; }}
    </style>
</head>
<body>
<pre>{markdown_content}</pre>
</body>
</html>"""
    return html


def save_report(report: str, output_path: str):
    """Save report to file."""
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
    
    with open(output_path, 'w') as f:
        f.write(report)


if __name__ == "__main__":
    main()
