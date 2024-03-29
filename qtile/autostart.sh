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
# Emacs daemon
emacs --daemon
# Wallpaper
nitrogen --restore
# bluetooth
blueman-applet &
# Compositor
picom &

# Betterblockscreen
if [ ! -e $HOME/.cache/betterlockscreen ]
then
   betterlockscreen -u $HOME/voidfiles/images/
fi
