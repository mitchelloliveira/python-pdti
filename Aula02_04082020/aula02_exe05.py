# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 04/08/2020
# --------------------------------------------------------------
# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
#   A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#   A mensagem "Reprovado", se a média for menor do que sete;
#   A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input("Informe a prmeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1+nota2)/2

aprovado_distinicao = media == 10
reprovado = media < 7
if reprovado:
    print("Reprovado")
elif aprovado_distinicao:
    print("Aprovado com distinção")
else:
    print("Aprovado")