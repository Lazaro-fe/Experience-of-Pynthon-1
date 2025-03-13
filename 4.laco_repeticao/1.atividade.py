# Limpeza de Terminal
import os
import time
os.system("clls || clear")

print("Contagem de 100 até 120 - Apenas pares ")
for i in range(100, 121, 2):
    print(f"Valor da variável i : {i}")
    time.sleep(0.5)

print("===== ACABOU =====")