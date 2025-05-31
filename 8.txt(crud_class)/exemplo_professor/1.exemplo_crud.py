import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Cliente:
    nome : str
    email : str
    telefone : str

#   Criando uma lista para adicionar clientes
lista_de_clientes = []
quantidade_de_clientes = 3  #   Constante que define a quantidade de clientes

#   Laço de repetição para adicionar clientes
print("Informe os dados do cliente : ")
for i in range(quantidade_de_clientes):
    cliente = Cliente(
        nome = input("Nome : "), #  Não esqueça da vírgula
        email = input("E-mail : "),
        telefone = input("Telefone : ") #   O último não coloca na lista
    )
    lista_de_clientes.append(cliente)   #   Adicionando cliente na lista
    print()

os.system("cls || clear")

#   Laço de repetição para exibir dados dos clientes
print("\n== Exibindo dados clientes ==")
for cliente in lista_de_clientes: # Mostra os dados por elementos na lista
    print(f"Nome : {cliente.nome}")
    print(f"E-mail : {cliente.email}")
    print(f"Telefone : {cliente.telefone}")
    print()

#   Salvando em um arquivo .txt
print("== Salvando os dados dos clientes ==")
nome_do_arquivo = "dados_clientes.txt"

# w --> escrita/salvar/sobrescrever
# a --> escrita/salvar/acumular
with open(nome_do_arquivo, "a") as arquivo:
    for cliente in lista_de_clientes:
        arquivo.write(f"Nome : {cliente.nome}, Email : {cliente.email}, Telefone : {cliente.telefone}\n")

print("\nSalvo com sucesso!")