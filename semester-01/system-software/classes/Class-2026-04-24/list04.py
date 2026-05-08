# Autor: João Pedro Gomes da Silva Rodrigues
# Exercicio 04: Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes. 

vetor = []
consoantes = []
vogais = "aeiouáéíóúaeiou"

while True:
    try:
        palavra = input("escreva uma palavra: ").strip().lower()
        
        if 0 <= len(palavra) <= 10:
            vetor.append(palavra)
            break
        else:
            print("ERRO: A palavra deve ter ao máximo de 0 a 10 caracteres!")
    except ValueError:
        print("ERRO: Deverá ser digitado apenas LETRAS!")

for letra in palavra:
    if letra.isalpha() and letra not in vogais:
        consoantes.append(letra)

quantidade = len(consoantes)

print("-" * 50)
print("CONTAGEM DE CONSOANTES\n")
print(f"A palavra {vetor[0]} possui: {quantidade} consoantes!")
print(f"As suas consoantes são: {", ".join(consoantes)}!\n")
print("-" * 50)
