# Exercício 06: Faça um programa que receba duas notas e calcule a média de um aluno. Depois pergunte se ele quer calcular outra média. O programa deve ser rodado ao menos uma vez.

while True:
    num1 = float(input("Informe a primeira nota do aluno: "))
    num2 = float(input("Informe a segunda nota do aluno: "))

    media = (num1 + num2) / 2

    print(f"A média do aluno é: {media:.2f}")

    continuar = input("Deseja continuar (s/n)? ").lower()
    if continuar == 'n':
        print("Encerramento o programa...")
        break
    else:
        continue

