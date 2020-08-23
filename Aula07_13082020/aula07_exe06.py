# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 17/08/2020
# --------------------------------------------------------------
# Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class TV:
    # canal = 13
    # volume = 5

    def __init__(self, canal = 2, volume = 10):
        self.__canal = canal
        self.__volume = volume

    def muda_canal(self, valor):
        lista = [2, 6, 9, 13, 50]
        if valor in lista:
            self.__canal = valor
        else:
            print("Canal não encontrado.")

    def diminui_volume(self):
        self.__volume -= 1
        if self.__volume < 0:
            self.__volume = 0

    def aumenta_volume(self):
        self.__volume += 1
        if self.__volume > 100:
            self.__volume = 100

    def __str__(self):
        return f'Canal: {self.__canal} Volume: {self.__volume}'

tv1 = TV()
tv2 = TV()

tv1.muda_canal(6)
tv2.muda_canal(9)
tv1.diminui_volume()
tv1.diminui_volume()

print(tv1)
print(tv2)





