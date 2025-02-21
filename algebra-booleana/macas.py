# Limpeza do Terminal
import os
os.system("clear")

# Solicitando Dados

quantidade_de_macas = int(input("Quantas maçãs foram compradas por você: "))

if quantidade_de_macas < 12 :
    preco_maca = 1.30
else:
    preco_maca = 1.80

valor_total = quantidade_de_macas * preco_maca

# Exibindo resultados

print()
print(f"Valor total da compra R$: {valor_total:.2f}")