#!/bin/sh

# Audio
pipewire &
pipewire-pulse &
wireplumber &
# systray battery icon
cbatticon -u 5 &
# systray volume
volumeicon &
# systray disk
udiskie -t &
# systray network-manager
nm-applet &
# Resolution
xrandr -s 1920x1080
# Keyboard layout
setxkbmap latam
# Emacs daemon
emacs --daemon
# Wallpaper
nitrogen --restore
