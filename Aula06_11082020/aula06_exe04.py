# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 11/08/2020
# --------------------------------------------------------------
# Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
#
# F
# FU
# FUL
# FULA
# FULAN
# FULANO

nome = "MITCHELL" #input("Informe seu nome: ")
parada_i = len(nome)
resposta = ""
for i in range(0, parada_i):
    parada_j = i+1
    for j in range(0, parada_j):
        resposta = resposta + nome[j]
    resposta += "\n"

print(resposta.upper())

#ou

resposta = ""
for letra in nome:
    resposta += letra
    print(resposta)