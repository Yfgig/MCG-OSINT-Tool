import json

def build_graph(data, module):
    nodes = []
    links = []

    # Always add the target node
    nodes.append({"id": data.get("target", "Target"), "group": "target"})

    # Dynamically create nodes & links based on module output
    if module == "whois_lookup":
        nodes.append({"id": f"Registrar: {data.get('registrar', 'N/A')}", "group": "whois"})
        nodes.append({"id": f"Created: {data.get('creation_date', 'N/A')}", "group": "whois"})
        nodes.append({"id": f"Country: {data.get('country', 'N/A')}", "group": "whois"})
        links.append({"source": data['target'], "target": f"Registrar: {data.get('registrar', 'N/A')}"})
        links.append({"source": data['target'], "target": f"Created: {data.get('creation_date', 'N/A')}"})
        links.append({"source": data['target'], "target": f"Country: {data.get('country', 'N/A')}"})

    elif module == "email_verify":
        nodes.append({"id": f"MX Record: {data.get('mx_record', 'N/A')}", "group": "email"})
        nodes.append({"id": f"Valid: {data.get('valid', 'Unknown')}", "group": "email"})
        links.append({"source": data['target'], "target": f"MX Record: {data.get('mx_record', 'N/A')}"})
        links.append({"source": data['target'], "target": f"Valid: {data.get('valid', 'Unknown')}"})

    elif module == "ip_geo":
        nodes.append({"id": f"City: {data.get('city', 'N/A')}", "group": "geo"})
        nodes.append({"id": f"ISP: {data.get('isp', 'N/A')}", "group": "geo"})
        nodes.append({"id": f"Lat/Lon: {data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}", "group": "geo"})
        links.append({"source": data['target'], "target": f"City: {data.get('city', 'N/A')}"})
        links.append({"source": data['target'], "target": f"ISP: {data.get('isp', 'N/A')}"})
        links.append({"source": data['target'], "target": f"Lat/Lon: {data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}"})

    # Add logic for other modules similarly...
    # This keeps it modular

    return json.dumps({"nodes": nodes, "links": links})
