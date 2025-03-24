import requests

social_platforms = {
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://instagram.com/{}",
    "Facebook": "https://facebook.com/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "GitHub": "https://github.com/{}",
    "Reddit": "https://reddit.com/user/{}",
    "Pinterest": "https://pinterest.com/{}"
}

def run():
    username = input("[Social Scan] Enter username/handle: ").strip()
    if not username:
        print("[Social Scan] No username entered.")
        return

    print(f"[Social Scan] Searching profiles for '{username}'...\n")
    
    for platform, url in social_platforms.items():
        profile_url = url.format(username)
        try:
            response = requests.get(profile_url, timeout=10)
            if response.status_code == 200:
                print(f"[+] Found on {platform}: {profile_url}")
            elif response.status_code == 404:
                print(f"[-] Not found on {platform}")
            else:
                print(f"[~] {platform} returned status code: {response.status_code}")
        except Exception as e:
            print(f"[!] Error checking {platform}: {e}")
