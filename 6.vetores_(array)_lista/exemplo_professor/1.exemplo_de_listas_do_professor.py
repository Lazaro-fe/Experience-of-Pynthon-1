import os
os.system("cls || clear")

#   Criando uma lista
lista_de_compras = []
quantidade = 3


#   Solicitando dados para o Usuário
print("== Lista de Compras ==")
for i in range(quantidade):
    item = input("Digite um item para a Lista : ")
    lista_de_compras.append(item)

#   Exibindo itens da lista de compras
print("\n == Itens da Lista ==")
for item in lista_de_compras:
    print(item)