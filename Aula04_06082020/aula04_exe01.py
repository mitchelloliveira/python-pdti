# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 06/08/2020
# --------------------------------------------------------------
# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

# numeros = [1,2,3,4,5]
# print(numeros)

numeros = []

for indice in range(5):
    numero = input(f"Informe o número {indice}: ")
    numero = int(numero)
    numeros.append(numero)

print(numeros)