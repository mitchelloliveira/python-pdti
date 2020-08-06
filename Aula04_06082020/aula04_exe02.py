# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 06/08/2020
# --------------------------------------------------------------
# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numeros = []

for indice in range(1,11):
    numero = input(f"Informe o número {indice}: ")
    numero = int(numero)
    numeros.append(numero)

numeros.sort(reverse = True)

print(numeros)