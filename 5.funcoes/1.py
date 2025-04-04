import os
os.system("cls || clear")

def verificar(numero):
    if numero > 0:
        print(f"{numero} é positivo")
    elif numero == 0:
        print(f"{numero} é neutro")
    else:
        print(f"{numero} é negativo")

print("Verificando se um número é Positivo ou Negativo!")
numero = int(input("Digite um número : "))
verificar(numero)