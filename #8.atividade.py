import os
import time
os.system("clls || clear")

notas = 0

for i in range(3):
    notas += float(input("Digite uma nota : "))

resultados = notas / 3

if resultados >= 7:
    print(" Você está Aprovado !!! =) ")
elif resultados <= 4:
    print(" Você está Reprovado )= ")
else :
    print

# Exibindo Resultados

print()
print(f"Média : {resultados:.2f}")