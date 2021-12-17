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
__version__ = "0.1.2"
__maintainer__ = "Isac Bruce"
__email__ = "irreq@protonmail.com"
__status__ = "Development"

config.placeholders["<VERSION>"] = __version__

if __name__ == "__main__":
    functions.initiate_cache()
    lines = functions.getlines("lib/landing.txt")
    result = display.generate(lines)
    main.main(result)
