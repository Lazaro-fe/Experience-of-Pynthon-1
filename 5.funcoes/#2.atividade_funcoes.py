import os
os.system("cls || clear")

def tabuada(numero):
    print("===== Tabuada ======")
    for i in range(1, 11) :
        print(f"{numero} X {i} = {numero * i}")

numero_informado = int(input("Informe o número para Tabuada : "))
tabuada(numero_informado)