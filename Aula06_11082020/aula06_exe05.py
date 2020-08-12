# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 11/08/2020
# --------------------------------------------------------------
# Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
#
# FULANO
# FULAN
# FULA
# FUL
# FU
# F

nome = "mitchell" #input("Informe seu nome: ")
parada_i = len(nome)
resposta = ""
for i in range(parada_i, -1, -1):
    parada_j = i
    for j in range(0, parada_j):
        resposta = resposta + nome[j]
    resposta += "\n"

print(resposta.upper())