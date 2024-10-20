def deposit(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print('_'*50)
        print(f"\nSeu saldo atual é de: R${saldo:.2f}\n",
              datetime.now())
        print('_' * 50)

    else:
        print('x' * 50)
        print("Operação falhou! O valor informado é inválido.")
        print('x' * 50)

    return saldo, extrato
