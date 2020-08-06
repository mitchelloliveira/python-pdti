# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 06/08/2020
# --------------------------------------------------------------
# Faça um Programa que leia um vetor de 10 caracteres e diga quantas consoantes foram lidas.
# Imprima as consoantes.

letras = []
consoantes = []

for indice in range(1,11):
    letra = input("Digite um caractere que ainda não foi usado: ")
    letras.append(letra)

    if "aeiou".find(letra.lower()) == -1: # ou if letra not in "aeiou":
        consoantes.append(letra)

print(consoantes)
