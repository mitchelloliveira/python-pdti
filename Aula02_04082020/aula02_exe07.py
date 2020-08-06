# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 04/08/2020
# --------------------------------------------------------------
# Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input("Informe o primero número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

if num1 > num2 and num2 > num3:
    maior = num1
    menor = num3
    print("{} é o maior e {} é o menor".format(maior, menor))
elif num1 > num3 and num3 > num2:
    maior = num1
    menor = num2
    print("{} é o maior e {} é o menor".format(maior, menor))
elif num2 > num1 and num1 > num3:
    maior = num2
    menor = num3
    print("{} é o maior e {} é o menor".format(maior, menor))
elif num2 > num3 and num3 > num1:
    maior = num2
    menor = num1
    print("{} é o maior e {} é o menor".format(maior, menor))
elif num3 > num1 and num1 > num2:
    maior = num3
    menor = num2
    print("{} é o maior e {} é o menor".format(maior, menor))
elif num3 > num2 and num2 > num1:
    maior = num3
    menor = num1
    print("{} é o maior e {} é o menor".format(maior, menor))
else:
    print("Os números são iguais.")