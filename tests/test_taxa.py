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

    def test_can_build_the_table_with_the_results(self):
        self.taxa._content = self.mocked_response['taxas']
        self.taxa._build_table(self.taxa._content)

        self.assertIsNotNone(self.taxa._table)

        self.assertEqual(len(self.taxa._table.columns), 2)
        self.assertEqual(len(self.taxa._table.rows), 2)

        self.assertEqual(self.taxa._table.columns[0].header, 'Taxa')
        self.assertEqual(self.taxa._table.columns[1].header, 'Valor')

    def test_can_display_the_table_on_console(self):
        self.taxa._content = self.mocked_response['taxas']
        self.taxa._build_table(self.taxa._content)
        with patch('core.taxa.Console.print') as mocked_print:
            self.taxa._show_table()
            mocked_print.assert_called_once()


if __name__ == '__main__':
    unittest.main()
