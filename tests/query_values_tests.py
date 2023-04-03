import unittest

import requests

from falu.list_options import BasicListOptions
from falu.query_values import QueryValues


class QueryValuesTests(unittest.TestCase):

    def test_query_is_generated(self):
        params = {
            "sort": "descending",
            "count": 100,
            "ct": 10,
            "age.lt": 40,
            "created.gt": "2021-03-10T19:41:25.0000000+03:00"
        }

        values = QueryValues(params)

        r = requests.get("https://example.com/test", params=values.values)
        self.assertEqual(
            "https://example.com/test?sort=descending&count=100&ct=10&age.lt=40&created.gt=2021-03-10T19%3A41%3A25.0000000%2B03%3A00",
            r.url
        )

    def test_basic_list_options(self):
        options = BasicListOptions(
            sorting="descending",
            count=12,
        )

        query = QueryValues()
        options.populate(query)

        self.assertFalse(len(query.values) < 0)
        self.assertEqual(["sort", "count"], list(query.get_keys()))

    def test_multiple_query_values(self):
        params = {
            "sort": "descending",
            "count": 100,
            "ct": 10,
            "age.lt": 40,
            "type": ["transfer.created", "transfer.failed", "transfer.succeeded"]
        }

        values = QueryValues(params)

        r = requests.get("https://example.com/test", params=values.values)
        self.assertEqual(
            'https://example.com/test?sort=descending&count=100&ct=10&age.lt=40&type=transfer.created&type=transfer.failed&type=transfer.succeeded',
            r.url
        )