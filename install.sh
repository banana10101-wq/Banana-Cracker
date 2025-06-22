#!/bin/bash

echo "Updating and upgrading Termux packages..."
pkg update && pkg upgrade -y
echo "Installing required Termux packages..."
pkg install clang python-dev libffi-dev openssl-dev cargo rust -y

echo "Upgrading pip and installing Python packages..."
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

echo "Installation complete!"
