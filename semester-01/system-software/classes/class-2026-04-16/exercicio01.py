# Autor: João Pedro Gomes da Silva Rodrigues
""" Exercicio 01: Faça um programa que peça dois números e imprima o maior deles.  """

num1 = float(input("Informe o primeiro número: ").strip())
num2 = float(input("Informe o segundo número: ").strip())

if num1 > num2:
    print(f"O maior número digitado foi o: {num1:g}!")
else:
    print(f"O maior número digitado foi o: {num2:g}!")