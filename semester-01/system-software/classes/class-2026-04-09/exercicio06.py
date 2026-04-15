# Autor: João Pedro Gomes da Silva Rodrigues
# Faça um programa que peça o raio de um círculo, calcule e mostre sua área:

import math

raio = int(input("Informe o raio do circulo: "))

area = math.pi * (raio ** 2)

print(f"A área do círculo que possue o raio de {raio:g} é igual a {area:.2f}!")