from projeto.models.endereco import Endereco
from projeto.models.engenheiro import Engenheiro
from projeto.models.medico import Medico

def main():
    endereco = Endereco("Rua A", "123", "Apt 1", "12345-678", "São Paulo")

    engenheiro = Engenheiro("João", "11999999999", "joao@exemplo.com", endereco, "123456")
    print(engenheiro)

    medico = Medico("Maria", "11988888888", "maria@exemplo.com", endereco, "654321")
    print(medico)

if __name__ == "__main__":
    main()