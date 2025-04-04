import os
os.system("cls || clear")

def somar(n1, n2):
    calcular = n1 + n2
    return calcular

def subtracao(n1, n2):
    calcular = n1 - n2
    return calcular

def multiplicacao(n1, n2):
    calcular = n1 * n2
    return calcular

def divisao(n1, n2):
    calcular = n1 / n2
    return calcular

#   Outra forma de Fazer

#def somar(n1, n2):
#   return = n1 + n2

#def subtracao(n1, n2):
# return = n1 - n2

#def multiplicacao(n1, n2):
#return = n1 * n2

#def divisao(n1, n2):
#return = n1 / n2

n1 = int(input("Digite o Primeiro Número : "))
n2 = int(input("Digite o Primeiro Número : "))

soma = somar(n1, n2)
subtracao = subtracao(n1, n2)
multiplicacao = multiplicacao(n1, n2)
divisao = divisao(n1, n2)

print()
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")