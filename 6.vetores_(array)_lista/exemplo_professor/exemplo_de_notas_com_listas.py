# Limpeza de Terminal
import os
os.system("clls || clear")

lista_notas = [] # Criando uma Lista

for i in range(3):
    nota = float(input("Digite uma nota : "))
    lista_notas.append(nota)

media = sum(lista_notas) / 3

# Mostrando cada nota informada
print()
for nota in lista_notas: # ForEach
    print(f"Nota : {nota}")

print()
print(f"Média : {media}")

print()
print(f"Somente a segunda nota : {lista_notas[2]}")