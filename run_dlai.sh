#!/bin/bash

# Define the directory where the code will be executed.
# It is assumed that you have already installed the code with install.sh.
# This script should exist on the parent folder of the installation. 
SCRIPT_DIR="`pwd`/email_scanner_dlai"


# Run the Python script
PYTHON_SCRIPT="dlai_scan.py"
echo "Running $PYTHON_SCRIPT..."
cd $SCRIPT_DIR/
uv run python "$PYTHON_SCRIPT"