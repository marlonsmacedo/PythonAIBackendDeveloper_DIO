from datetime import datetime
from time import sleep

def menu():
    menu = """
        [c] = Cadastrar novo cliente
        [C] = Criar nova conta
        [VC] = Consultar dados da Conta
        [d] = Depositar
        [s] = Sacar
        [e] = Extrato
        [q] = Sair
    => """

    opcao = input(menu)

    return opcao

def criar_usuário(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            print(f"\n@@@ Cliente. {usuario["nome"]} já existe. Retornando... @@@")
            return
    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado! ===")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            print("\n=== Conta criada com sucesso! ===")
            return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        return print("\n@@@ Usuário não encontrado !!! @@@")

def consultar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']}
        """
        print("=" * 100)
        print(linha)

# Definindo as Funções:
def deposito(saldo, valor, extrato, /):    
    if valor > 0:
        saldo += valor
        extrato += f"{datetime.now()} -  O valor depositado de R${valor:.2f}\n"
    else:
        mensagem = "A operação Falhou! Valor informado é inválido."
        return mensagem
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES): # type: ignore
    """
        Função para retirada de valores (Saque):
        sOMENTE Argumentos  nomeadps --> saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES.
        retorno : saldo e extrato
    """
        # Verifica se o valor do saque excede ao limite do saldo saldo:
    if valor > saldo:
        print("Operação Falhou! Você saldo insuficiente")

    # Verifica se o valor do saque é maior que a restrição de limite (saques limitados à R$500):
    elif valor > limite:
        print("Operação Falhou! Valor do saque acima do limite permitido.")
    
    # Verifica se o limite de saques esatbelecido foi atingido:
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação Falhou! Valor do saque acima do limite permitido.")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"{datetime.now()} - Saque realizado de R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação Falhou! o valor informado é inválido.")
    
    return saldo, extrato

def visualizar_extrato(saldo, numero_saques, LIMITE_SAQUES, *, extrato):
    print("\n============= EXTRATO ===============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print(f"Número de saques disponíveis: {LIMITE_SAQUES - numero_saques}" if numero_saques < 3 else f"Sem Saques disponíveis.")
    print("========================================")

def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    extrato = ''
    saldo = 0
    limite = 500
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Insira o valor que deseja depositar: "))
            saldo, extrato = deposito(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o Valor para saque: "))
            saldo, extrato = saque(
                saldo = saldo,
                valor = valor,
                extrato=extrato,
                limite = limite,
                numero_saques = numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES
                )
        elif opcao == "e":
            visualizar_extrato(saldo, numero_saques, LIMITE_SAQUES, extrato=extrato)
        elif opcao == "c":
            print('Cadastrar NOVO CLIENTE')
            criar_usuário(usuarios)
        elif opcao == "vc":
            print('CONSULTAR DADOS CLIENTE')
            criar_usuário(usuarios)
        elif opcao == "C":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
        elif opcao == "VC":
            consultar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            sleep(3)

main()
    
    