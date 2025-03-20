import os

os.system("cls || clear")

#   Exemplo de uso do laço de repetição

idade = int(input("Digite sua idade : "))

while idade < 18:
    print("Não autorizado   \nApenas para maiores de 18 anos. \n")
    idade = int(input("Digite sua idade : "))

print("========== Acesso Permitido ==========")
print("Fim")