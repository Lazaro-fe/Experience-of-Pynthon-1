# LIMPEZA DE TERMINAL
import os
import time
os.system("cls || clear")

contador = 0
soma_do_salario = 0
maior_idade = 0
menor_idade = 9999
mulheres_5k = 0

while True:
    print("""
Código   |  Descrição
    1    |  Adicinar pessoa
    2    |  Exibir resultados
    3    |  Sair
""")
    opcao = input("Digite o seu código : ")

    match opcao:
        case "1":
            sexo = input("Digite seu sexo com 'M' ou 'F' : ").upper()
            idade = int(input("Digite sua idade : "))
            salario = float(input("Digite seu sálario : "))
            contador += 1
            soma_do_salario += salario

            if idade > maior_idade :
                maior_idade = idade
            if idade < menor_idade:
                menor_idade = idade
            if sexo == "F" and salario >= 5000:
                mulheres_5k += 1
            
            os.system("cls || clear")
        case "2":
            if contador > 0:
                media_salario_grupo = soma_do_salario / contador
                print("\n Exibindo os resultados = ")
                print(f"Média de salário do grupo : {media_salario_grupo}")
                print(f"Maior idade do grupo : {maior_idade}")
                print(f"Menor idade do grupo : {menor_idade}")
                print(f"Quantidade de Mulheres com salário a partir de 5 mil : {mulheres_5k}")
            else:
                0
        case "3":
            print("\nFinalizando o programa .....")
            time.sleep(3)
            os.system("cls || clear")
        case _:
            print("\nOpção inválida")
            time.sleep(3)
            os.system("cls || clear")