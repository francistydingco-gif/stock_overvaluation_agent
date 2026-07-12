#!/bin/bash

cd "$(dirname "$0")"
clear

echo "Francis AI Investing"
echo "Portfolio Report"
echo

python3 -c "import yfinance, pandas" >/dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "Installing required Python packages..."
    python3 -m pip install -r requirements.txt
    echo
fi

python3 -c "from main import print_portfolio_report; print_portfolio_report()"

echo
read -p "Press Enter to refresh/close, then run again for updated prices..."
