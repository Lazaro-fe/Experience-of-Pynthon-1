import os
os.system('cls || clear')

#   Solicitando Dados ao usuário

matricula = input("Digite sua matrícula : ")
senha = int(input("Digite sua senha : "))
salario_base = float(input("Digite seu Sálario base : "))

vale_transporte = input("Você quer vale Transporte ? ").upper

match vale_transporte:
    case "sim":
        desconto_do_vale_transporte = salario_base * 0.06
    case "não":
        print("Não Há desconto no sálario")
    case _:
        print("Dados Inválidos")

vale_refeição_recebido = int(input("Quanto você recebe de vale refeição da sua impresa ? "))

def vale_refeição_recebido():
    vale_refeicao = salario_base - vale_refeição_recebido
    return vale_refeicao

vale_refeicao = vale_refeição_recebido()

plano_de_saude = input("Você possui dependentes ? ")

def plano_de_saude():

    match plano_de_saude:
        case "Sim":
            dependentes = int(input("Digite quantos dependentes você possui em casa ? "))
            descontos = 150 * dependentes
            descontos_do_plano_de_saude = salario_base * descontos
        case "Não":
            print("Não há desconto na seu sálario")
        case _:
            print("Dados Inválidos")
        
    return plano_de_saude

def inss(ins):
    if salario_base >= 1518.00:
        salario_com_desconto = salario_base * 0.075
    elif salario_base >= 1518.01 and salario_base <= 2793.88:
        salario_com_desconto = salario_base * 0.09 - 113.85
    if salario_base >= 2793.89 and salario_base <= 4190.83:
        salario_com_desconto = salario_base * 0.12 - 189.54
    elif salario_base >= 4190.84 and salario_base <= 8157.41:
        salario_com_desconto = salario_base * 0.14 - 318.38
    
    return inss(ins)

def irr(irrf):
    if salario_base <= 2259.20:
        print("Está isento de imposto")
    elif salario_base >= 2259.21 and salario_base <= 2826.65:
        salario_com_desconto = salario_base * 0.075 - 169.44
    if salario_base >= 2825.66 and salario_base <= 3751.05:
        salario_com_desconto = salario_base * 0.15 - 381.44
    elif salario_base >= 3751.06 and salario_base <= 4664.68:
        salario_com_desconto = salario_base * 0.225 - 662.77
    if salario_base > 4664.68:
        salario_com_desconto = salario_base * 0.275 - 896.00
    
    return irr(irrf)

print()
print(f"Matricula = {matricula}")
print(f"Vale refeição R$ {vale_refeicao}")
print(f"Valor do plano de saúde R$ {plano_de_saude}")
print(f"Valor do INSS R$ {inss}")
print(f"Valor do IRRF R$ = {irr}")