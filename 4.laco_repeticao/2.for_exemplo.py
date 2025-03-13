# Limpeza de Terminal
import os
import time
os.system("clls || clear")

print("Contagem Regressiva :")
for i in range(10, 0, -1):
    print(f"Valor da variável i : {i}")
    time.sleep(1)

print("===== ACABOU =====")