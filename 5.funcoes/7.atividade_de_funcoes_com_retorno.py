#   Limpeza do Terminal
import os
os.system("cls || clear")

def idade_do_usuario(data_do_nascimento):
    idade_total = 2025 - data_de_nascimento
    return idade_total

data_de_nascimento = float(input("Digite sua data de nascimento : "))

idade_total = idade_do_usuario(data_de_nascimento)

print()
print(f"Idade do Úsuario : {idade_total}")