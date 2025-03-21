# LIMPEZA DE TERMINAL
import os
import time
os.system("cls || clear")

notas = 0
quantidade_de_notas = ""

for i in range(quantidade_de_notas):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota : "))
        mais_notas = input("Você quer digitar putra nota ? ")
    

        media = (notas * quantidade_de_notas) / quantidade_de_notas
        
        if mais_notas == "Não":
            print(f"Média : {media}")
        else:
            mais_notas == "Sim"