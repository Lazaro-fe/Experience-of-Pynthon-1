#   Nome, cpf, data_nascimento, função
import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Funcionario:
    nome : str
    cpf : str
    data_de_nascimento : str
    funcao : str
    
    def mostrar_dados(self):
        print(f"Nome : {self.nome}")
        print(f"CPF : {self.cpf}")
        print(f"Data de Nascimento : {self.data_de_nascimento}")
        print(f"Função : {self.funcao}")
        print()
    
def verificar_lista_vazia(lista):
    if not lista:
        print("\nA lista está vazia.")
        return True
    return False

def adicionar(lista):
    funcionario = Funcionario(
        nome = input("Nome : "),
        cpf = input("CPF : "),
        data_de_nascimento = input("Data de Nascimento : "),
        funcao = input("Função : ")
    )
    lista.append(funcionario)
    print("Funcionário adicionado com sucesso.")
    
def mostrar_funcionario(lista):
    if verificar_lista_vazia(lista):
        return
    
    print("\n= Lista de Funcionários =")
    for funcionario in lista:
        funcionario.mostrar_dados()
        
def atualizar(lista):
    nome_atualizar = input("Digite o nome do funcionário que deseja atualizar : ")
    encontrado = False
    
    for funcionarios in lista:
        if funcionarios.nome == nome_atualizar:
            funcionarios.nome = input("Nome : "),
            funcionarios.cpf = input("CPF : "),
            funcionarios.data_de_nascimento = input("Data de Nascimento : ")
            funcionarios.funcao = input("Função : ")
            encontrado = True
            break
        
    if not encontrado:
        print(f"\nO funcionário com o nome {funcionarios.nome} não foi encontrado.")
        
    mostrar_funcionario(lista)
    
def excluir(lista):
    if verificar_lista_vazia(lista):
        return
    
    nome_excluir = input("Digite o nome do funcionário : ")
    for funcionarios in lista_funcionarios:
        if funcionarios.nome == nome_excluir:
            lista_funcionarios.remove(nome_excluir)
            print("Funcionário excluído com sucesso.")
        else:
            print("Funcionário não encontrado")                


lista_funcionarios = []
for i in range(1):
    adicionar(lista_funcionarios)
    
mostrar_funcionario(lista_funcionarios)
atualizar(lista_funcionarios)
excluir(lista_funcionarios)