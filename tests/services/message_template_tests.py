import unittest

import responses
from responses import matchers

import falu


class MessageTemplateTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"

    template = {
        "alias": "otp-v2",
        "description": "This is for my reference",
        "body": "Your OTP code is: {{otp}}",
        "metadata": {
            "property_1": "string",
            "property_2": "string"
        },
        "id": "mtpl_0O5fS0eelr0FuJhJBcNeTDuWqE3",
        "created": "2023-04-06T06:22:46Z",
        "updated": "2023-04-06T06:22:46Z",
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_get_message_templates_works(self):
        resp = responses.get("{}/message_templates".format(self.base_url), json=[self.template],
                             status=200)
        responses.add(resp)

        resources = falu.MessageTemplates.get_message_templates()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_create_message_template_works(self):
        request = {
            "alias": "otp-v2",
            "body": "Your OTP code is: {{otp}}"
        }

        resp = responses.post("{}/message_templates".format(self.base_url), json=self.template,
                              match=[matchers.json_params_matcher(request)], status=200)
        responses.add(resp)

        resources = falu.MessageTemplates.create_message_template(data=request)

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_get_message_template_works(self):
        resp = responses.get("{}/message_templates/{}".format(self.base_url, "mtpl_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
                             json=[self.template], status=200)
        responses.add(resp)

        resources = falu.MessageTemplates.get_message_template(template="mtpl_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_delete_message_template_works(self):
        resp = responses.delete("{}/message_templates/{}".format(self.base_url, "mtpl_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
                                json=[self.template], status=200)
        responses.add(resp)

        resources = falu.MessageTemplates.delete_message_template(template="mtpl_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_validate_message_template_works(self):
        request = {
            "body": "Your OTP code is: {{otp}}",
            "model": {
                "property_1": None
            }
        }

        resp = responses.post("{}/message_templates/validate".format(self.base_url), json=[self.template],
                              match=[matchers.json_params_matcher(request)], status=200)
        responses.add(resp)

        resources = falu.MessageTemplates.validate_message_template(data=request)

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)
