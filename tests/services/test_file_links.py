import datetime
import unittest

import responses
from responses import matchers

import falu
from falu.client.json_patch_document import JsonPatchDocument


class FileLinkTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"
    falu.api_key = "fkst_1234"

    file_link = {
        "metadata": {
            "property_1": "string",
            "property_2": "string"
        },
        "expires": "2023-04-05T07:32:02Z",
        "id": "flnk_0O5fS0eelr0FuJhJBcNeTDuWqE3",
        "created": "2023-04-05T07:32:02Z",
        "updated": "2023-04-05T07:32:02Z",
        "file": "file_602a8dd0a54847479a874de4",
        "url": "https://files.falu.io/v1/links/jfHCcvJ6nFNRpfksm",
        "expired": True,
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_getting_file_links_works(self):
        resp = responses.get("{}/file_links".format(self.base_url), json=[self.file_link], status=200)
        responses.add(resp)

        resource = falu.FileLink.get_file_links()

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_creating_file_link_works(self):
        request = {
            "file": "file_602a8dd0a54847479a874de4",
            "expires": "{}".format(datetime.datetime.now())
        }

        resp = responses.post(
            "{}/file_links".format(self.base_url),
            json=self.file_link,
            match=[matchers.json_params_matcher(request)],
            status=200
        )

        responses.add(resp)

        resource = falu.FileLink.create_file_link(data=request)

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_updating_file_link_works(self):
        document = JsonPatchDocument()
        document.replace("/expires", "2023-04-05T07:32:02Z")

        resp = responses.patch(
            "{}/file_links/{}".format(self.base_url, "flnk_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
            json=self.file_link,
            match=[matchers.json_params_matcher(document.operations)],
            status=200
        )

        responses.add(resp)

        resource = falu.FileLink.update_file_link(link="flnk_0O5fS0eelr0FuJhJBcNeTDuWqE3", document=document)

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_getting_file_link_works(self):
        resp = responses.get("{}/file_links/{}".format(self.base_url, "flnk_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
                             json=self.file_link, status=200)
        responses.add(resp)

        resource = falu.FileLink.get_file_link(link="flnk_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)
