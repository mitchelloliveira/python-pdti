from forca import Forca

jogar = True
jogando = False

while jogar:
    f1 = Forca()
    print("")
    print("Temas")
    print("")
    for temas in f1.lista_temas:
        print(temas)
    print("0. SAIR")
    print("")

    tema = input("Informe o número do tema desejado: ")
    if tema.isdigit():
        tema = int(tema)
        if tema == 0:
            break
        if 1 <= tema <= len(f1.lista_temas):
            f1.set_tema(tema)
            f1.monta_forca()
            f1.mascara()
            print(f1.palavra())
            jogando = True
        else:
            print("Opção inválida!")
            print("Pressione qualquer tecla para continuar")
            input("")
            print("")
            print("")
            print("")
            print("")
            jogando = False
    else:
        print("Não parece ser um número")
        jogando = False

    while jogando:
        letra = input("Digite uma letra ou tecla 0 para recomeçar: ")
        if letra == '0':
            break
        if f1.valida(letra):
            f1.monta_forca()
            print(f1.palavra())
            print("Parabéns. Você venceu.")
            jogar = False
            break

        if f1.tentativas <= 0:
            f1.monta_forca()
            f1.palavra()
            print("Você perdeu.")
            jogar = False
            break
        else:
            f1.monta_forca()
        print(f1.palavra())

print("Game Over!")
