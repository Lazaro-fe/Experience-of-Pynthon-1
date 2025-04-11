import os
os.system("cls || clear")

valor_da_gorjeta = 0
total = 0
lista_de_pratos = []
lista_de_preco = []

#   Solicitando Dados ao Usuário
while True:

    print("""
    ================ MENU ============
    Código \tPrato   \t\tValor
    1   \t\tPicanha   \t\t25,00
    2   \t\tLasanha    \t\t20,00
    3   \t\tStrogonoff  \t\t18,00
    4   \t\tBife acebolado \t\t15,00
    5   \t\tPão com ovo     \t5,00
    """)

    opcao = int(input("Digite o número da sua opcão : "))

    match opcao:
        case 1:
            prato = "Picanha"
            valor = 25
            lista_de_pratos.append(prato)
            lista_de_preco.append(valor)
        case 2:
            prato = "Lasanha"
            valor = 20
            lista_de_pratos.append(prato)
            lista_de_preco.append(valor)
        case 3:
            prato = "Strogonoff"
            valor = 18
            lista_de_pratos.append(prato)
            lista_de_preco.append(valor)
        case 4:
            prato = "Bife acebolado"
            valor = 15
            lista_de_pratos.append(prato)
            lista_de_preco.append(valor)
        case 5:
            prato = "Pão com ovo"
            valor = 5
            lista_de_pratos.append(prato)
            lista_de_preco.append(valor)

        case _:
            print("Opção Inválida. \nTente Novamente... \n")
            valor = 0

    total = valor
    pratos_solicitados += "," + prato if pratos_solicitados else prato
    pratos_pedidos = input("Deseja fazer um novo pedido ? \nUse 'S' or 'N' para responder : ").lower()

    pratos_solicitados
    if pratos_pedidos == "n":
        break

if total > 0:
    gorjeta_garcom = input("Deseja pagar 10% do valor da sua nota como gorjeta para o garçom ? ")
    if gorjeta_garcom == "s":
        valor_da_gorjeta = total * 0.10

total_a_pagar = total + valor_da_gorjeta

#   Exibindo Resultados

print()
print("\n ======== Valor da Conta ======== ")
print(f"Valor da Gorjeta : R$ {valor_da_gorjeta}")
print(f"Valor total da compra : R$ {total_a_pagar}")