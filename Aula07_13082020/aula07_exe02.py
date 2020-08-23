# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 17/08/2020
# --------------------------------------------------------------
# Classe Quadrado: Crie uma classe que modele um quadrado:
#
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self,tamanho_lado):
        self.__tamanho_lado = tamanho_lado

    def muda_tamanho_lado(self, novo_tamanho_lado):
        self.__tamanho_lado = novo_tamanho_lado

    def exibe_tamanho_lado(self):
        return self.__tamanho_lado

    def exibe_area(self):
        return self.__tamanho_lado * self.__tamanho_lado

quad = Quadrado(2)
print(quad.exibe_area())

quad.muda_tamanho_lado(5)
print(quad.exibe_area())