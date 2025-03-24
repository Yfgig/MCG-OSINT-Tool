import os
import subprocess
import sys

def update_tool():
    print("====================================")
    print("     MCG OSINT TOOL UPDATER")
    print("====================================")

    # Check if this is a git repository
    if not os.path.exists(".git"):
        print("[!] This directory is not a Git repository.")
        sys.exit(1)

    try:
        # Fetch latest changes
        print("[+] Fetching latest updates from remote...")
        subprocess.check_call(["git", "pull"])

        # Update Python dependencies for CLI only
        print("[+] Updating dependencies for CLI...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "-r", "requirements.txt"])

        print("[✓] MCG OSINT Tool is up to date!")
    except subprocess.CalledProcessError as e:
        print(f"[!] Update failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    update_tool()
