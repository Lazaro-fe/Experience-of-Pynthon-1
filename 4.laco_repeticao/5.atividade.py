# Limpeza de Terminal
import os
import time
os.system("clls || clear")

numero = 0
for i in range(1,6):
    numero += int(input("Digite um número : "))
    print(f"Soma : {numero}")