import os
class Endereco:
    def __init__(self, logradouro, numero, complemento, cep, cidade):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self):
        return f"{self.logradouro}, {self.numero}, {self.complemento}, {self.cidade} - {self.cep}"