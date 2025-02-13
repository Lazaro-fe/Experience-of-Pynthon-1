import os

#   Limpa o Terminal
os.system("clear")

#   Solicite dados para o usuário
nome = input("Digite seu nome : ")
idade = int(input("Digite sua idade :  "))
altura = float(input("Digite sua altura : "))

#   Exibindo dados.
print()
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura}")