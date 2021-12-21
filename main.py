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

path = "~"
import os, sys
path = os.path.expanduser("~/.config/")
sys.path.append(path)

if __name__ == "__main__":
    functions.initiate_cache()
    # from prog import package_manager_parser as pmp
    query = """
    core/python 3.10.1-1 [installed]
        Next generation of the python high-level scripting language
    extra/boost-libs 1.78.0-1
        Free peer-reviewed portable C++ source libraries (runtime libraries)
    extra/python-chardet 4.0.0-5
        Python3 module for character encoding auto-detection
    extra/python-cssselect 1.1.0-9
        A Python3 library that parses CSS3 Selectors and translates them to XPath 1.0
    extra/python-lxml 4.6.4-3
        Python3 binding for the libxml2 and libxslt libraries
    extra/python-pyopenssl 21.0.0-5
        Python3 wrapper module around the OpenSSL library
    extra/vim 8.2.3582-3 [installed]
        Vi Improved, a highly configurable, improved version of the vi text editor
    community/nemo-python 5.0.0-3
        Python3 binding for Nemo components
    community/pypy3 7.3.7-1
        A Python3 implementation written in Python, JIT enabled
    community/python-argparse 1.4.0-11
        Python3 command-line parsing library
    community/python-bitcoinlib 0.11.0-3
        Python3 library providing an easy interface to the Bitcoin data structures and protocol
    community/python-feedgenerator 1.9.2-3
        Standalone version of django.utils.feedgenerator (python3).
    community/python-isomd5sum 1.2.3-6
        Python3 bindings for isomd5sum
    community/python-pyenchant 3.2.1-3
        PyEnchant is a spellchecking library for Python3 based on the Enchant library
    community/python-pyzmq 22.2.1-3
        Python3 bindings for zeromq, written in Cython
    community/python-xcffib 0.11.1-3 [installed]
        Python3 drop in replacement for xpyb, an XCB python binding
    community/python2-wxpython3 3.0.2.0-3
        Classic wxWidgets GUI toolkit for Python
    """




    # import subprocess
    # output = subprocess.getoutput("ls -l")
    #
    #
    # from src.display import Display
    # config.display = Display()
    #
    # config.display.response("You emulated: 'pkg search python3' (for Pacman)")
    #
    #
    # lines = pmp.main(query)
    #
    # result = config.display.generate(lines)
    #
    # print()
    # for i in result:
    #     print(i)
    lines = functions.getlines("lib/landing.txt")
    result = display.generate(lines)
    main.main(result)
