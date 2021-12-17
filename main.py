#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File name: main.py
# Description: Start File For The Deer-Assistant
# Author: irreq (irreq@protonmail.com)
# Date: 17/12/2021

"""Documentation"""

__author__ = "Isac Bruce"
__copyright__ = "Copyright 2021, Irreq"
__credits__ = ["Isac Bruce"]
__license__ = "MIT"
__version__ = "0.1.2"
__maintainer__ = "Isac Bruce"
__email__ = "irreq@protonmail.com"
__status__ = "Development"

from src import main, c

def landing():
    """Generate a landing page"""

    with open('lib/landing.txt') as f:
        lines = f.readlines()
        f.close()

    result = []

    tags = {"<WHITE>": c.w,
            "<VERSION>": __version__,}

    # print(tags.keys())

    for i, line in enumerate(lines):
        # ignored = (7,)
        ignored = (99,)
        # if any(t in line for t in tags.keys()):
        #     line = line.replace(t, tags[t])

        # Replace all placeholders with correct values
        for item in [t for t in tags.keys() if t in line]:
            line = line.replace(item, tags[item])



        # if i in ignored:
        #     line = line.replace("$", __version__)
        result.append(c.y*(i not in ignored) + line.replace("\n", "") + c.w)

    return result


if __name__ == "__main__":
    result = landing()

    main.main(result)
