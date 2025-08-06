import os
import shutil
from constants import *

action = {}
def get_unique_path(dest, filename):
    name, ext = os.path.splitext(filename)
    counter = 1
    new_path = os.path.join(dest, filename)

    while os.path.exists(new_path):
        new_filename = f"{name}({counter}){ext}"
        new_path = os.path.join(dest, new_filename)
        counter += 1

    return new_path

def move_files(path, action):
    items = os.listdir(path)

    paths = {
        "Programs": os.path.join(path, "Programs"),
        "Documents": os.path.join(path, "Documents"),
        "Zip": os.path.join(path, "Zip"),
        "Videos": os.path.join(path, "Videos"),
        "Pictures": os.path.join(path, "Pictures"),
        "Music": os.path.join(path, "Music"),
        "Other": os.path.join(path, "Other"),
    }#_/path/folder_name

    for item in items:
        _, ext = os.path.splitext(item) #splits extension from the name
        item_path = os.path.join(path, item) #

        if os.path.isdir(item_path):
            continue

        ext = ext.lower()
        target_dir = None

        if ext in PROGRAM_EXTENSIONS:
            target_dir = paths["Programs"]
        elif ext in DOCUMENT_EXTENSIONS:
            target_dir = paths["Documents"]
        elif ext in ZIP_EXTENSIONS:
            target_dir = paths["Zip"]
        elif ext in VIDEO_EXTENSIONS:
            target_dir = paths["Videos"]
        elif ext in PICTURE_EXTENSIONS:
            target_dir = paths["Pictures"]
        elif ext in MUSIC_EXTENSIONS:
            target_dir = paths["Music"]
        elif ext != "":
            target_dir = paths["Other"]
            

        if target_dir:
            unique_path = get_unique_path(target_dir, item)
            shutil.move(item_path, unique_path)
            action[item_path.replace("\\", "/")] = unique_path.replace("\\", "/")

    print("Files in the given destination were successfully Organized.")
    print(f"Moved {len(action)} Files in total")
    for bef_p, aft_p in action.items():
        print(f"{bef_p} -> {aft_p}")

def undo(path, action):
    for bef_path, aft_path in action.items():
        shutil.move(aft_path, bef_path)
    paths = {
        "Programs": os.path.join(path, "Programs"),
        "Documents": os.path.join(path, "Documents"),
        "Zip": os.path.join(path, "Zip"),
        "Videos": os.path.join(path, "Videos"),
        "Pictures": os.path.join(path, "Pictures"),
        "Music": os.path.join(path, "Music"),
        "Other": os.path.join(path, "Other"),
    }

    for i in range(len(paths)):
        for path in paths:
            if path:
                
    print("Undone!")
