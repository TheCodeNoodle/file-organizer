import os
from folders import make_DIR
from organizer import move_files
from undo import undo

action = {}

folder_link_input = input("Folder to Organize: ")
link = folder_link_input.strip('"').replace("\\", "/")

if not os.path.exists(link):
    print("The path you entered does not exist.")
    exit()

make_DIR(link)
move_files(link, action)

undo_inp = input("Do you want to undo the file organization? (y/n): ").strip().lower()
if undo_inp == 'y':
    undo(action)
