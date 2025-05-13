import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Carro:
    marca : str
    modelo : str
    categoria : str
    preco : float

lista_de_carros = []
quantidade_de_carros = 2

print("Informa os dados do carro : ")
for i in range(quantidade_de_carros):
    car = Carro(
        marca = input("Marca : "),
        modelo = input("Modelo : "),
        categoria = input("Categoria : "),
        preco = float(input("Digite o preço do carro : "))
    )
    lista_de_carros.append(car)
    print()

os.system("cls || clear")

print("\n== Exibindo dados do carro ==")
for car in lista_de_carros:
    print(f"Marca : {car.marca}")
    print(f"Modelo : {car.modelo}")
    print(f"Categoria : {car.categoria}")
    print(f"Preço : {car.preco}")
    print()

print("== Salvando os dados dos clientes ==")
nome_do_arquivo = "dados_dos_carros.txt"

with open(nome_do_arquivo, "a") as arquivo:
    for car in lista_de_carros:
        arquivo.write(f"Marca: {car.marca}, Modelo : {car.modelo}, Categoria : {car.categoria}, Preço : R$ {car.preco}\n")

print("\nSalvo com Sucesso!!!!!!!")