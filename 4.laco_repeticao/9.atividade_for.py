import os
os.system("cls || clear")

# Solicitando os dados ao Usuário
login_cadastrado = "Jucival"
senha_cadastrada = "123"

for i in range(3):

    login = input("Digite seu login : ")
    senha = input("Digite sua senha : ")
    
    if login == login_cadastrado and senha == senha_cadastrada:
        print(" ======== Seja Bem-vindo ========")
        break
    else:
        print("========== Acesso Negado ==========")
        if i == 2:
            print(" ======= Tente novamente =======")

# Exibindo Resultados 

print()
print(f"Login digitado : {login}")
print(f"Senha digitada : {senha}")