# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 10/08/2020
# --------------------------------------------------------------
# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def somar(num1, num2, num3):
    result = num1 + num2 + num3
    return result

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))
numero3 = int(input("Informe o terceiro número: "))

print(somar(numero1, numero2, numero3))