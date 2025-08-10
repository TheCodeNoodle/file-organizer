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

A powerful Python application that automatically organizes files in a directory by moving them into categorized folders based on their file extensions. Supports **300+ file formats** across all major categories.

## ✨ Features

- Automatically sorts files into folders: Programs, Documents, Zip, Videos, Pictures, Music, and Other
- **Extensive format support** - Over 300 file extensions including modern formats like AVIF, HEIC, and JXL
- Creates only the folders needed based on files present
- Handles duplicate filenames by adding numbers (e.g., file(1).txt)
- **Professional-grade coverage** including RAW camera formats, development tools, and specialized formats
- Modern GUI with dark/light mode support

## 📂 File Structure

```
fileorganizer/
├── main.py          # GUI application
├── organizer.py     # Core logic for moving files, undo changes
├── folders.py       # Creates necessary folders
└── constants.py     # Comprehensive file extension definitions (300+ formats)
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

## 📁 Comprehensive File Type Support

### 🎵 **Music (30+ formats)**
- **Lossless**: FLAC, ALAC, WAV, AIFF, DSD formats
- **Compressed**: MP3, AAC, OGG, Opus, WMA
- **Specialized**: Tracker modules (.mod, .xm), MIDI files, rare codecs

### 💻 **Programs (50+ formats)**
- **Windows**: EXE, MSI, batch files, scripts, Control Panel applets
- **Linux/Unix**: Shell scripts, binary executables, packages (DEB, RPM)
- **Mobile**: APK (Android), IPA (iOS), cross-platform packages
- **Development**: Python, Java, JavaScript, and 15+ programming languages

### 📄 **Documents (60+ formats)**
- **Office**: Microsoft Office (DOC, XLS, PPT) + templates and macros
- **Open Formats**: OpenDocument (ODT, ODS, ODP) and variants
- **Publishing**: LaTeX, Adobe (PDF, InDesign), e-books (EPUB, MOBI)
- **Text**: Markdown, plain text, rich text, and documentation formats

### 🗜️ **Archives (50+ formats)**
- **Common**: ZIP, RAR, 7Z, TAR with all compression variants
- **Disk Images**: ISO, IMG, DMG, and virtual disk formats
- **Legacy**: ARJ, LZH, ACE, and vintage archive formats
- **Specialized**: Browser extensions, backup formats, torrents

### 🎬 **Videos (40+ formats)**
- **Standard**: MP4, MKV, AVI, MOV, WebM
- **Professional**: RAW cinema formats (R3D, BRAW), broadcast formats
- **Streaming**: HLS, DASH, Flash video
- **Subtitles**: SRT, VTT, ASS, and other caption formats

### 🖼️ **Pictures (70+ formats)**
- **Common**: JPEG, PNG, GIF, WebP, modern formats (AVIF, HEIC, JXL)
- **RAW Camera**: Support for all major camera brands (Canon, Nikon, Sony, etc.)
- **Professional**: Photoshop (PSD), vector formats (SVG, AI), design tools
- **Specialized**: Medical imaging (DICOM), HDR formats, scientific images

### 📊 **Format Statistics**
- **Total Extensions**: 300+
- **Modern Formats**: Includes cutting-edge codecs like AVIF, JXL, Opus
- **Professional Coverage**: RAW camera files, cinema formats, CAD files
- **Legacy Support**: Vintage formats and legacy file types
- **Cross-Platform**: Windows, macOS, and Linux formats

---

### ✅ Implemented Features

- **Graphical Interface (GUI)**: Full-featured desktop app built with CustomTkinter
- **Dark/Light Mode Support**: Automatically detects Windows theme and adapts colors
- **Persistent Undo Functionality**: Reverse file organization actions even after restarting, using a changelog file
- **Automatic Folder Creation**: Creates only the folders needed based on files present
- **Duplicate Handling**: Prevents overwriting by appending numbers (e.g., file(1).txt)
- **Industry-Leading Extension Support**: 300+ file formats across all categories
- **Real-Time Feedback**: Status messages displayed directly in the GUI
- **Safe Operations**: Skips important files like the changelog and existing folders
- **Smart Categorization**: Handles edge cases and multi-extension files

---

### 📋 Planned Improvements

- **Custom Categories**: Allow users to define their own file categories and extensions
- **Batch Processing**: Organize multiple folders at once
- **Progress Bar**: Show progress for large directories with file count
- **Configuration File**: Save user preferences and custom settings
- **Nested Organization**: Sub-categorize files (e.g., separate RAW vs JPEG, video by resolution)
- **Dry Run Mode**: Preview changes before actually moving files
- **Enhanced Logging**: Keep detailed records with timestamps and file paths
- **Command Line Arguments**: Optional CLI flags for automation and scripting
- **Cross-Platform Theming**: Extend dark/light mode detection to macOS and Linux
- **File Type Detection**: Use file headers in addition to extensions for accuracy
- **Smart Duplicate Handling**: Compare file contents to avoid unnecessary duplicates

## 🔍 Smart File Detection

The organizer uses intelligent file categorization:
- **Extension-based sorting** with case-insensitive matching
- **Multi-extension handling** (e.g., `.tar.gz` uses the final extension)
- **Priority system** ensures files go to the most appropriate category
- **Future-proof** design easily accommodates new file formats

## ⚠️ Important Notes

- Files without extensions and existing folders in the target directory are left untouched
- The system prioritizes file safety - no data loss from conflicts
- **Comprehensive format support** means virtually any file will be properly categorized
- RAW camera files and professional formats are fully supported for creative workflows

## 📖 Documentation

For a complete list of all supported file extensions with descriptions, see the [Supported Extensions Guide](EXTENSIONS.md) that documents all 300+ supported formats.

---

*FileOrganizer: Making file management effortless with professional-grade format support.*
