# Autor: João Pedro Gomes da Silva Rodrigues

""" Exercício 10: Faça um programa que pergunte em que turno você estuda. Peça para digitar: 

M - Matutino 
V - Vespertino 
N - Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.  """

turno_estudo = input("Qual turno você estuda? \n[M - Matutino]\n[V - Vespertino]\n[N - Noturno]\nResposta: ").strip().upper()

if turno_estudo == 'M':
    print('\nTe desejamos um Bom dia!\n')
elif turno_estudo == "V":
    print('\nTe desejamos uma Boa tarde!\n')
elif turno_estudo == "N":
    print('\nTe desejamos uma Boa noite!\n')
else:
    print('\nValor Inválido!\nTente novamente.\n')