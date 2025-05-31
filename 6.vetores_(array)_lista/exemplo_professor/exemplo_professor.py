import os
os.system('cls || clear')

#   Função para calcular média
def calcular_media(lista):
    #   sum(lista) irá mostrar os valores na lista
    #   len(lista) irá mostrar a quantidade de valores na lista
    media = sum(lista) / len(lista)
    return media

lista_notas = [] #  Criando uma lista
quantidade_notas = 2 #  Criando uma constante

#   Solicitando dados para o Usuário
for i in range(quantidade_notas):
    nota = float(input(f"Digite a {i + 1}º nota : "))
    lista_notas.append(nota)

#   Chamando a função para calcular a média
#   Enviando a lista de notas como parâmetro
#   Inserindo na variável 'media' o cálculo retornado pela função
media = calcular_media(lista_notas)

#   Exibindo a média
print(f"\nMédia : {media}")