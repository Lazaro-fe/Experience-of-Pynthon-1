import os
os.system("cls || clear")

#   Criando uma lista
lista_de_compras = []
quantidade = 3


#   Solicitando dados para o Usuário
print("== Lista de Compras ==")
for i in range(quantidade):
    item = input(f"Digite o {i+1}º para a Lista : ")
    lista_de_compras.append(item)

#   Exibindo itens da lista de compras
print("\n == Itens da Lista ==")
for i, item in enumerate(lista_de_compras, start=1):
    print(f"{i}º item : {item}")