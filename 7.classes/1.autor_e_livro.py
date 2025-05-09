import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Autor:
    nome : str
    biografia : str

@dataclass
class Livro:
    titulo : str
    ano : int
    autor : Autor
    
    #   Função = Método
    def exibir_detalhes(self):
        print("\n== Informações == \n")
        print(f"Nome : {self.autor.nome}\n")
        print(f"Biografia : {self.autor.biografia}\n")
        print(f"Titulo : {self.titulo}\n")
        print(f"Ano : {self.ano}\n")

#   Aplicando características da classe
autor1 = Autor("J. K. Rowling", "A escritora britânica Joanne Kathleen Rowling nasceu na cidade de Yate.")
livro1 = Livro("Harry Potter e a Pedra Filosofal", 1997, autor1)
livro1.exibir_detalhes()

print()
autor2 = Autor("C. S. Lewis", "Clive Staples Lewis, comumente referido como C. S. Lewis, foi um professor universitário, escritor, romancista, poeta, crítico literário, ensaísta e teólogo anglicano irlandês.")
livro2 = Livro("The Chronicles of Narnia", 1955, autor2)
livro2.exibir_detalhes()