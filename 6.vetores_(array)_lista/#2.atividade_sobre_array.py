import os
os.system("cls || clear")

def maior_menor(lista):
    maior = max(lista_de_numeros)
    menor = min(lista_de_numeros)
    return menor, maior

#   Criando uma lista

lista_de_numeros = []
quantidade_de_numeros = 5

#   Solicitando dados ao Usuário
for i in range(quantidade_de_numeros):
    numero = int(input("Digite um número para a lista : "))
    lista_de_numeros.append(numero)

menor, maior = maior_menor(lista_de_numeros)

#   Exibindo números da Lista
print("\n == ITENS DA LISTA == ")
for i, numero in enumerate(lista_de_numeros, start=1):
    print(f"{i} : {numero}")

print()
print(f"Maior Número : {maior}")
print(f"Menor Número : {menor}")