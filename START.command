#!/usr/bin/env bash
# Property Management — macOS Launcher
# Double-click this file in Finder to start the server and open the dashboard.
set -euo pipefail

# cd to the script's directory (handles Finder launch)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "============================================"
echo "  Property Management — Starting..."
echo "============================================"
echo ""

# Check if port 8000 is already in use
if lsof -i :8000 -sTCP:LISTEN >/dev/null 2>&1; then
    echo "Server is already running on port 8000."
    echo "Opening browser..."
    open "http://localhost:8000"
    exit 0
fi

# Find Python 3.11+
PYTHON=""
for cmd in python3.13 python3.12 python3.11 python3; do
    if command -v "$cmd" >/dev/null 2>&1; then
        version=$("$cmd" -c "import sys; print(sys.version_info.minor)" 2>/dev/null || echo "0")
        if [ "$version" -ge 11 ]; then
            PYTHON="$cmd"
            break
        fi
    fi
done

if [ -z "$PYTHON" ]; then
    echo ""
    echo "ERROR: Python 3.11 or later is required."
    echo ""
    echo "Install Python from: https://www.python.org/downloads/"
    echo ""
    # Show a dialog on macOS
    osascript -e 'display dialog "Python 3.11+ is required.\n\nDownload from python.org/downloads" buttons {"OK"} default button "OK" with icon stop with title "Property Management"' 2>/dev/null || true
    exit 1
fi

echo "Using: $PYTHON ($($PYTHON --version))"

# Create virtual environment if needed
VENV_DIR="$SCRIPT_DIR/webapp/.venv"
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    "$PYTHON" -m venv "$VENV_DIR"
fi

# Activate venv
source "$VENV_DIR/bin/activate"

# Install/update dependencies
echo "Checking dependencies..."
pip install -q -r "$SCRIPT_DIR/webapp/requirements.txt"

# Start the server (it opens the browser automatically)
echo ""
echo "Starting server..."
cd "$SCRIPT_DIR/webapp"
python -m app
