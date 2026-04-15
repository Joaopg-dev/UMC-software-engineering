# Autor: João Pedro Gomes da Silva Rodrigues
# Faça um programa que peça as 4 notas bimestrais e mostre a média.

nt1 = float(input("Digite a primeira nota do aluno: "))
nt2 = float(input("Digite a segunda nota do aluno: "))
nt3 = float(input("Digite a terceira nota do aluno: "))
nt4 = float(input("Digite a quarta nota do aluno: "))

media = (nt1 + nt2 + nt3 + nt4) / 4

print(f"A média final do aluno é: {media:g}")
