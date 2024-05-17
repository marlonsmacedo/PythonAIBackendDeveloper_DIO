from datetime import datetime
from time import sleep

menu = """
[d] = Depositar
[s] = Sacar
[e] = Extrato
[q] = Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        
        deposito = float(input("Insira o valor que deseja depositar: "))
        
        if deposito > 0:
            saldo += deposito
            extrato += f"{datetime.now()} -  O valor depositado de R${deposito:.2f}\n"
        else:
            print("A operação Falhou! Valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o Valor para saque: "))

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

    elif opcao == "e":
        print("\n============= EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(f"Número de saques disponíveis: {LIMITE_SAQUES - numero_saques}" if numero_saques < 3 else f"Sem Saques disponíveis.")
        print("========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        sleep(3)



    
    