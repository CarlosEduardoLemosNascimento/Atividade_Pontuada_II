import os

from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco

# Classe abstrata que representa um funcionário
class Funcionario(ABC):
    def __init__(self, nome, telefone, email, endereco: Endereco):
        # Inicializa os atributos de um funcionário
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    @abstractmethod
    def salario_final(self):
        # Método abstrato que deve ser implementado nas subclasses
        pass

    def __str__(self):
        # Retorna dados do funcionário
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}, Endereço: {self.endereco}"
