import os
os.system("cls || clear")

#   Solicitando dados ao Usuário

while True:
    login = input("Digite seu login : ")
    senha = int(input("Digite sua senha : "))
    login_cadastrado = "Lázaro Ramos"
    senha_cadastrada = "310308"

    if login != login_cadastrado and senha != senha_cadastrada:
        print(" Login and senha estão inválidos!!!")
    elif login == login_cadastrado and senha == senha_cadastrada:
        print(" Login e senha estão corretos ")
    else:
        break

# Exibindo resultados

print()
print(f"Login cadastrado : {login}")
print(F"Senha cadastrado : {senha}")