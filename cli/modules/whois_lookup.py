import whois

def run():
    domain = input("[WHOIS] Enter domain: ").strip()
    if not domain:
        print("[WHOIS] No domain entered.")
        return
    try:
        print(f"[WHOIS] Fetching WHOIS info for {domain}...\n")
        w = whois.whois(domain)
        print("Domain:", domain)
        print("Registrar:", w.registrar)
        print("Creation Date:", w.creation_date)
        print("Expiry Date:", w.expiration_date)
        print("Name Servers:", w.name_servers)
        print("Registrant Email:", w.emails)
        print("Organization:", w.org)
    except Exception as e:
        print("[WHOIS] Error:", str(e))
