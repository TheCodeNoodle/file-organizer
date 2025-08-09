import customtkinter as ctk
import os
from tkinter import filedialog
from organizer import move_files, undo
from folders import make_DIR
import platform
import json
import winreg

def is_dark_mode_windows():
    # Check the theme via reg
    key = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key) as reg_key:
            value, _ = winreg.QueryValueEx(reg_key, "AppsUseLightTheme")
            return value == 0  # 0: dark mode, 1: light
    except FileNotFoundError:
        return None

def get_style_for_mode(dark_mode: bool):
    if dark_mode:
        return {
            "bg_color": "#121417",
            "header": "#E1E4F2",
            "container_header": "#4E5C8A",
            "small_txt": "#AEB6CF",
            "container": "#4E5C8A",
            "container_select": "#B87F1A",
            "container_txt": "#E1E4F2",
            "btns": "#2C2F3A",
            "btns_txt": "#E1E4F2",
            "btns_hover": "#3B4162",
            "btns_disabled": "#555A6E",
            "btns_txt_disabled": "#8A8E9F",
            "organize_button": "#3BA74E",
            "organize_button_hover": "#2E7030",
            "organize_button_disabled": "#5B8F6B",
            "undo_button": "#B74141",
            "undo_button_hover": "#7F2A2A",
            "undo_button_disabled": "#885353",
            "disabled_txt": "#8A8E9F",
            "action_buttons__txt": "#FFFFFF",
            "icon": "dark-mode-icon.ico"
        }
    
    else:
        return {
            "bg_color": "#ffffff",
            "header": "#ffffff",
            "container_header": "#7382BF",
            "small_txt": "#ffffff",
            "container": "#7382BF",
            "container_select": "#F9AF2A",
            "container_txt": "#ffffff",
            "btns": "#ffffff",
            "btns_txt": "#000000",
            "btns_hover": "#E3E6F5",
            "btns_disabled": "#FFFFFF",
            "btns_txt_disabled": "#8A8A8E",
            "organize_button": "#388E3C",
            "organize_button_hover": "#2E7030",
            "organize_button_disabled": "#90B78A",
            "action_buttons__txt": "#FFFFFF",
            "undo_button": "#C62828",
            "undo_button_hover": "#9B2020",
            "undo_button_disabled": "#B07878",
            "disabled_txt": "#8A8A8E",
            "icon": "light-mode-icon.ico"
        }
# Main detection & style assignment
current_platform = platform.system()
script_dir = os.path.dirname(os.path.abspath(__file__))

if current_platform == "Windows":
    dark_mode = is_dark_mode_windows()
    if dark_mode is None:
        # Fallback if registry key not found
        ctk_mode = ctk.get_appearance_mode()
        dark_mode = (ctk_mode == "dark")
else:
    ctk_mode = ctk.get_appearance_mode()
    dark_mode = (ctk_mode == "dark")

style = get_style_for_mode(dark_mode)

if current_platform == "Windows":
    icon_path = os.path.join(script_dir, style["icon"])
else:
    icon_path = os.path.join(script_dir, "default.ico")
style = get_style_for_mode(dark_mode)

# Optionally set CTK appearance mode explicitly (keeps CTK widgets consistent)
ctk.set_appearance_mode("dark" if dark_mode else "light")
ctk.set_default_color_theme("blue")

# ----------- Stored Data -----------
state = {
    "path": None,
    "action" : {}
}

# ----------- Window size -----------
geo = {"width": 550,
       "height": 670}

root = ctk.CTk()
root.geometry(f"{geo['width']}x{geo['height']}")
root.minsize(geo['width'], geo['height'])
root.maxsize(geo['width'], geo['height'])
root.title("File Organizer")


root.iconbitmap(icon_path)
root.configure(fg_color = style["bg_color"])
file_path_label = None

# ----------- Function to choose a folder -----------
def choose_folder():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected: {folder}")
        # Shortening long paths (for the GUI)
        if len(folder) > 60:
            display_path = "..." + folder[-57:]
        else:
            display_path = folder
        file_path_label.configure(text=f"{display_path}")
        state["path"] = folder
        organizeBtn.configure(state="normal", fg_color= style["organize_button"], text_color=style["action_buttons__txt"])
        openFileLocation.configure(state="normal", fg_color = style["btns"], text_color = style["btns_txt"])
        changelog_path = os.path.join(folder, "changelog.json")
        if os.path.exists(changelog_path):
            undoBtn.configure(state="normal", fg_color=style["undo_button"], text_color=style["action_buttons__txt"])
        else:
            undoBtn.configure(state="disabled", fg_color=style["undo_button_disabled"], text_color = style["btns_txt_disabled"])

# it's Obvious dork, just read the name of the function
def openfileLoc():
    os.startfile(state["path"])

def organize_folder():
    path = state["path"]
    if not path or not os.path.exists(path):
        file_path_label.configure(text="⚠️ Please select a valid folder!")
        return
    
    make_DIR(path)
    move_files(path, state["action"])
    undoBtn.configure(state="normal", fg_color=style["undo_button"], text_color=style["action_buttons__txt"])
    status_label.configure(text="✅ Folder was successfully organized!", text_color="#2ecc71")

def undo_folder():
    path = state["path"]
    changelog_path = os.path.join(path, "changelog.json")

    if not path or not os.path.exists(changelog_path):
        status_label.configure(text="⚠️ Nothing to undo", text_color="#f39c12")
        return

    try:
        with open(changelog_path, "r") as f:
            changes = json.load(f)

        undo(path, changes)
        state["action"].clear()
        undoBtn.configure(state="disabled", fg_color=style["undo_button_disabled"], text_color = style["btns_txt_disabled"])
        status_label.configure(text="↩️ Changes were successfully undone!", text_color=style["btns_txt"])
    except Exception as e:
        status_label.configure(text=f"❌ Undo failed: {str(e)}", text_color=style["btns_txt"])
        print(f"Undo error: {e}")

    undo(path, changes)
    os.remove(changelog_path)  #Removes changelog after undo
    state["action"].clear()
    undoBtn.configure(state="disabled", fg_color=style["undo_button_disabled"], text_color = style["btns_txt_disabled"])
    status_label.configure(text="↩️ Changes were successfully undone!", text_color="#3498db")

# ----------- Header -----------
header_frame = ctk.CTkFrame(root, fg_color=style["container_header"], corner_radius=0)
header_frame.pack(fill="x", pady=(0, 30))

title_label = ctk.CTkLabel(
    header_frame, 
    text="File Organizer", 
    font=ctk.CTkFont(family="Segoe UI", size=24, weight="bold"),
    text_color=style["header"]
)
title_label.pack(pady = (20))

#----------- Main Container -----------
main_container = ctk.CTkFrame(root, fg_color="transparent")
main_container.pack(fill="both", expand=True, padx=20, pady=20)

# ----------- Folder Selection Section -----------
select_section = ctk.CTkFrame(main_container, fg_color=style["container"], corner_radius=15)
select_section.pack(fill="x", pady=(0, 25))

select_title = ctk.CTkLabel(
    select_section,
    text="Select Folder",
    font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
    text_color="#ecf0f1"
)
select_title.pack(pady=(20, 10))

file_path_label = ctk.CTkLabel(
    select_section,
    text="No folder selected",
    font=ctk.CTkFont(family="Segoe UI", size=12),
    text_color= style["small_txt"],
    wraplength=500
)
file_path_label.pack(pady=(0, 15))

chooseBtn = ctk.CTkButton(
    select_section,
    text="Browse Folders",
    font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
    corner_radius=25,
    height=45,
    width=200,
    command=choose_folder,
    fg_color= style["btns"],
    text_color = style["btns_txt"],
    hover_color= style["btns_hover"]
)
chooseBtn.pack(pady=(0, 25))

openFileLocation = ctk.CTkButton(
    select_section,
    text="Open in File Explorer",
    font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
    corner_radius=25,
    height=45,
    width=200,
    command=openfileLoc,
    fg_color=style["btns_disabled"],
    hover_color=style["btns_hover"],
    state = "disabled",
    text_color = style["btns_txt_disabled"]
)
openFileLocation.pack(pady=(0, 25))

# ----------- Action Section -----------
action_section = ctk.CTkFrame(main_container, fg_color= style["container_select"], corner_radius=15)
action_section.pack(fill="x", pady=(0, 20))

action_title = ctk.CTkLabel(
    action_section,
    text="Actions",
    font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
    text_color="#ecf0f1"
)
action_title.pack(pady=(20, 15))

# ----------- Button container ----------- 
button_container = ctk.CTkFrame(action_section, fg_color="transparent")
button_container.pack(pady=(0, 25))

organizeBtn = ctk.CTkButton(
    button_container,
    text="Organize Folder",
    font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
    corner_radius=25,
    height=45,
    width=180,
    command=organize_folder,
    state="disabled",
    fg_color= style["organize_button_disabled"],
    hover_color= style["organize_button_hover"],
    text_color = style["btns_txt_disabled"]
)
organizeBtn.pack(side="left", padx=(0, 15))

undoBtn = ctk.CTkButton(
    button_container,
    text="Undo Changes",
    font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
    corner_radius=25,
    height=45,
    width=180,
    command=undo_folder,
    state="disabled",
    fg_color= style["undo_button_disabled"],
    hover_color=style["undo_button_hover"],
    text_color = style["btns_txt_disabled"]
)
undoBtn.pack(side="left")

# ----------- Status Section -----------
status_section = ctk.CTkFrame(main_container, fg_color= style["container"], corner_radius=15)
status_section.pack(fill="x")

status_label = ctk.CTkLabel(
    status_section,
    text="Ready to organize files",
    font=ctk.CTkFont(family="Segoe UI", size=12),
    text_color=style["small_txt"]
)
status_label.pack(pady=15)

# ----------- GUI Loop -----------
root.mainloop()
