# Autor: João Pedro Gomes da Silva Rodrigues
# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

horaSalario = float(input("Informe o valor do salário por hora: "))
horasTrabalhadas = float(input("Informe quantas horas são trabalhadas por mês: "))

salarioBruto = horaSalario * horasTrabalhadas

print(f"O valor de seu salário bruto é: {salarioBruto:g}")