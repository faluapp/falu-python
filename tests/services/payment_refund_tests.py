import unittest

import responses
from responses import matchers

import falu


class PaymentRefundTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"

    refund = {
        "description": "This is for my reference",
        "metadata": {
            "property_1": "string",
            "property_2": "string"
        },
        "id": "pr_0O5fS0eelr0FuJhJBcNeTDuWqE3",
        "amount": 0,
        "currency": "kes",
        "reason": "duplicate",
        "status": "pending",
        "created": "2023-04-06T08:17:15Z",
        "updated": "2023-04-06T08:17:15Z",
        "succeeded": "2023-04-06T08:17:15Z",
        "customer": "cust_602a8dd0a54847479a874de4",
        "payment": "pa_602a8dd0a54847479a874de4",
        "mpesa": {
            "business_short_code": "200200",
            "request_id": "AG_20210803_000041754cc615312171",
            "receipt": "PGV520PUFN"
        },
        "error": {
            "code": "unknown",
            "timestamp": "2023-04-06T08:17:15Z",
            "description": "string"
        },
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_getting_payment_refunds_works(self):
        resp = responses.get("{}/payment_refunds".format(self.base_url), json=[self.refund], status=200)
        responses.add(resp)

        resources = falu.PaymentRefund.get_payment_refunds()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_getting_payment_refund_works(self):
        resp = responses.get("{}/payment_refunds/{}".format(self.base_url, "pr_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
                             json=[self.refund], status=200)
        responses.add(resp)

        resources = falu.PaymentRefund.retrieve_payment_refund(refund="pr_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_create_payment_refund_works(self):
        request = {
            "payment": "pa_602a8dd0a54847479a874de4",
            "reason": "customer_requested"
        }
        resp = responses.post(
            "{}/payment_refunds".format(self.base_url),
            match=[matchers.json_params_matcher(request)],
            json=[self.refund],
            status=200
        )
        responses.add(resp)

        resources = falu.PaymentRefund.create_payment_refund(data=request)

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)
