# MCG OSINT TOOL

Developed by Mera Cyber Gondia

A modular and automated OSINT (Open Source Intelligence) investigation framework with both CLI and Web UI. Designed for investigators, cybersecurity enthusiasts, and analysts running on Kali Linux or other Linux distros.

## Features

- CLI & Web Interface (localhost dashboard)
- Automated reports with graph (connecting dots visualization)
- Export reports as PDF, HTML, and TXT
- Modular OSINT scans (WHOIS, Email Verification, IP Geolocation, Social Media Scan, and more)
- Dark-themed, fully functional web dashboard
- Customizable logo (top-middle of web UI)
- Auto-update script
- Bash installer with global alias (mcgtool)

## Modules Included

- WHOIS Lookup
- Email Verification
- IP Geolocation
- Social Media Scan
- Breach Data Check
- Shodan Scan
- Subdomain Enumeration
- Reverse Image Search
- Metadata / EXIF Extractor

## Installation

git clone https://github.com/yourusername/mcg-osint-tool.git
cd mcg-osint-tool
chmod +x installer.sh
./installer.sh

## Usage

CLI Mode:
mcgtool cli

Web Mode (localhost dashboard):
mcgtool web

Access it on: http://127.0.0.1:5000

## Auto-Updater
python3 updater.py

## Directory Structure

MCG-OSINT-TOOL/
├── cli/
│   ├── main.py
│   ├── modules/
│   └── api_keys.py
├── web/
│   ├── app.py
│   ├── graph_builder.py
│   ├── report_engine.py
│   ├── templates/
│   └── static/
├── reports/
├── settings.py
├── start.sh
├── installer.sh
├── updater.py
├── requirements.txt
├── LICENSE
└── .gitignore

## Notes

- Compatible with Python 3.x
- Designed for Kali Linux, but works on most Unix-like systems.
- Reports will be saved inside the /reports directory.

## Credits
Developed by Mera Cyber Gondia Team.

## License
MIT License

