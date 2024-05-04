import unittest
from unittest.mock import patch
from core.cep import Cep


class CepTest(unittest.TestCase):
    def setUp(self):
        self.cep = Cep('01001000')
        self.mocked_response = {
            "cep": "01001-000",
            "logradouro": "Praça da Sé",
            "complemento": "lado ímpar",
            "bairro": "Sé",
            "localidade": "São Paulo",
            "uf": "SP",
            "ibge": "3550308",
            "gia": "1004",
            "ddd": "11",
            "siafi": "7107"
        }

    @patch('core.cep.requests.get')
    def test_can_get_cep_from_api(self, mock_get):
        mock_get.return_value.json.return_value = self.mocked_response

        self.cep._get()

        self.assertIsNotNone(self.cep._content)
        self.assertDictEqual(self.cep._content, self.mocked_response)


if __name__ == '__main__':
    unittest.main()
