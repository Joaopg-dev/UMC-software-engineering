# Exercício 01: Faça um programa para gerar os n primeiros termos da sequência: 1 1 2 3 5 8 13 21 ...


def gerar_fibonacci(n):

    a, b = 1, 1
    cont = 0

    if n <= 0:
        print("Por favor, insira um número maior que zero.")
    elif n == 1:
        print(a)
    else:
        while cont < n:
            print(a, end=' ')
            
            a, b = b, a + b
            cont += 1

n = int(input("Quantos termos você deseja gerar? "))
gerar_fibonacci(n)