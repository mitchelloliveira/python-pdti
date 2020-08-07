# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 06/08/2020
# --------------------------------------------------------------
# Faça um Programa que leia um vetor A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos do vetor.

a = []
soma_quadrado = 0

for indice in range(1,11):
    numero = int(input(f"Informe o {indice}º número inteiro: "))
    a.append(numero)

    soma_quadrado += numero ** 2

print("A soma dos quadrados dos elementos é: ", soma_quadrado)