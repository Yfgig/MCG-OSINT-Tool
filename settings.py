# Global settings for MCG OSINT Tool

# Replace this with your custom logo URL or file path
LOGO_URL = "/static/logo.png"

# Report export formats (can be customized)
EXPORT_FORMATS = ["pdf", "html", "txt"]

# Default graph settings (for D3.js visualization)
GRAPH_SETTINGS = {
    "node_color": "#00ffff",
    "link_color": "#999999",
    "force_charge": -400,
    "link_distance": 120
}

# Default output directory
REPORTS_DIR = "reports"

# Tool metadata
TOOL_NAME = "MCG OSINT TOOL"
AUTHOR = "Mera Cyber Gondia"

# Future API keys (imported by modules when needed)
API_KEYS_FILE = "cli/api_keys.py"
