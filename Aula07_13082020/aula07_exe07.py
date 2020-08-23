# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 17/08/2020
# --------------------------------------------------------------
# Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
#
# Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
# Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi,
# este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado,
# então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.

class Tamagushi:
    def __init__(self, nome, idade = 1, fome = 50, saude = 100):
        self.__nome = nome
        self.__fome = fome
        self.__saude = saude
        self.__idade = idade

    # NOME --------------------------------------
    def retornar_nome(self):
        return self.__nome

    def alterar_nome(self, novo_nome):
        self.__nome = novo_nome

    # FOME --------------------------------------
    def retornar_fome(self):
        return f'{self.__fome * 100 / 100}%'

    def alterar_fome(self, alimento, percentual = 1):
        if alimento:
            self.__fome += self.__fome * percentual / 100
        else:
            self.__fome -= self.__fome * percentual / 100

        if self.__fome > 100:
            self.__fome = 100

        if self.__fome <= 0:
            return False

        return True

    # SAUDE -------------------------------------
    def retornar_saude(self):
        return f'{self.__saude * 100 / 100}%'

    def alterar_saude(self, saude, percentual = 1):
        if saude:
            self.__saude += self.__saude * percentual / 100
        else:
            self.__saude -= self.__saude * percentual / 100

        if self.__saude > 100:
            self.__saude = 100

        if self.__saude <= 0:
            return False

        return True

    # IDADE -------------------------------------
    def retornar_idade(self):
        return self.__idade

    def alterar_idade(self):
        self.__idade += 1
        idade = self.__idade
        if idade <= 12:
            self.alterar_saude(True, 30)
            self.alterar_fome(False, 1)
        elif idade <= 20:
            self.alterar_saude(True, 20)
            self.alterar_fome(False, 5)
        elif idade <= 30:
            self.alterar_saude(True, 10)
            self.alterar_fome(False, 10)
        elif idade <= 50:
            self.alterar_saude(True, 5)
            self.alterar_fome(False, 20)
        else:
            self.alterar_saude(True, 1)
            self.alterar_fome(False, 30)

    # Risco ------------------------------------
    def risco(self):
        self.alterar_fome(True, 20)
        self.alterar_saude(False, 20)

    # Status ------------------------------------
    def status(self):
        print("")
        print("Nome:",self.retornar_nome())
        print("Idade:",self.retornar_idade())
        print("Fome:",self.retornar_fome())
        print("Saúde:",self.retornar_saude())


    # Aniversáveio -----------------------------
    def aniversario(self):
        self.__idade();

    # Humor ------------------------------------
    def humor(self):

bv1 = Tamagushi("Zé",18)

bv1.status()
bv1.alterar_idade()
bv1.status()
bv1.alterar_idade()
bv1.status()
bv1.alterar_idade()
bv1.status()
bv1.risco()
bv1.status()
bv1.risco()
bv1.status()
