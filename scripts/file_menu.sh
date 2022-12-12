#!/usr/bin/bash

AUTOSTART="$HOME/.config/herbstluftwm/autostart"
menu="$(cat "$HOME/scripts/menu_list.txt" | fzf --prompt="SELECCIONA ARCHIVO PARA EDITAR" )"

if [ "$menu" = "autostart" ]
then
    emacsclient -c -n -a 'emacs' "$AUTOSTART"
fi
