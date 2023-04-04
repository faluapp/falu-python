import unittest

import responses

import falu


class IdentityVerificationReportTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"

    report = {
        "id": "idvr_0O5fS0eelr0FuJhJBcNeTDuWqE3",
        "verification": "idv_602a8dd0a54847479a874de4",
        "created": "2023-04-04T12:36:23Z",
        "updated": "2023-04-04T12:36:23Z",
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
        "consent": {
            "date": "2023-04-04T12:36:23Z",
            "ip": "::ffff:127.0.0.1",
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
        },
        "id_number": {
            "error": {
                "code": "id_number_unverified_other",
                "timestamp": "2023-04-04T12:36:23Z",
                "description": "string"
            },
            "verified": True,
            "id_number_type": "string",
            "id_number": "123456789",
            "issuer": "ken",
            "first_name": "JOHN",
            "last_name": "KAMAU",
            "other_names": [
                "ONYANGO"
            ],
            "birthday": "1989-10-20T00:00:00.0000000+00:00",
            "sex": "M"
        },
        "document": {
            "error": {
                "code": "document_expired",
                "timestamp": "2023-04-04T12:36:23Z",
                "description": "string"
            },
            "verified": True,
            "expiry": "2025-10-20T00:00:00.0000000+00:00",
            "issued": "2020-10-20T00:00:00.0000000+00:00",
            "issuer": "ken",
            "nationality": "ken",
            "type": "driving_license",
            "id_card_type": "civilian",
            "passport_type": "civilian",
            "number": "string",
            "personal_number": "string",
            "first_name": "JOHN",
            "last_name": "KAMAU",
            "other_names": [
                "ONYANGO"
            ],
            "sex": "M",
            "birthday": "1989-10-20T00:00:00.0000000+00:00",
            "address": {
                "line1": "14 Riverside Drive",
                "line2": "Block B3, Suite 1Z3",
                "city": "Nairobi",
                "postal_code": "00100",
                "state": "Nairobi",
                "country": "Kenya"
            },
            "driving_license_categories": [
                {
                    "category": "C1",
                    "issued": "2020-10-20T00:00:00.0000000+00:00",
                    "expires": "2025-10-20T00:00:00.0000000+00:00"
                }
            ],
            "issuing_authority": "string",
            "files": [
                "file_602a8dd0a54847479a874de4",
                "file_602a8dd0a54847479a874de4"
            ]
        },
        "selfie": {
            "error": {
                "code": "selfie_document_missing_photo",
                "timestamp": "2023-04-04T12:36:23Z",
                "description": "string"
            },
            "verified": True,
            "document": "file_602a8dd0a54847479a874de4",
            "selfie": "file_602a8dd0a54847479a874de4"
        },
        "video": {
            "error": {
                "code": "video_document_missing_photo",
                "timestamp": "2023-04-04T12:36:23Z",
                "description": "string"
            },
            "verified": True,
            "document": "file_602a8dd0a54847479a874de4",
            "video": "file_602a8dd0a54847479a874de4",
            "portrait": "file_602a8dd0a54847479a874de4"
        },
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_getting_identity_verification_reports_works(self):
        resp = responses.get("{}/identity/verification_reports".format(self.base_url), json=[self.report], status=200)
        responses.add(resp)

        resources = falu.IdentityVerificationReport.get_identity_verification_reports()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)
