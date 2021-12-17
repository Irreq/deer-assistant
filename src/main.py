#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File name: main.py
# Description: Main File For The Deer-Assistant
# Author: irreq (irreq@protonmail.com)
# Date: 17/12/2021

"""Documentation"""

import time, sys, struct, os, textwrap

not_utf8_environment = "UTF-8" not in sys.stdout.encoding

from . import c, config

from concurrent.futures import ThreadPoolExecutor



# LANDING = skel.LANDING.replace("$", __version__)
# LANDING = LANDING.replace("USER", get_username()).split("\n")

LANDING = []

config.default_color = config.placeholders["<YELLOW>"]




def run_io_tasks_in_parallel(tasks):

    """
    Run functions in paralell.
    NOTE:     This function can be used for any type of functions.
    ARGUMENTS:
        - tasks:             list() representing function variables.
                             Eg, [foo, bar]
    TODO:     None
    """

    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            running_task.result()


from .assistant import Assistant
from .display import Display


from .ai import AI

def assistant():
    from .assistant import Assistant
    config.assistant = Assistant()

def display():
    from .display import Display
    config.display = Display()

def main(lines):
    config.output = lines
    config.display = Display()
    run_io_tasks_in_parallel([Assistant, AI,])
