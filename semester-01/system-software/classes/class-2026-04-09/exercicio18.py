# Autor: João Pedro Gomes da Silva Rodrigues
""" Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)
 """
arq_MB = float(input('Informe o tamanho do arquivo para dowmload (MB): '))
velocidade_Mbps = float(input('informe a velocidade '))

tamanho_bits = arq_MB * 8
tempo_seg = tamanho_bits / velocidade_Mbps
tempo_min = tempo_seg / 60

print(f"\nO tempo aproximado de download é de: {tempo_min:.2f} minutos")