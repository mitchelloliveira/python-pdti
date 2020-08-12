# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 11/08/2020
# --------------------------------------------------------------
# Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se
# feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos.
# Em textos mais complexos os espaços e pontuação são ignorados.
# A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados.
# Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

def palidromo(frase_original):
    frase_original = frase_original.split(" ")
    frase_original = "".join(frase_original)

    frase_invertida = frase_original[::-1]

    if frase_original == frase_invertida:
        print("É um palídromo.")
    else:
        print("Não é um palídromo.")
# fim fincao palindromo ------------------

frase = input("Digite uma frase: ")
palidromo(frase)

