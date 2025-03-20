import os

os.system("cls || clear")

#   Solicitando Dados ao Usuário
while True:
    n1 = int(input("Digite um número : "))
    n2 = int(input("Digite um número : "))
    media = (n1 + n2) / 2
    
    if media < 0 or media >10:
        print("Nota Inválida, tente novamente. \n")
    else:
        break

print(f"Primeira nota informada : {n1}")
print(f"Segunda nota informada : {n2}")
print(f"Média : {media}")