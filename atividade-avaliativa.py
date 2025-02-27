# Limpeza do Terminal
import os
os.system("clear")

# Solicitando os dados ao Usuario
print("""
==============Dias da Semana ===============
codigo    \t Dia da semana
1         \t\tDomingo
2         \t\tSegunda
3         \t\tTerça
4         \t\tQuarta
5         \t\tQuinta
6         \t\tSexta
7         \t\tSábado
""")

opcao = int(input("Digite o código correspondente ao dia da semana : "))

#Verificando

match opcao:# type: ignore
    case 1 :
        dia = "Domingo"
        semana = "Final de semana"
    case 2 :
        dia = "Segunda"
        semana = "Dia útil"
    case 3 :
        dia = "Terça"
        semana = "Dia útil"
    case 4 :
        dia = "Quarta"
        semana = "Dia útil"
    case 5 : 
        dia = "Quinta"
        semana = "Dia útil"
    case 6 :
        dia = "Sexta"
        semana = "Sextouu"
    case 7 :
        dia = "Sábado"
        semana = "Final de Semana"

# Exibindo Resultados 
print()
print(f"Dia da Semana : {dia}")
print(f"Corresponde a : {semana}")