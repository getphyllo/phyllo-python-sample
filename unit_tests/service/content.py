import unittest
from unittest.mock import patch
from app.services.content import get_all, get_by_id


class TestContent(unittest.TestCase):
    @patch('app.utils.phyllo_api.content.requests.get')
    def test_get_all_content(self, mock_api):
        mock_api.return_value = {"status": 200, "body": ""}
        result = get_all({"offset": 0, "limit": 1})
        self.assertEqual(result, {"status": 200,
                                  "body": ""})

    @patch('app.utils.phyllo_api.content.requests.get')
    def test_get_by_id_content(self, mock_api):
        expected_value = {"status": 400, "body": "Bad request"}
        mock_api.return_value = expected_value
        result = get_by_id(id="test_id")
        self.assertEqual(result, expected_value)
