#!/bin/bash
set -e

echo "Updating Termux packages..."
pkg update -y && pkg upgrade -y

echo "Installing necessary system packages..."
pkg install -y python clang libffi openssl rust make git

echo "Upgrading pip, setuptools, wheel and maturin..."
pip install --upgrade pip setuptools wheel maturin

echo "Installing Paramiko and related Python packages..."
pip install paramiko colorama requests scapy flask bs4 bcrypt cryptography==40.0.2

echo "Installation complete!"
