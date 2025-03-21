# LIMPEZA DE TERMINAL
import os
os.system("cls || clear")

soma = 0
contador = -1
nota = 0

while True:
    nota = float(input("Digite uma nota : "))
    soma += nota
    contador += 1
    
    if nota > 0:
        soma += nota
        contador += 1
    else:
        break

media = soma / contador

print()
print(f"\nMédia : {media}")