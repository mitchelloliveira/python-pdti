# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 17/08/2020
# --------------------------------------------------------------
# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
# Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional,
# com valor default zero e os demais atributos são obrigatórios.

class Conta:

    def __init__(self, numero, nome_correntista, saldo = 0.0):
        self.__numero = numero
        self.__nome_correntista = nome_correntista
        self.__saldo = saldo

    def alterar_nome(self, novo_nome):
        self.__nome_correntista = novo_nome

    def deposito(self, valor):
        if valor > 0.0:
            self.__saldo +=  valor
            return True
        return False

    def saque(self, valor):
        if valor > 0.0  and valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False

    def saldo(self):
        return self.__saldo

    def exibe_dados(self):
        print(self.__numero)
        print(self.__nome_correntista)
        print(self.__saldo)

    def transferir(self, valor, conta):
        if self.saque(valor):
            return conta.deposito(valor)
        return False

conta1 = Conta(222, "maria", 1000.0)
conta2 = Conta(333, "josé")
conta1.exibe_dados()
conta2.exibe_dados()
print("")
print(conta1.saldo())
conta1.deposito(500.0)
print(conta1.saldo())
print("")
conta1.saque(500.0)
print(conta1.saldo())
print(conta2.saldo())
conta1.transferir(500, conta2)
print(conta1.saldo())
print(conta2.saldo())
conta1.saque(1000)