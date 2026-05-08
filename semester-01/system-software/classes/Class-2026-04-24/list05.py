# Autor: João Pedro Gomes da Silva Rodrigues
# Exercicio 05: Faça um programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores. 

numeros = []
par = []
impar = []

for n in range(1, 21):
    while True:
        try:
            num = int(input(f"Digite o {n}° número: "))
            numeros.append(num)
            if num % 2 == 0:
                par.append(num)
            else: 
                impar.append(num)
            break
        except ValueError:
            print("ERRO: Só é permitido utilizar números inteiros.")

print("-" * 50)
print(f"Números digitados: {numeros}\n")
print(f"Números pares: {par}\n")
print(f"Números impares: {impar}")
print("-" * 50)