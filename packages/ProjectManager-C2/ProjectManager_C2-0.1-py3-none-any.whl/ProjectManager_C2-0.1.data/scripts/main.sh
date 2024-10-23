#!/bin/bash

SESSION_TRACKER_FILE="/tmp/git_manager_session_tracker"

# Source the helper script
SCRIPT_DIR="$(dirname "$0")"
. "${SCRIPT_DIR}/helper.sh"

# Function to check if this is a new session
is_new_session() {
    if [ ! -f "$SESSION_TRACKER_FILE" ]; then
        return 0 # New session
    else
        current_tty=$(tty)
        stored_tty=$(cat "$SESSION_TRACKER_FILE")
        if [ "$current_tty" != "$stored_tty" ]; then
            return 0 # New session
        else
            return 1 # Existing session
        fi
    fi
}

# first time checks
if is_new_session; then
    check_git_installed
    check_user_details
    touch .gitignore
    echo response.txt >> .gitignore
    echo status.txt >> .gitignore
    tty > "$SESSION_TRACKER_FILE"
fi


while true; do
    show_menu
    read_choice
done