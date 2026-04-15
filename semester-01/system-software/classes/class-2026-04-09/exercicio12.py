# Autor: João Pedro Gomes da Silva Rodrigues
""" Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes"""

arqGiga = float(input('Informe o tamaanho do arquivo em Gigabytes: '))

arqMega = arqGiga * 1024

print(f'\n--- Resultado da conversão ---')
print(f'Tamanho em Gigabytes: {arqGiga:g}')
print(f'Tamanho em Megabytes: {arqMega:.2f}')