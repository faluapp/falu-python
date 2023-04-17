import unittest

import responses
from responses import matchers

import falu


class VisitorDestinationTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"
    falu.api_key = "fkst_1234"

    destination = {
        "name": "KIMANI AND CO. ADVOCATES (Suite 3B)",
        "enabled": True,
        "metadata": {
            "property_1": "string",
            "property_2": "string"
        },
        "id": "vdst_602a8dd0a54847479a874de4",
        "created": "2023-04-06T13:16:22Z",
        "updated": "2023-04-06T13:16:22Z",
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_getting_visitor_destinations_works(self):
        resp = responses.get("{}/visits/destinations".format(self.base_url), json=[self.destination],
                             status=200)
        responses.add(resp)

        resources = falu.VisitorDestination.get_destinations()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_getting_visitor_destination_works(self):
        resp = responses.get("{}/visits/destinations/{}".format(self.base_url, "vdst_602a8dd0a54847479a874de4"),
                             json=self.destination, status=200)
        responses.add(resp)

        resources = falu.VisitorDestination.get_destination(destination="vdst_602a8dd0a54847479a874de4")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_adding_visitor_destination_works(self):
        request = {
            "name": "KIMANI AND CO. ADVOCATES (Suite 3B)",
            "enabled": True,
        }

        resp = responses.post(
            "{}/visits/destinations".format(self.base_url),
            json=self.destination,
            match=[matchers.json_params_matcher(request)],
            status=200
        )
        responses.add(resp)

        resource = falu.VisitorDestination.create_destination(data=request)

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_deleting_visitor_destination_works(self):
        resp = responses.delete("{}/visits/destinations/{}".format(self.base_url, "vdst_602a8dd0a54847479a874de4"),
                                json=self.destination, status=200)
        responses.add(resp)

        resource = falu.VisitorDestination.delete_destination(destination="vdst_602a8dd0a54847479a874de4")

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)
