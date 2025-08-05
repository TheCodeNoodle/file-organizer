from folders import make_DIR
from organizer import move_files

folder_link_input = input("Folder to Organize: ")
link = folder_link_input.strip('"').replace("\\", "/")

make_DIR(link)
move_files(link)
