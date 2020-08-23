import random

numero_escolhido = random.randint(1, 99)
tentativas = 1

chute = -1
while chute != numero_escolhido:
    print(f'Tentativa {tentativas}')
    chute = int(input("Chute um número: "))
    if chute == numero_escolhido:
        print("Parabéns, você acertou")
    else:
        if tentativas <= 5:
            if chute < numero_escolhido:
                print(f"O número é maior que {chute}")
            else:
                print(f"O número é menor que {chute}")
    tentativas += 1
    if tentativas > 5:
        print(f"Você perdeu, o número secreto era {numero_escolhido}")
        break
print("Game Over")
