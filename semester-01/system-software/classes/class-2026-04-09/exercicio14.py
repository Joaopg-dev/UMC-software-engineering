# Autor: João Pedro Gomes da Silva Rodrigues
""" João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas. """

peso = float(input('Informe o peso de peixes adquirido: '))

limite = 50.0

if peso >= limite:
    excesso = peso - limite
    multa = excesso * 4.00

    print(f'Houve um excesso de peso adquirido: {excesso:g}kg. Sendo necesserário pagar uma multa equivalente a: R${multa:.2f}.')
else:
    print(f'Peso de peixes adquirido: OK. \nNão haverá multa.')