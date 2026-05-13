# Exercício 04: Receba N números do usuário e calcule a média aritmética.

n = int(input("Quantos números você deseja inserir? "))

if n <= 0:
    print("A quantidade deve ser maior que zero.")
else:
    soma = 0
    for i in range(n):
        num = float(input(f"Digite o {i+1}º número: "))
        soma += num

    media = soma / n
    print(f"\nA média aritmética dos {n} números é: {media:.2f}")