import unittest

import responses
from responses import matchers

import falu


class TransferTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"

    transfer = {
        "description": "This is for my reference",
        "metadata": {
            "property_1": "string",
            "property_2": "string"
        },
        "id": "tr_0O5fS0eelr0FuJhJBcNeTDuWqE3",
        "amount": 0,
        "currency": "kes",
        "status": "pending",
        "created": "2023-04-06T11:06:47Z",
        "updated": "2023-04-06T11:06:47Z",
        "succeeded": "2023-04-06T11:06:47Z",
        "customer": "cust_602a8dd0a54847479a874de4",
        "type": "mpesa",
        "purpose": "business",
        "mpesa": {
            "business_short_code": "200200",
            "request_id": "AG_20210803_000041754cc615312171",
            "receipt": "PGV520PUFN",
            "destination": "string",
            "charges": 0,
            "receiver": "254722000000 - JOHN KAMAU ONYANGO"
        },
        "error": {
            "code": "unknown",
            "timestamp": "2023-04-06T11:06:47Z",
            "description": "string"
        },
        "reversal": "trr_602a8dd0a54847479a874de4",
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_getting_transfers_works(self):
        resp = responses.get("{}/transfers".format(self.base_url), json=[self.transfer],
                             status=200)
        responses.add(resp)

        resources = falu.Transfer.get_transfers()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_getting_transfer_works(self):
        resp = responses.get("{}/transfers/{}".format(self.base_url, "tr_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
                             json=self.transfer, status=200)
        responses.add(resp)

        resources = falu.Transfer.retrieve_transfer(transfer="tr_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_adding_transfer_works(self):
        request = {
            "currency": "kes",
            "purpose": "business",
            "amount": 1000
        }

        resp = responses.post(
            "{}/transfers".format(self.base_url),
            json=self.transfer,
            match=[matchers.json_params_matcher(request)],
            status=200
        )
        responses.add(resp)

        resource = falu.Transfer.create_transfer(data=request)

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)
