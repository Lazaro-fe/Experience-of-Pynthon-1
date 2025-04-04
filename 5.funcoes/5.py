#   Limpeza do Terminal
import os
os.system("cls || clear")

#   Pdindo Dados

def converter_metros_para_centimetros(metros):
    cm = metros * 100
    return cm

metros = float(input("Digite uma medida em metros : "))
cm = converter_metros_para_centimetros(metros)
print()
print(f"Comvertendo {metros} metros em centímetros é : {cm} cm.")