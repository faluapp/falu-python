import unittest

import responses

import falu


class WalletTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"

    wallet = {
        "created": "2023-04-11T05:35:10Z",
        "updated": "2023-04-11T05:35:10Z",
        "actual_balance": 0,
        "available_balance": 0,
        "last_transaction": "string",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_getting_wallet_works(self):
        resp = responses.get("{}/wallet".format(self.base_url), json=self.wallet,
                             status=200)
        responses.add(resp)

        resources = falu.Wallet.get_wallet()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)
