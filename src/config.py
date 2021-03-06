#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File name: config.py
# Description: Configuration File For Variables
# Author: irreq (irreq@protonmail.com)
# Date: 17/12/2021

"""File that holds global variables for the program"""

logging = False

things_to_display = ["",]

functions_to_display = ["battery", "storage_test", "memory", "cpu", "datetime"]

alias = {
    # Programs
    "alacritty": "alacritty",
    "discord": "Discord",

    # Programming
    "atom": "atom",
    "nvim": "nvim",
    "vim": "vim",
    "python3": "alacritty",

    # Web
    "firefox": "firefox",
    "github": "firefox https://github.com/Irreq",
    "youtube": "https://www.youtube.com/results?search_query=QUERY",

    # System (be careful, some stuff might break)
    "update": "sudo xbps-install -Su",
    "reboot": "sudo reboot now",
    "shutdown": "sudo shutdown -h now",

    "tester": "(alacritty &)",

    # Audio
    "vol_up": "amixer -q sset Master 10%+",
    "vol_down": "amixer -q sset Master 10%-",
    "pause": "python3 -q /home/irreq/github/programs/audio.py toggle",
    "gesture_audio": "python3 -q /home/irreq/github/programs/handVolumeController.py",
    "pavucontrol": "pavucontrol",
    "spotify": "spotify -no-zygote",

    # Meta
    "open": "atom",
    "filebrowser": "thunar",
    "tts": "sam",  # requires 'SAM' as /bin/sam
    "searchbrowser": "firefox",
    "search": "firefox https://duckduckgo.com/?q=QUERY&ia=web", # QUERY is what you type after search
    "terminal": "alacritty",
    "keyboard": "setxkbmap se",
    "wifi": "sudo wpa_supplicant -B -iwlo1 -c/etc/wpa_supplicant/wpa_supplicant-wlo1.conf",
    "screen_hdmi": "xrandr --output VGA-0 --off --output LVDS --off --output HDMI-0 --mode 1920x1200 --pos 0x0 --rotate normal",
    "screen_vga": "xrandr --output HDMI-0 --off --output LVDS --off --output VGA-0 --mode 1920x1200 --pos 0x0 --rotate normal",
    "screen_vga_thinkpad": "xrandr --output HDMI-0 --off --output LVDS1 --off --output VGA1 --mode 1920x1200 --pos 0x0 --rotate normal",
}


distro_skeleton = {
"Venom Linux": {"package_manager": ("scratch", {"install": "scratch install $",
                                                "sync": "scratch sync",
                                                "search": "scratch search $",
                                                "upgrade": "scratch upgrade $ -y",
                                                "remove": "scratch remove $ -y",
                                                "info": "scratch info $",
                                                "list": "scratch installed"})
                },

"Arch Linux": {"package_manager": ("pacman", {"install": "pacman -S $",
                                              "sync": "pacman -S",
                                              "search": "pacman -Ss $",
                                              "upgrade": "pacman -U $",
                                              "remove": "pacman -R $",
                                              "info": "pacman -Qi",
                                              "list": "pacman -Qe"})
                },

"Void Linux": {"package_manager": ("xbps", {})},

# Skeleton
"GENERIC Linux": {"package_manager": ("MANAGER", {"install": "METHOD",
                                               "sync": "METHOD",
                                               "search": "METHOD",
                                               "upgrade": "METHOD",
                                               "remove": "METHOD",
                                               "info": "METHOD",
                                               "list": "METHOD"})
}
}


system = None

user_history = []

filenames = []

output = []

placeholders = {}

default_color = None

running = True

display = None

assistant = None
