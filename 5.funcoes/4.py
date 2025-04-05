#   Limpeza do Terminal
import os
os.system("cls || clear")

def contar_pares_impares():
    pares = 0
    impares = 0

    for i in range(5):
        numero = int(input("Digite um número : "))
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

quantidade_de_pares, quantidade_de_impares = contar_pares_impares()

print(f"\nQuantidde de Pares : {quantidade_de_pares}")
print(f"Quantidde de Ímpares : {quantidade_de_impares}")