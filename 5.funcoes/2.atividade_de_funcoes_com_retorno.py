import os
os.system("clls || clear")


nota = float(input("Digite uma nota : "))
quantidade_de_notas = 3

def verificar():
    for i in range(3):
        if resultados >= 7:
            print(" Você está Aprovado !!! =) ")
        elif resultados <= 4:
            print(" Você está Reprovado )= ")
        else :
            print("Não foi possivel ver nota")

nota += float(input("Digite uma nota : "))
quantidade_de_notas == nota
resultados = nota / 3
print()
print(f"Média : {resultados:.2f}")