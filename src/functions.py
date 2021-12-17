#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File name: functions.py
# Description: Basic System Functions
# Author: irreq (irreq@protonmail.com)
# Date: 17/12/2021

"""Documentation"""

import os, pwd, time

from . import config

def _get_terminal_size_linux():
    """ Get terminal size Linux. """
    def ioctl_GWINSZ(fd):
        """ ioctl_GWINSZ. """
        try:
            import fcntl
            import termios
            cr = struct.unpack('hh',
                               fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
            return cr

        except:
            pass

    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)

    if not cr or cr == (0, 0):

        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)

        except:
            pass

    if not cr or cr == (0, 0):

        try:
            cr = (os.environ['LINES'], os.environ['COLUMNS'])

        except:
            return

    return int(cr[1]), int(cr[0])

def get_username():
    return pwd.getpwuid(os.getuid())[0]

def getlines(path):
    with open(path, "r") as f:
        lines = [line.replace("\n", "") for line in f.readlines()]
        f.close()
    return lines

def terminate():

    config.running = False

    time.sleep(2)

    print("\n"*200)

    lines = getlines("lib/landing.txt")
    result = config.display.generate(lines)

    config.display.output(None, lines=result)

    lines = getlines("lib/exit.txt")
    result = config.display.generate(lines)

    for i in result:
        print(i)

    print("\n")
    exit()


def make_file(name):
    lines = getlines("lib/{}.txt".format(name))
    result = config.display.generate(lines)
    for i in result:
        print(i)

    # config.display.output(None, lines=result)

def initiate_cache():
    """This function is not finished but will create a dynamic program list"""
    config.filenames = next(os.walk("lib/"), (None, None, []))[2]  # [] if no file
    config.filenames = [i.replace(".txt","") for i in config.filenames]

def get_from_file(path):
    content=open(path, "r").readline().strip()
    return content

def launch(command):
    """Launch a program as it would have been launched in terminal"""
    commands = command.split()
    subprocess.Popen(commands)
    return True
