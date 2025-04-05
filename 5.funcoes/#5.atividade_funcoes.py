import os
os.system("clls || clear")


notas = 0
quantidade_de_notas = 3

def verificar(notas):
    for i in range(3):
        if resultados >= 7:
            print(" Você está Aprovado !!! =) ")
        elif resultados <= 4:
            print(" Você está Reprovado )= ")
        else :
            print("Não foi possivel ver nota")

notas += float(input("Digite uma nota : "))
quantidade_de_notas == notas
resultados = notas / 3
print()
print(f"Média : {resultados:.2f}")