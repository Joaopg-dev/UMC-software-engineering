# Autor: João Pedro Gomes da Silva Rodrigues

""" Exercício 05: Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: 

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; 
A mensagem "Reprovado", se a média for menor do que sete; 
A mensagem "Aprovado com Distinção", se a média for igual a dez.  """

aluno = input("Informe o nome do aluno: ").strip()
nota1 = float(input("Digite a primeira nota: ").strip())
nota2 = float(input("Digite a segunda nota: ").strip())

media = (nota1 + nota2) / 2

if media == 10:
    print(f"\nO aluno {aluno} obteve {media:g} de édia! \nAprovado com Distinção!\n")
elif media >= 7:
    print(f"\nO aluno {aluno} obteve {media:g} de média! \nAprovado!\n")
else:
    print(f"\nO aluno {aluno} obteve {media:g} de média! \nReprovado!\n")
