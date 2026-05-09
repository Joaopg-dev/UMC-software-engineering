# Autor: João Pedro Gomes da Silva Rodrigues

# Exercício 01: Escreva um programa Python que leia o nome (string), idade (int), altura (float). Se os 03 dados estiverem correto o sistema define o aluno como matriculado = “sim”, senão, matriculado = “não“.

print(" ---SISTEMA CADASTRAL DO ALUNO--- ")

nome = input("\nDigite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

validar_nome = len(nome) > 0
validar_idade = 16 <= idade <= 60 
validar_altura = 1.0 <= altura <= 2.5

if validar_nome and validar_idade and validar_altura:
    matriculado = "sim"
else:
    matriculado = "não"

print("\n\nInformações do aluno\n")
print("=" * 20)
print(f"Matriculado: {matriculado}")
print(f"Nome: {nome:>5.5}")
print(f"Idade: {idade}")
print(f"Altura: {altura}")
print("=" * 20)


