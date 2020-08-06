# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 04/08/2020
# --------------------------------------------------------------
# Faça um Programa que leia três números e mostre o maior deles.

num1 = int(input("Informe o primero número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

if num1 > num2 and num1 > num3:
    print("O maior número é ", num1)
elif num2 > num1 and num2 > num3:
    print("O maior número é ", num2)
elif num3 > num1 and num3 > num2:
    print("O maior número é ", num3)
else:
    print("Os números são iguais.")


