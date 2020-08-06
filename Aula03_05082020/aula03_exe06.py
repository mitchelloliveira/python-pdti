# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 05/08/2020
# --------------------------------------------------------------
# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do outro.

contador = 1
lado_a_lado = ""

while contador <= 20:
    print(contador)
    lado_a_lado = lado_a_lado + str(contador) + ", "
    contador += 1
    
print("\n")
print(lado_a_lado)
