import os
import cv2

def is_valid_image(path):
    try:
        img=cv2.imread(path)
        if img is None or img.shape[0] <=30 or img.shape[1] <=30:
            return False
        return True
    except(cv2.error, ValueError):
        return False

def clean_directory(folder):
    for filename in os.listdir(folder):
        file_path=os.path.join(folder, filename)
        if not is_valid_image(file_path):
            os.remove(file_path)