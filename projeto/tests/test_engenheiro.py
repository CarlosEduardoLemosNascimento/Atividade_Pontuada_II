import unittest
from projeto.models.endereco import Endereco
from projeto.models.engenheiro import Engenheiro

class TestEngenheiro(unittest.TestCase):
    def test_engenheiro_creation(self):
        endereco = Endereco("Rua A", "123", "Apt 1", "12345-678", "Bahia")
        engenheiro = Engenheiro("João", "71999999999", "joao@exemplo.com", endereco, "123456")
        self.assertEqual(engenheiro.nome, "João")
        self.assertEqual(engenheiro.crea, "123456")
        self.assertEqual(engenheiro.salario_final(), 8000.0)

    def test_engenheiro_str(self):
        endereco = Endereco("Rua A", "123", "Apt 1", "12345-678", "Bahia")
        engenheiro = Engenheiro("João", "71999999999", "joao@exemplo.com", endereco, "123456")
        self.assertEqual(str(engenheiro), "Engenheiro: Nome: João, Telefone: 71999999999, Email: joao@exemplo.com, Endereço: Rua A, 123, Apt 1, Bahia - 12345-678, CREA: 123456, Salário: 8000.0")

if __name__ == '__main__':
    unittest.main()
