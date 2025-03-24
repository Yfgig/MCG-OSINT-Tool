import webbrowser
import os

def run():
    image_path = input("[Reverse Image] Enter image file path: ").strip()
    if not image_path or not os.path.isfile(image_path):
        print("[Reverse Image] File does not exist.")
        return

    print("[Reverse Image] Opening reverse image search engines...")

    try:
        # Encode the image file as base64 or just direct it to search engines manually
        print("[+] Opening Google Reverse Image Search")
        webbrowser.open("https://images.google.com")

        print("[+] Opening Bing Visual Search")
        webbrowser.open("https://www.bing.com/visualsearch")

        print("[+] Opening Yandex Reverse Image Search")
        webbrowser.open("https://yandex.com/images/search?rpt=imageview")

        print("[+] Opening Tineye Search")
        webbrowser.open("https://tineye.com")

        print("\n[!] Now manually upload the image to the search engines.")
    except Exception as e:
        print(f"[Reverse Image] Error: {e}")
