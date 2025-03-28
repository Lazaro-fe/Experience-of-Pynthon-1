# LIMPEZA DE TERMINAL
import os
os.system("cls || clear")

numero_inteiro = 0
pares = 0
impares = 0
soma_pares = 0
soma_geral = 0
quantidade_geral = 0


while True:
    numero_inteiro = int(input("Digite um número : "))
    if numero_inteiro == 0:
        break
    if numero_inteiro % 2 == 0:
        pares += 1
        soma_pares += numero_inteiro
    else:
        impares += 1 

    soma_geral += numero_inteiro
    quantidade_geral += 1

if quantidade_geral > 0:
    media_pares = soma_pares / pares
    media_pares = soma_geral / quantidade_geral

    print(f"\nQuantidade de pares : {pares}")
    print(f"Quantidade de ímpares : {impares}")
    print(f"Média de números pares : {media_pares}")
    print(f"Média geral : {quantidade_geral}")
else:
    print("\nNão foram informados os números de forma coerente.")