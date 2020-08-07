# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 05/08/2020
# --------------------------------------------------------------
# Faça um programa que leia 5 números e informe o maior número.

maior = 0

for i in range(1,6):
    numero = int(input("Informe um número inteiro qualquer: "))

    if numero > maior:
        maior = numero

print("O maior número digitado foi: ", maior)