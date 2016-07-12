import argparse
from functools import lru_cache
import json

import betterreads


class CLI:
    """
    Command line interface to BetterReads literary database API
    """

    def __init__(self, *args, **kwargs):
        with open('config.json') as f:
            self.settings = json.load(f)
        self.betterreads = betterreads.BetterReads(self.settings['api'])

    @property
    @lru_cache(1)
    def args(self):
        parser = argparse.ArgumentParser(description=self.__doc__)


if __name__ == '__main__':
    CLI()
