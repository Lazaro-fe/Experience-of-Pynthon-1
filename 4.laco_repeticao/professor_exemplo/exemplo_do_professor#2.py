import os 
os.system("cls || clear")

#   Atividade com laço de repetição while
QUANTIDADE_NOTAS = 2
soma = 0

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota : "))

        if nota < 0 or nota > 10:
            print("Nota inválida, tente novamente. \n")
        else:
            soma += nota
            break

media = soma / QUANTIDADE_NOTAS

print(f"Média {media}")