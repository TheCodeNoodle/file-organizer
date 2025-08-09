#!/bin/bash

# Colors for better output
RED='\033[0;91m'
GREEN='\033[0;92m'
YELLOW='\033[0;93m'
BLUE='\033[0;94m'
PURPLE='\033[0;95m'
CYAN='\033[0;96m'
WHITE='\033[0;97m'
NC='\033[0m' # No Color

# Function to print colored output
print_step() { echo -e "${BLUE}[STEP $1/$2]${NC} $3"; }
print_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
print_error() { echo -e "${RED}[ERROR]${NC} $1"; }
print_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
print_info() { echo -e "${CYAN}[INFO]${NC} $1"; }
print_help() { echo -e "${YELLOW}[HELP]${NC} $1"; }

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function for error exit
error_exit() {
    echo
    echo -e "${RED}============================================${NC}"
    echo -e "${RED}           INSTALLATION FAILED!${NC}"
    echo -e "${RED}============================================${NC}"
    echo
    exit 1
}

# Header
echo -e "${CYAN}============================================${NC}"
echo -e "${CYAN}    File Organizer - Dependency Installer${NC}"
echo -e "${CYAN}============================================${NC}"
echo

# Detect OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="Linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macOS"
elif [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]]; then
    OS="Windows (WSL/Cygwin)"
else
    OS="Unknown"
fi

print_info "Detected OS: $OS"

# Check if running with sudo (warn if yes)
if [[ $EUID -eq 0 ]]; then
    print_warn "Running as root - this may cause permission issues with pip"
    print_help "Consider running without sudo for user-local installation"
fi
echo

# Step 1: Check Python3 installation
print_step "1" "5" "Checking Python3 installation..."

if ! command_exists python3; then
    print_error "Python3 is not installed or not in PATH"
    echo
    print_help "Installation instructions by OS:"
    print_help "Ubuntu/Debian: sudo apt update && sudo apt install python3 python3-pip"
    print_help "CentOS/RHEL:   sudo yum install python3 python3-pip"
    print_help "Arch Linux:    sudo pacman -S python python-pip"
    print_help "macOS:         brew install python3 (or download from python.org)"
    print_help "Alpine:        sudo apk add python3 py3-pip"
    error_exit
fi

# Get Python version
PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2)
print_success "Python3 $PYTHON_VERSION found"

# Check Python version (basic check for 3.x and minimum version)
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d'.' -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d'.' -f2)

if [[ $PYTHON_MAJOR -lt 3 ]] || [[ $PYTHON_MAJOR -eq 3 && $PYTHON_MINOR -lt 8 ]]; then
    print_error "Python version $PYTHON_VERSION detected"
    print_help "This application requires Python 3.8 or higher"
    print_help "Please upgrade your Python installation"
    error_exit
fi
echo

# Step 2: Check pip3 installation
print_step "2" "5" "Checking pip3 installation..."

if ! command_exists pip3; then
    print_warn "pip3 not found, attempting to install..."
    
    if python3 -m ensurepip --upgrade >/dev/null 2>&1; then
        print_success "pip3 installed via ensurepip"
    else
        print_error "Failed to install pip3 automatically"
        echo
        print_help "Manual installation by OS:"
        print_help "Ubuntu/Debian: sudo apt install python3-pip"
        print_help "CentOS/RHEL:   sudo yum install python3-pip"
        print_help "Arch Linux:    sudo pacman -S python-pip"
        print_help "macOS:         python3 -m ensurepip --upgrade"
        error_exit
    fi
else
    print_success "pip3 is available"
fi

# Verify pip3 works with python3
if ! python3 -m pip --version >/dev/null 2>&1; then
    print_error "pip3 is installed but not working with python3"
    print_help "Try: python3 -m ensurepip --upgrade"
    error_exit
fi
echo

# Step 3: Check virtual environment (optional but recommended)
print_step "3" "5" "Checking installation environment..."

if [[ -n "$VIRTUAL_ENV" ]]; then
    print_info "Virtual environment detected: $(basename $VIRTUAL_ENV)"
    print_success "Installing in virtual environment (recommended)"
else
    print_warn "No virtual environment detected"
    print_help "Consider using: python3 -m venv venv && source venv/bin/activate"
    print_info "Proceeding with user-local installation..."
fi
echo

# Step 4: Upgrade pip
print_step "4" "5" "Upgrading pip to latest version..."

if python3 -m pip install --upgrade pip --quiet --user >/dev/null 2>&1; then
    print_success "pip upgraded successfully"
else
    print_warn "Failed to upgrade pip, continuing with current version..."
fi
echo

# Step 5: Install customtkinter
print_step "5" "5" "Installing required dependencies..."
echo -e "${WHITE}          Installing customtkinter...${NC}"

# Try installation with different methods
if python3 -m pip install customtkinter --quiet --user >/dev/null 2>&1; then
    INSTALL_METHOD="user-local"
elif python3 -m pip install customtkinter --quiet >/dev/null 2>&1; then
    INSTALL_METHOD="system-wide"
else
    print_error "Failed to install customtkinter"
    echo
    print_help "Troubleshooting steps:"
    print_help "1. Check internet connection"
    print_help "2. Try: python3 -m pip install --upgrade pip"
    print_help "3. Try: python3 -m pip install customtkinter --user"
    print_help "4. Check if you need to install build tools"
    error_exit
fi

# Verify installation
if python3 -c "import customtkinter" 2>/dev/null; then
    print_success "customtkinter installed and verified ($INSTALL_METHOD)"
else
    print_error "customtkinter installed but import test failed"
    print_help "Try restarting your terminal or check your Python path"
    error_exit
fi

echo

# Success message
echo -e "${GREEN}============================================${NC}"
echo -e "${GREEN}           INSTALLATION COMPLETE!${NC}"
echo -e "${GREEN}============================================${NC}"
echo
print_info "All dependencies installed successfully"
echo -e "${CYAN}[NEXT]${NC}  You can now run: ${WHITE}python3 main.py${NC}"
echo
print_info "Installation method: $INSTALL_METHOD"
if [[ -z "$VIRTUAL_ENV" ]]; then
    print_help "Tip: Consider using virtual environments for future projects"
fi
echo

exit 0
