import textwrap
from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    total_clientes = 0

    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []
        Cliente.total_clientes += 1

    def adicionar_conta(self, conta):
        if conta not in self.contas:
            self.contas.append(conta)

    @classmethod
    def quantidade_clientes(cls):
        return cls.total_clientes

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Transacao(ABC):
    def __init__(self, valor):
        self.valor = valor
        self.data = datetime.now()

    @abstractmethod
    def tipo(self):
        pass

class Deposito(Transacao):
    def tipo(self):
        return "Depósito"

class Saque(Transacao):
    def tipo(self):
        return "Saque"

class Conta(ABC):
    agencia_padrao = "0001"

    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = Conta.agencia_padrao
        self._cliente = cliente
        self._historico = Historico()

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

    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self.historico.adicionar_transacao(Deposito(valor))
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        print("\n@@@ Valor inválido para depósito. @@@")
        return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        saques = [t for t in self.historico.transacoes if isinstance(t, Saque)]
        if len(saques) >= self.limite_saques:
            print("\n@@@ Limite de saques atingido. @@@")
            return False
        if valor > self.limite:
            print("\n@@@ Valor excede o limite permitido. @@@")
            return False
        if valor <= 0 or valor > self._saldo:
            print("\n@@@ Valor inválido para saque. @@@")
            return False
        self._saldo -= valor
        self.historico.adicionar_transacao(Saque(valor))
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def __str__(self):
        return f"""\
Agência:\t{self.agencia}
C/C:\t\t{self.numero}
Titular:\t{self.cliente.nome}
Saldo:\t\tR$ {self.saldo:.2f}
"""

class ContaPoupanca(Conta):
    def __init__(self, numero, cliente, rendimento=0.005):
        super().__init__(numero, cliente)
        self.rendimento = rendimento
        self.ultimo_rendimento = datetime.now()

    def sacar(self, valor):
        if valor <= 0 or valor > self._saldo:
            print("\n@@@ Valor inválido para saque. @@@")
            return False
        self._saldo -= valor
        self.historico.adicionar_transacao(Saque(valor))
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def aplicar_rendimento(self):
        hoje = datetime.now()
        if (hoje - self.ultimo_rendimento).days >= 30:
            ganho = self._saldo * self.rendimento
            self._saldo += ganho
            self.historico.adicionar_transacao(Deposito(ganho))
            self.ultimo_rendimento = hoje
            print(f"\n=== Rendimento aplicado: R$ {ganho:.2f} ===")
            return True
        print("\n@@@ Rendimento ainda não disponível. @@@")
        return False

    def __str__(self):
        return f"""\
Agência:\t{self.agencia}
C/C:\t\t{self.numero}
Titular:\t{self.cliente.nome}
Saldo:\t\tR$ {self.saldo:.2f}
"""

# ... (restante do seu código permanece igual)

# Atualize a função listar_contas assim:
contas = []  # Defina a lista de contas globalmente

def listar_contas():
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada. @@@")
        return
    for conta in contas:
        print("=" * 40)
        print(conta)

# Seu loop principal e demais funções seguem iguais

def main():
    while True:
        print("\n=== Sistema Bancário ===")
        print("1 - Listar contas")
        print("2 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            listar_contas()
        elif opcao == "2":
            print("Saindo...")
            break
        else:
            print("\n@@@ Opção inválida. @@@")

if __name__ == "__main__":
    main()


       
