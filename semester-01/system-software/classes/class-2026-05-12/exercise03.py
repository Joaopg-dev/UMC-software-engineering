# Exercício 03: Ler um número e escreva se ele "é primo" ou "não é primo".

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