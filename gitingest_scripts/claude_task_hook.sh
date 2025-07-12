#!/bin/bash
# Claude Code Task Completion Hook
# This script is called automatically by Claude Code after each task completion
# to generate a digest of changes made during the task.

# Get the directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"

# Log file for hook execution (optional)
LOG_FILE="$REPO_DIR/.claude_digests/hook.log"

# Ensure log directory exists
mkdir -p "$REPO_DIR/.claude_digests"

# Function to log messages
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

# Start logging
log_message "Claude Code task completion hook started"

# Check if we're in a git repository
if ! git -C "$REPO_DIR" rev-parse --git-dir > /dev/null 2>&1; then
    log_message "Not in a git repository, skipping digest generation"
    exit 0
fi

# Check if Python is available
if ! command -v python3 > /dev/null 2>&1; then
    log_message "Python3 not found, skipping digest generation"
    exit 0
fi

# Run the auto digest generator
log_message "Running auto digest generator..."

cd "$REPO_DIR"
python3 "$SCRIPT_DIR/auto_digest_task.py" --quiet

RESULT=$?

if [ $RESULT -eq 0 ]; then
    log_message "Auto digest completed successfully"
else
    log_message "Auto digest failed with exit code $RESULT"
fi

# Optional: Clean up old digests weekly (only run once per day)
LAST_CLEANUP_FILE="$REPO_DIR/.claude_digests/.last_cleanup"
TODAY=$(date '+%Y-%m-%d')

if [ ! -f "$LAST_CLEANUP_FILE" ] || [ "$(cat "$LAST_CLEANUP_FILE" 2>/dev/null)" != "$TODAY" ]; then
    log_message "Running weekly cleanup..."
    python3 "$SCRIPT_DIR/auto_digest_task.py" --cleanup 7 --quiet
    echo "$TODAY" > "$LAST_CLEANUP_FILE"
    log_message "Cleanup completed"
fi

log_message "Hook execution completed"

# Always exit successfully to avoid interfering with Claude Code
exit 0