import unittest

import responses
from responses import matchers

import falu


class WebhookEndpointTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"

    endpoint = {
        "events": [
            "customer.created"
        ],
        "description": "This is for my reference",
        "status": "enabled",
        "url": "https://example.com",
        "token": "mF_9.B5f-4.1JqM",
        "metadata": {
            "property_1": "string",
            "property_2": "string"
        },
        "id": "we_0O5fS0eelr0FuJhJBcNeTDuWqE3",
        "created": "2023-04-11T05:48:21Z",
        "updated": "2023-04-11T05:48:21Z",
        "secret": "string",
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_getting_webhook_endpoints_works(self):
        resp = responses.get("{}/webhooks/endpoint".format(self.base_url), json=[self.endpoint],
                             status=200)
        responses.add(resp)

        resources = falu.WebhookEndpoint.get_webhook_endpoints()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_getting_webhook_endpoint_works(self):
        resp = responses.get("{}/webhooks/endpoint/{}".format(self.base_url, "we_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
                             json=self.endpoint, status=200)
        responses.add(resp)

        resources = falu.WebhookEndpoint.get_webhook_endpoint(webhook_endpoint="we_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_adding_webhook_endpoint_works(self):
        request = {
            "events": "customer.created",
            "url": "https://example.com",
        }

        resp = responses.post(
            "{}/webhooks/endpoint".format(self.base_url),
            json=self.endpoint,
            match=[matchers.json_params_matcher(request)],
            status=200
        )
        responses.add(resp)

        resource = falu.WebhookEndpoint.create_webhook_endpoint(data=request)

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_delete_webhook_endpoint_works(self):
        resp = responses.delete(
            "{}/webhooks/endpoint/{}".format(self.base_url, "we_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
            status=200
        )
        responses.add(resp)

        falu.WebhookEndpoint.delete_webhook_endpoint(webhook_endpoint="we_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertEqual(200, resp.status)

    @responses.activate
    def test_roll_webhook_endpoint_works(self):
        request = {
            "ttl": "P1D15M"
        }

        resp = responses.post(
            "{}/webhooks/endpoint/{}".format(self.base_url, "we_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
            json=self.endpoint,
            match=[matchers.json_params_matcher(request)],
            status=200
        )
        responses.add(resp)

        resource = falu.WebhookEndpoint.roll_webhook_endpoint(webhook_endpoint="we_0O5fS0eelr0FuJhJBcNeTDuWqE3",
                                                              data=request)

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)
