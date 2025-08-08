import os
import shutil
from constants import *
import json

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
    }

    changelog_file = os.path.join(path, "changelog.json")
    if os.path.exists(changelog_file):
        with open(changelog_file, "r") as f:
            existing_changes = json.load(f)
    else:
        existing_changes = {}

    action.clear()

    for item in items:
        _, ext = os.path.splitext(item)
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):
            continue

        # Skip changelog
        if item.lower() == "changelog.json":
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
            action[item_path] = unique_path

    existing_changes.update(action)

    with open(changelog_file, "w") as file:
        json.dump(existing_changes, file, indent=4)
        print(f"{changelog_file} updated with {len(action)} new entries")

        
def undo(path, action):
    try:
        for bef_path, aft_path in action.items():
            if os.path.exists(aft_path):
                shutil.move(aft_path, bef_path)
                print(f"Moved {aft_path} back to {bef_path}")
            else:
                pass
        
        # Remove empty folders
        folders = [
            "Programs", "Documents", "Zip", "Videos", 
            "Pictures", "Music", "Other"
        ]
        
        for folder in folders:
            folder_path = os.path.join(path, folder)
            if os.path.exists(folder_path):
                try:
                    os.rmdir(folder_path)  # Only removes if empty
                    print(f"{folder} folder was removed!")
                except OSError:
                    print(f"{folder} folder is not empty, keeping it.")
        
        print("Undo completed successfully!")
        
    except Exception as e:
        print(f"Error during undo: {e}")
        raise
