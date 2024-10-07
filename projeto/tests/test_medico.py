import unittest
from projeto.models.endereco import Endereco
from projeto.models.medico import Medico

class TestMedico(unittest.TestCase):
    def test_medico_creation(self):
        endereco = Endereco("Rua A", "123", "Apt 1", "12345-678", "Bahia")
        medico = Medico("Maria", "71988888888", "maria@exemplo.com", endereco, "654321")
        self.assertEqual(medico.nome, "Maria")
        self.assertEqual(medico.crm, "654321")
        self.assertEqual(medico.salario_final(), 10000.0)

    def test_medico_str(self):
        endereco = Endereco("Rua A", "123", "Apt 1", "12345-678", "Bahia")
        medico = Medico("Maria", "71988888888", "maria@exemplo.com", endereco, "654321")
        self.assertEqual(str(medico), "Médico: Nome: Maria, Telefone: 71988888888, Email: maria@exemplo.com, Endereço: Rua A, 123 Apt 1, Bahia - 12345-678, CRM: 654321, Salário: 10000.0")

if __name__ == '__main__':
    unittest.main()
