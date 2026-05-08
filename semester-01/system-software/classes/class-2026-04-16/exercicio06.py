# Autor: João Pedro Gomes da Silva Rodrigues

""" Exercício 06: Faça um programa que leia três números e mostre o maior deles:  """

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

if num1 >= num2 and num1 >= num3:
    print(f"O número {num1:g} é o maior deles!")
elif num2 >= num1 and num2 >= num3:
    print(f"O número {num2:g} é o maior deles!")
else:
    print(f"O número {num3:g} é o maior deles!")
