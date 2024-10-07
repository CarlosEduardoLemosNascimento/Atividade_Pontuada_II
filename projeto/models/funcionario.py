import os
from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    @abstractmethod
    def salario_final(self):
        pass

    def __str__(self):
        return f"{self.nome}, {self.telefone}, {self.email}, {self.endereco}"