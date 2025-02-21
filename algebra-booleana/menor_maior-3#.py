# Limpando o Terminal
import os
os.system("clear")

# Solicitando dados ao usuário

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
terceiro_numero = int(input("Digite o terceiro número: "))

# Verificando maior e menor
maior = max(primeiro_numero, segundo_numero, terceiro_numero)
menor = min(primeiro_numero,segundo_numero,terceiro_numero)
numero = (primeiro_numero, segundo_numero, terceiro_numero)

# Exibindo resultados
print()
print(f"Número: {numero}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")