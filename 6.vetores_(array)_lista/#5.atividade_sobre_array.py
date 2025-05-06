import os
os.system("cls || clear")

#   CRIANDO LISTA

lista_de_numeros = []
quantidade = 5

#   SOLICITANDO DADOS AO USUÁRIO

for i in range(quantidade):
    numeros = int(input("Digite um número para lista: "))
    if numeros < 0:
        numeros = 0
    lista_de_numeros.append(numeros)

print("\n == ITENS DA LISTA == ")
for i, numero in enumerate(lista_de_numeros, start=1):
    print(f"{i} : {numero}")