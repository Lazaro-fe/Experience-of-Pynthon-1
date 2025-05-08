import os
from dataclasses import dataclass


#   LIMPEZA DO TERMINAL
os.system("cls || clear")

#   CRIANDO UMA CLASSE

@dataclass
class Pessoa:
    nome : str
    idade : int
    peso : float
    altura : float

#   APLICANDO CARACTERÍTICAS DA CLASSE

pessoa1 = Pessoa(
    nome = input("Digite o nome da pessoa : "),
    idade = int(input("Digite a idade da pessoa : ")),
    peso = float(input("Digite o peso : ")),
    altura = float(input("Digite a altura : ")),
    )

os.system("cls || clear")

print("\n= Dados da Pessoa =")
print(f"Nome : {pessoa1.nome}, idade : {pessoa1.idade} anos, peso : {pessoa1.peso} kg, altura : {pessoa1.altura} metros de altura")