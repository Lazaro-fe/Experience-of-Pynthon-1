import os
from dataclasses import dataclass 
os.system("cls || clear")

@dataclass
class Livros:
    nome_do_livro : str
    autor : str
    categoria : str
    preco_do_livro : float

lista_de_livros = []