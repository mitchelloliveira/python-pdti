# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 06/08/2020
# --------------------------------------------------------------
# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

numeros = []
par = []
impar = []

for indice in range(1,21):
    numero = input(f"Informe o número {indice}: ")
    numero = int(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
    numeros.append(numero)

print(numeros)
print(par)
print(impar)