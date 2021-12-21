#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File name: assistant.py
# Description: Configuration File For Variables
# Author: irreq (irreq@protonmail.com)
# Date: 17/12/2021

import time, readline

from . import config, functions

from .display import response

def user_input(message="\n > "):
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

    def handle_keypress(self, userinput):

        config.user_history.append(userinput)

        userinput = userinput.split()

        ui = userinput[0]

        if " ".join(userinput).startswith("pkg "):
            if "search" in ui:
                ui = ui[len("pkg search "):]
            import subprocess
            output = subprocess.getoutput("pacman -Ss {}".format(ui))
            print(output)
            # config.display.response("You emulated: 'pkg search python3' (for Pacman)")
            from prog import package_manager_parser as pmp

            lines = pmp.main(output)

            result = config.display.generate(lines)

            print()
            for i in result:
                print(i)

        if ui in ("exit", "quit"):
            config.display.response("Deer-Assistant is shutting down\n")
            functions.terminate()





        elif ui == "spotify":
            config.display.response("Let's play some music!")

        elif ui in ("iteration", "iter"):
            response(str(self.iteration))

        else:
            # Generate a file if user input matches that file, eg. 'help'
            if [ui for _ in config.filenames if ui in config.filenames]:
                functions.make_file(ui)
