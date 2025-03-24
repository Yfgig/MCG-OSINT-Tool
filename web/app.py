from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import sys

# Adjust path for CLI modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../modules')))

import whois_lookup
import email_verify
import ip_geo
import social_scan
import breach_check
import shodan_scan
import reverse_image
import exif_extractor
import subdomain_enum

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target = request.form.get('target')
    module = request.form.get('module')

    if not target:
        return "Target required", 400

    # Dynamic routing to each module
    if module == "whois_lookup":
        result = whois_lookup.run_web(target)
    elif module == "email_verify":
        result = email_verify.run_web(target)
    elif module == "ip_geo":
        result = ip_geo.run_web(target)
    elif module == "social_scan":
        result = social_scan.run_web(target)
    elif module == "breach_check":
        result = breach_check.run_web(target)
    elif module == "shodan_scan":
        result = shodan_scan.run_web(target)
    elif module == "subdomain_enum":
        result = subdomain_enum.run_web(target)
    elif module == "reverse_image":
        result = reverse_image.run_web(target)
    elif module == "exif_extractor":
        result = exif_extractor.run_web(target)
    else:
        result = "Module not found."

    return render_template('result.html', result=result, target=target, module=module)

@app.route('/export/<fmt>/<target>')
def export(fmt, target):
    # Placeholder for export logic (PDF, HTML, TXT)
    if fmt not in ['pdf', 'html', 'txt']:
        return "Invalid format", 400
    return f"Export {target} as {fmt} coming soon."

if __name__ == '__main__':
    app.run(debug=True)
