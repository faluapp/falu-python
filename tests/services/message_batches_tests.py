import unittest

import responses

import falu


class MessageBatchesTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"

    batch = {
        "description": "This is for my reference",
        "metadata": {
            "property_1": "string",
            "property_2": "string"
        },
        "id": "msba_0O5fS0eelr0FuJhJBcNeTDuWqE3",
        "created": "2023-04-05T12:17:10Z",
        "updated": "2023-04-05T12:17:10Z",
        "stream": "mstr_602a8dd0a54847479a874de4",
        "sender": "msdr_602a8dd0a54847479a874de4",
        "schedule": {
            "time": "2023-04-05T12:17:10Z",
            "delay": "P1D15M"
        },
        "messages": [
            "msg_0O5fS0eelr0FuJhJBcNeTDuWqE3"
        ],
        "segments": 0,
        "redaction": {
            "status": "redacted"
        },
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_getting_message_batches(self):
        resp = responses.get("{}/message_batches".format(self.base_url), json=[self.batch],
                             status=200)
        responses.add(resp)

        resources = falu.MessageBatch.get_message_batches()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_getting_message_batch(self):
        resp = responses.get("{}/message_batches/{}".format(self.base_url, "msba_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
                             json=[self.batch], status=200)
        responses.add(resp)

        resources = falu.MessageBatch.get_message_batch("msba_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_getting_message_batch_status(self):
        resp = responses.get("{}/message_batches/{}/status".format(self.base_url, "msba_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
                             json=[self.batch], status=200)
        responses.add(resp)

        resources = falu.MessageBatch.get_status("msba_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_cancel_message_batch_works(self):
        resp = responses.post(
            "{}/message_batches/{}/cancel".format(self.base_url, "msba_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
            json=self.batch,
            status=200
        )

        responses.add(resp)

        resource = falu.MessageBatch.cancel_message_batch(batch_id="msba_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_redact_message_batch_works(self):
        resp = responses.post(
            "{}/message_batches/{}/redact".format(self.base_url, "msba_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
            json=self.batch,
            status=200
        )

        responses.add(resp)

        resource = falu.MessageBatch.redact_message_batch(batch_id="msba_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)
