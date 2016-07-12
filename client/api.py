from http.client import responses
from pprint import pprint as pp

import requests


RESOURCE_ACTIONS = {
    'list': {
        'view': 'list',
        'method': 'get'},
    'create': {
        'view': 'list',
        'method': 'post'},
    'retrieve': {
        'view': 'detail',
        'method': 'get'},
    'update': {
        'view': 'detail',
        'method': 'patch'},
    'delete': {
        'view': 'detail',
        'method': 'delete'}}


class API:
    def __init__(self, api):
        self.api = api
        self.endpoints = requests.get(api).json()

    def format_location(self, view, resource=None, instance=None):
        """
        Returns the formatted location of a resource' list view
        """
        if resource:
            if view == 'detail':
                return '{}{}/{}/'.format(self.api, resource, instance)
            return '{}{}/'.format(self.api, resource)
        return self.api

    def handle_request(self, method, location, data=None, display_output=True):
        if data:
            response = getattr(requests, method)(location, data=data)
        else:
            response = getattr(requests, method)(location)

        try:
            data = response.json()
        except:
            if not display_output:
                raise Exception('No JSON response in silent call')
            data = '{} {}'.format(response.status_code, responses[response.status_code])

        if display_output:
            pp(data)
        return data

    def handle_action(self, action, resource, instance):
        """
        Dispatches action requests to the appropriate handler
        """
        location = self.format_location(RESOURCE_ACTIONS[action]['view'], resource, instance)
        method = RESOURCE_ACTIONS[action]['method']
        if action in ('list', 'retrieve', 'delete'):
            self.handle_request(method, location)
        else:
            data = self.handle_request('get', location, display_output=False) if action == 'update' else {}
            options = list(self.handle_request('options', location, display_output=False)['actions'].values())[0]
            data = self.gather_data(data, options)
            self.handle_request(method, location, data=data)

    def gather_data(self, data, options):
        new_data = {}
        for name, info in options.items():
            if info.get('read_only'):
                continue

            if data:
                header = '{} (type:{}, default:{})'.format(info['label'], info['type'], data.get(name))
            else:
                header = '{} (type:{})'.format(info['label'], info['type'])
            print(header)

            if 'choices' in info:
                for choice in info['choices']:
                    print('{} - {}'.format(choice['value'], choice['display_name']))

            value = None
            while value is None:
                value = input('Value: ')
                if value:
                    if info['type'] == 'integer':
                        try:
                            value = int(value)
                        except:
                            value = None
                    elif info['type'] == 'boolean':
                        value = value.lower() in ('1', 't', 'true', 'y', 'yes', 'ya', 'yeah', 'yup', 'uh-huh')
                    elif ',' in value:
                        value = list(map(str.strip, value.split(',')))

            if value:
                new_data[name] = value
            print()

        return new_data
