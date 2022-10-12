import json
from urllib.request import Request, urlopen

from falu.client.authentication_header.provider import IAuthenticationProvider


def make_json(data):
    return json.dumps(data).encode()


class BaseApiClient:
    def __init__(self, provider: IAuthenticationProvider):
        self.provider = provider
        pass

    def _execute(self, request: Request):
        self.provider.process(request)

        # send the request over wire
        response = urlopen(request)

        # handle the resulting responses

        pass
