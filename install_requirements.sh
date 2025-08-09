#!/bin/bash

# Check if python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install Python 3 before proceeding."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null
then
    echo "pip3 is not installed. Installing pip3..."
    python3 -m ensurepip --upgrade || {
        echo "Failed to install pip3. Please install it manually."
        exit 1
    }
fi

echo "Installing required Python package: customtkinter"
python3 -m pip install --upgrade pip
python3 -m pip install customtkinter

echo "Installation complete!"
