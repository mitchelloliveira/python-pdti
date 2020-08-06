# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 04/08/2020
# --------------------------------------------------------------
#Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print("O número {} é maior".format(num1))
elif num2 > num1:
    print("O número {} é maior".format(num2))
else:
    print("Os números são iguais.")