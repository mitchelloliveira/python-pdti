from conta import Conta

class ContaCorrente(Conta):

    __tarifa = 1.1

    def __init__(self, titular, saldo = 0.0):
        super().__init__(titular, saldo)

    def sacar(self, valor):
        valor_saque = 0
        valor_saque += valor * self.__tarifa
        super().saque(valor_saque)