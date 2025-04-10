import os
os.system("cls || clear")

peso = float(input("Digite seu peso : "))
altura = float(input("Digite seu altura : "))

def massa():
    al = altura * altura
    imc = peso / al
    return imc

imc = massa()

if imc < 18.5:
    classificacao = "Abaixo do pesso"
    recomendação = "Consulte um nutricionista para Orientação"
    print()
    print(f"Classificação : {classificacao}")
    print(f"Recomendação : {recomendação}")
elif imc >= 18.5 and imc < 24.9:
    classificacao = "Peso Normal"
    recomendação = "Mantenha Hábitos Saudáveis!!"
    print()
    print(f"Classificação : {classificacao}")
    print(f"Recomendação : {recomendação}")
elif imc >= 25 and imc < 29.9:
    classificacao = "Sobrepeso"
    recomendação = "Considere uma dieta balanceada e atividade física"
    print()
    print(f"Classificação : {classificacao}")
    print(f"Recomendação : {recomendação}")
elif imc >= 30 and imc < 34.9:
    classificacao = "Obesidade Grau 1"
    recomendação = "Procure Orientação de um profissional de saúde"
    print()
    print(f"Classificação : {classificacao}")
    print(f"Recomendação : {recomendação}")
elif imc >= 35 and imc < 39.9:
    classificacao = "Obesidade Grau 2"
    recomendação = "Consulte um médico para avaliação e orientação"
    print()
    print(f"Classificação : {classificacao}")
    print(f"Recomendação : {recomendação}")
elif imc > 40:
    classificacao = "Obesidade Grau 3"
    recomendação = "Busque assistência médica imediatamente"
    print()
    print(f"Classificação : {classificacao}")
    print(f"Recomendação : {recomendação}")

print()
print(f"Peso : {peso}")
print(f"Altura : {altura}")
print(f"I.M.C : {imc:.2f}")