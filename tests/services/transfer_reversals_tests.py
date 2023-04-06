import unittest

import responses
from responses import matchers

import falu


class TransferReversalTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"

    reversal = {
        "description": "This is for my reference",
        "metadata": {
            "property_1": "string",
            "property_2": "string"
        },
        "id": "trr_0O5fS0eelr0FuJhJBcNeTDuWqE3",
        "amount": 0,
        "currency": "kes",
        "reason": "duplicate",
        "status": "pending",
        "created": "2023-04-06T10:42:52Z",
        "updated": "2023-04-06T10:42:52Z",
        "succeeded": "2023-04-06T10:42:52Z",
        "customer": "cust_602a8dd0a54847479a874de4",
        "transfer": "tr_602a8dd0a54847479a874de4",
        "mpesa": {
            "business_short_code": "200200",
            "request_id": "AG_20210803_000041754cc615312171",
            "receipt": "PGV520PUFN"
        },
        "error": {
            "code": "unknown",
            "timestamp": "2023-04-06T10:42:52Z",
            "description": "string"
        },
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_getting_transfer_reversals_works(self):
        resp = responses.get("{}/transfer_reversal".format(self.base_url), json=[self.reversal],
                             status=200)
        responses.add(resp)

        resources = falu.TransferReversal.get_transfer_reversals()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_getting_transfer_reversal_works(self):
        resp = responses.get("{}/transfer_reversal/{}".format(self.base_url, "trr_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
                             json=self.reversal, status=200)
        responses.add(resp)

        resources = falu.TransferReversal.retrieve_transfer_reversal(reversal="trr_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_adding_transfer_reversal_works(self):
        request = {
            "transfer": "tr_602a8dd0a54847479a874de4",
            "reason": "duplicate",
        }

        resp = responses.post(
            "{}/transfer_reversal".format(self.base_url),
            json=self.reversal,
            match=[matchers.json_params_matcher(request)],
            status=200
        )
        responses.add(resp)

        resource = falu.TransferReversal.create_transfer_reversal(data=request)

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)
