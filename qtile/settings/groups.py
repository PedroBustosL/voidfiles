# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile workspaces

from libqtile.config import Key, Group, ScratchPad, DropDown
from libqtile.command import lazy
from .keys import mod, keys


# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Icons: 
# nf-fa-firefox, 
# nf-fae-python, 
# nf-dev-terminal, 
# nf-fa-code, 
# nf-oct-git_merge, 
# nf-linux-docker,
# nf-mdi-image, 
# nf-mdi-layers

# groups = [ Group(i) for i in [
# "   ", "   ", "   ", "   ", "  ", "   ", " 󰉋  ", "   ", " 󰌨  ",
# ]]

groups = [ ScratchPad('scratchpad', [
                          DropDown('tilix', 'tilix', opacity=0.8),
                          DropDown('iotas', 'flatpak run org.gnome.gitlab.cheywood.Iotas', opacity=0.9)]),
           Group('  '),
           Group('  '),
           Group('  '),
           Group('  '),
           Group('  '),
           Group('  '),
           Group(' 󰉋 '),
           Group('  '),
           Group(' 󰌨 '),
          ]

for i, group in enumerate(groups[1:]):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
