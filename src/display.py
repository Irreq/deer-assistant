#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File name: display.py
# Description: Basic System Functions
# Author: irreq (irreq@protonmail.com)
# Date: 17/12/2021

"""Documentation"""

import time

from . import config, c

from .functions import _get_terminal_size_linux

def response(message, color=config.default_color):
    print("\n{0}{1}{2}".format(color, message, c.w))

class Display:

    def __init__(self):
        config.display = self
        self.response = response
        self.iteration = 0
        self.x, self.y = _get_terminal_size_linux()
        self.run()


    def run(self):
        self.reset()
        self.output(None, lines=config.output)

        # while config.running:
        #     if config.output:
        #         self.output(None, lines=config.output)
        #         config.output = []

    def box(self):
        self.data = ["|"+" "*(self.x-2)+"|",]*(self.y-1)

        self.data[0] = "+" + "-"*(len(self.data[0])-2) + "+"
        self.data[-1] = "+" + "-"*(len(self.data[-1])-2) + "+"

        middle = [self.x//2, self.y//2]
        # text = "Hello World!"
        beg = self.data[middle[1]][:self.x//2-len(text)//2] + text
        self.data[middle[1]] = beg + self.data[middle[1]][len(beg):]

    def reset(self):
        """Create a grid of blank lines to print to"""
        print("\n"*200)
        self.data = [" "*self.x,]*self.y

    def pprint(self, text):
        print("\n"+text)

    def output(self, text, lines=False, reset=False):
        if reset:
            self.reset()

        # self.F("Well this is a wonderful and qwertyuiopåasdfghjklöäzxcvbnm123456789 unexpected treat. I was lookiiiiing up something completely unrelated and came upon you. And now I have a new favorite band. Your sound engineer needs all the praise. It's absolutely perfect here. I hope to see you in America someday! I've been listening to a melodic death metal mixd every weekend for months now while I clean. The three mixes in this series are my favorite. I always come back to them becuase.", 2, 2, width=20, max_lines=18)
        #
        # self.F("Well this is a wonderful and qwertyuiopåasdfghjklöäzxcvbnm123456789 unexpected treat. I was lookiiiiing up something completely unrelated and came upon you. And now I have a new favorite band. Your sound engineer needs all the praise. It's absolutely perfect here. I hope to see you in America someday! I've been listening to a melodic death metal mixd every weekend for months now while I clean. The three mixes in this series are my favorite. I always come back to them becuase.", 2+20+2, 2, width=self.x-(26), max_lines=None)

        if lines:
            self.F(None, (self.x//2-32), (self.y//2-10), lines=lines, )
            # return

        for row, line in enumerate(self.data):
            # print("\n"+line, end="\r")
            print(line)

        time.sleep(1)

    def F(self, text, x, y, width=False, max_lines=None, lines=False, fixed_length=False):
        if not 0 <= x <= self.x or not 0 <= y <= self.y:
            return
        if not lines:
            lines = textwrap.wrap(text, width=width, max_lines=max_lines)

        for i in range(len(lines)):
            # print(len(lines[i]), x, self.x)
            # first = self.data[y+i][:x] + lines[i]
            # first += " "*(self.x - len(first))
            # last = self.data[y+i][fixed_length or len(first)-0:]
            # self.data[y+i] = first + last
            self.data[y+i] = self.data[y+i][:x] + lines[i] + self.data[y+i][len(self.data[y+i][:x] + lines[i]):]
