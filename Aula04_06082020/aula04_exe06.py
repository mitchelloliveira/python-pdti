# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 06/08/2020
# --------------------------------------------------------------
# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

notas = []
medias = []
alunos = ["maria", "joão", "pedro", "josé","ester", "thiago", "lucas", "sara", "jaco", "abraão"]

total = 0

for aluno in alunos:
    soma = 0
    media = 0
    for indice in range(1,5):
        nota = input(f"Informe a {indice}ª nota de {aluno}: ")
        nota = int(nota)
        notas.append(nota)
        soma += nota

    media = soma / indice
    medias.append(media)

    if media >= 7:
        total += 1

for i in range(0,4):
    print(alunos[i], medias[i])

print("A quantidade de alunos com média >= a 7.0 é: ", total)