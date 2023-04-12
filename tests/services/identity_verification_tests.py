import unittest

import responses
from responses import matchers

import falu
from falu.client.json_patch_document import JsonPatchDocument


class IdentityVerificationTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"

    identity_verification = {
        "description": "This is for my reference",
        "metadata": {
            "property_1": "string",
            "property_2": "string"
        },
        "id": "idv_0O5fS0eelr0FuJhJBcNeTDuWqE3",
        "created": "2023-04-04T13:49:03Z",
        "updated": "2023-04-04T13:49:03Z",
        "status": "input_required",
        "type": "id_number",
        "options": {
            "countries": [
                "ken",
                "uga",
                "tza"
            ],
            "allow_uploads": True,
            "document": {
                "allowed": [
                    "driving_license"
                ]
            },
            "video": {
                "poses": [
                    "blink",
                    "nod"
                ],
                "recital": 102
            }
        },
        "customer": "cust_602a8dd0a54847479a874de4",
        "client_secret": "idv_0O5fS0eelr0FuJhJBcNeTDuWqE3_secret_test_1dhDoi1oJYTsZSA8tblyEEXqXz11IMV3mx",
        "url": "https://verify.falu.io/start/test_1dhDoi1oJYTsZSA8tblyEEXqXz11IMV3mx",
        "reports": [
            "idvr_0O5fS0eelr0FuJhJBcNeTDuWqE3"
        ],
        "error": {
            "code": "consent_declined",
            "description": "string"
        },
        "outputs": {
            "id_number_type": "string",
            "id_number": "123456789",
            "issuer": "ken",
            "first_name": "JOHN",
            "last_name": "KAMAU",
            "other_names": [
                "ONYANGO"
            ],
            "birthday": "1989-10-20T00:00:00.0000000+00:00",
            "address": {
                "line1": "14 Riverside Drive",
                "line2": "Block B3, Suite 1Z3",
                "city": "Nairobi",
                "postal_code": "00100",
                "state": "Nairobi",
                "country": "Kenya"
            },
            "sex": "string"
        },
        "redaction": {
            "status": "redacted"
        },
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_getting_identity_verifications_works(self):
        resp = responses.get("{}/identity/verifications".format(self.base_url), json=[self.identity_verification],
                             status=200)
        responses.add(resp)

        resources = falu.IdentityVerification.get_identity_verifications()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_adding_identity_verifications_works(self):
        request = {
            "type": "id_number",
            "return_url": "https://example.com",
            "options": {
                "countries": [
                    "ken",
                    "uga",
                    "tza"
                ],
                "allow_uploads": True,
                "document": {
                    "allowed": [
                        "driving_license"
                    ]
                },
                "video": {
                    "poses": [
                        "blink",
                        "nod"
                    ],
                    "recital": 102
                }
            },
        }

        resp = responses.post(
            "{}/identity/verifications".format(self.base_url),
            json=self.identity_verification,
            match=[matchers.json_params_matcher(request)],
            status=200
        )
        responses.add(resp)

        resource = falu.IdentityVerification.create_identity_verification(data=request)

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_updating_identity_verifications_works(self):
        document = JsonPatchDocument()
        document.replace("/description", "This is for my reference")

        resp = responses.patch(
            "{}/identity/verifications/{}".format(self.base_url, "idv_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
            json=self.identity_verification,
            match=[matchers.json_params_matcher(document.operations)],
            status=200
        )
        responses.add(resp)

        resource = falu.IdentityVerification.update_identity_verification(
            verification="idv_0O5fS0eelr0FuJhJBcNeTDuWqE3", document=document
        )

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_getting_identity_verification_works(self):
        resp = responses.get("{}/identity/verifications/{}".format(self.base_url, "idv_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
                             json=[self.identity_verification],
                             status=200)
        responses.add(resp)

        resources = falu.IdentityVerification.get_identity_verification(verification="idv_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_cancel_identity_verification_works(self):
        resp = responses.post(
            "{}/identity/verifications/{}/cancel".format(self.base_url, "idv_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
            json=self.identity_verification,
            status=200
        )

        responses.add(resp)

        resources = falu.IdentityVerification.cancel_identity_verification(
            verification="idv_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_redact_identity_verification_works(self):
        resp = responses.post(
            "{}/identity/verifications/{}/redact".format(self.base_url, "idv_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
            json=self.identity_verification,
            status=200
        )

        responses.add(resp)

        resources = falu.IdentityVerification.redact_identity_verification(
            verification="idv_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)
