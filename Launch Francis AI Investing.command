#!/bin/bash

cd "$(dirname "$0")"
clear

echo "Starting Francis AI Investing..."
echo

python3 -c "import yfinance, pandas" >/dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "Installing required Python packages..."
    python3 -m pip install -r requirements.txt
    echo
fi

python3 main.py

echo
read -p "Press Enter to close this window..."
