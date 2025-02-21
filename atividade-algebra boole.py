# Limpando o Terminal
import os
os.system("clear")

# Solicitando dados ao usuário

primeiro_numero = float(input("Digite o primeiro número : "))
segundo_numero = float(input("Digite o segundo número : "))

maior_numero = max(primeiro_numero, segundo_numero)
menor_numero = min(primeiro_numero, segundo_numero)

# Apresentação dos dados 

print(f"Maior número : {maior_numero}")
print(f"Menor número : {menor_numero}")