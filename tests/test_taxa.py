import unittest
from unittest.mock import patch
from core.taxa import Taxa


class TestTaxa(unittest.TestCase):
    def setUp(self):
        self.taxa = Taxa()
        self.mocked_response = {
            'taxas': [
                {'nome': 'SELIC', 'valor': 2.25},
                {'nome': 'CDI', 'valor': 2.15}
            ]
        }

    @patch('core.taxa.requests.get')
    def test_can_get_taxa_from_api(self, mock_get):
        mock_get.return_value.json.return_value = self.mocked_response

        self.taxa._get()

        self.assertIsNotNone(self.taxa._content)
        self.assertDictEqual(self.taxa._content, self.mocked_response)


if __name__ == '__main__':
    unittest.main()
