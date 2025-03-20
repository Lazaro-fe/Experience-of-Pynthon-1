import os 
os.system("cls || clear")

#   Atividade com laço de repetição while
q_d_notas = 5
soma = 0

for i in range(q_d_notas):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota : "))

        if nota < 0 or nota > 10:
            print("Nota inválida, tente novamente. \n")
        else:
            soma += nota
            break

media = soma / q_d_notas

print(f"Média {media}")