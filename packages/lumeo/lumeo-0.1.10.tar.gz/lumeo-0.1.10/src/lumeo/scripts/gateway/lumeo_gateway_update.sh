#!/bin/bash

set -eo pipefail

# Check if pipx is installed
if ! command -v pipx &> /dev/null
then
    echo "pipx not found. Installing pipx..."
    sudo apt-get update
    sudo apt-get install -y pipx python3
    pipx ensurepath
fi

# Install lumeo using pipx
if pipx list | grep -q "lumeo"; then
    echo "Updating lumeo CLI to the latest version..."
    pipx upgrade lumeo
else
    echo "Installing lumeo CLI..."
    pipx install lumeo
fi

# Update lumeo gateway containers
lumeo-gateway-manager update --script

# Update lumeo gateway manager web interface
lumeo-gateway-manager update-wgm --script
