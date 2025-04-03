# Limpeza de Terminal
import os
os.system("clls || clear")

def verificar(numero_inteiro):
    for i in range(1):
        if numero_inteiro % 2 == 0:
            print()
            print(f"{numero_inteiro} é um número par!!")
        else:
            print()
            print(f"{numero_inteiro} é impar!!!")

print("Verificando se um número é pior ou impar!!!")
numero_inteiro = int(input("Digite um número : "))
verificar(numero_inteiro)