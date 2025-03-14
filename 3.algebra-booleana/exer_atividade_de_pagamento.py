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

# Verificando 

match case :
    case 1:
        print