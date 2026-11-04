#!/bin/zsh
# usage: shot.sh <preview.html> <out.png>
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
  --window-size=1440,900 --virtual-time-budget=4000 \
  --screenshot="$2" "file://$PWD/$1" >/dev/null 2>&1
