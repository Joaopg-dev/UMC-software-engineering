# Autor: João Pedro Gomes da Silva Rodrigues

# Exercício 07:  Escreva um programa Python que simule um caixa eletrônico com saldo inicial de R$ 1000.00 (float). Use um laço while para o menu: 1) Saque, 2) Depósito, 3) Extrato, 4) Sair. Armazene cada transação em uma lista de strings. No extrato, use um laço for para exibir todas as transações. Utilize bool para controlar se a sessão está ativa.

saldo = 1000.00
extratos = []

sessao_ativa = True

print("\n---CAIXA ELETRÔNICO---")
print(f"SALDO TOTAL: {saldo}")
while sessao_ativa:
    print("\nMENU\n")
    print("1) Saque")
    print("2) Depósito")
    print("3) Extrato")
    print("4) Sair")

    resposta = input("\nSelecione sua resposta (1/2/3/4): ")

    if resposta == "1":
        valor_saque = float(input("Digite o valor a ser sacado: R$ "))
        if valor_saque <= 0:
            print("Erro: O valor deve ser maior que zero.")
        elif valor_saque <= saldo:
            saldo -= valor_saque
            transacao = f"Saque: R$ {valor_saque:.2f}"
            extratos.append(transacao)

            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
        else:
            print("Erro: Saldo insuficiente.")

    elif resposta == "2":
        valor_deposito = float(input("Digite o valor a ser depositado: R$ "))
        if valor_deposito <= 0:
            print("Erro: O valor deve ser maior que zero.")
        else:
            saldo += valor_deposito
            transacao = f"Depósito: R$ {valor_deposito:.2f}"
            extratos.append(transacao)

            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
    
    elif resposta == "3":
        print("\n---RESUMO DO DIA---\n")
        for contador, extrato in enumerate(extratos):
            print(f"{contador + 1}. {extrato}")
        print(f"\nSaldo final: {saldo}")    
    
    elif resposta == "4":
        print("Encerrando o programa...")
        sessao_ativa = False
    
    else:
        print("Opção inválida! Tente novamente.")
    