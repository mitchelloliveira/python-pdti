
class Tamagushi:

    __nome = ''
    __idade = 0
    __fome = 0
    __saude = 0

    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @property
    def fome(self):
        return self.__fome

    @property
    def saude(self):
        return self.__saude