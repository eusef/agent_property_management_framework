#!/usr/bin/env bash
# Property Management — Linux Launcher
# Run this script to start the server and open the dashboard.
set -euo pipefail

# cd to the script's directory
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "============================================"
echo "  Property Management — Starting..."
echo "============================================"
echo ""

# Check if port 8000 is already in use
if ss -tlnp 2>/dev/null | grep -q ':8000 ' || netstat -tlnp 2>/dev/null | grep -q ':8000 '; then
    echo "Server is already running on port 8000."
    echo "Opening browser..."
    xdg-open "http://localhost:8000" 2>/dev/null || echo "Open http://localhost:8000 in your browser."
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
    echo "Install Python:"
    echo "  Ubuntu/Debian: sudo apt install python3.12"
    echo "  Fedora:        sudo dnf install python3.12"
    echo "  Or download:   https://www.python.org/downloads/"
    echo ""
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
