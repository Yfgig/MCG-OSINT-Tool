import requests

def run():
    domain = input("[Subdomain Enum] Enter domain: ").strip()
    if not domain:
        print("[Subdomain Enum] No domain entered.")
        return

    print(f"[Subdomain Enum] Enumerating subdomains for {domain}...")

    try:
        response = requests.get(f"https://api.hackertarget.com/hostsearch/?q={domain}")
        if response.status_code == 200:
            results = response.text.strip().split('\n')
            if len(results) == 1 and "error" in results[0].lower():
                print(f"[Subdomain Enum] No subdomains found or API limit reached.")
                return

            print(f"[+] Found {len(results)} subdomains:")
            for line in results:
                parts = line.split(',')
                subdomain = parts[0]
                print(f"- {subdomain}")
        else:
            print(f"[Subdomain Enum] API returned status code: {response.status_code}")

    except Exception as e:
        print(f"[Subdomain Enum] Error: {e}")
