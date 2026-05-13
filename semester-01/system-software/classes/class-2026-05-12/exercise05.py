# Exercício 05: Crie um algoritmo que, dado um número informado pelo usuário, imprima a tabuada dele de 1 a 10. Use o formato de apresentação (considerando que o usuário informou o número 5):

num = int(input("Informe o número que deseja: "))

print(f"---TABUADA DO {num}---")

for i in range(1, 11):
    resultado = num * i
    print(f"{num} * {i} = {resultado}")