# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 06/08/2020
# --------------------------------------------------------------
# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

numeros = []
soma = 0
multiplicacao = 1

for indice in range(1,6):
    numero = input(f"Informe o número {indice}: ")
    numero = int(numero)
    numeros.append(numero)

    soma += numero
    multiplicacao *= numero

print("Soma: ", soma)
print("Multiplicação: ", multiplicacao)
print("Números: ", numeros)