import os
from dataclasses import dataclass


#   LIMPEZA DO TERMINAL
os.system("cls || clear")

#   CRIANDO UMA CLASSE

@dataclass
class Pessoa:
    nome : str
    idade : int

#   Aplicando características da classe

pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

print("\n= Dados da Pessoa =")
print(f"Nome : {pessoa1.nome}, idade : {pessoa1.idade} anos")
print(f"Nome : {pessoa2.nome}, idade : {pessoa2.idade} anos")