# Autor: João Pedro Gomes da Silva Rodrigues

# Exercício 03: Escreva um programa Python que inicie com um estoque de 100 unidades. Use um laço while para repetidamente perguntar ao usuário se deseja adicionar ou remover itens (digitando 'a' para adicionar, 'r' para remover ou 'sair' para encerrar). O programa deve impedir que o estoque fique negativo e exibir o estoque atual a cada operação.

estoque = 100
estoque_inicial = estoque

print("=" * 20)
print("SISTEMA DE ESTOQUE")
print("=" * 20)

while True:
    print("\n'a' - Adicionar\n'r' - Remover  \n'sair' - Encerrar")
    digito = input("\nDigite sua opção: ").lower().strip()

    if digito == "a":
       quantidade = int(input("Informe o valor a ser adicionado no estoque: "))
       estoque += quantidade
    
    elif digito == "r":
        quantidade = int(input("Informe o valor a ser retirado no estoque: \n"))
        if quantidade > estoque:
            print("Unidades em falta no estoque!")
        else:
            estoque -= quantidade

    elif "sair" == digito:
        print("Encerrando o programa...")
        break
    else:
        print("ERRO: Entrada inválida. Tente novamente.")

print("\n" + "=" * 20)
print(" ---RESULTADO FINAL--- ")
print(f"Valor do estoque anterior: {estoque_inicial}")
print(f"Valor do estoque atual: {estoque}")
print("=" * 20)