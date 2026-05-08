# Autor: João Pedro Gomes da Silva Rodrigues

""" Exercício 09: Faça um programa que leia três números e mostre-os em ordem decrescente: """

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        ordem = [num1, num2, num3]
    else:
        ordem = [num1, num3, num2]

elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        ordem = [num2, num1, num3]
    else:
        ordem = [num2, num3, num1]
        
else: 
    if num1 >= num2:
        ordem = [num3, num1, num2]
    else:
        ordem = [num3, num2, num1]

print(f"A ordem decrescente desses números são: {ordem[0]:g}, {ordem[1]:g}, {ordem[2]:g}.")