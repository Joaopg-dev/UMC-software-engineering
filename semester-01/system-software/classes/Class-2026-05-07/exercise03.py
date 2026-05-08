# Autor: João Pedro Gomes da Silva Rodrigues

# Exercicio 03: Faça um programa, utilizando while e listas, que permita o usuário escrever o nome de cinco pessoas e os mostre na tela.

nomes = []

print("\nDigite os nomes que desejar!")
print("Para sair, digite: 'sair' \n")

while True:
            nome = input(f"Digite um nome: ")
            
            if nome.lower() == "sair":
                break

            nomes.append(nome)

print(f"{nomes}")