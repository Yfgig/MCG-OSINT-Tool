![1000058855](https://github.com/user-attachments/assets/7f739d31-c531-47fb-9378-8d819e54f85b)
---

MCG OSINT Tool (CLI Version)

MCG OSINT Tool is an advanced Open Source Intelligence (OSINT) framework designed for investigators, security professionals, and researchers. This tool provides powerful modules to collect intelligence on emails, IPs, domains, and social media through an easy-to-use CLI interface.


---

Features

WHOIS Lookup

Email Verification

IP Geolocation

Social Media Scanner

Breach Data Check

Shodan Scan

Reverse Image Search

Metadata (EXIF) Extraction

Subdomain Enumeration

Auto-generated PDF/HTML/TXT reports

Dark-themed CLI output

Auto-update support via updater.py



---

Prerequisites

Before running the tool, ensure you have the following installed on your system:

Python 3.8+

python3-venv

Git

Kali Linux or any Debian-based distribution

Internet Connection (for API-based modules like Shodan, HaveIBeenPwned, etc.)


To install essential dependencies on Kali/Debian:

sudo apt update
sudo apt install python3 python3-venv git -y


---

Installation

git clone https://github.com/Yfgig/MCG-OSINT-Tool.git

cd MCG-OSINT-Tool

bash installer.sh

OR

./installer.sh

This will:

Create a virtual environment.

Install required dependencies.

Set up a global alias mcgtool for easy access.



---

Usage

mcgtool cli

Select a module from the CLI dashboard to start an OSINT investigation.


---

Update Tool

To pull the latest version and dependencies:

python3 updater.py


---

File Structure

MCG-OSINT-Tool/

├── cli/

│   ├── main.py

│   └── modules/

│       ├── breach_check.py

│       ├── email_verify.py

│       ├── exif_extractor.py

│       ├── ip_geo.py

│       ├── reverse_image.py

│       ├── shodan_scan.py

│       ├── social_scan.py

│       ├── subdomain_enum.py

│       └── whois_lookup.py

├── reports/

├── installer.sh

├── requirements.txt

├── start.sh

├── updater.py

├── settings.py

├── .gitignore


└── README.md


---

Notes

Only for Kali Linux/Debian-based distros (tested).

Make sure python3-venv is installed (auto-installed via installer.sh).

CLI-only version, web interface removed.



---

License

MIT License

