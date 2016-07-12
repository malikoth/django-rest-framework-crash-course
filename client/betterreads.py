import requests


class BetterReads:
    def __init__(self, api):
        self.api = api
        self.endpoint = {
            name: {
                'endpoint': endpoint,
                'metadata': requests.get(endpoint + 'metadata/').json()
            }
            for name, endpoint in requests.get(api).json().items()}
