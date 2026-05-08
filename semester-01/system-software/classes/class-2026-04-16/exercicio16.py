# Autor: João Pedro Gomes da Silva Rodrigues

""" Exercício 16: Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações: 

Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado; 

Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa; 

Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário; 

Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;  """

print("--- Calculadora de Equação do 2º Grau ---")

a = float(input("Digite o valor de a: "))

if a == 0:
    print("O valor de 'a' é igual a zero. Programa encerrado.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = (b ** 2) - (4 * a * c)
    print(f"\nDelta calculado: {delta}")

    if delta < 0:
        print("O delta é negativo. A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f"A equação possui apenas uma raiz real: {raiz:.2f}")
    else:
        raiz_delta = delta ** 0.5 
        raiz1 = (-b + raiz_delta) / (2 * a)
        raiz2 = (-b - raiz_delta) / (2 * a)
        
        print(f"A equação possui duas raízes reais:")
        print(f"Raiz 1: {raiz1:.2f}")
        print(f"Raiz 2: {raiz2:.2f}")