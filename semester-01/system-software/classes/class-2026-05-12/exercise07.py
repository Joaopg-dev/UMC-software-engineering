# Exercício 07: Crie uma calculadora que resolva as quatro operações (soma, subtração, multiplicação e divisão). O programa deve perguntar qual operação o usuário quer resolver, receber dois números, e efetuar a operação. Em seguida, o programa pergunta novamente qual operação deve ser resolvida. O programa só será finalizado quando o usuário pressionar uma tecla de finalização.

while True:
    print("="*30)
    print("      CALCULADORA PYTHON")
    print("="*30)
    print("Operações disponíveis:")
    print("1: Soma (+)")
    print("2: Subtração (-)")
    print("3: Multiplicação (*)")
    print("4: Divisão (/)")
    print("S: Sair do programa")
    
    opcao = input("\nEscolha a operação ou 'S' para sair: ").upper().strip()

    if opcao == 'S':
        print("Encerrando a calculadora... Até logo!")
        break


    if opcao not in ['1', '2', '3', '4']:
        print("Opção inválida! Tente novamente.")
        continue

    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        if opcao == '1':
            resultado = n1 + n2
            print(f"\nResultado: {n1} + {n2} = {resultado}")
        
        elif opcao == '2':
            resultado = n1 - n2
            print(f"\nResultado: {n1} - {n2} = {resultado}")
            
        elif opcao == '3':
            resultado = n1 * n2
            print(f"\nResultado: {n1} * {n2} = {resultado}")
            
        elif opcao == '4':
            if n2 == 0:
                print("\nErro: Não é possível dividir por zero!")
            else:
                resultado = n1 / n2
                print(f"\nResultado: {n1} / {n2} = {resultado}")

    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos.")