import json

import requests
from requests import Response

from falu.client.falu_model import FaluModel
from falu.client.falu_model import deserialize_falu_response
from falu.list_options import BasicListOptions
from falu.query_values import QueryValues


class ApiClient(FaluModel):
    def __init__(self):
        super().__init__()
        self.base_url = 'https://api.falu.io/v1'

    @classmethod
    def _execute(cls, method, path, data=None, options: BasicListOptions = None, key=None, idempotency_key: str = None,
                 workspace=None, live: bool = None, params=None):
        params = cls._generate_params(options, params)
        client = ApiClient()
        return client.execute(method, path, data, key, idempotency_key, workspace, live, params)

    def execute(self, method, path, data=None, key=None, idempotency_key: str = None, workspace=None, live: bool = None,
                params=None):

        url = self._build_url(path)
        headers = self.build_headers(key=key, idempotency_key=idempotency_key, workspace=workspace, live=live)

        response = requests.request(method=method, url=url, headers=headers, data=data, params=params)
        return self.response_handler(response)

    def _build_url(self, path):
        return "%s%s" % (self.base_url, path)

    @staticmethod
    def _generate_params(options: BasicListOptions = None, params=None):
        args = QueryValues()
        if options is not None:
            options.populate(args)
            return args.values.update(params)
        return params

    @staticmethod
    def build_headers(key=None, idempotency_key: str = None, workspace: str = None, live: bool = None):
        if key:
            api_key = key
        else:
            from falu import api_key
            api_key = api_key

        if api_key is None:
            pass
            # TODO: raise error

        headers = {
            "Authorization": "Bearer %s" % api_key,
            "X-Falu-Version": "2022-09-01",
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }

        if idempotency_key is not None:
            headers['X-Idempotency-Key'] = idempotency_key

        if workspace is not None:
            headers['X-Workspace-Id'] = workspace

        live = live is not None and live
        headers['X-Live-Mode'] = str(live)
        return headers

    def response_handler(self, response: Response):
        code = response.status_code
        resource = None

        if response and response.content:
            resource = response.json()

        return self.deserialize_response(code, response.headers, resource)

    @staticmethod
    def deserialize_response(code, headers, resource):
        return deserialize_falu_response(code, headers, resource)

    @classmethod
    def serialize(cls, data: dict):
        return json.dumps(data)
