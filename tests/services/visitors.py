import unittest

import responses
from responses import matchers

import falu


class VisitorTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"

    visitor = {
        "phones": [
            "+254722000000"
        ],
        "metadata": {
            "property_1": "string",
            "property_2": "string"
        },
        "id": "vstr_602a8dd0a54847479a874de4",
        "created": "2023-04-11T04:39:07Z",
        "updated": "2023-04-11T04:39:07Z",
        "verification": "idv_602a8dd0a54847479a874de4",
        "documents": [
            {
                "type": "string",
                "number": "string",
                "issuer": "string",
                "full_name": "string"
            }
        ],
        "birthday": "2023-04-11T04:39:07Z",
        "sex": "string",
        "full_name": "string",
        "redaction": {
            "status": "redacted"
        },
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_getting_visitors_works(self):
        resp = responses.get("{}/visits/visitors".format(self.base_url), json=[self.visitor],
                             status=200)
        responses.add(resp)

        resources = falu.Visitor.get_visitors()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_getting_visitor_works(self):
        resp = responses.get("{}/visits/visitors/{}".format(self.base_url, "vstr_602a8dd0a54847479a874de4"),
                             json=self.visitor, status=200)
        responses.add(resp)

        resources = falu.Visitor.get_visitor(visitor="vstr_602a8dd0a54847479a874de4")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_adding_visitor_works(self):
        request = {
            "verification": "idv_602a8dd0a54847479a874de4",
            "phones": [
                "+254722000000"
            ],
        }

        resp = responses.post(
            "{}/visits/visitors".format(self.base_url),
            json=self.visitor,
            match=[matchers.json_params_matcher(request)],
            status=200
        )
        responses.add(resp)

        resource = falu.Visitor.create_visitor(data=request)

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_deleting_visitor_works(self):
        resp = responses.delete("{}/visits/visitors/{}".format(self.base_url, "vstr_602a8dd0a54847479a874de4"),
                                json=self.visitor, status=200)
        responses.add(resp)

        resource = falu.Visitor.delete_visitor(visitor="vstr_602a8dd0a54847479a874de4")

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_redact_visitor_works(self):
        resp = responses.post(
            "{}/visits/visitors/{}/redact".format(self.base_url, "vstr_602a8dd0a54847479a874de4"),
            json=self.visitor,
            status=200
        )
        responses.add(resp)

        resource = falu.Visitor.redact_visitor(visitor="vstr_602a8dd0a54847479a874de4")

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)
