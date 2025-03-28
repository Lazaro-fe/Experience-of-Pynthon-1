# LIMPEZA DE TERMINAL
import os
os.system("cls || clear")

sexo = input("Digite seu sexo : ")
idade = int(input("Digite sua idade : "))
salario = float(input("Digite seu sálario : "))
quantidade_de_salário = 0
idade_geral = 0

while True:
    print("""
================ MENU ============
\tCódigo            Descrição
    1           |   Adicinar pessoa
    2           |   Exibir resultados
    3           |   Sair
    """)

    codigo = int(input("Digite o seu código : "))
    
    match codigo:
        case "Adicionar pessoa":
            sexo = input("Digite seu sexo : ")
            idade = int(input("Digite sua idade : "))
            salario = float(input("Digite seu sálario : "))
        case "Exibir esultados":
            media_salario_grupo = salario / quantidade_de_salário
            if idade > idade_geral:
                print(f"Maior idade : {idade}")
            elif idade < idade:
                print(f"Menor idade : {idade}")
            else:
                0
        case "Sair":
            break

