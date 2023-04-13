import json
import unittest

from falu.client.json_patch_document import JsonPatchDocument


class JsonPatchDocumentTests(unittest.TestCase):

    def test_patch_document_generated(self):
        document = JsonPatchDocument()
        document.add(path="/amount", value=100)
        document.replace(path="/isVerified", value="verified")

        operations = document.operations

        self.assertEqual(
            '[{"op": "add", "path": "/amount", "value": 100}, {"op": "replace", "path": "/isVerified", "value": "verified"}]',
            json.dumps(operations)
        )
