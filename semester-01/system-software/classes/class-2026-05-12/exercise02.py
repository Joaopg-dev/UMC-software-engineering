# Exercício 02: Faça um programa que receba o valor de  e o valor de  e imprima todos os membros do somatório, e diga qual é o resultado da soma.


r = float(input("Digite o valor de r (número real): "))
n = int(input("Digite o valor de N (número natural): "))

termos = []
soma_total = 0


for i in range(n + 1):
    valor_termo = r ** i
    termos.append(str(valor_termo))
    soma_total += valor_termo

print(f"S_{n} = {' + '.join(termos)} = {soma_total}")