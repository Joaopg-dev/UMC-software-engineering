# Autor: João Pedro Gomes da Silva Rodrigues
# Exercicio 09: Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

numeros = []
soma_quadrados = 0

for i in range(1, 5):
    while True:
        try:
            num = int(input(f'Informe o {i} número: '))
            numeros.append(num)
            break
        except ValueError:
            print("Entrada inválida: Digite um número inteiro.\n")

for num in numeros:
    soma_quadrados += num ** 2

print(f"Números digitados: {numeros}")
print(f"A soma dos quadrados é: {soma_quadrados}")