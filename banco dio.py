menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>'''
saldo=0
limite=500
extrato=""
numero_saques = 0
LIMITE_SAQUES = 3
while True:
    opcao = input(menu)
    if opcao == 'd':
        valor = float(input('Informe o valor do deposito: '))
        if valor > 0:
            saldo+=valor
            extrato+=f"Depósito: R${valor:.2f}\n"
        else:
            print('Operação falhou! O valor informado é invalido.')
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        exedeu_saldo = valor > saldo
        exedeu_limite = valor > limite
        exedeu_saques = numero_saques >= LIMITE_SAQUES
        if exedeu_saldo:
            print("Operação falhou! Você não tem saldo o suficiente.")
        elif exedeu_limite:
            print("Operação falhou! O valor do saque exede o limite.")
        elif exedeu_saques:
            print("Operação falhou! Número maximo de saques exedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! Vavor informado é inválido.")
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("não foram realizadaa movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")
    elif opcao == "q":
        break
    else:
        print("Operação invalida, por favor selecione novamente  a operação desejada.")