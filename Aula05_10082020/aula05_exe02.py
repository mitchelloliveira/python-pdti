# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 10/08/2020
# --------------------------------------------------------------
# Faça um programa para imprimir:
#    1
#    1   2
#    1   2   3
#     .....
#    1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def niveis(numero):
    parada_i = numero + 1
    resposta = ""
    for i in range(1, parada_i):
        parada_j = i+1
        for j in range(1, parada_j):
            resposta += str(j) + " "
        resposta += "\n"

    return resposta

# Início do algoritmo
qtd_niveis = int(input("Informe a quantidade de níveis: "))

print(niveis(qtd_niveis))