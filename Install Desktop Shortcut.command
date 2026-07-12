#!/bin/bash

APP_DIR="$(cd "$(dirname "$0")" && pwd)"
DESKTOP_LINK="$HOME/Desktop/Francis Portfolio.command"

ln -sf "$APP_DIR/Francis Portfolio.command" "$DESKTOP_LINK"
chmod +x "$APP_DIR/Francis Portfolio.command"

echo "Desktop shortcut created:"
echo "$DESKTOP_LINK"
echo
echo "You can now double-click Francis Portfolio.command on your Desktop."
echo
read -p "Press Enter to close this window..."
