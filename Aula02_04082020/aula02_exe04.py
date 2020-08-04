#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Informe uma letra qualquer: ")
vogal = letra.lower() == "a" or letra.lower() == "e" or \
        letra.lower() == "i" or letra.lower() == "o" or letra == "u"
if vogal:
    print("A letra digitada é uma vogal.")
else:
    print("A letra digitada é uma consoante.")