# Autor: João Pedro Gomes da Silva Rodrigues

""" Exercício 08: Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:  """

preco1 = float(input("Informe o preço do primeiro produto: "))
preco2 = float(input("Informe o preço do segundo produto: "))
preco3 = float(input("Informe o preço do terceiro produto: "))

if preco1 <= preco2 and preco1 <= preco3:
    escolha = "o primeiro produto"
    valor = preco1
elif preco2 <= preco1 and preco2 <= preco3:
    escolha = "o segundo produto"
    valor = preco2
else:
    escolha = "o terceiro produto"
    valor = preco3

print(f"\nVocê deve comprar {escolha}, pois ele custa R$ {valor:.2f} e é o mais barato!")