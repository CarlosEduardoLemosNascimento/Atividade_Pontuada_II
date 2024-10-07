import os
from projeto.models.funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, nome, telefone, email, endereco, crm):
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm

    # Cada subclasse precisa implementar seu próprio cálculo de salário
    def salario_final(self):
        return 10000.0

    def __str__(self):
        return f"Médico: {super().__str__()}, CRM: {self.crm}, Salário: {self.salario_final()}"
