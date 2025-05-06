import os
os.system("clear") 

def calcular_inss(salario):
    if salario <= 1518.00:
        return salario * 0.075
    elif salario <= 2793.88:
        return salario * 0.09 - 113.85
    elif salario <= 4190.83:
        return salario * 0.12 - 189.54
    elif salario <= 8157.41:
        return salario * 0.14 - 318.38
    else:
        return 1142.04

def calcular_irrf(salario, dependentes):
    base_calculo = salario - (189.59 * dependentes)
    if base_calculo <= 2259.20:
        return 0  
    elif base_calculo <= 2826.65:
        return base_calculo * 0.075 - 169.44
    elif base_calculo <= 3751.05:
        return base_calculo * 0.15 - 381.44
    elif base_calculo <= 4664.68:
        return base_calculo * 0.225 - 662.77
    else:
        return base_calculo * 0.275 - 896.00

def calcular_vt(salario, opta_vt):
    return salario * 0.06 if opta_vt else 0

def calcular_plano_saude(dependentes):
    return dependentes * 150.00


matricula = input("Digite a sua matrícula: ")
senha = input("Digite sua senha: ")
salario_base = float(input("Digite o seu salário base (R$): "))
opcao_vt = input("Deseja receber vale transporte? Digite 'S' para sim ou 'N' para não: ")
optou_vt = opcao_vt == 's'
valor_vr_total = float(input("Digite o valor do vale refeição oferecido (R$): "))
dependentes = int(input("Informe a quantidade de dependentes: "))


desconto_inss = calcular_inss(salario_base)
desconto_irrf = calcular_irrf(salario_base, dependentes)
desconto_vt = calcular_vt(salario_base, optou_vt)
desconto_saude = calcular_plano_saude(dependentes)


salario_parcial = salario_base - (desconto_inss + desconto_irrf + desconto_vt + desconto_saude)


desconto_vr = salario_parcial * 0.20


salario_liquido = salario_parcial - desconto_vr


print("\n--- Resultado ---")
print(f"Matrícula: {matricula}")
print(f"Senha: {senha}")
print(f"Salário Base: R$ {salario_base:.2f}")
print(f"Vale Transporte: R$ {desconto_vt:.2f}")
print(f"Plano de Saúde: R$ {desconto_saude:.2f}")
print(f"Vale Refeição: R$ {desconto_vr:.2f}")
print(f"Salário Líquido Final: R$ {salario_liquido:.2f}")