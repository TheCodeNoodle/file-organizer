# 📁 FileOrganizer
<div align="center">
  <img 
    src="https://github.com/user-attachments/assets/6acefc26-89b3-4eda-9cae-cbbb8529bd9b" 
    alt="File Organizer app in light mode" 
    width="410" 
    height="529" 
    style="margin-right: 20px;"
  />
  <img 
    src="https://github.com/user-attachments/assets/c2d2ca8e-b512-4b59-9243-231a72d671cf" 
    alt="File Organizer app in dark mode" 
    width="410" 
    height="529"
  />
</div>

A simple Python script that automatically organizes files in a directory by moving them into categorized folders based on their file extensions.


## ✨ Features

- Automatically sorts files into folders: Programs, Documents, Zip, Videos, Pictures, Music, and Other
- Creates only the folders needed based on files present
- Handles duplicate filenames by adding numbers (e.g., file(1).txt)
- Supports a wide range of file extensions

## 📂 File Structure

```
fileorganizer/
├── main.py          # GUI
├── organizer.py     # Core logic for moving files, undo changes
├── folders.py       # Creates necessary folders
└── constants.py     # File extension definitions
```

## 🚀 Getting Started

### 📋 Requirements

**System Requirements:**
- **Python 3.8+** (Python 3.10+ recommended)
- **Cross-platform compatibility** (Windows, macOS, Linux)

> **Note:** Dark/Light mode detection is Windows-specific. The app runs on all platforms but uses the default theme on non-Windows systems.

**Dependencies:**
- `customtkinter` - Modern UI framework
- `tkinter` - GUI toolkit (pre-installed with Python)
- Built-in modules: `platform`, `shutil`, `json`, `os`, `winreg` (Windows only)

---

### 📦 Installation

#### Windows
- Simply run the automated installer:
```batch
install_requirements.bat
```
- Or you can just download the .exe file <a href="https://github.com/TheCodeNoodle/file-organizer/releases/tag/v0.3.0">from here</a>.

#### Linux/macOS
1. **Clone the repository:**
   ```bash
   git clone https://github.com/TheCodeNoodle/file-organizer.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd file-organizer
   ```

3. **Make the install script executable:**
   ```bash
   chmod +x install_requirements.sh
   ```

4. **Run the installer:**
   ```bash
   ./install_requirements.sh
   ```

#### Manual Installation (All Platforms)
If you prefer to install dependencies manually:
```bash
pip install customtkinter
```

---

### 🎯 Running the Application

Once dependencies are installed, launch the file organizer:

```bash
python main.py
```

**That's it!** The application will start with your system's theme (dark/light mode on Windows).

## 📁 Supported File Types

- **💻 Programs**: .exe, .msi, .bat, .py, .jar, .apk, etc.
- **📄 Documents**: .pdf, .doc, .docx, .txt, .xlsx, .ppt, etc.
- **🗜️ Zip**: .zip, .rar, .7z, .tar, .gz, .iso, etc.
- **🎬 Videos**: .mp4, .mkv, .avi, .mov, .wmv, etc.
- **🖼️ Pictures**: .jpg, .png, .gif, .bmp, .svg, etc.
- **🎵 Music**: .mp3, .wav, .flac, .aac, .ogg, etc.
- **📦 Other**: Any other file types not listed above

---
### ✅ Implemented Features

- **Graphical Interface (GUI)**: Full-featured desktop app built with CustomTkinter
- **Dark/Light Mode Support**: Automatically detects Windows theme and adapts colors
- **Persistent Undo Functionality**: Reverse file organization actions even after restarting, using a changelog file
- **Automatic Folder Creation**: Creates only the folders needed based on files present
- **Duplicate Handling**: Prevents overwriting by appending numbers (e.g., file(1).txt)
- **Wide Extension Support**: Organizes files into Programs, Documents, Zip, Videos, Pictures, Music, and Other
- **Real-Time Feedback**: Status messages displayed directly in the GUI
- **Safe Operations**: Skips important files like the changelog and existing folders

---

### 📋 Planned Improvements

- **Custom Categories**: Allow users to define their own file categories and extensions
- **Batch Processing**: Organize multiple folders at once
- **Progress Bar**: Show progress for large directories
- **Configuration File**: Save user preferences and custom settings
- **Nested Organization**: Sub-categorize files (e.g., separate image formats, document types)
- **Dry Run Mode**: Preview changes before actually moving files
- **Logging**: Keep a permanent record of moved files
- **Command Line Arguments**: Optional CLI flags for automation
- **Cross-Platform Theming**: Extend dark/light mode detection to macOS and Linux
## ⚠️ Note

Files without extensions and existing folders in the target directory are left untouched.
