# Limpeza de Terminal
import os
import time
os.system("clls || clear")

print("Contagem de 2 em 2 : ")
for i in range(1, 22, 2):
    print(f"Valor da variável i : {i}")
    time.sleep(0.5)

print("===== ACABOU =====")