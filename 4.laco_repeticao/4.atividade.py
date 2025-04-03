# Limpeza do Terminal
import os
import time
os.system("clls || clear")

numero = int(input("Digite um número : "))

print("\nIniciando Contagem : ")
for i in range(numero, -1, -1):
    print(f"{i}")
    time.sleep(0.1)

print("\n===== ACABOU =====")