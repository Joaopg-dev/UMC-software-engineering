# Autor: João Pedro Gomes da Silva Rodrigues

""" Exercicio 18: Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. """

data = input("Informe uma data no formato dd/mm/aaaa: ")
partes = data.split('/')

# Verificando se o formato básico está correto
if len(partes) != 3:
    print("Formato inválido! Use dd/mm/aaaa.")

else:
    dia = int(partes[0])
    mes = int(partes[1])
    ano = int(partes[2])

    valida = False

    if mes in (1, 3, 5, 7, 8, 10, 12):
        if 1 <= dia <= 31:
            valida = True
    elif mes in (4, 6, 9, 11):
        if 1 <= dia <= 30:
            valida = True
    elif mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if 1 <= dia <= 29:
                valida = True
        else:
            if 1 <= dia <= 28:
                valida = True
    if valida:
        print(f"A data {data} é VÁLIDA.")
    else:
        print(f"A data {data} é INVÁLIDA.")