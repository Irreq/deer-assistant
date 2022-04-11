#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File name: main.py
# Description: Start File For The Deer-Assistant
# Author: irreq (irreq@protonmail.com)
# Date: 17/12/2021

"""Documentation"""

from src import main, config, display, functions

__author__ = "Isac Bruce"
__copyright__ = "Copyright 2021, Irreq"
__credits__ = ["Isac Bruce"]
__license__ = "MIT"
__version__ = "0.1.3"
__maintainer__ = "Isac Bruce"
__email__ = "irreq@protonmail.com"
__status__ = "Development"

config.placeholders["<VERSION>"] = __version__

path = "~"
import os, sys
path = os.path.expanduser("~/.config/")
sys.path.append(path)

def test():
    from prog import package_manager_parser as pmp
    from src.display import Display
    functions.initiate_cache()
    config.display = Display()
    PACKAGE = "python3"
    config.display.response("You emulated: 'pkg search {}' (for Pacman)".format(PACKAGE))

    lines = pmp.main(PACKAGE)

    result = config.display.generate(lines)

    print()
    for i in result:
        print(i)

    exit()

if __name__ == "__main__":
    test()
    functions.initiate_cache()
    lines = functions.getlines("lib/landing.txt")
    result = display.generate(lines)
    main.main(result)
