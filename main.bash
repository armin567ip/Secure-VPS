#!/bin/bash

# Check if script is run as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root."
    exit 1
fi

# Update package list
sudo apt update

# Install Python 3 and pip
sudo apt install -y python3 python3-pip

# Fetch Python script from GitHub and save it as main.py
curl -sSL https://raw.githubusercontent.com/armin567ip/Secure-VPS/main/main.py -o main.py

# Run the main.py script
python3 main.py
