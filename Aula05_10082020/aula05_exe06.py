# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 10/08/2020
# --------------------------------------------------------------
# Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
# Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída.
# Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.
# Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def converter_hora(v_hora, v_minuto):
    simbolo = "a.m."

    if v_hora > 12:
        v_hora = v_hora - 12
        simbolo = "p.m."

    hora_convertida = str(v_hora) + ":" + str(v_minuto) + " " + simbolo

    return hora_convertida

hora = int(input("Informe o valor da hora no formato 24h: "))
minuto = int(input("Informe o valor dos minutos: "))

print(converter_hora(hora, minuto))