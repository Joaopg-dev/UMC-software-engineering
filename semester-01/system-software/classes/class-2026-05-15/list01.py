# Exercício 01: Crie uma lista com 5 números e mostre o maior valor.

numeros = []

for i in range(1, 6):
    num = float(input(f"Digite o {i}° número: "))
    numeros.append(num)

maior_número = max(numeros)

print("\n" + "=" * 35)
print(f"O maior número é: {maior_número:g}")
print("=" * 35)