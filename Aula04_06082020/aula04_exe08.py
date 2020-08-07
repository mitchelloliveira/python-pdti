# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 06/08/2020
# --------------------------------------------------------------
# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.

pessoas = ["maria", "joão", "pedro", "josé", "ester"]
idades = []
alturas = []

for pessoa in pessoas:
    idade = float(input("Digite a idade: "))
    idades.append(idade)

    altura = float(input("Digite a altura: "))
    alturas.append(altura)

print(pessoas)
print(idades)
idades.reverse()
print(idades)

print(alturas)
alturas.reverse()
print(alturas)

