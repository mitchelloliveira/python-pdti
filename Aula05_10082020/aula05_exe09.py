# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 10/08/2020
# --------------------------------------------------------------
# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.


numero = input("Informe um número inteiro: ")

for i in range(len(numero)-1,-1,-1):
    print(numero[i],end="")


