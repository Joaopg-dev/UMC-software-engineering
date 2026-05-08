# Autor: João Pedro Gomes da Silva Rodrigues

""" Exercicio 03: Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: 
F - Feminino 
M - Masculino 
Sexo Inválido. """

genero = input("Informe seu gênero [F/M]: ").strip().upper()

if genero == "M":
    print("\nSeu gênero é masculino!\n")
elif genero == "F":
    print("\nSeu gênero é feminino!\n")
else:
    print("\nSexo inválido! Digite novamente.\n")