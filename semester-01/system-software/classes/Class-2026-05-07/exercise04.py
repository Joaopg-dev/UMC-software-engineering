# Autor: João Pedro Gomes da Silva Rodrigues

# Exercicio 04: Faça um programa, utilizando while, que permita o usuário fazer contas de adição enquanto quiser.

print("=" * 30)
print("Operação - Adição")
print("=" * 30)

while True:
    try:
        num1 = int(input("\nDigite um número: "))
        num2 = int(input("\nDigite outro número: "))

        adição = num1 + num2

        print(f"\nResultado: {num1} + {num2} = {adição}")

        print("Deseja continuar mais uma soma? [s / n]")
        
        continuar = input("Resposta: ").lower()

        if continuar == "n":
            break
    except ValueError:
        print("ERRO: Entrada inválida. Tente novamente")