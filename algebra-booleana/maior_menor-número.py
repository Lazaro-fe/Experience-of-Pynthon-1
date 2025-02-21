# Limpando o Terminal
import os
os.system("clear")

# Solicitando dados ao usuário
primeiro_numero = int(input("Digite o primeiro número : "))
segundo_numero = int(input("Digite o segundo número : "))

# Verificando maior e menor 
if primeiro_numero > segundo_numero :
    maior = primeiro_numero
    menor = segundo_numero
else:
    maior = segundo_numero
    menor = primeiro_numero

# Exibindo resultados

print()
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")