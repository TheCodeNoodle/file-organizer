import os
import shutil
from constants import *

def get_unique_path(dest, filename):
    name, ext = os.path.splitext(filename)
    counter = 1
    new_path = os.path.join(dest, filename)

    while os.path.exists(new_path):
        new_filename = f"{name}({counter}){ext}"
        new_path = os.path.join(dest, new_filename)
        counter += 1

    return new_path

def move_files(path):
    items = os.listdir(path)

    paths = {
        "Programs": os.path.join(path, "Programs"),
        "Documents": os.path.join(path, "Documents"),
        "Zip": os.path.join(path, "Zip"),
        "Videos": os.path.join(path, "Videos"),
        "Pictures": os.path.join(path, "Pictures"),
        "Music": os.path.join(path, "Music"),
        "Other": os.path.join(path, "Other"),
    }

    for item in items:
        _, ext = os.path.splitext(item)
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):
            continue

        ext = ext.lower()
        moved = False

        if ext in PROGRAM_EXTENSIONS:
            shutil.move(item_path, get_unique_path(paths["Programs"], item))
            moved = True
        elif ext in DOCUMENT_EXTENSIONS:
            shutil.move(item_path, get_unique_path(paths["Documents"], item))
            moved = True
        elif ext in ZIP_EXTENSIONS:
            shutil.move(item_path, get_unique_path(paths["Zip"], item))
            moved = True
        elif ext in VIDEO_EXTENSIONS:
            shutil.move(item_path, get_unique_path(paths["Videos"], item))
            moved = True
        elif ext in PICTURE_EXTENSIONS:
            shutil.move(item_path, get_unique_path(paths["Pictures"], item))
            moved = True
        elif ext in MUSIC_EXTENSIONS:
            shutil.move(item_path, get_unique_path(paths["Music"], item))
            moved = True

        if not moved and ext != "":
            shutil.move(item_path, get_unique_path(paths["Other"], item))

    print("Files in the given destination were successfully Organized.")
