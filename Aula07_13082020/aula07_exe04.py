# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 17/08/2020
# --------------------------------------------------------------
# Classe Pessoa: Crie uma classe que modele uma pessoa:
#
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa
# pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    def engordar(self, quilo):
        self.__peso += quilo

    def emagrecer(self, quilo):
        self.__peso -= quilo

    def crescer(self, cm):
        self.__altura += cm

    def envelhecer(self, anos):
        self.__idade += anos
        if self.__idade < 21:
            self.__altura += anos * 0.05

    def exibe_dados(self):
        print(self.__nome)
        print(self.__idade)
        print(self.__peso)
        print(self.__altura)

pessoa1 = Pessoa("Ze", 16, 55, 1.6)
pessoa1.exibe_dados()

pessoa1.emagrecer(1)
pessoa1.envelhecer(2)

pessoa1.exibe_dados()