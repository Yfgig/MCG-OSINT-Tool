from fpdf import FPDF
import os

def export_report(data, module, fmt, export_dir='reports/'):
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)

    filename = f"{export_dir}{data.get('target', 'report')}_{module}.{fmt}"

    if fmt == "txt":
        with open(filename, "w") as file:
            file.write(generate_txt(data, module))
    elif fmt == "html":
        with open(filename, "w") as file:
            file.write(generate_html(data, module))
    elif fmt == "pdf":
        generate_pdf(data, module, filename)
    else:
        return None

    return filename

def generate_txt(data, module):
    lines = [f"--- {module.upper()} REPORT ---\n"]
    for key, value in data.items():
        lines.append(f"{key}: {value}")
    return "\n".join(lines)

def generate_html(data, module):
    html = f"<html><head><title>{module} Report</title></head><body>"
    html += f"<h1>{module.upper()} REPORT</h1><ul>"
    for key, value in data.items():
        html += f"<li><strong>{key}</strong>: {value}</li>"
    html += "</ul></body></html>"
    return html

def generate_pdf(data, module, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"{module.upper()} REPORT", ln=True, align='C')
    pdf.ln(10)
    for key, value in data.items():
        pdf.multi_cell(0, 10, txt=f"{key}: {value}")
    pdf.output(filename)
