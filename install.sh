#!/bin/bash

echo "Updating Termux packages..."
pkg update && pkg upgrade -y

echo "Installing Termux system packages required for building some Python packages..."
pkg install -y clang python-dev libffi-dev openssl-dev cargo rust

echo "Upgrading pip and related tools..."
pip install --upgrade pip setuptools wheel

echo "Installing Python packages via pip..."
pip install paramiko colorama requests scapy flask bs4

echo "All specified Python packages installed successfully!"
