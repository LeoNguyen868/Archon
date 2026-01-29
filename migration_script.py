#!/usr/bin/env python3
"""
Migration script to rename agent-orchestrator to agent-orchestrator
Maintains backward compatibility during transition
"""

import os
import shutil
import re
from pathlib import Path

def find_files_with_pattern(root_dir, pattern):
    """Find all files containing the given pattern"""
    matches = []
    for path in Path(root_dir).rglob('*'):
        if path.is_file() and path.suffix in ['.md', '.mdc', '.txt', '.py', '.sh']:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if pattern in content:
                        matches.append(path)
            except (UnicodeDecodeError, PermissionError):
                continue
    return matches

def replace_in_file(file_path, replacements):
    """Replace patterns in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        for old_pattern, new_pattern in replacements.items():
            content = content.replace(old_pattern, new_pattern)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def create_migration_script():
    """Create the migration script"""
    root_dir = "/home/hieu/Work/acp_testing"
    
    # Define replacements
    replacements = {
        "agent-orchestrator": "agent-orchestrator",
        "Agent Orchestrator": "Agent Orchestrator",
        "agent orchestrator": "agent orchestrator"
    }
    
    print("=== BACKLOG-001 Migration: agent-orchestrator -> agent-orchestrator ===")
    print(f"Root directory: {root_dir}")
    
    # Step 1: Rename directory structure
    old_dir = Path(root_dir) / "cursor" / "skills" / "agent-orchestrator"
    new_dir = Path(root_dir) / "cursor" / "skills" / "agent-orchestrator"
    
    if old_dir.exists():
        print(f"\n1. Renaming directory: {old_dir} -> {new_dir}")
        try:
            shutil.move(str(old_dir), str(new_dir))
            print("✓ Directory renamed successfully")
        except Exception as e:
            print(f"✗ Error renaming directory: {e}")
    else:
        print(f"✗ Directory not found: {old_dir}")
    
    # Step 2: Find all files with references
    print("\n2. Finding files with references to 'agent-orchestrator'")
    files_to_update = find_files_with_pattern(root_dir, "agent-orchestrator")
    print(f"Found {len(files_to_update)} files to update")
    
    # Step 3: Update content in files
    print("\n3. Updating content in files")
    updated_files = []
    for file_path in files_to_update:
        if replace_in_file(file_path, replacements):
            updated_files.append(file_path)
            print(f"✓ Updated: {file_path.relative_to(root_dir)}")
    
    print(f"\nUpdated {len(updated_files)} files successfully")
    
    # Step 4: Update SKILL.md file
    skill_file = new_dir / "SKILL.md"
    if skill_file.exists():
        print(f"\n4. Updating SKILL.md file: {skill_file}")
        try:
            with open(skill_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Update the frontmatter
            content = content.replace("name: agent-orchestrator", "name: agent-orchestrator")
            content = content.replace("# Agent Orchestrator Skill", "# Agent Orchestrator Skill")
            
            with open(skill_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print("✓ SKILL.md updated successfully")
        except Exception as e:
            print(f"✗ Error updating SKILL.md: {e}")
    
    # Step 5: Create backward compatibility alias
    print("\n5. Creating backward compatibility alias")
    compatibility_file = Path(root_dir) / "cursor" / "skills" / "agent-orchestrator.md"
    try:
        with open(compatibility_file, 'w', encoding='utf-8') as f:
            f.write("""---
name: agent-orchestrator (DEPRECATED)
description: DEPRECATED - Use agent-orchestrator instead. This is a backward compatibility alias.
---

# DEPRECATED: Agent Orchestrator Skill

**This skill has been renamed to `agent-orchestrator`. Please use that instead.**

This file exists for backward compatibility during the transition period.
""")
        print("✓ Backward compatibility alias created")
    except Exception as e:
        print(f"✗ Error creating compatibility alias: {e}")
    
    print("\n=== Migration Summary ===")
    print(f"Directory renamed: {old_dir} -> {new_dir}")
    print(f"Files updated: {len(updated_files)}")
    print(f"Compatibility alias created: {compatibility_file}")
    print("\nMigration completed successfully!")

if __name__ == "__main__":
    create_migration_script()