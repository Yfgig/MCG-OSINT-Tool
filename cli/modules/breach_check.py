import requests

def run():
    email = input("[Breach Check] Enter email address: ").strip()
    if not email or "@" not in email:
        print("[Breach Check] Invalid email address.")
        return

    api_key = None
    try:
        with open('config/api_keys.py') as f:
            exec(f.read())  # Loads api_key from the config/api_keys.py file
    except:
        print("[Breach Check] API key not found. Make sure api_keys.py exists.")
        return

    headers = {
        'hibp-api-key': api_key.strip(),
        'user-agent': 'MCG-OSINT-Tool'
    }

    try:
        print(f"[Breach Check] Querying HaveIBeenPwned API for {email}...")
        response = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=false", headers=headers)
        if response.status_code == 200:
            breaches = response.json()
            print(f"[!] {email} found in {len(breaches)} breach(es):")
            for breach in breaches:
                print(f"- {breach['Name']} | Date: {breach['BreachDate']} | Compromised Data: {', '.join(breach['DataClasses'])}")
        elif response.status_code == 404:
            print(f"[+] No breaches found for {email}.")
        else:
            print(f"[~] API returned status code: {response.status_code}")
    except Exception as e:
        print(f"[Breach Check] Error: {e}")
