import os
import time
os.system("clls || clear")

notas = 0

for i in range(4):
    notas += float(input("Digite uma nota : "))

resultados = notas / 4

#   Exibindo Resultados
print()
print(f"Média : {resultados}")
