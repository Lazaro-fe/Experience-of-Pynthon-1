#   Limpando o Terminal
import os
os.system("clear")

#   Solicitando dados ao usuário

primeiro_numero = int(input("Digite o primeiro número : "))
segundo_numero = int(input("Digite o segundo número : "))
operacao = input("Digite a operação desejada : ")

#   Verificando

match operacao:
    case"+":
        resultado = primeiro_numero + segundo_numero
    case"-":
        resultado = primeiro_numero - segundo_numero
    case"*":
        resultado = primeiro_numero * segundo_numero
    case"/":
        resultado = primeiro_numero / segundo_numero
    case _:
        print("Opção invalida")
    
#   Exibindo Resultados
print()
print(f"Primeiro número: {primeiro_numero}")
print(f"Operação: {operacao}")
print(f"Segundo número: {segundo_numero}")
print(f"Resultado: {resultado}")