import os
from projeto.models.funcionario import Funcionario

# Classe que representa um médico, herda de Funcionario
class Medico(Funcionario):
    def __init__(self, nome, telefone, email, endereco, crm):
        # Chama o construtor da classe pai Funcionario
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm

    def salario_final(self):
        # Retorna o salário final fixo de um médico
        return 10000.0

    def __str__(self):
        # Retorna dados do médico, incluindo o CRM e o salário
        return f"Médico: {super().__str__()}, CRM: {self.crm}, Salário: {self.salario_final()}"
