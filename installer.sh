#!/bin/bash

echo "======================================="
echo "    Installing MCG OSINT Tool"
echo "======================================="

# Step 1: Create virtual environment
echo "[+] Creating Python virtual environment..."
python3 -m venv venv

# Step 2: Activate virtualenv and install dependencies
source venv/bin/activate

echo "[+] Installing dependencies..."
pip install --upgrade pip
pip install -r cli/requirements.txt
pip install -r web/requirements.txt

# Step 3: Make start.sh executable
chmod +x start.sh

# Step 4: Add global alias
echo "[+] Adding global alias 'mcgtool'..."
echo "alias mcgtool='$(pwd)/start.sh'" >> ~/.bashrc
source ~/.bashrc

echo "[+] Installation complete!"
echo "You can now run the tool using: mcgtool cli or mcgtool web"

# Step 5: Optional - Create reports directory if missing
mkdir -p reports

echo "======================================="
echo "      MCG OSINT Tool Ready"
echo "======================================="
