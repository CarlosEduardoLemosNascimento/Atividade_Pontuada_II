import unittest
from projeto.models.endereco import Endereco
from projeto.models.funcionario import Funcionario

class FuncionarioTest(Funcionario):
    # Implementa o método abstrato para teste
    def salario_final(self):
        return 0

class TestFuncionario(unittest.TestCase):
    def test_funcionario_creation(self):
        endereco = Endereco("Rua A", "123", "Apt 1", "12345-678", "Bahia")
        funcionario = FuncionarioTest("Carlos", "71999999999", "carlos@exemplo.com", endereco)
        self.assertEqual(funcionario.nome, "Carlos")
        self.assertEqual(funcionario.telefone, "71999999999")
        self.assertEqual(funcionario.email, "carlos@exemplo.com")
        self.assertEqual(funcionario.endereco, endereco)

    def test_funcionario_str(self):
        endereco = Endereco("Rua A", "123", "Apt 1", "12345-678", "Bahia")
        funcionario = FuncionarioTest("Carlos", "71999999999", "carlos@exemplo.com", endereco)
        self.assertEqual(str(funcionario), "Nome: Carlos, Telefone: 71999999999, Email: carlos@exemplo.com, Endereço: Rua A, 123 Apt 1, Bahia - 12345-678")

if __name__ == '__main__':
    unittest.main()
