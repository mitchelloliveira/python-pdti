# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 17/08/2020
# --------------------------------------------------------------
# Classe Bola: Crie uma classe que modele uma bola:
#
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material): #Por convenção, paravras iniciadas com dois underlines são privadas
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material

    def trocaCor(self, nova_cor):
        self.__cor = nova_cor

    def mostraCor(self):
        return self.__cor

# Testa classe Bola

bola_futebol = Bola("azul", 20, "borracha")

print(bola_futebol.mostraCor())

bola_futebol.trocaCor("amarela")

print(bola_futebol.mostraCor())