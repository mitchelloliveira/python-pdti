# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 17/08/2020
# --------------------------------------------------------------
# Classe Retangulo: Crie uma classe que modele um retangulo:
#
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def muda_valor_base(self, valor):
        self.__base = valor

    def muda_valor_altura(self, valor):
        self.__altura = valor

    def exibe_base(self):
        return self.__base

    def exibe_altura(self):
        return self.__altura

    def area(self):
        return self.__base * self.__altura

    def perimetro(self):
        return 2 * (self.__base + self.__altura)

retangulo = Retangulo(2, 5)
print("Área:", retangulo.area())
print("Perímetro:", retangulo.perimetro())
retangulo.muda_valor_base(5)
print("Área:", retangulo.area())
print("Perímetro:", retangulo.perimetro())
retangulo.muda_valor_altura(10)
print("Área:", retangulo.area())
print("Perímetro:", retangulo.perimetro())