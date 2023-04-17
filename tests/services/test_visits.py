import unittest

import responses
from responses import matchers

import falu


class VisitsTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"
    falu.api_key = "fkst_1234"

    visit = {
        "metadata": {
            "property_1": "string",
            "property_2": "string"
        },
        "id": "vst_602a8dd0a54847479a874de4",
        "created": "2023-04-11T05:06:40Z",
        "updated": "2023-04-11T05:06:40Z",
        "status": "pending",
        "visitor_destination": "vdst_602a8dd0a54847479a874de4",
        "visitor": "vstr_602a8dd0a54847479a874de4",
        "entry": {
            "time": "2023-04-11T05:06:40Z",
            "terminal": "tdev_602a8dd0a54847479a874de4",
            "user": "string"
        },
        "document_type": "driving_license",
        "document_number": "string",
        "phone": "+254722000000",
        "exit": {
            "time": "2023-04-11T05:06:40Z",
            "terminal": "tdev_602a8dd0a54847479a874de4",
            "user": "string"
        },
        "redaction": {
            "status": "redacted"
        },
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_getting_visits_works(self):
        resp = responses.get("{}/visits/visits".format(self.base_url), json=[self.visit],
                             status=200)
        responses.add(resp)

        resources = falu.Visit.get_visits()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_getting_visit_works(self):
        resp = responses.get("{}/visits/visits/{}".format(self.base_url, "vst_602a8dd0a54847479a874de4"),
                             json=self.visit, status=200)
        responses.add(resp)

        resources = falu.Visit.get_visit(visit="vst_602a8dd0a54847479a874de4")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_adding_visit_works(self):
        request = {
            "visitor_destination": "vdst_602a8dd0a54847479a874de4",
            "visitor": "vstr_602a8dd0a54847479a874de4",
        }

        resp = responses.post(
            "{}/visits/visits".format(self.base_url),
            json=self.visit,
            match=[matchers.json_params_matcher(request)],
            status=200
        )
        responses.add(resp)

        resource = falu.Visit.create_visit(data=request)

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_start_visit_works(self):
        request = {
            "visitor_destination": "vdst_602a8dd0a54847479a874de4",
            "time": ""
        }

        resp = responses.post(
            "{}/visits/visits/{}/start".format(self.base_url, "vst_602a8dd0a54847479a874de4"),
            json=self.visit,
            status=200
        )
        responses.add(resp)

        resource = falu.Visit.start_visit(visit="vst_602a8dd0a54847479a874de4", data=request)

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_end_visit_works(self):
        request = {
            "time": ""
        }

        resp = responses.post(
            "{}/visits/visits/{}/end".format(self.base_url, "vst_602a8dd0a54847479a874de4"),
            json=self.visit,
            status=200
        )
        responses.add(resp)

        resource = falu.Visit.end_visit(visit="vst_602a8dd0a54847479a874de4", data=request)

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_redact_visit_works(self):
        resp = responses.post(
            "{}/visits/visits/{}/redact".format(self.base_url, "vst_602a8dd0a54847479a874de4"),
            json=self.visit,
            status=200
        )
        responses.add(resp)

        resource = falu.Visit.redact_visit(visit="vst_602a8dd0a54847479a874de4")

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)
