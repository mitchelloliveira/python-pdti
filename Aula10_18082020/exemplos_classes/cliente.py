class Cliente:
    def __init__(self, nome, idade, sexo):
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo

    # def __get_nome(self):
    #     return self.__nome.upper()
    #
    # def __set_nome(self, nome):
    #     self.__nome = nome
    #
    # nome = property(__get_nome(), __set_nome())
    @property
    def nome(self):
        return self.__nome.upper()

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

cl1 = Cliente('Zé', 25, "M")
cl2 = Cliente('Lu', 19, "F")

print(cl1.nome)

cl1.nome = "Biu"
cl2.nome = "Ana"

print(cl1.nome)
print(cl2.nome)