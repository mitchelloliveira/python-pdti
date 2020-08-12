# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 10/08/2020
# --------------------------------------------------------------
# Jogo de Craps. Faça um programa que implemente um jogo de Craps.
# O jogador lança um par de dados, obtendo um valor entre 2 e 12.
# Se, na primeira jogada, você tirar 7 ou 11, você é um "natural" e ganhou.
# Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
# Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
# Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

import random
jogar = "s"
contador = 1
pontuacao = 0

while jogar.lower() == "s":
    print("")
    jogar = input(f"Joagada{contador}-Deseja lançar os dados (S/N): ")
    if jogar.lower() == "n":
        break

    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)

    pontos = dado1+dado2

    print("O valor do dado 1 foi ", dado1)
    print("O valor do dado 2 foi ", dado2)
    print("A soma dos dados deu ", pontos)

    if contador == 1:
        if pontos == 7 or pontos == 11:
            print("Parabéns, você ganhou. Você é um Natural")
            print("O jogo será reiniciado.")
            contador = 0
        elif pontos == 2 or pontos == 3 or pontos == 12:
            print("Craps, você perdeu.")
            print("O jogo será reiniciado.")
            contador = 0
        else:
            print(f"Sua pontuação foi {pontos}")
            print("Você continua no jogo, lance os dados novamente.")
            pontuacao = pontos
    else:
        if pontos == pontuacao:
            print("Parabéns, você tirou uma pontuação igual a sua.")
        elif pontos == 7:
            print(f"Você perdeu. Você tirou a pontuação {pontos} antes de repetir sua pontuação anterior que foi {pontuacao}")
        elif pontos == 11 or pontos == 7:
            print("Você conseguiu 7 ou 11 mas não foi na primeira jogada.")
            print("Mas você continua no jogo, lance os dados novamente.")
        else:
            print("Você continua no jogo, lance os dados novamente.")

    contador += 1
