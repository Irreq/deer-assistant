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

def terminate():

    config.running = False

    time.sleep(2)

    exit()


def initiate_cache():
    """This function is not finished but will create a dynamic program list"""
    return

def get_from_file(path):
    content=open(path, "r").readline().strip()
    return content

def launch(command):
    """Launch a program as it would have been launched in terminal"""
    commands = command.split()
    subprocess.Popen(commands)
    return True
