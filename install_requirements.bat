@echo off
:: Check if python is installed
where python >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python 3 before proceeding.
    exit /b 1
)

:: Upgrade pip and install customtkinter
echo Installing required Python package: customtkinter
python -m pip install --upgrade pip
python -m pip install customtkinter

echo Installation complete!
pause