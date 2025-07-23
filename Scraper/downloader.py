import cv2
import requests
import numpy as np
from config import resize_dim

def download_image(url, path):
    try:
        response=requests.get(url, timeout=10, stream=True)
        response.raise_for_status()
        img_array=np.asarray(bytearray(response.content), dtype=np.uint8)
        img=cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        if img is None:
            return False
        resized_img=cv2.resize(img, resize_dim)
        cv2.imwrite(path, resized_img)
        return True
    except (requests.exceptions.RequestException, cv2.error, ValueError):
        return False