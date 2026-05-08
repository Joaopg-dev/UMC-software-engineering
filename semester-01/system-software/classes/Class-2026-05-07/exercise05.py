# Autor: João Pedro Gomes da Silva Rodrigues

# Exercicio 05: Faça um programa, utilizando while e listas, que permita o usuário realizar o cadastro de um número indeterminado de pessoas enquanto quiser e os mostre na tela ao finalizar.

print("CADASTRO - PYTHON JOBS\n")

print("DIGITE 0 PARA FINALIZAR O CADASTRO: \n")

funcionarios = []
contador = 1

while True:
    funcionario = input(f"Funcionário {contador}: ").lower()

    if funcionario.lower() == "0":
        break

    funcionarios.append(funcionario)
    contador += 1

print(f"\nfuncionários: {funcionarios}", end=" ")