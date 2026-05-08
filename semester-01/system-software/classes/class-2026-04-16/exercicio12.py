# Autor: João Pedro Gomes da Silva Rodrigues

""" Exercício 12: Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês. 

Desconto do IR:

 - Salário Bruto até 900 (inclusive)  
 - isento 
 - Salário Bruto até 1500 (inclusive) 
 - desconto de 5% 
 - Salário Bruto até 2500 (inclusive) 
 - desconto de 10% 
 - Salário Bruto acima de 2500 
 - desconto de 20%  """

valor_hora = float(input("Informe o valor pela hora trabalhada: "))
horas_trabalhadas = float(input("Informe sua quantidade de horas no trabalho: "))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    desconto_ir = 0
elif salario_bruto <= 1500:
    desconto_ir = 0.05
elif salario_bruto <= 2500:
    desconto_ir = 0.1
else:
    desconto_ir = 0.2

valor_ir = salario_bruto * desconto_ir
valor_sindicato = salario_bruto * 0.03
valor_fgts = salario_bruto * 0.11

total_descontos = valor_sindicato + valor_ir
salario_liquido = salario_bruto - total_descontos

print(f"\n----- Folha de Pagamento -----\n")
print(f"Salário Bruto                   : R$ {salario_bruto:>8.2f}")
print(f"(-) IR ({desconto_ir * 100:g}%)                     : R$ {valor_ir:>8.2f}")
print(f"(-) Sindicato (3%)              : R$ {valor_sindicato:>8.2f}")
print(f"FGTS (11%)                      : R$ {valor_fgts:>8.2f}")
print(f"Total de descontos              : R$ {total_descontos:>8.2f}")
print(f"Salário Liquido                 : R$ {salario_liquido:>8.2f}")

