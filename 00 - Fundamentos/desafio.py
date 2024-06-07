# Desafio sistema bancário #

print("Bem-Vindo ao sistema bancário")

saldo = 0
transacoes = 0
saques_realizados = 0
LIMITE = 500
LIMITE_SAQUES = 3
operacoes = []

while True:
    print("Selecione a ação desejada:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Sair")
    print()
    opcao = input()

    if opcao == "1":
        valor_deposito = float(input("Qual valor você deseja depositar?.: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            operacoes.append(f"Depósito: R$ {valor_deposito:.2f}\n")
        else:
            print("Operação falhou! O valor deve ser maior que 0\n")

    elif opcao == "2":
        valor_saque = float(input("Qual valor você deseja retirar?.: "))

        if valor_saque > saldo or valor_saque > LIMITE or saques_realizados >= LIMITE_SAQUES:
            print("Não foi possível realizar a retirada! O motivo pode ser:")
            print("1 - O valor da retirada é maior que o saldo em conta")
            print("2 - O valor da retirada supera o limite por saque")
            print("3 - O limite de retiradas diária foi atingido")
            print("----- VERIFIQUE SE VOCÊ SE ENQUADRA EM QUALQUER DESSAS SITUAÇÕES")
            print("----- Caso esteja tudo certo entre em contato pelo nosso telefone.: 0800 888 9999 Atendimento das 9h às 18h, em dias úteis.\n")
        elif valor_saque > 0:
            saldo -= valor_saque
            saques_realizados += 1
            operacoes.append(f"Saque: R$ {valor_saque:.2f}\n")
        else:
            print("Operação falhou! O valor informado é inválido.\n")
    
    elif opcao == "3":
        print("\n================ EXTRATO ================\n")
        if len(operacoes) == 0:
            print("Não foram realizadas movimentações.")
            print("==========================================\n")
        else:
            for operacao in operacoes:
                print(f"{operacao}")
            print(f"***Saldo***.: {saldo:.2f}")
            print("==========================================\n")

    elif opcao == "4":
        print("Obrigado por ser nosso cliente! Volte sempre\n")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.\n")