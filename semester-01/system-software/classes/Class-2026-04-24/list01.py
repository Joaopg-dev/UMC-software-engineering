# Autor: João Pedro Gomes da Silva Rodrigues
# Exercicio 01: Faça um programa que leia um vetor de 5 números inteiros e mostre-os. 

vetor = []

for v in range(1,6):
    num = int(input(f"Informe o {v}° número: "))
    vetor.append(num)

print(vetor)