# Limpeza de Terminal
import os
os.system("clls || clear")

lista_notas = [] # Criando uma Lista

for i in range(4):
    nota = float(input("Digite uma nota : "))
    lista_notas.append(nota)

media = sum(lista_notas) / 4

if nota >= 7:
    print()
    resultado = "Aprovado!!"
elif nota >= 5:
    print()
    resultdo = "Recuperação!!!"
elif nota < 5:
    print()
    resultado = "Reprovado!!!"

print()
for nota in lista_notas:
    print(f"Nota : {nota}")

print()
print(f"Média : {media:.2f}")
print(f"Resultado : {resultado}")