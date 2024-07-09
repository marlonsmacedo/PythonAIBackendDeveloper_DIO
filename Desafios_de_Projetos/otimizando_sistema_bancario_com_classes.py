from abc import ABC, abstractmethod
from datetime import datetime
from time import sleep

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Transacao(ABC):
    @property
    @abstractmethod # Python 3.12.2 Deprecated warning with @abstractproperty, change to @abstractmethod
    def valor(self):
        pass

    @classmethod
    @abstractmethod # Python 3.12.2 Deprecated warning with @abstractproperty, change to @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


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
    print(f"Número de saques disponíveis: {LIMITE_SAQUES - numero_saques}" if numero_saques < 3 else "Sem Saques disponíveis.")
    print("========================================")

def main():
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
    
    