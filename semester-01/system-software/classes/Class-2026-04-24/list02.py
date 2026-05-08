# Autor: João Pedro Gomes da Silva Rodrigues
# Exercício 02: Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vetor = []

for v in range(1, 11):
    num = float(input(f"Digite o {v}° número: "))
    vetor.append(num)

print(vetor[::-1])
    
        