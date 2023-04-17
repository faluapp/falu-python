import unittest

import responses
from responses import matchers

import falu


class TerminalConfigurationTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"
    falu.api_key = "fkst_1234"

    config = {
        "description": "This is for my reference",
        "sz_joan_c50": {
            "splash_screen": "file_602a8dd0a54847479a874de4"
        },
        "id": "tcfg_602a8dd0a54847479a874de4",
        "created": "2023-04-06T08:39:06Z",
        "updated": "2023-04-06T08:39:06Z",
        "default": True,
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_getting_terminal_configs_works(self):
        resp = responses.get("{}/terminals/configurations".format(self.base_url), json=[self.config],
                             status=200)
        responses.add(resp)

        resources = falu.TerminalConfiguration.get_configurations()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_getting_terminal_config_works(self):
        resp = responses.get("{}/terminals/configurations/{}".format(self.base_url, "tcfg_602a8dd0a54847479a874de4"),
                             json=[self.config], status=200)
        responses.add(resp)

        resources = falu.TerminalConfiguration.get_configuration(config="tcfg_602a8dd0a54847479a874de4")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_adding_terminal_config_works(self):
        request = {
            "sz_joan_c50": {
                "splash_screen": "file_602a8dd0a54847479a874de4"
            }
        }

        resp = responses.post(
            "{}/terminals/configurations".format(self.base_url),
            json=self.config,
            match=[matchers.json_params_matcher(request)],
            status=200
        )
        responses.add(resp)

        resource = falu.TerminalConfiguration.create_configuration(data=request)

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_deleting_terminal_config_works(self):
        resp = responses.delete("{}/terminals/configurations/{}".format(self.base_url, "tcfg_602a8dd0a54847479a874de4"),
                                status=200)
        responses.add(resp)

        falu.TerminalConfiguration.delete_configuration(config="tcfg_602a8dd0a54847479a874de4")

        self.assertEqual(200, resp.status)
