# Autor: João Pedro Gomes da Silva Rodrigues

# Exercício 04: Escreva um programa Python que leia 5 notas (float) e armazene-as em uma lista. Usando um laço for,calcule e exiba: a média da turma, a maior nota, a menor nota e quantos alunos foram aprovados (média >= 6.0).


notas = []

print("\n ---CALCULADORA DE MEDIA DOS ALUNOS---\n")

for i in range(5):
    nota = float(input(f"Informe a nota do {i+1}° aluno: "))
    notas.append(nota)

soma = 0
aprovados = 0
maior_nota = notas[0]
menor_nota = notas[0]

for nota in notas:
    soma += nota

    if nota >= 6.0:
        aprovados += 1

    if nota > maior_nota:
        maior_nota = nota
    if nota < menor_nota:
        menor_nota = nota

media_turma = soma / len(notas)

print("-" * 30)
print(f"Média da Turma: {media_turma:.2f}")
print(f"Maior Nota: {maior_nota:.2f}")
print(f"Menor Nota: {menor_nota:.2f}")
print(f"Alunos Aprovados: {aprovados}")






