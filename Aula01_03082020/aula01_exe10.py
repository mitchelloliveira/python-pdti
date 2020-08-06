# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 04/08/2020
# --------------------------------------------------------------
# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

temperatura_c = float(input("Informe o valor da temperatura em Celsius: "))
temperatura_f = (temperatura_c * 9 / 5) + 32
print("A temperatura em graus Farenheit é: ", temperatura_f)