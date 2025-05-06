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
    return salario_base, vale_transporte, vale_refeicao, dependentes

def calcular_vale_transporte(salario_base, vale_transporte):
    if vale_transporte == "sim":
        salario_base * 0.06
    else:
        0

def plano_de_saude(dependentes):
    return dependentes * 150.00

def calculo_do_vale_refeição(vale_refeicao):
    return vale_refeicao * 0.20

def INSS(salario_base):
    if salario_base < 1518.00:
        desconto = salario_base * 0.75
    elif salario_base > 1518.01 and salario_base <= 2793.88:
        desconto = salario_base * 0.09 - 113.85
    elif salario_base > 2793.89 and salario_base <= 4190.83:
        desconto = salario_base * 0.12 - 189.54
    elif salario_base > 4190.84 and salario_base <= 8157.41:
        desconto = salario_base * 0.14 - 318.38
    
    return desconto

def IRRF(salario_base, dependentes):
    if s