import unittest

import responses
from responses import matchers

import falu


class PaymentAuthorizationTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"

    authorization = {
        "metadata": {
            "property_1": "string",
            "property_2": "string"
        },
        "id": "pauth_0O5fS0eelr0FuJhJBcNeTDuWqE3",
        "amount": 0,
        "currency": "kes",
        "approved": True,
        "status": "pending",
        "reason": "default",
        "created": "2023-04-06T07:48:45Z",
        "updated": "2023-04-06T07:48:45Z",
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
        "payment": "pa_602a8dd0a54847479a874de4",
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_getting_payment_authorizations_works(self):
        resp = responses.get("{}/payments_authorizations".format(self.base_url), json=[self.authorization], status=200)
        responses.add(resp)

        resources = falu.PaymentAuthorization.get_payment_authorizations()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_getting_payment_authorization_works(self):
        resp = responses.get("{}/payments_authorizations/{}".format(self.base_url, "pauth_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
                             json=self.authorization, status=200)
        responses.add(resp)

        resources = falu.PaymentAuthorization.get_payment_authorization(
            payment_authorization="pauth_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_approve_payment_authorization_works(self):
        request = {
            "metadata": {
                "property_1": "string",
                "property_2": "string"
            }
        }
        resp = responses.post(
            "{}/payments_authorizations/{}/approve".format(self.base_url, "pauth_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
            match=[matchers.json_params_matcher(request)], json=self.authorization, status=200
        )
        responses.add(resp)

        resources = falu.PaymentAuthorization.approve_payment_authorization(
            payment_authorization="pauth_0O5fS0eelr0FuJhJBcNeTDuWqE3", data=request
        )

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_decline_payment_authorization_works(self):
        request = {
            "metadata": {
                "property_1": "string",
                "property_2": "string"
            }
        }
        resp = responses.post(
            "{}/payments_authorizations/{}/decline".format(self.base_url, "pauth_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
            match=[matchers.json_params_matcher(request)], json=self.authorization, status=200
        )
        responses.add(resp)

        resources = falu.PaymentAuthorization.decline_payment_authorization(
            payment_authorization="pauth_0O5fS0eelr0FuJhJBcNeTDuWqE3", data=request
        )

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)
