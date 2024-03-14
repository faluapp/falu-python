import unittest

import responses

import falu


class WalletTransactionTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"
    falu.api_key = "fkst_1234"

    transaction = {
        "id": "wtxn_0O5fS0eelr0FuJhJBcNeTDuWqE3",
        "created": "2023-04-11T05:38:48Z",
        "updated": "2023-04-11T05:38:48Z",
        "currency": "kes",
        "amount": 0,
        "description": "This is for my reference",
        "exchange_rate": 0,
        "type": "topup",
        "reporting_category": "string",
        "previous": "string",
        "transacted": "2023-04-11T05:38:48Z",
        "reference": "string",
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_getting_wallet_transactions_works(self):
        resp = responses.get("{}/wallet_transactions".format(self.base_url), json=[self.transaction],
                             status=200)
        responses.add(resp)

        resources = falu.WalletTransaction.get_transactions()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_getting_wallet_transaction_works(self):
        resp = responses.get("{}/wallet_transactions/{}".format(self.base_url, "wtxn_0O5fS0eelr0FuJhJBcNeTDuWqE3"),
                             json=self.transaction, status=200)
        responses.add(resp)

        resources = falu.WalletTransaction.get_transaction(transaction="wtxn_0O5fS0eelr0FuJhJBcNeTDuWqE3")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)
