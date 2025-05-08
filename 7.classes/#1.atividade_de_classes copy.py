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

pessoa1 = Pessoa("Lázaro", 16, 88.50, 1.68)

print("\n= Dados da Pessoa =")
print(f"Nome : {pessoa1.nome}, idade : {pessoa1.idade} anos, peso : {pessoa1.peso} kg, altura : {pessoa1.altura} metros de altura")