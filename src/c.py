#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File name: c.py
# Description: Font Color File
# Author: irreq (irreq@protonmail.com)
# Date: 17/12/2021

"""Module for generating colour code values."""

form = {"special": [0, 10],
        "normal": [30, 38],
        "normal_inverted": [40, 48],
        "bright": [90, 98],
        "bright_inverted": [100, 108],
        }

dd = []

for item in form.copy():
    # Create terminal colors
    dd.append(["\x1b[%sm" % n for n in range(*form[item])])

special, normal, normal_inverted, bright, bright_inverted = dd

w = white = special[0]
ul = special[4]

b, r, g, y, b, p, = normal[:6]
