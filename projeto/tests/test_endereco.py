import unittest
from projeto.models.endereco import Endereco

class TestEndereco(unittest.TestCase):
    def test_endereco_creation(self):
        endereco = Endereco("Rua A", "123", "Apt 1", "12345-678", "São Paulo")
        self.assertEqual(endereco.logradouro, "Rua A")
        self.assertEqual(endereco.numero, "123")
        self.assertEqual(endereco.complemento, "Apt 1")
        self.assertEqual(endereco.cep, "12345-678")
        self.assertEqual(endereco.cidade, "São Paulo")

    def test_endereco_str(self):
        endereco = Endereco("Rua A", "123", "Apt 1", "12345-678", "São Paulo")
        self.assertEqual(str(endereco), "Rua A, 123 Apt 1, São Paulo - 12345-678")

if __name__ == '__main__':
    unittest.main()
