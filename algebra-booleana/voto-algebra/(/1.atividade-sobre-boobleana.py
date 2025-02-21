import os

os.system("clear")

# Solicintando dados ao Usuário

idade = int(input("Qual é sua idade? "))

# Verificando os dados informados pelo Usuário
if idade >= 18 or idade <= 65:
    print("Não é obrigado a votar!")
else:
    print("É obrigado a votar!")

