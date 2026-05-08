# Autor: João Pedro Gomes da Silva Rodrigues

""" Exercício 19: Faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.  """

numero = int(input("Digite um número inteiro menor que 1000: "))

if numero >= 1000 or numero < 0:
    print("Número inválido! Por favor, digite um número entre 0 e 999.")
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    partes = []

    if centenas > 0:
        texto = f"{centenas} centena" + ("s" if centenas > 1 else "")
        partes.append(texto)

    if dezenas > 0:
        texto = f"{dezenas} dezena" + ("s" if dezenas > 1 else "")
        partes.append(texto)

    if unidades > 0:
        texto = f"{unidades} unidade" + ("s" if unidades > 1 else "")
        partes.append(texto)

    resultado = ""
    n_partes = len(partes)

    if n_partes == 3:
        resultado = f"{partes[0]}, {partes[1]} e {partes[2]}"
    elif n_partes == 2:
        resultado = f"{partes[0]} e {partes[1]}"
    elif n_partes == 1:
        resultado = partes[0]
    else:
        resultado = "0 unidades"

    print(f"{numero} = {resultado}")