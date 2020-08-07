# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 06/08/2020
# --------------------------------------------------------------
# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
soma = 0

for indice in range(1,5):
    nota = input(f"Informe a nota {indice}: ")
    nota = int(nota)
    notas.append(nota)
    soma += nota

media = soma / indice
print(media)

# for i in range(1,5):
#     notas.append(int(input("Informe a {}ª nota: ".format(i))))
#     # nota = int(input("Informe a {}ª nota: ".format(i)))
#     # soma += nota
# for nota in notas:
#     soma += nota
#
# print(soma)