# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 04/08/2020
# --------------------------------------------------------------
# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = int(input("Informe o valor do raio: "))
area = 3.14159 * raio ** 2
print("A área do circulo é: ", area)
print("A área do circulo com raio {} é {} ".format(raio, area))