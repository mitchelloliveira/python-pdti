# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 05/08/2020
# --------------------------------------------------------------
# Faça um programa que receba dois números inteiros e
# gere os números inteiros que estão no intervalo compreendido por eles.

numero1 = int(input("Informe o primeiro número inteiro: "))
numero2 = int(input("Informe o segundo número inteiro maior que o primeiro: "))

numero1 += 1

for i in range(numero1, numero2):
    print(i)