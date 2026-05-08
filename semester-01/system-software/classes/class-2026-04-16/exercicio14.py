# Autor: João Pedro Gomes da Silva Rodrigues

""" Exercício 14: Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo: 

Média de Aproveitamento Conceito 

Entre 9.0 e 10.0         A 
Entre 7.5 e 9.0          B 
Entre 6.0 e 7.5          C 
Entre 4.0 e 6.0          D 
Entre 4.0 e zero         E 

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.  """

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


media = (nota1 + nota2) / 2

if 9.0 <= media <= 10.0:
    conceito = "A"
elif 7.5 <= media < 9.0:
    conceito = "B"
elif 6.0 <= media < 7.5:
    conceito = "C"
elif 4.0 <= media < 6.0:
    conceito = "D"
else:
    conceito = "E"

if conceito in ("A", "B", "C"):
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"


print(f"\n-----RELATÓRIO DO ALUNO-----\n")
print(f"Nota 1:          {nota1:>5.1f}")
print(f"Nota 2:          {nota2:>5.1f}")
print(f"Média:           {media:>5.1f}")
print(f"Conceito:        {conceito:>5}")
print(f"Situação:        {situacao}")
