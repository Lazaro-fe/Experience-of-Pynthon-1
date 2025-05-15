import os
import time
from dataclasses import dataclass 
os.system("cls || clear")

@dataclass
class Funcionarios:
    nome : str
    data_de_emissao : float
    matrícula : str
    endereco : str

@dataclass
class Clientes:
    nome : str
    data_de_nascimento : float
    endereco : str

lista_de_funcionarios = []
quantidade_de_funcionarios = 3

lista_de_clientes = []
quantidade_de_clientes = 3

print(" == Informe os dados dos Funcionários == ")
for i in range(quantidade_de_funcionarios):
    dados_do_funcionario = Funcionarios(
    print(),
    nome = input("Digite o nome do funcionário : "),
    data_de_emissao = float(input("Digite a data de emissão : ")),
    matricula = input("Digite a matrícula do funcionário : "),
    endereco = input("Digite o endereço do funcionário : ")
    )

    lista_de_funcionarios.append(dados_do_funcionario) 
    os.system("cls || clear")

print(" == Informe os dados dos Clientes == ")
for i in range(quantidade_de_clientes):
    dados_do_cliente = Clientes(
    print(),
    nome = input("Digite o nome do funcionário : "),
    data_de_nascimento = float(input("Digite a data de emissão : ")),
    endereco = input("Digite o endereço do funcionário : ")
    )

    lista_de_clientes.append(dados_do_cliente) 
    os.system("cls || clear")

print("\n== Exibindo dados do Funcionário ==")
for dados_do_funcionario in lista_de_funcionarios:
    print(f"Nome : {dados_do_funcionario.nome}")
    print(f"Data de Emissão : {dados_do_funcionario.data_de_emissao}")
    print(f"Matrícula : {dados_do_funcionario.matricula}")
    print(f"Endereço : R$ {dados_do_funcionario.endereco}")
    print()

print("== Salvando os dados dos funcionários ==")
nome_do_arquivo = "dados_dos_funcionários e clientes.csv"

time.sleep(2)

print("\n== Exibindo dados do Funcionário ==")
for dados_do_cliente in lista_de_clientes:
    print(f"Nome : {dados_do_cliente.nome}")
    print(f"Data de Nascimento : {dados_do_cliente.data_de_nascimento}")
    print(f"Endereço : R$ {dados_do_funcionario.endereco}")
    print()

print("== Salvando os dados dos clçientes ==")
nome_do_arquivo = "dados_dos_funcionários e clientes.csv"
