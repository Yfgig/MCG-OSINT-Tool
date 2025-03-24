import shodan

def run():
    ip = input("[Shodan Scan] Enter IP address or domain: ").strip()
    if not ip:
        print("[Shodan Scan] No input provided.")
        return

    try:
        from config.api_keys import shodan_api_key
    except:
        print("[Shodan Scan] Shodan API key not found in api_keys.py")
        return

    api = shodan.Shodan(shodan_api_key)

    try:
        print(f"[Shodan Scan] Querying Shodan for {ip}...")
        result = api.host(ip)
        
        print(f"IP: {result.get('ip_str', 'N/A')}")
        print(f"Organization: {result.get('org', 'N/A')}")
        print(f"Operating System: {result.get('os', 'N/A')}")
        print(f"Country: {result.get('country_name', 'N/A')}")
        print(f"City: {result.get('city', 'N/A')}")
        print(f"Last Update: {result.get('last_update', 'N/A')}")
        
        print("\n[Open Ports & Services]:")
        for service in result.get('data', []):
            print(f"Port: {service['port']}, Service: {service.get('product', 'Unknown')} | Banner: {service.get('banner', '')[:50]}")

    except shodan.APIError as e:
        print(f"[Shodan Scan] API Error: {e}")
