import unittest

import responses
from responses import matchers

import falu


class PaymentTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"
    falu.api_key = "fkst_1234"

    payment = {
        "description": "This is for my reference",
        "metadata": {
            "property_1": "string",
            "property_2": "string"
        },
        "id": "pa_0O5fS0eelr0FuJhJBcNeTDuWqE3",
        "amount": 0,
        "currency": "kes",
        "status": "pending",
        "created": "2023-04-06T07:07:42Z",
        "updated": "2023-04-06T07:07:42Z",
        "succeeded": "2023-04-06T07:07:42Z",
        "customer": "cust_602a8dd0a54847479a874de4",
        "authorization": "pauth_602a8dd0a54847479a874de4",
        "type": "mpesa",
        "mpesa": {
            "business_short_code": "200200",
            "request_id": "AG_20210803_000041754cc615312171",
            "receipt": "PGV520PUFN",
            "type": "Paybill",
            "reference": "INV-2020-12-01-1234",
            "phone": "+254722000000",
            "payer": "JOHN KAMAU ONYANGO"
        },
        "error": {
            "code": "unknown",
            "timestamp": "2023-04-06T07:07:42Z",
            "description": "string"
        },
        "refund": "pr_602a8dd0a54847479a874de4",
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_getting_payments_works(self):
        resp = responses.get("{}/payments".format(self.base_url), json=self.payment, status=200)
        responses.add(resp)

        resources = falu.Payment.get_payments()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_getting_a_payment_works(self):
        resp = responses.get("{}/payments/{}".format(self.base_url, "pa_0O5fS0eelr0FuJhJBcNeTDuWqE3"), json=self.payment,
                             status=200)
        responses.add(resp)

        resources = falu.Payment.get_payment(payment="pa_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_create_payment_works(self):
        request = {
            "amount": 1000,
            "currency": "kes",
            "mpesa": {
                "phone": "+254722000000",
                "reference": "INV-2020-12-01-1234",
                "destination": "200200"
            },
            "customer": "cust_602a8dd0a54847479a874de4"
        }

        resp = responses.post(
            "{}/payments".format(self.base_url),
            json=self.payment,
            match=[matchers.json_params_matcher(request)],
            status=200
        )

        responses.add(resp)

        resource = falu.Payment.create_payment(data=request)

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)
