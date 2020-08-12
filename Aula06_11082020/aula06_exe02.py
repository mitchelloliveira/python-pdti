# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 11/08/2020
# --------------------------------------------------------------

# Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar
# o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.
# Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

nome = input("Informe seu nome: ")

# Exemplo 1
print(nome[::-1])

# Exemplo 2
lista = list(nome)
lista.reverse()
print("".join(lista)) #O join junta o conteúdo de uma lista como uma string

# Exemplo 3
for i in range(len(nome)-1,-1,-1):
    print(nome[i].upper(),end="")