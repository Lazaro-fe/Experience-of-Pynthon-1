import os
from dataclasses import dataclass

#   LIMPEZA DO TERMINAL
os.system("cls || clear")

#   CRIANDO UMA CLASSE

@dataclass
class Endereco:
    #   Variáveis = Atributos
    logradouro : str
    numero : int
    cidade : str

@dataclass
class Pessoa:
    #   Variáveis = Atributos
    nome : str
    email : str
    endereco : Endereco

    #   Função = Método
    def exibir_dados(self):
        print("\n== Informações ==")
        print(f"Nome : {self.nome}")
        print(f"Idade : {self.idade}")
        print(f"Nome : {self.endereco.logradouro}, número : {self.endereco.numero}")


pessoa1 = Pessoa(
    nome = input("Digite o nome da pessoa : "),
    email = input("Digite o email da pessoa : "),
    endereco = input("Digite o endereço da pessoa : "),
    logradouro = input("Digite o logradouro da pessoa : "),
    numero = int(input("Digite o número da casa da pessoa : ")),
    cidade = input("Digite a cidade que a pessoa mora : "),
    )