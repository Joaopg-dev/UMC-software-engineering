# Autor: João Pedro Gomes da Silva Rodrigues

# Exercício 06: Escreva um programa Python com uma lista de compras inicialmente vazia. Use um laço while com um menu de opções: 1) Adicionar item (string), 2) Remover item pelo nome, 3) Listar todos os itens com numeração, 4) Sair. Trate o caso em que o usuário tenta remover um item que não existe na lista.

lista_de_compras = []

while True:
    print("\n---LISTA DE COMPRAS---\n")
    print("1) Adicionar item")
    print("2) Remover item pelo nome")
    print("3) Listar todos os itens com numeração")
    print("4) Sair")
    
    resposta = input("\nInforme sua resposta (1/2/3/4): ")

    if resposta == "1":
        item = input("\nDigite o nome do item a ser adicionado: ")
        lista_de_compras.append(item)
        print(f"O item '{item}' foi adicionado a lista!")
    
    elif resposta == "2":
        item = input("\nDigite o item que deseja remover: ")
        
        if item in lista_de_compras:
            lista_de_compras.remove(item)
            print(f"O item '{item}' foi removido a lista!")
        else:
            print(f"Erro: O item '{item}' não foi encontrado na lista.")
    
    elif resposta == "3":
        if not lista_de_compras:
            print("Sua lista está vazia: ")
        else:
            print("\nSua lista atual:")
            for contador, item in enumerate(lista_de_compras):
                print(f"{contador + 1}. {item}")
    
    elif resposta == "4":
        print("Encerrando o programa...")
        break
    
    else:
        print("Opção inválida! Escolha entre 1 e 4.")
