# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 10/08/2020
# --------------------------------------------------------------
# Faça um programa, com uma função que necessite de um argumento.
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’,
# se seu argumento for zero ou negativo.

def positivo_negativo(num):
    if num > 0:
        return "P"
    else:
        return "N"

numero = int(input("Informe um número inteiro: "))

print(positivo_negativo(numero))