# Autor: João Pedro Gomes da Silva Rodrigues
# Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

tempF = float(input('Informe a temperatura em Graus Fahrenheit:'))

tempC = ((tempF - 32)*5) / 9

print(f'A conversão foi de {tempF} graus Fahrennheit para {tempC} graus Celsius')