from conta import Conta

class ContaPoupanca(Conta):

    __rendimento = 0.1

    def __init__(self, titular, saldo = 0.0):
        super().__init__(titular, saldo)

    def render(self):
        self.set_saldo(self.get_saldo() + self.get_saldo() * self.__rendimento)
        print("")
