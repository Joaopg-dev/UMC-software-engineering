# Autor: João Pedro Gomes da Silva Rodrigues

""" Exercício 15: Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 

Dicas: 

Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro; 
Triângulo Equilátero: três lados iguais; 
Triângulo Isósceles: quaisquer dois lados iguais; 
Triângulo Escaleno: três lados diferentes;  """

lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

e_triangulo = (lado1 + lado2 > lado3) and \
              (lado1 + lado3 > lado2) and \
              (lado2 + lado3 > lado1)

if e_triangulo:
    print("\nOs valores informados FORMAM um triângulo.")
    if lado1 == lado2 == lado3:
        print("Tipo: Equilátero (Três lados iguais)")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Tipo: Isósceles (Dois lados iguais)")
    else:
        print("Tipo: Escaleno (Três lados diferentes)")
else:
    print("\nOs valores informados NÃO podem formar um triângulo.")