import unittest

import responses
from responses import matchers

import falu


class MessageSuppressionTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"

    message = {
        "metadata": {
            "property_1": "string",
            "property_2": "string"
        },
        "id": "msg_0O5fS0eelr0FuJhJBcNeTDuWqE3",
        "created": "2023-04-06T05:44:43Z",
        "updated": "2023-04-06T05:44:43Z",
        "status": "accepted",
        "type": "sms",
        "from": "string",
        "to": "+254722000000",
        "body": "string",
        "template": {
            "id": "mtpl_602a8dd0a54847479a874de4",
            "model": {
                "property_1": None,
                "property_2": None
            }
        },
        "media": [
            {
                "url": "https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg",
                "file": "file_602a8dd0a54847479a874de4",
                "type": "image/jpeg",
                "size": 167802
            }
        ],
        "stream": "mstr_602a8dd0a54847479a874de4",
        "sender": "msdr_602a8dd0a54847479a874de4",
        "batch": "msba_602a8dd0a54847479a874de4",
        "customer": "cust_602a8dd0a54847479a874de4",
        "segments": 0,
        "schedule": {
            "time": "2023-04-06T05:44:43Z",
            "delay": "P1D15M"
        },
        "sent": "2023-04-06T05:44:43Z",
        "error": {
            "code": "blocked",
            "timestamp": "2023-04-06T05:44:43Z",
            "description": "string"
        },
        "delivered": "2023-04-06T05:44:43Z",
        "redaction": {
            "status": "redacted"
        },
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_getting_messages_works(self):
        resp = responses.get("{}/messages".format(self.base_url), json=[self.message],
                             status=200)
        responses.add(resp)

        resources = falu.Messages.get_messages()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_sending_messages_works(self):
        request = {
            "to": "+254722000000",
            "stream": "transactional",
            "body": "Welcome home John!"
        }

        resp = responses.post(
            "{}/messages".format(self.base_url),
            json=self.message,
            match=[matchers.json_params_matcher(request)],
            status=200
        )

        responses.add(resp)

        resource = falu.Messages.send_message(data=request)

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_getting_message_works(self):
        resp = responses.get("{}/messages/{}".format(self.base_url, "msg_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
                             json=[self.message], status=200)
        responses.add(resp)

        resources = falu.Messages.get_message(message_id="msg_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_canceling_message_works(self):
        resp = responses.post("{}/messages/{}/cancel".format(self.base_url, "msg_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
                              json=[self.message], status=200)
        responses.add(resp)

        resources = falu.Messages.cancel_message(message_id="msg_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)
