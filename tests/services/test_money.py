import unittest

import responses

import falu


class MoneyTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"
    falu.api_key = "fkst_1234"

    money = {
        "created": "2023-04-06T06:59:43Z",
        "updated": "2023-04-06T06:59:43Z",
        "mpesa": {
            "property_1": 0,
            "property_2": 0
        },
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_get_money_balance_works(self):
        resp = responses.get("{}/money_balances".format(self.base_url),
                             json=self.money, status=200)
        responses.add(resp)

        resources = falu.Money.get_money_balance()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_force_money_balance_refresh_works(self):
        resp = responses.post("{}/money_balances/refresh".format(self.base_url), json=self.money, status=200)
        responses.add(resp)

        resources = falu.Money.force_balance_refresh()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)
