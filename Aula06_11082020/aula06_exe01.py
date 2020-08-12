# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 11/08/2020
# --------------------------------------------------------------

# Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
#
# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.

texto1 = "Brasil Hexa 2006"
texto2 = "Brasil! Hexa 2006!"

print(texto1,len(texto1),"caracteres")
print(texto2,len(texto2),"caracteres")

conteudo_igual = texto1.lower() == texto2.lower()
tamanho_igual = len(texto1) == len(texto2)

if conteudo_igual:
    print("As duas strings possuem conteúdo iguais.")
else:
    print("As duas strings possuem conteúdo diferente.")

if tamanho_igual:
    print("As duas strings são de tamanhos iguais.")
else:
    print("As duas strings são de tamanhos diferentes.")