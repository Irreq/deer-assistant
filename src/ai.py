import time

from . import config

class AI:
    def __init__(self):
        pass

    def run(self):

        while config.running:
            time.sleep(1)
