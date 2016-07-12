#! /usr/bin/env python3

import argparse
from functools import lru_cache
import json

import api


class BetterReads:
    """
    Command line interface to BetterReads literary database API
    """

    def __init__(self, *args, **kwargs):
        with open('config.json') as f:
            self.settings = json.load(f)
        try:
            self.betterreads = api.API(self.settings['api'])
            self.betterreads.handle_action(self.args.action, self.args.resource, self.args.instance)
        except Exception as e:
            raise
            argparse.ArgumentParser().exit(1, str(e))

    @property
    @lru_cache(1)
    def args(self):
        parser = argparse.ArgumentParser(description=self.__doc__)
        parser.add_argument('-r', '--resource', choices=self.betterreads.endpoints.keys(),
                            help='Specify a resource to consume')
        parser.add_argument('-i', '--instance', help='Specify the primary key of a resource instance')
        parser.add_argument('-a', '--action', choices=api.RESOURCE_ACTIONS, help='Specify an action to take')
        args = parser.parse_args()

        if not args.action:
            args.action = 'retrieve' if args.instance else 'list'
        if api.RESOURCE_ACTIONS[args.action]['view'] == 'detail' and not args.instance:
            raise Exception('That action requires a resource instance')

        return args


if __name__ == '__main__':
    BetterReads()
