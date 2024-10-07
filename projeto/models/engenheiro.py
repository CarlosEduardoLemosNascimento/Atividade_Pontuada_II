import os
from projeto.models.funcionario import Funcionario

class Engenheiro(Funcionario):
    def __init__(self, nome, telefone, email, endereco, crea):
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea

    # Cada subclasse precisa implementar seu próprio cálculo de salário
    def salario_final(self):
        return 8000.0

    def __str__(self):
        return f"Engenheiro: {super().__str__()}, CREA: {self.crea}, Salário: {self.salario_final()}"
