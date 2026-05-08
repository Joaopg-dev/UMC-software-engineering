# Autor: João Pedro Gomes da Silva Rodrigues
# Exercicio 07: Faça um programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números. 

numeros = []
soma = 0
multiplicacao = 1

for num in range(1, 6):
    while True:
        try:
            numero = int(input(f"Informe o {num} número: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Entrada inválida: Digite um número inteiro.")

for n in numeros:
    soma += n
    multiplicacao *= n

print("-" * 30)
print(f"Números digitados: {', '.join(map(str, numeros))}")
print(f"Soma total: {soma}")
print(f"Multiplicação total: {multiplicacao}")