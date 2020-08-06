# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 04/08/2020
# --------------------------------------------------------------
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

val_hora = float(input("Informe o valor da sua hora/mês: "))
qtd_horas = float(input("Informe a quantidade de horas trabalhadas por mês: "))
salario = val_hora * qtd_horas
print("O salário corresponde é: ", salario)