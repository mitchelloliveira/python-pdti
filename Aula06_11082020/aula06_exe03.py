# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 11/08/2020
# --------------------------------------------------------------

# Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
#
# F
# U
# L
# A
# N
# O

nome = input("Informe seu nome: ")

nome_lista = list(nome)
print("\n".join(nome_lista))

#ou pode usar o comando for

for i in range(0, len(nome)):
    print(nome[i].upper(),)

#ou

for letra in nome:
    print(letra)