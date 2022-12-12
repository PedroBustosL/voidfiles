#!/usr/bin/env sh

SNIPPETS_DIR="$HOME/scripts/snippets"
selected_snippet=$(ls $SNIPPETS_DIR | fzf)
SNIPPET_PATH="$SNIPPETS_DIR/$selected_snippet"

xclip -sel clip $SNIPPET_PATH
xclip -o > clipmenu
CM_LAUNCHER=rofi clipmenu
