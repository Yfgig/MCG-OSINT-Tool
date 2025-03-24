#!/bin/bash
echo "Starting MCG OSINT Tool..."

# Auto activate virtualenv
source $(pwd)/venv/bin/activate

if [ "$1" == "cli" ]; then
    python3 cli/main.py
else
    echo "Usage: mcgtool cli"
fi
