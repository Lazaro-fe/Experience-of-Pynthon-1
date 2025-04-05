import os
os.system("cls || clear")

def somar(n1, n2):
    calcular = n1 + n2
    return calcular

def media(n1, n2):
    media = soma / 2
    return media

n1 = int(input("Digite o Primeiro Número : "))
n2 = int(input("Digite o Segundo Número : "))

soma = somar(n1, n2)
media = media(n1, n2)

print()
print(f"Soma: {soma}")
print(f"Média: {media}")