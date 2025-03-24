#!/bin/bash

# MCG OSINT TOOL STARTER

echo "Starting MCG OSINT Tool..."

# Activate Python virtual environment if present
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run CLI version
if [[ "$1" == "cli" ]]; then
    python3 cli/main.py

# Run Web version
elif [[ "$1" == "web" ]]; then
    cd web
    python3 app.py

else
    echo "Usage:"
    echo "./start.sh cli    # Start CLI mode"
    echo "./start.sh web    # Start Web UI (localhost)"
fi
