# Autor: João Pedro Gomes da Silva Rodrigues

""" Exercício 04: Faça um programa que verifique se uma letra digitada é vogal ou consoante.  """

letra = input("Digite uma letra: ").strip().upper()

vogal = ["A", "E", "I", "O","U"]
consoante = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

if letra in vogal:
    print(f"\nA letra {letra} é uma vogal!\n")
elif letra in consoante:
    print(f"\nA letra {letra} é uma consoante!\n")
else:
    print("\nIsso não é uma letra. \nTente novamente.\n")