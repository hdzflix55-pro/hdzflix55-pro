#!/bin/bash

echo "Updating and Installing requirements..."
pkg update && pkg upgrade -y
pkg install python git -y

echo "Installing Python libraries..."
pip install requests beautifulsoup4


git config --global credential.helper store

echo "Setup Complete!"
