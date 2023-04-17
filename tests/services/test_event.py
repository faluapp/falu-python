import unittest

import responses

import falu


class EventTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"
    falu.api_key = "fkst_1234"

    event = {
        "id": "evt_0O5fS0eelr0FuJhJBcNeTDuWqE3",
        "created": "2023-04-05T06:45:16Z",
        "updated": "2023-04-05T06:45:16Z",
        "type": "customer.created",
        "request": {
            "id": "req_0O5fS0eelr0FuJhJBcNeTDuWqE3",
            "idempotency_key": "string"
        },
        "data": {
            "object": {
                "property_1": None,
                "property_2": None
            },
            "previous": {
                "property_1": None,
                "property_2": None
            }
        },
        "redaction": {
            "status": "redacted"
        },
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True
    }

    @responses.activate
    def test_getting_events_works(self):
        resp = responses.get("{}/events".format(self.base_url), json=[self.event], status=200)
        responses.add(resp)

        resource = falu.Event.get_events()

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_getting_event_works(self):
        resp = responses.get("{}/events/{}".format(self.base_url, "evt_0O5fS0eelr0FuJhJBcNeTDuWqE3"), json=self.event,
                             status=200)
        responses.add(resp)

        resource = falu.Event.get_event(event="evt_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)
        #self.assertEqual(resource.id, 'evt_0O5fS0eelr0FuJhJBcNeTDuWqE3')
