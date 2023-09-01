# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile keybindings

import os
import subprocess
from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # ScratchPads
    ([mod], "t", lazy.group["scratchpad"].dropdown_toggle('tilix')),
    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "q", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),

    # ------------ App Configs ------------

    # Menu
    # ([mod], "m", lazy.spawn("rofi -show drun")),
    ([mod], "m", lazy.spawn(os.path.expanduser("~/.config/rofi/bin/launcher"))),

    # Prompt
    ([mod], "c", lazy.spawn(os.path.expanduser("~/.config/rofi/bin/runner"))),

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "b", lazy.spawn("firefox")),

    # File Explorer
    ([mod], "e", lazy.spawn("nautilus")),

    # Terminal
    ([mod], "Return", lazy.spawn("tilix")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 2400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    ([mod], "s", lazy.spawn("scrot -s")),
    ([mod, "shift"], "s", lazy.spawn(os.path.expanduser("~/.config/rofi/bin/screenshot"))),

    # Powermenu
    ([mod, "shift"], "p", lazy.spawn(os.path.expanduser("~/.config/rofi/bin/powermenu"))),

    # ------------ Hardware Configs ------------

    # Volume
    ([mod], "F9", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([mod], "F10", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([mod], "F8", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),
    # Brightness
    ([mod], "F7", lazy.spawn("brightnessctl set +10%")),
    ([mod], "F6", lazy.spawn("brightnessctl set 10%-")),
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
