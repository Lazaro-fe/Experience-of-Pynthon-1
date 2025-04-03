# LIMPEZA DE TERMINAL
import os
os.system("cls || clear")

soma = 0
contador = 1

while True:
    nota = float(input(f"Digite uma nota : "))
    soma += nota
    contador += 1

    resposta = input("Dejesa digitar mais uma nota ? \nResponda com 'Sim' ou 'Não' : ").lower()
    if resposta == "n":
        break

media = soma / contador

print()
print(f"\nMédia : {media}")