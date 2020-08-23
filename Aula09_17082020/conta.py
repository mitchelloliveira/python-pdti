
class Conta:

    __contador_contas = 1

    def __init__(self, titular, saldo = 0.0):
        # atributos
        self.__numero = Conta.__contador_contas
        self.__saldo = saldo
        self.titular = titular
        Conta.__contador_contas += 1

    # aqui vai a indicação que é estático
    @staticmethod
    def contador_contas():
        return Conta.__contador_contas

    # propriedade getter
    @property
    def titular(self):
        return self.__titular.upper()

    # propriedade setter
    @titular.setter
    def titular(self, novo_titular):
        self.__titular = novo_titular

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def deposito(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False

    def saque(self, valor):
        if 0 < valor <= valor:
            self.__saldo -= valor
            return True
        return False

    def transferir(self, valor, conta_destino):
        if self.saque(valor):
            return conta_destino.deposito(valor)
        return False

    def __str__(self):
        return f'Cliente:{self.titular.capitalize()} conta:{self.__numero} saldo:{self.__saldo}'

