import unittest

import responses
from responses import matchers

import falu


class MessageStreamTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"

    stream = {
        "description": "This is for my reference",
        "metadata": {
            "property_1": "string",
            "property_2": "string"
        },
        "id": "mstr_0O5fS0eelr0FuJhJBcNeTDuWqE3",
        "name": "string",
        "created": "2023-04-05T12:47:21Z",
        "updated": "2023-04-05T12:47:21Z",
        "type": "transactional",
        "archived": "2023-04-05T12:47:21Z",
        "default": True,
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    def test_get_message_streams(self):
        resp = responses.get("{}/message_streams".format(self.base_url), json=[self.stream],
                             status=200)
        responses.add(resp)

        resources = falu.MessageStream.get_message_streams()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_creating_message_stream_works(self):
        request = {
            "name": "Outsider Marketing",
            "type": "transactional"
        }

        resp = responses.post(
            "/message_streams".format(self.base_url),
            json=self.stream,
            match=[matchers.json_params_matcher(request)],
            status=200
        )

        responses.add(resp)

        resource = falu.MessageStream.create_message_stream(data=request)

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_get_message_stream(self):
        resp = responses.get("{}/message_streams/{}".format(self.base_url, "mstr_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
                             json=self.stream, status=200)
        responses.add(resp)

        resources = falu.MessageStream.get_message_stream(stream="mstr_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_delete_message_stream(self):
        resp = responses.delete("{}/message_streams/{}".format(self.base_url, "mstr_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
                                status=200)
        responses.add(resp)

        falu.MessageStream.delete_message_stream(stream="mstr_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertEqual(200, resp.status)

    @responses.activate
    def test_archive_message_stream(self):
        resp = responses.post(
            "{}/message_streams/{}/archive".format(self.base_url, "mstr_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
            status=200
        )
        responses.add(resp)

        falu.MessageStream.archive_message_stream(stream="mstr_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertEqual(200, resp.status)


    @responses.activate
    def test_unarchive_message_stream(self):
        resp = responses.post(
            "{}/message_streams/{}/unarchive".format(self.base_url, "mstr_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
            status=200
        )
        responses.add(resp)

        falu.MessageStream.unarchive_message_stream(stream="mstr_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertEqual(200, resp.status)
