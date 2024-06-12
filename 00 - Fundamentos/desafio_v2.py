import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDeposito
    [2]\tSaque
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [7]\tSair
    => """
    return input(textwrap.dedent(menu))

def exibir_extrato(saldo, /, *, extrato):
    movimento = ""
    for lancamentos in extrato:
        movimento += lancamentos
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else movimento)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def valida_deposito(valor_do_deposito) -> bool:
    return (valor_do_deposito > 0)

def adicionar_movimento_ao_extrato(mov: str, extrato: list):
    extrato.append(mov)

def verifica_disponibilidade_de_saque(saldo, valor_saque, saques_realizados, limite_de_saques, limite_valor_saque) -> list:
    erros = []
    if valor_saque > saldo:
        erros.append("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    if valor_saque > limite_valor_saque:
        erros.append("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    if saques_realizados >= limite_de_saques:
        erros.append("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    return erros

def depositar(saldo, valor, extrato, /):
    if valida_deposito(valor):
        saldo += valor
        adicionar_movimento_ao_extrato(f"Depósito:\tR$ {valor:.2f}\n", extrato)
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo , extrato

def sacar(*, saldo, valor_saque, extrato, limite_saques, saques_realizados, limite_valor_saque):
    erros = verifica_disponibilidade_de_saque(saldo, valor_saque, saques_realizados, limite_saques, limite_valor_saque)
    if not (len(erros) > 0):
        saldo -= valor_saque
        adicionar_movimento_ao_extrato(f"Saque:\t\tR$ {valor_saque:.2f}\n", extrato)
        saques_realizados += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        for err in erros:
            print(err)
    return saldo, extrato

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario in usuarios:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\n
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))    

def main():
    saldo_na_conta = 0
    transacoes = 0
    saques_realizados = 0
    LIMITE = 500
    LIMITE_SAQUES = 3
    extrato = []
    usuarios = []
    contas = []
    AGENCIA = "0001"

    while True:
        opcao = menu()
        if opcao == "1":
            valor_do_deposito = float(input("Informe o valor do depósito: "))
            saldo_na_conta, transacoes = depositar(saldo_na_conta, valor_do_deposito, extrato)

        elif opcao == "2":
            valor_do_saque_informado = float(input("Informe o valor do saque: "))
            saldo_na_conta, extrato = sacar(
                saldo=saldo_na_conta, 
                valor_saque=valor_do_saque_informado, 
                extrato=extrato,
                limite_saques=LIMITE_SAQUES, 
                saques_realizados=saques_realizados, 
                limite_valor_saque=LIMITE)
            
        elif opcao == "3":
            exibir_extrato(saldo_na_conta, extrato=extrato)        

        elif opcao == "4":
            numero_conta = len(contas) + 1
            contas.append(criar_conta(AGENCIA, numero_conta, usuarios))

        elif opcao == "5":
            listar_contas(contas)
        
        elif opcao == "6":
            criar_usuario(usuarios)
    
if __name__ == "__main__":
    main()
