def removal(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    saldo = 0
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('x' * 50)
        print("Operação falhou! Você não tem saldo suficiente.")
        print('x' * 50)

    elif excedeu_limite:
        print('x' * 50)
        print("Operação falhou! O valor do saque excede o limite.")
        print('x' * 50)

    elif excedeu_saques:
        print('x' * 50)
        print("Operação falhou! Número máximo de saques excedido.")
        print('x' * 50)

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        print('_' * 50)
        print(f"\nSeu saldo atual é de: R${saldo:.2f}",
              datetime.now())
        print('_' * 50)

    return saldo, extrato
