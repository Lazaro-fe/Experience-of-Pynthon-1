import os
os.system("cls || clear")
import time

soma = 0

def calcular(soma):
    return soma / 2

for i in range(2):
    nota = float(input("Digite uma nota : "))
    soma += nota

media = calcular(soma)

if media >= 7:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

print()
print(f"Média : {media}")
print(f"Resultado : {resultado}")