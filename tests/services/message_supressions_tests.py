import unittest

import responses
from responses import matchers

import falu


class MessageSuppressionTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"

    suppression = {
        "id": "msup_0O5fS0eelr0FuJhJBcNeTDuWqE3",
        "created": "2023-04-06T05:06:18Z",
        "updated": "2023-04-06T05:06:18Z",
        "stream": "mstr_602a8dd0a54847479a874de4",
        "to": "+254722000000",
        "origin": "recipient",
        "reason": "spam_complaint",
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_getting_message_suppressions_works(self):
        resp = responses.get("{}/message_suppressions".format(self.base_url), json=[self.suppression],
                             status=200)
        responses.add(resp)

        resources = falu.MessageSuppressions.get_message_suppressions()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_create_message_suppression_works(self):
        request = {
            "to": "+254722000000",
            "stream": "transactional"
        }

        resp = responses.post(
            "{}/message_suppressions".format(self.base_url),
            json=self.suppression,
            match=[matchers.json_params_matcher(request)],
            status=200
        )

        responses.add(resp)

        resource = falu.MessageSuppressions.create_message_suppression(data=request)

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_getting_message_suppression_works(self):
        resp = responses.get("{}/message_suppressions/{}".format(self.base_url, "msup_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
                             json=[self.suppression], status=200)
        responses.add(resp)

        resource = falu.MessageSuppressions.get_message_suppression(suppression="msup_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_deleting_message_suppression_works(self):
        resp = responses.delete("{}/message_suppressions/{}".format(self.base_url, "msup_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
                                json=[self.suppression], status=200)
        responses.add(resp)

        resource = falu.MessageSuppressions.delete_message_suppression(suppression="msup_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)
