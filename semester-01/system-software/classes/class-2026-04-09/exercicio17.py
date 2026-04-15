# Autor: João Pedro Gomes da Silva Rodrigues
""" Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
 """

cobertura_tinta = 6
capacidade_lata = 18
preco_lata = 80.0
capacidade_galao = 3.6
preco_galao = 25.0

tamanho_area = float(input("Informe o tamanho da área em metros quadrados a ser pintada: "))

litros_necessarios = tamanho_area / cobertura_tinta
litros_folga = litros_necessarios * 1.1

qtd_latas_apenas = int(litros_necessarios // capacidade_lata)
if litros_necessarios % capacidade_lata > 0:
    qtd_latas_apenas += 1

preco_total_latas = qtd_latas_apenas * preco_lata

qtd_galoes_apenas = int(litros_necessarios // capacidade_galao)
if litros_necessarios % capacidade_galao > 0:
    qtd_galoes_apenas += 1

preco_total_galoes = qtd_galoes_apenas * preco_galao

qtd_latas_mistas = int(litros_folga // capacidade_lata)
resto_litros = litros_folga % capacidade_lata

qtd_galoes_mistos = int(resto_litros // capacidade_galao)
if resto_litros % capacidade_galao > 0:
    qtd_galoes_mistos += 1

preco_total_misto = (qtd_latas_mistas * preco_lata) + (qtd_galoes_mistos * preco_galao)

print(f"\n--- Resultados para {tamanho_area:.2f} m² ---")

print(f"\n1. Apenas latas de 18L:")
print(f"   Quantidade: {qtd_latas_apenas}")
print(f"   Preço: R$ {preco_total_latas:.2f}")

print(f"\n2. Apenas galões de 3,6L:")
print(f"   Quantidade: {qtd_galoes_apenas}")
print(f"   Preço: R$ {preco_total_galoes:.2f}")

print(f"\n3. Mistura otimizada (com 10% de folga):")
print(f"   Latas de 18L: {qtd_latas_mistas}")
print(f"   Galões de 3,6L: {qtd_galoes_mistos}")
print(f"   Preço total: R$ {preco_total_misto:.2f}")