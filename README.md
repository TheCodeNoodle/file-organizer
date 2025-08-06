# 📁 FileOrganizer

A simple Python script that automatically organizes files in a directory by moving them into categorized folders based on their file extensions.

## ✨ Features

- Automatically sorts files into folders: Programs, Documents, Zip, Videos, Pictures, Music, and Other
- Creates only the folders needed based on files present
- Handles duplicate filenames by adding numbers (e.g., file(1).txt)
- Supports a wide range of file extensions

## 📂 File Structure

```
fileorganizer/
├── main.py          # Entry point - gets folder path and runs organizer
├── organizer.py     # Core logic for moving files
├── folders.py       # Creates necessary folders
└── constants.py     # File extension definitions
```

## 🚀 How to Use

1. Run the script:
   ```bash
   python main.py
   ```

2. When prompted, enter the path to the folder you want to organize:
   ```
   Folder to Organize: /path/to/your/messy/folder
   ```

3. The script will:
   - Create necessary folders based on file types found
   - Move files into appropriate categories
   - Display confirmation messages

## 📁 Supported File Types

- **💻 Programs**: .exe, .msi, .bat, .py, .jar, .apk, etc.
- **📄 Documents**: .pdf, .doc, .docx, .txt, .xlsx, .ppt, etc.
- **🗜️ Zip**: .zip, .rar, .7z, .tar, .gz, .iso, etc.
- **🎬 Videos**: .mp4, .mkv, .avi, .mov, .wmv, etc.
- **🖼️ Pictures**: .jpg, .png, .gif, .bmp, .svg, etc.
- **🎵 Music**: .mp3, .wav, .flac, .aac, .ogg, etc.
- **📦 Other**: Any other file types not listed above

## ⚙️ Requirements

- Python 3.x
- No external dependencies (uses only built-in modules)
---
### ✅ Implemented Features

- **Undo Functionality**: Reverse file organization operations performed in the current session

### 📋 Planned Improvements

- **GUI Interface**: Add a simple graphical interface for easier use
- **Custom Categories**: Allow users to define their own file categories and extensions
- **Batch Processing**: Organize multiple folders at once
- **Progress Bar**: Show progress for large directories
- **Configuration File**: Save user preferences and custom settings
- **Nested Organization**: Sub-categorize files (e.g., separate image formats, document types)
- **Dry Run Mode**: Preview changes before actually moving files
- **Logging**: Keep track of what files were moved where
- **Command Line Arguments**: Skip the input prompt with CLI flags
## ⚠️ Note

Files without extensions and existing folders in the target directory are left untouched.
