# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 05/08/2020
# --------------------------------------------------------------
# Supondo que a população de um país A seja da ordem de 80000 habitantes
# com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes
# com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população
# do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

pais_a = 80000
pais_b = 200000
taxa_a = 0.03
taxa_b = 0.015
anos = 0

while pais_a < pais_b:
    pais_a = pais_a + pais_a * taxa_a
    pais_b = pais_b + pais_b * taxa_b
    anos += 1

print(anos)
