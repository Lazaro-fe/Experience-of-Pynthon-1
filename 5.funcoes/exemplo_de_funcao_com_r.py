import os
from datetime import date

os.system("cls || clear")

def calcular(data_nascimento):
    # return 2025 - data_nascimento
    return date.today().year - data_nascimento

data_nascimento = int(input("Digite seu ano de nascimento : "))

idade = calcular(data_nascimento)

print(f"Idade : {idade}")