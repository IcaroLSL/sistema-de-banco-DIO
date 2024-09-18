import textwrap
def menu():
    menu = '''
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    =>'''
    return input(textwrap.dedent(menu))    
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo+=valor
        extrato+=f"Depósito: R${valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print('\n@@@ Operação falhou! O valor informado é invalido. @@@')
    return saldo, extrato
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    exedeu_saldo = valor > saldo
    exedeu_limite = valor > limite
    exedeu_saques = numero_saques >= limite_saques
    if exedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo o suficiente. @@@")
    elif exedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque exede o limite. @@@")
    elif exedeu_saques:
        print("\n@@@ Operação falhou! Número maximo de saques exedido. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! Vavor informado é inválido. @@@")
    return saldo, extrato
def exibirExtrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("não foram realizadaa movimentações" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===========================================")
def criarUsuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrarUsuarios(cpf, usuarios)
    if usuario:
        print("\n@@@ Já existe um usuario com esse CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    dataDeNacimento =  input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logadouro, nro - bairo - cidade/sigla estado): ")
    usuarios.append({"nome":nome, "dataDeNacimento":dataDeNacimento, "cpf":cpf, "endereco":endereco})
    print("=== Usuário criado com sucesso! ===")
def filtrarUsuarios(cpf, usuarios):
    usuariosFiltrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuariosFiltrados[0] if usuariosFiltrados else None
def criarConta(agencia, numeroConta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrarUsuarios(cpf, usuarios)
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia":agencia, "numeroConta":numeroConta, "usuario":usuario}
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
def listarContas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t{conta["numeroConta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print("="*100)
        print(textwrap.dedent(linha))
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo=0
    limite=500
    extrato=""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == 'd':
            valor = float(input('Informe o valor do deposito: '))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )
        elif opcao == "e":
            exibirExtrato(saldo, extrato = extrato)
        elif opcao == "nu":
            criarUsuario(usuarios)
        elif opcao == "nc":
            numeroConta = len(contas) + 1
            conta = criarConta(AGENCIA, numeroConta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listarContas(conta)
        elif opcao == "q":
            break
        else:
            print("Operação invalida, por favor selecione novamente  a operação desejada.")
main()