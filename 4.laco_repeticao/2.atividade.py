# Limpeza de Terminal
import os
import time
os.system("clls || clear")

print("ÍMPARES DE 1 ATÉ 20: ")
for i in range(1,21):
    if i % 2 == 1:
        print(f"Numero : {i}")
        time.sleep(1)