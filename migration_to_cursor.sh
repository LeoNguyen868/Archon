#!/bin/bash

# Migration script to sync ONLY existing top-level directories from ./cursor to ~/.cursor/
# Does NOT replace or delete other directories/files inside ~/.cursor

set -e  # Exit on any error

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$SCRIPT_DIR/cursor"
TARGET_DIR="$HOME/.cursor"

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() { echo -e "${BLUE}[INFO]${NC} $1"; }
print_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
print_warning() { echo -e "${YELLOW}[WARNING]${NC} $1"; }
print_error() { echo -e "${RED}[ERROR]${NC} $1"; }

check_rsync() {
    if ! command -v rsync &> /dev/null; then
        print_error "rsync is not installed. Please install it first."
        exit 1
    fi
}

create_backup() {
    if [ -d "$TARGET_DIR" ]; then
        BACKUP_DIR="${TARGET_DIR}.backup.$(date +%Y%m%d_%H%M%S)"
        print_warning "Creating backup of existing ~/.cursor to $BACKUP_DIR"
        cp -r "$TARGET_DIR" "$BACKUP_DIR"
        print_success "Backup created successfully"
    fi
}

# Sync only agents/ and skills/ directories from cursor/ to ~/.cursor/, do NOT delete or replace unrelated things in ~/.cursor
sync_cursor() {
    print_status "Syncing agents and skills directories from $SOURCE_DIR to $TARGET_DIR..."

    mkdir -p "$TARGET_DIR"

    # Only sync specific directories: agents and skills
    for dirname in "agents" "skills"; do
        if [ -d "$SOURCE_DIR/$dirname" ]; then
            print_status "Syncing directory: $dirname"
            # Do NOT use --delete at target to avoid removing unrelated files/dirs from ~/.cursor/
            rsync -avz \
                --exclude='.git/' \
                --exclude='__pycache__/' \
                --exclude='*.pyc' \
                "$SOURCE_DIR/$dirname/" "$TARGET_DIR/$dirname/"
        else
            print_warning "Source directory does not exist: $SOURCE_DIR/$dirname"
        fi
    done

    print_success "Directory sync completed (agents and skills only, no replacement of extra dirs in ~/.cursor)."
}

verify_sync() {
    print_status "Verifying sync..."

    # We'll only check counts for what we synced: agents and skills
    local mismatch_found=0

    for dirname in "agents" "skills"; do
        if [ -d "$SOURCE_DIR/$dirname" ]; then
            source_count=$(find "$SOURCE_DIR/$dirname" -type f -name "*.md" | wc -l)
            target_count=$(find "$TARGET_DIR/$dirname" -type f -name "*.md" 2>/dev/null | wc -l)
            print_status "[$dirname] Files in src:$source_count, dst:$target_count"
            if [ "$source_count" != "$target_count" ]; then
                print_warning "File count mismatch in directory: $dirname"
                mismatch_found=1
            fi
        fi
    done

    if [ "$mismatch_found" -eq 0 ]; then
        print_success "Verification successful!"
    else
        print_warning "Sync verification detected mismatches! Manual review recommended."
    fi
}

setup_alias() {
    print_status "Setting up convenient alias..."

    ALIAS_NAME="sync-cursor"
    SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/migration_to_cursor.sh"
    ALIAS_COMMAND="bash \"$SCRIPT_PATH\""

    if grep -q "alias $ALIAS_NAME=" "$HOME/.bashrc" 2>/dev/null; then
        print_warning "Alias '$ALIAS_NAME' already exists in .bashrc"
    else
        echo "" >> "$HOME/.bashrc"
        echo "# Alias for syncing cursor skills" >> "$HOME/.bashrc"
        echo "alias $ALIAS_NAME='$ALIAS_COMMAND'" >> "$HOME/.bashrc"
        print_success "Alias '$ALIAS_NAME' added to .bashrc"
        print_status "You can now use 'sync-cursor' command from anywhere"
    fi
}

create_watch_script() {
    print_status "Creating watch mode script..."

    WATCH_SCRIPT="$HOME/.cursor_sync_watch.sh"

    # Get the absolute path to the cursor directory from this script's location
    CURSOR_DIR="$SCRIPT_DIR/cursor"

    cat > "$WATCH_SCRIPT" << EOF
#!/bin/bash
# Watch script for automatic cursor sync (current directories/files only)

SOURCE_DIR="$CURSOR_DIR"
TARGET_DIR="\$HOME/.cursor"

sync_current() {
    # Only sync agents and skills directories, don't replace ~/.cursor
    for dirname in "agents" "skills"; do
        if [ -d "\$SOURCE_DIR/\$dirname" ]; then
            rsync -avz --exclude='.git/' --exclude='__pycache__/' --exclude='*.pyc' "\$SOURCE_DIR/\$dirname/" "\$TARGET_DIR/\$dirname/"
        fi
    done
}

if command -v inotifywait &> /dev/null; then
    echo "Watching for changes in \$SOURCE_DIR..."
    inotifywait -m -r -e modify,create,delete "\$SOURCE_DIR" |
    while read path action file; do
        echo "Change detected: \$action on \$path\$file"
        sync_current
        echo "Sync completed at \$(date)"
    done
else
    echo "inotifywait not available. Please install inotify-tools for watch functionality."
fi
EOF

    chmod +x "$WATCH_SCRIPT"
    print_success "Watch script created at $WATCH_SCRIPT"
    print_status "Run 'bash $WATCH_SCRIPT' to start automatic syncing"
}

# Create a backup of the local SOURCE_DIR (useful before reverse syncing)
create_source_backup() {
    if [ -d "$SOURCE_DIR" ]; then
        SRC_BACKUP_DIR="${SOURCE_DIR}.backup.$(date +%Y%m%d_%H%M%S)"
        print_warning "Creating backup of existing source directory $SOURCE_DIR to $SRC_BACKUP_DIR"
        cp -r "$SOURCE_DIR" "$SRC_BACKUP_DIR"
        print_success "Source backup created successfully"
    fi
}

# Reverse sync: copy only agents/ and skills/ from TARGET_DIR (~/.cursor) back to SOURCE_DIR (project)
reverse_sync() {
    print_status "Reverse syncing 'agents/' and 'skills/' from $TARGET_DIR to $SOURCE_DIR..."

    mkdir -p "$SOURCE_DIR"

    for dirname in "agents" "skills"; do
        if [ -d "$TARGET_DIR/$dirname" ]; then
            print_status "Syncing directory from target: $dirname"
            # Mirror from target -> source, but do NOT use --delete to avoid removing local-only files
            rsync -avz \
                --exclude='.git/' \
                --exclude='__pycache__/' \
                --exclude='*.pyc' \
                "$TARGET_DIR/$dirname/" "$SOURCE_DIR/$dirname/"
        else
            print_warning "Target directory does not exist, skipping: $TARGET_DIR/$dirname"
        fi
    done

    print_success "Reverse sync completed for agents/ and skills/."
}

main() {
    echo -e "${BLUE}╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║                 Cursor Skills Migration Script                 ║${NC}"
    echo -e "${BLUE}╚══════════════════════════════════════════════════════════════════╝${NC}"
    echo

    while [[ $# -gt 0 ]]; do
        case $1 in
            --no-backup)
                NO_BACKUP=true
                shift
                ;;
            --reverse)
                REVERSE=true
                shift
                ;;
            --setup-alias)
                SETUP_ALIAS=true
                shift
                ;;
            --create-watch)
                CREATE_WATCH=true
                shift
                ;;
            --help|-h)
                echo "Usage: $0 [OPTIONS]"
                echo
                echo "Options:"
                echo "  --no-backup      Skip creating backup of existing ~/.cursor"
                echo "  --reverse        Reverse sync only 'agents/' and 'skills/' from ~/.cursor to ./cursor"
                echo "  --setup-alias    Add sync alias to .bashrc"
                echo "  --create-watch   Create automatic watch script"
                echo "  --help, -h       Show this help message"
                echo
                echo "Examples:"
                echo "  $0                           # Basic sync with backup"
                echo "  $0 --no-backup              # Sync without backup"
                echo "  $0 --setup-alias --create-watch  # Setup convenience features"
                echo "  $0 --reverse                 # Reverse sync agents/ and skills/ from ~/.cursor to local ./cursor"
                exit 0
                ;;
            *)
                print_error "Unknown option: $1"
                echo "Use --help for usage information"
                exit 1
                ;;
        esac
    done

    print_status "Checking prerequisites..."
    check_rsync
    if [ "$REVERSE" = true ]; then
        # Reverse sync flow: backup source (unless skipped), then pull agents/ and skills/
        if [ -z "$NO_BACKUP" ]; then
            create_source_backup
        fi
        reverse_sync
        verify_sync
        echo
        print_success "Reverse migration completed successfully!"
        return 0
    fi

    if [ -z "$NO_BACKUP" ]; then
        create_backup
    fi

    sync_cursor

    verify_sync

    if [ "$SETUP_ALIAS" = true ]; then
        setup_alias
    fi

    if [ "$CREATE_WATCH" = true ]; then
        create_watch_script
    fi

    echo
    print_success "Migration completed successfully!"
    echo
    print_status "Next steps:"
    echo "  • Selected cursor directories/files have been synced to ~/.cursor/"
    echo "  • You can now use 'source ~/.bashrc' to load the new alias (if created)"
    echo "  • Use 'sync-cursor' command for quick future syncs"
    echo "  • Run the watch script for automatic updates"
}

main "$@"