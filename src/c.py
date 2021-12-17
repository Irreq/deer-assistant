#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File name: c.py
# Description: Font Color File
# Author: irreq (irreq@protonmail.com)
# Date: 17/12/2021

"""
Module for dynamically generating colour code values.
Will then be used as a dictionary of placeholders

Eg. every instance of: '<YELLOW>' will make everything
after that yellow until there is a '<RESET>' character.

Run this file separately to get a hint of what can be used.
"""

from . import config

# Colour codes: https://en.wikipedia.org/wiki/ANSI_escape_code
form = {"special": ([0, 10], ""),
        "normal": ([30, 38], ""),
        "normal_inverted": ([40, 48], " inverted"),
        "bright": ([90, 98], " bright"),
        "bright_inverted": ([100, 108], " bright inverted"),
        }

special = ["reset", "bold", "faint", "italic", "underline", "slow blink", "fast blink", "invert", "hide", "strike", "default"]
colors = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]

placeholders = {}

# Generate colors
for item in form:
    if item == "special":
        for n, k in enumerate(special):
            placeholders["<"+k.upper()+">"] = "\x1b[%sm" % n
    else:
        for i, v in enumerate(range(*form[item][0])):
            placeholders["<"+colors[i].upper()+form[item][1].upper()+">"] = "\x1b[%sm" % v

config.placeholders = placeholders


def test():
    print("\nIgnore index\n")
    for i, thing in enumerate(placeholders):
        print(i, thing, placeholders[thing]+"Hello World!"+placeholders["<RESET>"])

if __name__ == "__main__":
    test()
