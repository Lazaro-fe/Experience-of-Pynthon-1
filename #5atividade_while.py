import os
os.system("cls || clear")

# Atividade com laço de repetição while

quantidade_de_notas = 3
soma = 0

for i in range(quantidade_de_notas):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota : "))

        if nota < 0 or nota > 10:
            print("Nota inválida, tente novamente. \n")
        else:
            soma += nota
            break

media = soma / quantidade_de_notas

if media >= 7:
    resultado = "Aprovado"
elif media >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

#   Exibindo Resultados

print()
print(f"Média : {media}")
print(f"Resultado : {resultado}")