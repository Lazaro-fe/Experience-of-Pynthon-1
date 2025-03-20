import os

os.system("cls || clear")

#   Solicitando Dados ao Usuário
while True:
    n1 = int(input("Digite um número : "))
    if n1 < 0 or n1 >10:
        print("Nota Inválida, tente novamente. \n")
    else:
        break

print(f"Nota informada : {n1}")