# Autor: João Pedro Gomes da Silva Rodrigues
""" Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:
Para Megabytes: Gigabytes * 1024
Para Kilobytes: Gigabytes * 1024 * 1024
Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes """

arqGiga = float(input('Informe o tamaanho do arquivo em Gigabytes: '))

arqMega = arqGiga * 1024
arqKilo = arqGiga * 1024 * 1024

print(f'\n--- Resultado da conversão ---')
print(f'Tamanho em Gigabytes: {arqGiga:g}')
print(f'Tamanho em Megabytes: {arqMega:.2f}')
print(f'Tamanho em Kilobytes: {arqKilo:.2f}')