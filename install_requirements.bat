@echo off
setlocal enabledelayedexpansion
title File Organizer - Dependency Installer

:: Colors for better output
call :setESC

echo %ESC%[96m============================================%ESC%[0m
echo %ESC%[96m    File Organizer - Dependency Installer%ESC%[0m
echo %ESC%[96m============================================%ESC%[0m
echo.

:: Check if running as administrator (optional for better pip experience)
net session >nul 2>&1
if %errorLevel% == 0 (
    echo %ESC%[92m[INFO]%ESC%[0m Running with administrator privileges
) else (
    echo %ESC%[93m[WARN]%ESC%[0m Not running as administrator - some operations may require elevated privileges
)
echo.

:: Check if Python is installed
echo %ESC%[94m[STEP 1/4]%ESC%[0m Checking Python installation...
where python >nul 2>&1
if errorlevel 1 (
    echo %ESC%[91m[ERROR]%ESC%[0m Python is not installed or not in PATH
    echo %ESC%[93m[HELP]%ESC%[0m Please install Python 3.8+ from: https://python.org/downloads/
    echo %ESC%[93m[HELP]%ESC%[0m Make sure to check "Add Python to PATH" during installation
    goto :error_exit
)

:: Get Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo %ESC%[92m[SUCCESS]%ESC%[0m Python %PYTHON_VERSION% found

:: Check Python version (basic check for 3.x)
echo %PYTHON_VERSION% | findstr /r "^3\." >nul
if errorlevel 1 (
    echo %ESC%[91m[ERROR]%ESC%[0m Python version %PYTHON_VERSION% detected
    echo %ESC%[93m[HELP]%ESC%[0m This application requires Python 3.8 or higher
    goto :error_exit
)
echo.

:: Check if pip is available
echo %ESC%[94m[STEP 2/4]%ESC%[0m Checking pip installation...
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo %ESC%[91m[ERROR]%ESC%[0m pip is not available
    echo %ESC%[93m[HELP]%ESC%[0m Please reinstall Python with pip included
    goto :error_exit
)
echo %ESC%[92m[SUCCESS]%ESC%[0m pip is available
echo.

:: Upgrade pip
echo %ESC%[94m[STEP 3/4]%ESC%[0m Upgrading pip to latest version...
python -m pip install --upgrade pip --quiet
if errorlevel 1 (
    echo %ESC%[93m[WARN]%ESC%[0m Failed to upgrade pip, continuing with current version...
) else (
    echo %ESC%[92m[SUCCESS]%ESC%[0m pip upgraded successfully
)
echo.

:: Install customtkinter
echo %ESC%[94m[STEP 4/4]%ESC%[0m Installing required dependencies...
echo %ESC%[97m          Installing customtkinter...%ESC%[0m

python -m pip install customtkinter --quiet
if errorlevel 1 (
    echo %ESC%[91m[ERROR]%ESC%[0m Failed to install customtkinter
    echo %ESC%[93m[HELP]%ESC%[0m Try running this script as administrator
    echo %ESC%[93m[HELP]%ESC%[0m Or install manually: pip install customtkinter
    goto :error_exit
)

:: Verify installation
python -c "import customtkinter" 2>nul
if errorlevel 1 (
    echo %ESC%[93m[WARN]%ESC%[0m customtkinter installed but import test failed
    goto :error_exit
)

echo %ESC%[92m[SUCCESS]%ESC%[0m customtkinter installed and verified
echo.

:: Success message
echo %ESC%[92m============================================%ESC%[0m
echo %ESC%[92m           INSTALLATION COMPLETE!%ESC%[0m
echo %ESC%[92m============================================%ESC%[0m
echo.
echo %ESC%[96m[READY]%ESC%[0m All dependencies installed successfully
echo %ESC%[96m[NEXT]%ESC%[0m  You can now run: %ESC%[97mpython main.py%ESC%[0m
echo.
echo %ESC%[93mPress any key to exit...%ESC%[0m
pause >nul
exit /b 0

:error_exit
echo.
echo %ESC%[91m============================================%ESC%[0m
echo %ESC%[91m           INSTALLATION FAILED!%ESC%[0m
echo %ESC%[91m============================================%ESC%[0m
echo.
echo %ESC%[93mPress any key to exit...%ESC%[0m
pause >nul
exit /b 1

:setESC
:: Set up ANSI escape sequences for colors (Windows 10+)
for /F %%a in ('echo prompt $E ^| cmd') do set "ESC=%%a"
exit /b 0
