# Autor: João Pedro Gomes da Silva Rodrigues
# Exercicio 08: Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idades = []
alturas = []

for i in range(1, 6):
    print(f"\n--- Cadastro número {i} ---\n")
    while True:
        try:
            
            idade = int(input("Informe a idade: "))
            
            idades.append(idade)
            break
        except ValueError:
            print("ERRO: Digite uma idade válida.\n")
    while True:
        try:
            alt = float(input("Informe a altura: ").
            replace(",", "."))

            alturas.append(alt)
            break
        except ValueError:
            print("ERRO: Digite uma altura válida.\n")

print("\n" + "="*30)
print(f"Idades (ordem inversa): {idades[::-1]}")
print(f"Alturas (ordem inversa): {alturas[::-1]}")
print("="*30)
