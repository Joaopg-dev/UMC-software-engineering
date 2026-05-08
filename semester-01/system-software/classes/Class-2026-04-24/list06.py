# Autor: João Pedro Gomes da Silva Rodrigues
# Exercicio 06: Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0. 


media = []
alunos_acima_media = 0

for alunos in range(1, 11):
    soma_notas = 0
    print(f"--- Notas do Aluno {alunos} ---")
    for nota in range (1, 5):
        while True:
            try:
                notas = float(input(f"Digite a {nota}ª nota: "))

                if 0 <= notas <= 10:
                    soma_notas += notas
                    break
                else:
                    print("Por favor, digite uma nota entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
    
    media_aluno = soma_notas / 4
    media.append(media_aluno)

    if media_aluno >= 7.0:
            alunos_acima_media += 1

print("-" * 30) 
print(f"Médias calculadas: {media}")
print(f"Quantidade de alunos com média >= 7.0: {alunos_acima_media}")