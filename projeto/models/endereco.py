import os
class Endereco:
    def __init__(self, logradouro, numero, complemento, cep, cidade):
        # Inicializando atributos
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self):
        # Retorna o endereço
        return f"{self.logradouro}, {self.numero}, {self.complemento}, {self.cidade} - {self.cep}"