# Constantes
LIMITE_SAQUE = 300
LIMITE_SAQUES = 3

def menu():
    """
    Exibe o menu de opções e retorna a escolha do usuário.
    """
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    return input(menu).strip().lower()

def depositar(saldo, extrato, transacoes):
    """
    Realiza um depósito na conta e atualiza o extrato.
    
    Args:
        saldo (float): Saldo atual da conta.
        extrato (str): Histórico das transações.
        transacoes (list): Lista de transações.

    Returns:
        tuple: saldo atualizado, extrato atualizado e lista de transações atualizada.
    """
    try:
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            transacoes.append({"tipo": "Depósito", "valor": valor})
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    except ValueError:
        print("Valor inválido! Por favor, insira um número válido.")
    
    return saldo, extrato, transacoes

def sacar(saldo, extrato, transacoes, numero_saques):
    """
    Realiza um saque da conta, respeitando os limites estabelecidos.
    
    Args:
        saldo (float): Saldo atual da conta.
        extrato (str): Histórico das transações.
        transacoes (list): Lista de transações.
        numero_saques (int): Número atual de saques realizados.

    Returns:
        tuple: saldo atualizado, extrato atualizado, lista de transações atualizada e número de saques atualizado.
    """
    try:
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > LIMITE_SAQUE
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {LIMITE_SAQUE:.2f}.")
        elif excedeu_saques:
            print(f"Operação falhou! Número máximo de saques ({LIMITE_SAQUES}) excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            transacoes.append({"tipo": "Saque", "valor": -valor})
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    except ValueError:
        print("Valor inválido! Por favor, insira um número válido.")

    return saldo, extrato, transacoes, numero_saques

def exibir_extrato(saldo, extrato, transacoes):
    """
    Exibe o extrato das transações e o saldo final.

    Args:
        saldo (float): Saldo atual da conta.
        extrato (str): Histórico das transações.
        transacoes (list): Lista de transações.
    """
    print("\n============= EXTRATO ==============")
    
    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in transacoes:
            print(f"{transacao['tipo']}: R$ {transacao['valor']:.2f}")

    print(f"\nSALDO: R$ {saldo:.2f}")
    print("===================================")

def main():
    """
    Função principal que controla o fluxo do sistema bancário.
    """
    saldo = 0
    extrato = ""
    transacoes = []
    numero_saques = 0

    while True:
        opcao = menu()

        if opcao == "d":
            saldo, extrato, transacoes = depositar(saldo, extrato, transacoes)

        elif opcao == "s":
            saldo, extrato, transacoes, numero_saques = sacar(saldo, extrato, transacoes, numero_saques)

        elif opcao == "e":
            exibir_extrato(saldo, extrato, transacoes)

        elif opcao == "q":
            print("Obrigado por utilizar o sistema bancário. Até a próxima!")
            break

        else:
            print("Operação Inválida! Por favor, selecione uma opção válida.")

if __name__ == "__main__":
    main()
