# Exercício 02: Monte uma matriz 2x2 e calcule a soma dos elementos.

matriz = []
quantidade = 2

for i in range(quantidade):
    linha = []
    for j in range(quantidade):
        num = float(input(f"Digite o {j+1} número: "))
        linha.append(num)
    matriz.append(linha)

print(matriz)