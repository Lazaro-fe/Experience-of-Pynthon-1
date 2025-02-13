import os

os.system("clear") # Limpa o Terminal

#   Solicitando Dados (Entrada)
idade = int(input("Digite sua idade : "))

#   Verificando (Processamento)
if idade < 18: 
    print("Acesso Negado!!")
else:
    print("Acesso Permitido!!")

#   Exibindo dados (Saída)
print("== Fim ==")
