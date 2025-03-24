#!/bin/bash

echo "======================================="
echo "    Installing MCG OSINT Tool"
echo "======================================="

# Check if python3-venv is installed
if ! dpkg -s python3-venv &> /dev/null; then
    echo "[+] Installing python3-venv package..."
    sudo apt install python3-venv -y
fi

echo "[+] Creating Python virtual environment..."
python3 -m venv venv

echo "[+] Activating virtual environment..."
source venv/bin/activate

echo "[+] Installing dependencies inside venv..."
pip install --upgrade pip
pip install -r requirements.txt

# Detect if user is root or non-root
if [ "$EUID" -eq 0 ]; then
    BASHRC_PATH="/root/.bashrc"
else
    BASHRC_PATH="$HOME/.bashrc"
fi

echo "[+] Adding global alias 'mcgtool' for user..."
echo "alias mcgtool='bash $(pwd)/start.sh'" >> $BASHRC_PATH
source $BASHRC_PATH

echo "======================================="
echo "      MCG OSINT Tool Ready"
echo "======================================="
echo "You can now run the tool using: mcgtool cli"
