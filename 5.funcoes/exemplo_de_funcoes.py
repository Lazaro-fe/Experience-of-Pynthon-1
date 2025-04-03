import os
os.system("cls || clear")

# Função Sem Retorno
# Definindo caracteristicas  da função
def saudacao(nome):
    print(f"Olá, {nome}! Bem-vindo ao curso de Ds!")

def disciplina(nome_disciplina):
    print(f"A disciplina {nome_disciplina} faz parte do curso de Ds")

nome = input("Digite seu nome : ")
nome_disciplina = input("Digite o nome da Disciplina : ")

print()
saudacao(nome) # Chamando Função
disciplina(nome_disciplina) # Chamando Função