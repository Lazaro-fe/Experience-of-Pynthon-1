import os
from dataclasses import dataclass 
os.system("cls || clear")

@dataclass
class Livros:
    nome_do_livro : str
    autor : str
    categoria : str
    preco : float

lista_de_livros = []
quantidade_de_livros = 3

print(" == Informe os dados do livro == ")
for i in range(quantidade_de_livros):
        dados_do_livro = Livros(
        nome_do_livro = input("Digite o nome do livro : "),
        autor = input("Digite o nome do autor : "),
        categoria = input("Digite a categoria que esses livro pertence : "),
        preco = float(input("Digite quanto custa o livro : "))
        )

        lista_de_livros.append(dados_do_livro) 
        os.system("cls || clear")

print("\n== Exibindo dados do carro ==")
for dados_livro in lista_de_livros:
    print(f"Título : {dados_do_livro.nome_do_livro}")
    print(f"Autor : {dados_do_livro.autor}")
    print(f"Categoria : {dados_do_livro.categoria}")
    print(f"Preço : R$ {dados_do_livro.preco}")
    print()

print("== Salvando os dados dos clientes ==")
nome_do_arquivo = "dados_do_livro.txt"

with open(nome_do_arquivo, "w") as arquivo:
    for car in lista_de_livros:
        arquivo.write(f"Título : {dados_do_livro.nome_do_livro}, Autor : {dados_do_livro.autor}, Categoria : {dados_do_livro.categoria}, Preço : R$ {dados_do_livro.preco}")

print("\nSalvo com Sucesso!!")

print("\nAcessando dados do arquivo")
try:
    with open(nome_do_arquivo, "r") as nome_do_arquivo:
        linhas = nome_do_arquivo.readline()
        for linha in linhas:
            print(f"- {linha.strip()}")

except FileNotFoundError:
    print(" === ARQUIVO NÃO ENCONTRADO === ")