#!/usr/bin/env bash
set -euo pipefail

# Property Management Web App Startup Script
# Creates virtual environment, installs dependencies, and launches the app

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WEBAPP_DIR="$SCRIPT_DIR/webapp"
VENV_DIR="$WEBAPP_DIR/.venv"
REQUIREMENTS="$WEBAPP_DIR/requirements.txt"

# Check Python version
PYTHON=""
for cmd in python3.11 python3.12 python3.13 python3; do
    if command -v "$cmd" &>/dev/null; then
        version=$("$cmd" -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
        major=$("$cmd" -c "import sys; print(sys.version_info.major)")
        minor=$("$cmd" -c "import sys; print(sys.version_info.minor)")
        if [ "$major" -ge 3 ] && [ "$minor" -ge 11 ]; then
            PYTHON="$cmd"
            break
        fi
    fi
done

if [ -z "$PYTHON" ]; then
    echo "Error: Python 3.11+ is required but not found."
    echo "Install Python 3.11 or later and try again."
    exit 1
fi

echo "Using $PYTHON ($($PYTHON --version))"

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment at $VENV_DIR..."
    "$PYTHON" -m venv "$VENV_DIR"
fi

# Activate and install dependencies
source "$VENV_DIR/bin/activate"
echo "Installing dependencies..."
pip install -q -r "$REQUIREMENTS"

# Launch the app
echo "Starting Property Management Web App..."
cd "$WEBAPP_DIR"
python -m app
