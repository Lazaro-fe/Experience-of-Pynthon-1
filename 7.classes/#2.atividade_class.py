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

@dataclass
class Pessoa:
    #   Variáveis = Atributos
    nome : str
    idade : int
    endereco : Endereco
    
    #   Função = Método
    def exibir_dados(self):
        print("\n== Informações ==")
        print(f"Nome : {self.nome}")
        print(f"Idade : {self.idade}")
        print(f"Nome : {self.endereco.logradouro}, número : {self.endereco.numero}")

#   Aplicando caracteristicas da classe
endereco1 = Endereco("Rua Estados Unidos", 35)
pessoa1 = Pessoa("Luiz", 59, endereco1)
pessoa1.exibir_dados()

print()
endereco2 = Endereco("Rua China", 95)
pessoa2 = Pessoa("Jonh", 25, endereco2)
pessoa2.exibir_dados()