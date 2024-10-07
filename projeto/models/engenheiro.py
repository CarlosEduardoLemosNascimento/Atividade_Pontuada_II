import os
from projeto.models.funcionario import Funcionario

# Classe que representa um engenheiro, herda de Funcionario
class Engenheiro(Funcionario):
    def __init__(self, nome, telefone, email, endereco, crea):
        # Chama o construtor da classe pai Funcionario
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea

    def salario_final(self):
        # Retorna o salário final fixo de um engenheiro
        return 8000.0

    def __str__(self):
        # Retorna dados do engenheiro
        return f"Engenheiro: {super().__str__()}, CREA: {self.crea}, Salário: {self.salario_final()}"
