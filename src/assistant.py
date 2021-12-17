#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File name: assistant.py
# Description: Configuration File For Variables
# Author: irreq (irreq@protonmail.com)
# Date: 17/12/2021

import time, readline

from . import config, functions

from .display import response

def user_input(message="\n> "):
    return input(message)

class Assistant:

    def __init__(self):

        self.run()

    def run(self):
        time.sleep(0.1)
        config.display.response("Hey I'm Online Now!")
        while config.running:
            self.handle_keypress(user_input().lower())




            # self.iteration += 1

    def handle_keypress(self, ui):

        if ui in ("exit", "quit"):
            config.display.response("Deer-Assistant is shutting down")
            functions.terminate()

        elif ui == "spotify":
            config.display.response("Let's play some music!")

        elif ui in ("iteration", "iter"):
            response(str(self.iteration))
