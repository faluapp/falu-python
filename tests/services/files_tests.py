import unittest

import responses
from responses import matchers

import falu


class FileTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"

    file = {
        "id": "file_0O5fS0eelr0FuJhJBcNeTDuWqE3",
        "created": "2023-04-05T11:25:31Z",
        "updated": "2023-04-05T11:25:31Z",
        "description": "This is for my reference",
        "purpose": "business.icon",
        "type": "image/png",
        "filename": "string",
        "size": 0,
        "hashes": {
            "md5": "string",
            "sha256": "string"
        },
        "expires": "2023-04-05T11:25:31Z",
        "redaction": {
            "status": "redacted"
        },
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_getting_files_works(self):
        resp = responses.get("{}/files".format(self.base_url), json=[self.file], status=200)
        responses.add(resp)

        resource = falu.File.get_files()

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_file_uploads_works(self):
        request = {"file": "cake"}

        resp = responses.post(
            "{}/files".format(self.base_url),
            json=self.file,
            match=[matchers.multipart_matcher(request)],
            status=200
        )
        responses.add(resp)

        resources = falu.File.upload_files(data=request)

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_getting_file_works(self):
        resp = responses.get("{}/files/{}".format(self.base_url, "file_0O5fS0eelr0FuJhJBcNeTDuWqE3"), json=self.file,
                             status=200)
        responses.add(resp)

        resource = falu.File.get_file(file="file_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_redacting_file_works(self):
        resp = responses.post("{}/files/{}/redact".format(self.base_url, "file_0O5fS0eelr0FuJhJBcNeTDuWqE3"), json=self.file,
                             status=200)
        responses.add(resp)

        resource = falu.File.redact_file(file="file_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)
