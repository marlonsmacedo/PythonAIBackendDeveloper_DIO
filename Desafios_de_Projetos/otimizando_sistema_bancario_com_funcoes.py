from datetime import datetime
from time import sleep

def menu():
    menu = """
        [c] = Cadastrar novo cliente
        [C] = Criar nova conta
        [d] = Depositar
        [s] = Sacar
        [e] = Extrato
        [q] = Sair
    => """

    opcao = input(menu)

    return opcao


def criar_usuário():
    pass
    return 

def criar_conta(usuario):
    if usuario:
        pass
    return f"Usuário inválido ou Não Existe."

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

def visualizar_extrato(saldo, /, *, extrato ):
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
            visualizar_extrato(saldo, numero_saques, extrato=extrato)
        elif opcao == "c":
            print('Cadastrar NOVO CLIENTE')
            visualizar_extrato()
        elif opcao == "C":
            print('Cadastrar NOVA CONTA')
            visualizar_extrato()
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            sleep(3)
main()
    
    