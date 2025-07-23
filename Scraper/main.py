from config import Classes, images_per_class, save_root
from downloader import download_image
from validator import is_valid_image, clean_directory
from search import search_image
import os
from tqdm import tqdm
from hashlib import sha1

# Run this file to start scraping!
if __name__ == "__main__":
    os.makedirs(save_root, exist_ok=True)

    for Class in Classes:
        print(f"\n🔍 Scraping: {Class}")
        folder=os.path.join(save_root, Class.replace(" ", "_"))
        os.makedirs(folder, exist_ok=True)

        urls=search_image(Class + " pics", images_per_class)
        print(f"Found {len(urls)} image URLs")

        downloaded = 0
        for url in tqdm(urls, desc=f"Downloading {Class}"):
            file_hash = sha1(url.encode()).hexdigest()[:10]
            save_path = os.path.join(folder, f"{file_hash}.jpg")
            if os.path.exists(save_path):
                continue
            if download_image(url, save_path) and is_valid_image(save_path):
                downloaded += 1
            else:
                if os.path.exists(save_path):
                    os.remove(save_path)

        print(f"✅ {downloaded} valid images saved for '{Class}'")
        clean_directory(folder)
