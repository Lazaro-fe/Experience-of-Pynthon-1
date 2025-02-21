#   Limpando o Terminal
import os
os.system("clear")

#   Solicitando dados ao usuário
print("""
================ MENU ============
Código \tPrato   \t\tValor
1   \t\tPicanha   \t\t25,00
2   \t\tLasanha    \t\t20,00
3   \t\tStrogonoff  \t\t18,00
4   \t\tBife acebolado \t\t15,00
5   \t\tPão com ovo     \t5,00
""")

opcao = int(input("Digite a sua opcão : "))

#   Verificando
match opcao:
    case 1:
        prato = "Picanha"
        valor = 25
    case 2:
        prato = "Lasanha"
        valor = 20
    case 3:
        prato = "Strogonoff"
        valor = 18
    case 4:
        prato = "Bife acebolado"
        valor = 15
    case 5:
        prato = "Pão com ovo"
        valor = 5
    case _:
        prato = "Opção Inválida"
        valor = 0


#   Exibindo resultados
print()
print(f"Prato escolhido: {prato}")
print(f"Valor: {valor:.2f}")
