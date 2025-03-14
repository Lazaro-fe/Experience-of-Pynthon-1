# Limpeza do Terminal
import os
import time
os.system("clls || clear")

n1 = float(input("Digite um número : "))

print(f"Tabuada do número {n1 :}")
for i in range(1, 11):
    print(f"{n1} x {i} = {i * n1}")
    time.sleep(0.7)

print("Tabuada feita")