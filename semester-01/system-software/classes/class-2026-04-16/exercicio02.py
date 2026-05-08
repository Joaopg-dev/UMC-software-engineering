# Autor: João Pedro Gomes da Silva Rodrigues

""" Exercicio 02: Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo. """

num = float(input("Informe um número: ").strip())

if num > 0:
    print(f"\nO número {num:g} é um número positivo!\n")
elif num < 0:
    print(f"\nO número {num:g} é um número negativo!\n")
else:
    print(f"\nO número zero é um valor neutro.\n")