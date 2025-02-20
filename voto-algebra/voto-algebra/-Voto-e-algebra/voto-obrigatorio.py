# Limpando o Terminal
import os
os.system("clear")

# Solicitando dados do Usuário

idade = int(input("Qual é a sua idade?"))

# Processamento

if idade < 16 :
    print("Não podem votar!")
elif idade > 18 :
    print("Voto Opcional!")
if idade <= 65:
    print("Voto obrigatorio!")
else:
    print("Não é obrigado a votar!")