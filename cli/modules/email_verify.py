import smtplib
import dns.resolver

def run():
    email = input("[Email Verify] Enter email address: ").strip()
    if not email or "@" not in email:
        print("[Email Verify] Invalid email address.")
        return
    domain = email.split('@')[1]

    try:
        print(f"[Email Verify] Resolving MX records for {domain}...")
        mx_records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(mx_records[0].exchange)
    except Exception as e:
        print(f"[Email Verify] MX record lookup failed: {e}")
        return

    try:
        print(f"[Email Verify] Connecting to SMTP server {mx_record}...")
        server = smtplib.SMTP(timeout=10)
        server.connect(mx_record)
        server.helo(server.local_hostname)
        server.mail('mcg-osint@example.com')
        code, message = server.rcpt(email)
        if code == 250 or code == 251:
            print(f"[Email Verify] ✅ Email address {email} is VALID.")
        else:
            print(f"[Email Verify] ❌ Email address {email} is INVALID or does not exist.")
        server.quit()
    except Exception as e:
        print(f"[Email Verify] SMTP check failed: {e}")
