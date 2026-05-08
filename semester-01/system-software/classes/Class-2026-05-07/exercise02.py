# Autor: João Pedro Gomes da Silva Rodrigues

# Exercicio 02: Faça um programa, utilizando while, que mostre na tela de 0 até N, em que Né o limite inserido pelo usuário.

print("=" * 50)
print("CONTADOR DE NÚMEROS")
print("=" * 50)

num = int(input("Informe a quantidade de vezes a ser executado: "))
contador = 0

while contador < num + 1:
    print(contador, end=" ")
    contador += 1 
