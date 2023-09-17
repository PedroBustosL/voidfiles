from libqtile import widget, qtile
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def open_calendar(qtile):
   qtile.cmd_spawn('gsimplecal')

def close_calendar(qtile):
   qtile.cmd_spawn('killall -q gsimplecal')

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    widget.Prompt(
                background=colors['dark'],
    ),

    separator(),

    powerline('color4', 'dark'),

    icon(bg="color4", text=' '), # Icon: nf-fa-download
    
    widget.CheckUpdates(
        distro='Void',
        background=colors['color4'],
        foreground=colors['text'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='xbps-install -nuMS',
        execute='tilix -e sudo xbps-install -Suv && qtile cmd-obj -o widget checkupdates -f force_update',
        initial_text = '󰇘',
    ),

    powerline('color3', 'color4'),

    icon(bg="color3", text=" "),  # Icon: nf-fa-hdd_o
    # icon(bg="color3", text=' '),  # Icon: nf-fa-feed
    # icon(bg="color3", text='󰛳 '),  # Icon: nf-md-network
    
    # widget.Net(**base(bg='color3'), interface='wlp1s0'),
    widget.DF(**base(bg="color3"), visible_on_warn=False, warn_color="e67e80", warn_space=2),

    widget.Sep(**base(bg="color3"), linewidth=0, padding=5),

    icon(bg="color3", text=" "),  # Icon: nf-fae-chip

    widget.Memory(**base(bg="color3")),  # , measure_mem='G'

    widget.Sep(**base(bg="color3"), linewidth=0, padding=5),

    icon(bg="color3", text=" "),  # Icon: nf-oct-cpu

    widget.CPU(**base(bg="color3"), format='{freq_current}GHz {load_percent}%'),

    powerline('color1', 'color3'),

    icon(bg="color1", fontsize=17, text='󰃰 '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color1'), mouse_callbacks = {'Button1': lambda:
                                                         qtile.cmd_function(open_calendar), 'Button3': lambda: qtile.cmd_function(close_calendar)},format='%d/%m/%Y - %H:%M '),

    powerline('color5', 'color1'),

    icon(bg="color5", text="󰃞 "),  # Icon: nf-md-brigthness-5

    widget.Backlight(**base(bg='color5'), backlight_name='amdgpu_bl0'),

    powerline('color2', 'color5'),

    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    # widget.CurrentLayout(**base(bg='color2'), padding=5),

    powerline('color4', 'color2'),

    widget.KeyboardLayout(**base(bg='color4'), configured_keyboards=["us", "us dvorak", "latam"], display_map={"us":"US", "us dvorak":"DVK", "latam":"LAT"}),

    powerline('dark', 'color4'),

    widget.Systray(background=colors['dark'], padding=5),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    # widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color1'), mouse_callbacks = {'Button1': lambda:
   qtile.cmd_function(open_calendar)},format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
