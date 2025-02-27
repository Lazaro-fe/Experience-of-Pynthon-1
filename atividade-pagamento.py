# Limpeza do Terminal
import os
os.system("clear")

# Solicitando dados ao Usuário

valor_do_produto_comprado = float(input("Digite o valor do produto comprado : "))

print("""
            //========FORMA DE PAGAMENTO========\\
                1-Á VISTA
                2-Parcelado
""")
print()

pagamento = int(input("Digite sua forma de pagamento : "))

# Verficando 
match pagamento:
    case 1:
        # Obtendo valor do desconto de 10%
        print()
        valor_inicial = valor_do_produto_comprado
        desconto = valor_do_produto_comprado * 0,10
        print(f"Valor obtido : {desconto}")
        print(f"Valor do Produto : {valor_inicial}")
    case 2:
        print()
        parcelas = int(input("Digite a quantidade de parcelas que o você quer :"))
        valor_da_parcela = valor_do_produto_comprado / parcelas
        valor_inicial2 = valor_do_produto_comprado
        print(f"Valor obtido : {valor_da_parcela}")
        print(f"Valor do Produto : {valor_do_produto_comprado}")
        print(f"Valor da Parcela : {valor_da_parcela}")
    case _:
        print()
        print("====OPERAÇÃO INVÁLIDA====")
    