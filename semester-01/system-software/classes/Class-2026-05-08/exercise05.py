# Autor: João Pedro Gomes da Silva Rodrigues

# Exercício 05: Escreva um programa Python que use um laço while para repetidamente ler um número inteiro positivo everificar se ele é primo, usando um laço for interno para a verificação. Use uma variável booleana para controlar o resultado. Exiba se o número é primo ou não, e pergunte se o usuário deseja verificar outro número.

continuar = 's'

while continuar.lower() == 's':
    print("\n--- Verificador de Números Primos ---")
    num = int(input("Digite um número inteiro positivo: "))

    if num <= 1:
        print(f"O número {num} não é primo (primos são maiores que 1).")
    else:
        e_primo = True 
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                e_primo = False 
                break 
        
        if e_primo:
            print(f"O número {num} é PRIMO!")
        else:
            print(f"O número {num} NÃO é primo.")

    continuar = input("\nDeseja verificar outro número? (s/n): ")

print("Programa encerrado.")