# Autor: João Pedro Gomes da Silva Rodrigues
# Exercicio 10: Faça um programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. 

vetor1 = []
vetor2 = []
vetor_intercalado = []

print("--- Preenchendo o Primeiro Vetor ---")
for i in range(1, 11):
    while True:
        try:
            num = int(input(f"Vetor 1 - Elemento {i}: "))
            vetor1.append(num)
            break
        except ValueError:
            print("Entrada inválida: Digite um número inteiro")

print("\n--- Preenchendo o Segundo Vetor ---")
for i in range(1, 11):
    while True:
        try:
            num = int(input(f"Vetor 2 - Elemento {i}: "))
            vetor2.append(num)
            break
        except ValueError:
            print("Entrada inválida: Digite um número inteiro")

for i in range(10):
    vetor_intercalado.append(vetor1[i])
    vetor_intercalado.append(vetor2[i])

print("\n" + "="*30)
print(f"Vetor 1: {vetor1}")
print(f"Vetor 2: {vetor2}")
print(f"Vetor Intercalado: {vetor_intercalado}")
print(f"Total de elementos: {len(vetor_intercalado)}")