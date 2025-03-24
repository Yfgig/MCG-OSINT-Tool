import requests

def run():
    ip = input("[IP Geolocation] Enter IP address: ").strip()
    if not ip:
        print("[IP Geolocation] No IP address entered.")
        return

    try:
        print(f"[IP Geolocation] Querying ipinfo.io for {ip}...")
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()

        print(f"IP Address: {data.get('ip', 'N/A')}")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')}")
        print(f"Country: {data.get('country', 'N/A')}")
        print(f"Location (Lat/Lon): {data.get('loc', 'N/A')}")
        print(f"Organization: {data.get('org', 'N/A')}")
        print(f"Timezone: {data.get('timezone', 'N/A')}")
    except Exception as e:
        print(f"[IP Geolocation] Error: {e}")
