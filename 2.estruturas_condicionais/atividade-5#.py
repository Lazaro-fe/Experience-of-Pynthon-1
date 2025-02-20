import os

os.system("clear") # Limpe o Terminal

# Solicitando os dados 

primeiro_numero = float(input("Digite o primeiro número : "))
segundo_numero = float(input("Digite o segundo número : "))

media = (primeiro_numero + segundo_numero) / 2
soma = (primeiro_numero + segundo_numero)
produto = (primeiro_numero * segundo_numero)

menor_numero = max(primeiro_numero, segundo_numero)
maior_numero = min(primeiro_numero, segundo_numero)

print()
print(f"Media : {media}")
print(f"Soma : {soma}")
print(f"Produto : {produto}")
print(f"Menor número : {menor_numero}")
print(f"Maior número : {maior_numero}")