# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 05/08/2020
# --------------------------------------------------------------
# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0

for i in range(1,6):
    numero = float(input("Informe o número {}: ".format(i)))
    soma += numero

media = soma / i
print(soma, media)