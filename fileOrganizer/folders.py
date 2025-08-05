import os
from constants import *

def make_DIR(path):
    #----------Collects all file extensions in the directory----------
    items = os.listdir(path)
    needed_folders = set()

    for item in items:
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            continue

        _, ext = os.path.splitext(item)
        ext = ext.lower()

        if ext in VIDEO_EXTENSIONS:
            needed_folders.add("Videos")
        elif ext in PICTURE_EXTENSIONS:
            needed_folders.add("Pictures")
        elif ext in ZIP_EXTENSIONS:
            needed_folders.add("Zip")
        elif ext in DOCUMENT_EXTENSIONS:
            needed_folders.add("Documents")
        elif ext in PROGRAM_EXTENSIONS:
            needed_folders.add("Programs")
        elif ext in MUSIC_EXTENSIONS:
            needed_folders.add("Music")
        elif ext != "":
            needed_folders.add("Other")

    #----------Creates the needed folders----------
    for folder in needed_folders:
        folder_path = os.path.join(path, folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

    print("Needed folders were successfully created.")

