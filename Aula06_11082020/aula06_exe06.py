# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 11/08/2020
# --------------------------------------------------------------
# Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário
# e imprima a data com o nome do mês por extenso.
#
# Data de Nascimento: 29/10/1973
# Você nasceu em  29 de Outubro de 1973.

def nome_mes(mes):
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
             'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    return meses[mes-1]

def data_extenso(data):
    dia = int(data_nasc[0:2:])
    mes = int(data_nasc[3:5:])
    ano = int(data_nasc[6:10:])
    return f"{dia} de {nome_mes(mes)} de {ano}"

data_nasc = input("Informe sua data de nascimento: ")

print("Você nasceu em", data_extenso(data_nasc))