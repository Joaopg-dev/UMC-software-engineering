# Exercício 08: Faça um programa que receba um número do usuário e imprima todos os números de 0 até ele.

num = int(input("Informe um número: "))

for i in range(num + 1):
    print(i, end=" ")