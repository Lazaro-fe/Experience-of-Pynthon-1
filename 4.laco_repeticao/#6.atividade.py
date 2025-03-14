# Limpeza de Terminal
import os
import time
os.system("clls || clear")

numero_inteiro = 0
pares = 0
impares = 0

for i in range(5):
    numero_inteiro = int(input("Digite um número : "))
    if numero_inteiro % 2 == 0:
        pares += 1
    else:
        impares += 1
    
# Exibindo Resultados

print()
print(f"Pares : {pares}")
print(f"Impares : {impares}")