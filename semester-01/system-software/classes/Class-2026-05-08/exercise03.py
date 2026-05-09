# Autor: João Pedro Gomes da Silva Rodrigues

# Exercício 03: Escreva um programa Python que inicie com um estoque de 100 unidades. Use um laço while para repetidamente perguntar ao usuário se deseja adicionar ou remover itens (digitando 'a' para adicionar, 'r' para remover ou 'sair' para encerrar). O programa deve impedir que o estoque fique negativo e exibir o estoque atual a cada operação.

estoque = 100

print("SISTEMA DE ESTOQUE")


while True:
    print("Digite para: \n\nAdicionar ao estoque: 'a' \nRemover do estoque: 'r' \nEncerrar Programa: 'sair' ")
    digito = input("\nDigite aqui: ")
    if "a" in digito:
       novas_unidades = int(input("Informe o valor a ser adicionado no estoque: "))
       estoque += novas_unidades
       break
    elif "r" in digito:
        unidades_retiradas = int(input("Informe o valor a ser retirado no estoque: "))
        novo_valor = estoque - unidades_retiradas
        if novo_valor < 0:
            print("Unidades em falta no estoque!")
        else:
            estoque += novo_valor
            break
    elif "sair" in digito:
        print("Encerrando o programa...")
        break
    else:
        print("ERRO: Entrada inválida. Tente novamente.")
        
print(f"Valor do estoque anterior: ")
print(f"Valor do estoque atual: {estoque}")
