import os

os.system("clear") #Limpa o Terminal

# Solicitando os dados para o usuário
nome = input("Qual o seu nome ? ")
teste = float(input("Digite a nota de seu teste : "))
prova  = float(input("Digite a nota da sua prova : "))
qualitativo = float(input("Digite seu qualitativo : "))

media = (teste + prova + qualitativo) / 3

if media < 7:
    print("Reprovado!")
else: 
    print("Aprovado!(=")

print()
print(f"Nome : {nome}")
print(f"Media Escolar : {media:.1f}")




