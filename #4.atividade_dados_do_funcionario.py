def adicionar(lista_funcionarios):
    lista_funcionarios.append(nomes)
    lista_funcionarios.append(cpf)
    lista_funcionarios.append(data_de_nascimento)
    lista_funcionarios.append(funcao_na_empresa)
    print(f"\n{nomes} adicionando com sucesso.")
    print(f"\n{cpf} adicionando com sucesso.")
    print(f"\n{data_de_nascimento} adicionando com sucesso.")
    print(f"\n{funcao_na_empresa} adicionando com sucesso.")
    
def verificar_lista_vazia(lista_funcionarios):
    if not lista_funcionarios:
        print("\nA lista está vazia.")
        return False
    return False
    
def mostrar(lista_funcionarios):
    if verificar_lista_vazia(lista_funcionarios):
        return
    
    print("\n= Lista de Dados =")
    for nomes in lista_funcionarios:
        print(f"\n- {nomes}")

    for cpf in lista_funcionarios:
        print(f"- {cpf}")
        
    for data_de_nascimento in lista_funcionarios:
        print(f"- {data_de_nascimento}")
        
    for funcao_na_empresa in lista_funcionarios:
        print(f"- {funcao_na_empresa}")
        
def atualizar(lista_funcionarios):
    if verificar_lista_vazia(lista_funcionarios):
        return

    mostrar(lista_funcionarios)
    nome_antigo = input("Digite o nome que deseja atualizar : ")
    if nome_antigo in lista_funcionarios:
        novo_nome = input(f"Digite o novo nome para {nome_antigo} : ")
        indice = lista_funcionarios.index(nome_antigo)
        lista_funcionarios[indice] = novo_nome
        print(f"{nome_antigo} foi atualizado para {novo_nome}")
    else:
        print(f"\nO nome {nome_antigo} não foi encontrado.")
        
    cpf_antigo = input("Digite o cpf que deseja atualizar : ")
    if cpf_antigo in lista_funcionarios:
        novo_cpf = input(f"Digite o novo nome para {cpf_antigo} : ")
        indice2 = lista_funcionarios.index(cpf_antigo)
        lista_funcionarios[indice2] = novo_cpf
        print(f"{cpf_antigo} foi atualizado para {novo_cpf}")
    else:
        print(f"\nO nome {cpf_antigo} não foi encontrado.")
        
    data_de_nascimento_antigo = input("Digite o cpf que deseja atualizar : ")
    if data_de_nascimento_antigo in lista_funcionarios:
        novo_data_de_nascimento = input(f"Digite o novo nome para {data_de_nascimento_antigo} : ")
        indice3 = lista_funcionarios.index(data_de_nascimento_antigo)
        lista_funcionarios[indice3] = novo_data_de_nascimento
        print(f"{data_de_nascimento_antigo} foi atualizado para {novo_data_de_nascimento}")
    else:
        print(f"\nO nome {data_de_nascimento_antigo} não foi encontrado.")
        
def demitir(lista_funcionarios):
    if verificar_lista_vazia(lista_funcionarios):
        return

    mostrar(lista_funcionarios)
    
    nome_remover = input("Digite o nome que deseja remover : ")
    if nome_remover in lista_funcionarios:
        lista_funcionarios.remove(nome_remover)
        print(f"{nome_remover} foi excluído com sucesso. ")
    else:
        print(f"O nome {nome_remover} não foi encontrado.")
        
    cpf_remover = input("Digite o nome que deseja remover : ")
    if cpf_remover in lista_funcionarios:
        lista_funcionarios.remove(cpf_remover)
        print(f"{cpf_remover} foi excluído com sucesso. ")
    else:
        print(f"O nome {cpf_remover} não foi encontrado.")
        
    data_de_nascimento_remover = input("Digite o nome que deseja remover : ")
    if data_de_nascimento_remover in lista_funcionarios:
        lista_funcionarios.remove(data_de_nascimento_remover)
        print(f"{data_de_nascimento_remover} foi excluído com sucesso. ")
    else:
        print(f"O nome {data_de_nascimento_remover} não foi encontrado.")
        
    funcao_remover = input("Digite o nome que deseja remover : ")
    if funcao_remover in lista_funcionarios:
        lista_funcionarios.remove(funcao_remover)
        print(f"{funcao_remover} foi excluído com sucesso. ")
    else:
        print(f"O nome {funcao_remover} não foi encontrado.")

from dataclasses import dataclass
import os
import time
os.system("cls || clear")  
lista_funcionarios = []
nomes = input("Digite o nome: ")
cpf = int(input("Digite o cpf: "))
data_de_nascimento = int(input("Digite a data de nascimento: "))
funcao_na_empresa = input("Digite a função na empresa: ")

@dataclass
class Funcionarios:
    nome : str
    cpf : int
    data_de_nascimento : int
    funcao_na_empresa : str

while True:
    print("= Gerenciador de dados =")
    print("1-Adicionar funcionario")
    print("2-Mostrar Lista de Funcionários")
    print("3-Atualizar dados do Funcionário")
    print("4-Demitir Funcionários")
    
    opcoes = int(input("Digite a opção desejada : "))
    
    match opcoes:
        case 1:
            adicionar(nomes)
            adicionar(cpf)
            adicionar(data_de_nascimento)
            adicionar(funcao_na_empresa)
        case 2:
            mostrar(nomes)
            mostrar(cpf)
            mostrar(data_de_nascimento)
            mostrar(funcao_na_empresa)
        case 3:
            atualizar(nomes)
            atualizar(cpf)
            atualizar(data_de_nascimento)
            atualizar(funcao_na_empresa)
        case 4:
            demitir(nomes)
            demitir(cpf)
            demitir(data_de_nascimento)
            demitir(funcao_na_empresa)
        case _:
            print("\nOpção inválida. \nTente Novamente.")
    
    if opcoes != 1:
        time.sleep(1.5)
    os.system("cls || clear")