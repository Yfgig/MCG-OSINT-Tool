from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os

def run():
    image_path = input("[EXIF Extractor] Enter image file path: ").strip()
    if not image_path or not os.path.isfile(image_path):
        print("[EXIF Extractor] File does not exist.")
        return

    try:
        image = Image.open(image_path)
        exif_data = image._getexif()

        if not exif_data:
            print("[EXIF Extractor] No EXIF metadata found.")
            return

        print("[EXIF Extractor] Extracting EXIF data...\n")
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            if tag == 'GPSInfo':
                gps_data = {}
                for key in value.keys():
                    gps_tag = GPSTAGS.get(key, key)
                    gps_data[gps_tag] = value[key]
                print(f"{tag}: {gps_data}")
            else:
                print(f"{tag}: {value}")

    except Exception as e:
        print(f"[EXIF Extractor] Error: {e}")
