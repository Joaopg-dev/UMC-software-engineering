# Autor: João Pedro Gomes da Silva Rodrigues

# Exercício 02: Escreva um programa Python que leia um número inteiro do usuário e utilize um laço for para exibir a tabuada desse número de 1 a 10, no formato: '5 x 3 = 15'. Ao final, exiba a soma de todos os resultados da tabuada.

print("\n ---TABUADA DE MULTIPLICAÇÃO--- \n")

num = int(input("Digite um número: "))
soma_total = 0

print("=" * 20)
print(f"TABUADA DO {num}")
print("=" * 20)

for i in range(1, 11):
    resultado = num * i
    soma_total += resultado

    print(f"{i} * {num} = {resultado}")

print(f"A soma total da tabuada é: {soma_total}")