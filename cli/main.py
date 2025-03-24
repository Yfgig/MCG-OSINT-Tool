import sys
import os
from modules import whois_lookup, email_verify, ip_geo, social_scan, breach_check, shodan_scan, reverse_image, exif_extractor, subdomain_enum

def banner():
    print("""
███╗   ███╗ ██████╗  ██████╗ 
████╗ ████║██╔══════██╗
██╔████╔██║██║      ██║
██║╚██╔╝██║██║      ██║   ██║
██║ ╚═╝ ██║╚██████╔╝╚██████╔╝
╚═╝     ╚═╝ ╚═════╝  ╚═════╝ 
         MCG OSINT TOOL
    by Mera Cyber Gondia

Follow both on instagram and share feedback
INSTAGRAM: @Krishdhurve104 (main account)
           @mera_cyber_gondia


EMAIL : Meracybergondia@proton.me

""")

def menu():
    print("""
[1] WHOIS Lookup
[2] Email Verification
[3] IP Geolocation
[4] Social Media Scanner
[5] Breach Check
[6] Shodan IoT Scan
[7] Reverse Image Search
[8] EXIF Metadata Extractor
[9] Subdomain Enumeration
[0] Run All Modules
[q] Quit
""")

def main():
    banner()
    while True:
        menu()
        choice = input("Select module: ").strip()
        if choice == "1":
            whois_lookup.run()
        elif choice == "2":
            email_verify.run()
        elif choice == "3":
            ip_geo.run()
        elif choice == "4":
            social_scan.run()
        elif choice == "5":
            breach_check.run()
        elif choice == "6":
            shodan_scan.run()
        elif choice == "7":
            reverse_image.run()
        elif choice == "8":
            exif_extractor.run()
        elif choice == "9":
            subdomain_enum.run()
        elif choice == "0":
            print("[*] Running all modules...")
            whois_lookup.run()
            email_verify.run()
            ip_geo.run()
            social_scan.run()
            breach_check.run()
            shodan_scan.run()
            reverse_image.run()
            exif_extractor.run()
            subdomain_enum.run()
        elif choice.lower() == "q":
            print("Exiting MCG OSINT Tool.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
