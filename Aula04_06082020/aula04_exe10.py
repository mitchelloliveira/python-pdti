# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 06/08/2020
# --------------------------------------------------------------
# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor_1 = ["-","-","-","-","-","-","-","-","-","-"]

vetor_2 = ["x","x","x","x","x","x","x","x","x","x"]

vetor_3 = []

for indice in range(0,10):
    vetor_3.append(vetor_1[indice])
    vetor_3.append(vetor_2[indice])

print(vetor_3)