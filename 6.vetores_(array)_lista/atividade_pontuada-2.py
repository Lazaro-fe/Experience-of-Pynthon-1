import os
os.system('cls || clear')

#   Solicitando Dados ao usuário

matricula = input("Digite sua matrícula : ")
senha = input("Digite sua senha : ")
print("\nAcesso Permitido!!")

def obtendo_dados_do_funcionario():
    salario_base = float(input("Digite seu salário base em R$ : "))
    vale_transporte = input("Deseja receber vale transporte 'sim' ou 'não' : ").lower() == 'sim'
    vale_refeicao = float(input("Informe o valor do vale refeição fornecido pela empresa em R$ : "))
    dependentes = int(input("Informe a quantidade de dependentes que possui na sua casa : "))

def calcular_vale_transporte(salario_base, vale_transporte):
    if vale_transporte == "sim":
        salario_base * 0.06
    else:
        0

def plano_de_saude(dependentes):
    return dependentes * 150.00

def calculo_do_vale_refeição(vale_refeicao):
    return vale_refeicao * 0.20