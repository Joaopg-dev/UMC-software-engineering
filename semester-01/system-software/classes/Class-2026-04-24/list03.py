# Autor: João Pedro Gomes da Silva Rodrigues
# Exercicio 03: Faça um programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

for n in range(4):
    while True:
        try: 
            nota = float(input(f"Informe a {n+1}° nota: "))
            
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("ERRO: O número deverá ser entre 0 a 10!")
        except ValueError:
            print("Entrada errada: digite um número real!")
            
soma = sum(notas)
media = soma / len(notas)

print("-" * 50)
print("MÉDIA DAS NOTAS\n")
print(f"Notas digitadas: {notas}")
print(f"Média das notas: {media:.2f}")
print("-" * 50)

