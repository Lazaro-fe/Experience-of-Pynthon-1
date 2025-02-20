import os

os.system("clear") # Limpe o Terminal

# Solicitando os dados 

primeiro_numero = float(input("Digite o numero : "))
segundo_numero = float(input("Digite o segundo numero : "))

media = (primeiro_numero + segundo_numero) / 2
soma = (primeiro_numero + segundo_numero)
produto = (primeiro_numero * segundo_numero)

if primeiro_numero < segundo_numero:
    print(f"Maior numero é : {segundo_numero}")
elif segundo_numero < primeiro_numero:
    print(f"Maior número é : {primeiro_numero}")
if primeiro_numero < segundo_numero:
    print(f"Menor número é : {primeiro_numero}")
elif segundo_numero < primeiro_numero:
    print(f"Menor número é : {segundo_numero}")
else:
    print("São iguais")

print()
print(f"Media : {media}")
print(f"Soma : {soma}")
print(f"Produto : {produto:.2f}")