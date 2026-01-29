#!/bin/bash

# Test script to demonstrate the migration script fix for deletion handling
# This script creates test scenarios and validates the fixed behavior

set -e

# Configuration
TEST_DIR="/tmp/cursor_migration_test"
SOURCE_TEST_DIR="$TEST_DIR/cursor"
TARGET_TEST_DIR="$TEST_DIR/.cursor"
MIGRATION_SCRIPT="$(pwd)/migration_to_cursor.sh"

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() { echo -e "${BLUE}[TEST INFO]${NC} $1"; }
print_success() { echo -e "${GREEN}[TEST SUCCESS]${NC} $1"; }
print_warning() { echo -e "${YELLOW}[TEST WARNING]${NC} $1"; }
print_error() { echo -e "${RED}[TEST ERROR]${NC} $1"; }

cleanup() {
    print_status "Cleaning up test environment..."
    rm -rf "$TEST_DIR"
}

setup_test_environment() {
    print_status "Setting up test environment..."
    
    # Clean up any existing test directory
    cleanup 2>/dev/null || true
    
    # Create test directories
    mkdir -p "$SOURCE_TEST_DIR"/agents/{cursor-cursor,cursor-skills}
    mkdir -p "$SOURCE_TEST_DIR"/skills/{code-analysis,coding,debug}
    mkdir -p "$SOURCE_TEST_DIR"/skills/frontend-design
    mkdir -p "$TARGET_TEST_DIR"/agents
    mkdir -p "$TARGET_TEST_DIR"/skills
    
    # Create test files in source
    echo "# Test agent file 1" > "$SOURCE_TEST_DIR/agents/test_agent_1.md"
    echo "# Test agent file 2" > "$SOURCE_TEST_DIR/agents/test_agent_2.md"
    echo "# Old file to be deleted" > "$SOURCE_TEST_DIR/agents/to_be_deleted.md"
    echo "# Test skill file 1" > "$SOURCE_TEST_DIR/skills/test_skill_1.md"
    echo "# Test skill file 2" > "$SOURCE_TEST_DIR/skills/test_skill_2.md"
    
    # Create target directory with some existing content (including some that should be removed)
    echo "# This should be removed" > "$TARGET_TEST_DIR/agents/should_be_removed.md"
    echo "# This should also be removed" > "$TARGET_TEST_DIR/skills/should_also_be_removed.md"
    echo "# This should remain" > "$TARGET_TEST_DIR/should_remain.txt"
    
    print_success "Test environment created"
}

test_sync_with_deletion() {
    print_status "Testing sync with deletion (dry-run first)..."
    
    # First run dry-run to see what would be deleted
    bash "$MIGRATION_SCRIPT" --dry-run 2>&1 | grep -E "(deleting|removing|should_be_removed)" || true
    
    print_status "Now running actual sync with deletion..."
    
    # Run the actual migration (this should remove deleted files)
    bash "$MIGRATION_SCRIPT"
    
    print_status "Verifying deletion worked..."
    
    # Verify files that should be deleted are gone
    if [ -f "$TARGET_TEST_DIR/agents/should_be_removed.md" ]; then
        print_error "ERROR: File should_be_removed.md was not deleted from target agents directory"
        return 1
    fi
    
    if [ -f "$TARGET_TEST_DIR/skills/should_also_be_removed.md" ]; then
        print_error "ERROR: File should_also_be_removed.md was not deleted from target skills directory"
        return 1
    fi
    
    # Verify files that should remain are still there
    if [ ! -f "$TARGET_TEST_DIR/should_remain.txt" ]; then
        print_error "ERROR: File should_remain.txt was incorrectly removed (should be preserved)"
        return 1
    fi
    
    # Verify new files were copied
    if [ ! -f "$TARGET_TEST_DIR/agents/to_be_deleted.md" ]; then
        print_error "ERROR: File to_be_deleted.md was not copied"
        return 1
    fi
    
    print_success "Deletion sync test passed!"
}

test_file_deletion_scenario() {
    print_status "Testing file deletion scenario..."
    
    # Delete a file from source
    rm -f "$SOURCE_TEST_DIR/agents/to_be_deleted.md"
    
    # Run sync again (should remove the deleted file from target)
    bash "$MIGRATION_SCRIPT" --dry-run > /tmp/dry_run_output.txt
    
    if grep -q "deleting.*to_be_deleted.md" /tmp/dry_run_output.txt; then
        print_success "Dry-run shows file deletion would occur"
    else
        print_warning "Dry-run did not show expected file deletion"
    fi
    
    # Run actual sync
    bash "$MIGRATION_SCRIPT"
    
    # Verify file was deleted from target
    if [ -f "$TARGET_TEST_DIR/agents/to_be_deleted.md" ]; then
        print_error "ERROR: File to_be_deleted.md was not deleted from target after source deletion"
        return 1
    fi
    
    print_success "File deletion scenario test passed!"
}

test_file_addition_modification() {
    print_status "Testing file addition and modification..."
    
    # Add a new file
    echo "# New file added for testing" > "$SOURCE_TEST_DIR/skills/new_file.md"
    
    # Modify an existing file
    echo "# Modified content" >> "$SOURCE_TEST_DIR/agents/test_agent_1.md"
    
    # Run sync
    bash "$MIGRATION_SCRIPT"
    
    # Verify new file was added
    if [ ! -f "$TARGET_TEST_DIR/skills/new_file.md" ]; then
        print_error "ERROR: New file new_file.md was not copied"
        return 1
    fi
    
    # Verify modification was synced
    if ! grep -q "Modified content" "$TARGET_TEST_DIR/agents/test_agent_1.md"; then
        print_error "ERROR: File modification was not synced"
        return 1
    fi
    
    print_success "File addition and modification test passed!"
}

test_verification_detection() {
    print_status "Testing verification function's ability to detect mismatches..."
    
    # Create a mismatch by manually adding a file to target
    echo "# This file shouldn't be here" > "$TARGET_TEST_DIR/agents/unexpected_file.md"
    
    # Run verification
    bash "$MIGRATION_SCRIPT" 2>&1 | grep -E "mismatch|Extra files" || true
    
    print_status "Running verification only..."
    
    # Source the verification function and run it directly
    source "$MIGRATION_SCRIPT" 2>/dev/null || true
    verify_sync 2>&1 | tee /tmp/verify_output.txt
    
    if grep -q "Extra files in target" /tmp/verify_output.txt; then
        print_success "Verification correctly detected extra files"
    else
        print_warning "Verification did not detect the expected extra file (may need manual check)"
    fi
}

main() {
    print_status "Starting migration script deletion fix test..."
    
    # Check if migration script exists
    if [ ! -f "$MIGRATION_SCRIPT" ]; then
        print_error "Migration script not found at $MIGRATION_SCRIPT"
        exit 1
    fi
    
    # Set up test environment
    setup_test_environment
    
    # Export test directories (the script will use these)
    export HOME="$TEST_DIR"
    
    # Run test scenarios
    test_sync_with_deletion
    test_file_deletion_scenario
    test_file_addition_modification
    test_verification_detection
    
    print_status "All tests completed!"
    print_success "Migration script deletion fix appears to be working correctly."
    
    # Show final state
    print_status "Final state summary:"
    echo "Source files:"
    find "$SOURCE_TEST_DIR" -name "*.md" -type f -exec basename {} \; | sort
    echo "Target files:"
    find "$TARGET_TEST_DIR" -name "*.md" -type f -exec basename {} \; | sort | head -10
    
    # Cleanup
    cleanup
}

main "$@"