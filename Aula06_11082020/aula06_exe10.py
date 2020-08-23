# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 11/08/2020
# --------------------------------------------------------------
# Número por extenso. Escreva um programa que solicite ao usuário a
# digitação de um número até 99 e imprima-o na tela por extenso.

# Outra regra sugerida pelo professor foi dividir a dezena por 10 e pegar o quociente e o resto.
# Exemplo: 53 / 10 => Quociente 5 e resto 3

unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']

dezenas = ['', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
           'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']

numero = input("Digite numero: ")

extenso = ''

if len(numero) == 1:
    extenso = unidades[int(numero)]
elif len(numero) == 2:
    if int(numero[0]) == 1:
        extenso = dezenas[int(numero[0])+int(numero[1])]
    elif int(numero[1] == 0):
        extenso = dezenas[int(numero[0]) + 9]
    else:
        extenso = dezenas[int(numero[0]) + 9] + " e " + unidades[int(numero[1])]

print(extenso)

