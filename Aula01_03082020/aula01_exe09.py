# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 04/08/2020
# --------------------------------------------------------------
# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# Fórmula: C = 5 * ((F-32) / 9).

temperatura_f = float(input("Informe o valor da temperatura em Farenheit: "))
temperatura_c = 5*((temperatura_f-32)/9)
print("A temperatura em graus Celsius é: ", temperatura_c)