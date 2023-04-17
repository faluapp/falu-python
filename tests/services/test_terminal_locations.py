import unittest

import responses
from responses import matchers

import falu


class TerminalLocationTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"
    falu.api_key = "fkst_1234"

    device = {
        "address": {
            "line1": "14 Riverside Drive",
            "line2": "Block B3, Suite 1Z3",
            "city": "Nairobi",
            "postal_code": "00100",
            "state": "Nairobi",
            "country": "Kenya"
        },
        "name": "My First Building",
        "configuration": "tcfg_602a8dd0a54847479a874de4",
        "metadata": {
            "property_1": "string",
            "property_2": "string"
        },
        "id": "tloc_602a8dd0a54847479a874de4",
        "created": "2023-04-06T10:19:31Z",
        "updated": "2023-04-06T10:19:31Z",
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_getting_terminal_locations_works(self):
        resp = responses.get("{}/terminals/locations".format(self.base_url), json=[self.device],
                             status=200)
        responses.add(resp)

        resources = falu.TerminalLocation.get_terminal_locations()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_getting_terminal_location_works(self):
        resp = responses.get("{}/terminals/locations/{}".format(self.base_url, "tloc_602a8dd0a54847479a874de4"),
                             json=self.device, status=200)
        responses.add(resp)

        resources = falu.TerminalLocation.get_terminal_location(terminal_location="tloc_602a8dd0a54847479a874de4")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_adding_terminal_location_works(self):
        request = {
            "address": {
                "line1": "14 Riverside Drive",
                "line2": "Block B3, Suite 1Z3",
                "city": "Nairobi",
                "postal_code": "00100",
                "state": "Nairobi",
                "country": "Kenya"
            },
            "name": "My First Building",
            "configuration": "tcfg_602a8dd0a54847479a874de4"
        }

        resp = responses.post(
            "{}/terminals/locations".format(self.base_url),
            json=self.device,
            match=[matchers.json_params_matcher(request)],
            status=200
        )
        responses.add(resp)

        resource = falu.TerminalLocation.create_terminal_location(data=request)

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_deleting_terminal_location_works(self):
        resp = responses.delete("{}/terminals/locations/{}".format(self.base_url, "tloc_602a8dd0a54847479a874de4"),
                                status=200)
        responses.add(resp)

        falu.TerminalLocation.delete_terminal_location(terminal_location="tloc_602a8dd0a54847479a874de4")

        self.assertEqual(200, resp.status)
