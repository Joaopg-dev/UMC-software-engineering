# Autor: João Pedro Gomes da Silva Rodrigues
""" Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
O produto do dobro do primeiro com metade do segundo.
A soma do triplo do primeiro com o terceiro.
O terceiro elevado ao cubo. """

numInt1 = int(input('Digite um número inteiro: '))
numInt2 = int(input('Digite outro número inteiro: '))
numReal = float(input('Digite um número real: '))

resultado1 = (numInt1 * 2) + (numInt2 / 2)
resultado2 = (numInt2 * 3) + numReal
resultado3 = numReal ** 3

print('\n--- Resultados ---')
print(f'O produto do dobro do primeiro com metade do segundo: {resultado1:g}.')
print(f'A soma do triplo do primeiro com o terceiro: {resultado2:g}.')
print(f'O terceiro elevado ao cubo: {resultado3:g}.')
