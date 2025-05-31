# Limpeza de Terminal
import os
import time
os.system("clls || clear")

soma = 0
for i in range(1, 6):
    numero = int(input("Digite um número : "))
    soma += numero
print(f"Soma : {soma}")

#   OUTRO MODO DE FAZER :

#numero = 0
#for in range(1,6):
#numero += int(input("Digite um número :"))
#print(f"Soma : {numero}")