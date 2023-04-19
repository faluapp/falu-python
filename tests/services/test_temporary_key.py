import unittest

import responses
from responses import matchers

import falu


class TemporaryKeyTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"
    falu.api_key = "fkst_1234"

    key = {
        'id': 'key_2oDiYsWsqjSYZXFZAjyAHBgPRHu',
        'created': '2023-04-19T06:04:46.3288263+00:00',
        'objects': ['idv_2oDiYsHV1KIBAIn5BL1RFL2Gpa2'],
        'expires': '2023-04-19T07:04:46.3288263+00:00',
        'secret': 'ftkt_4kAjRQC2peXNLhT4EIvtMewrKes8XHMUsm',
        'workspace': 'wksp_602cd2747409e867a240d7c7',
        'live': False
    }

    @responses.activate
    def test_create_temporary_key_works(self):
        request = {
            "identity_verification": "idv_2oDiYsHV1KIBAIn5BL1RFL2Gpa2"
        }

        resp = responses.post(
            "{}/temporary_keys".format(self.base_url),
            json=self.key,
            match=[matchers.json_params_matcher(request)],
            status=200
        )

        responses.add(resp)

        resource = falu.TemporaryKey.create_temporary_key(data=request)

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)
