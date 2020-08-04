letra = input("Informe uma letra qualquer: ")
vogal = letra == "a" or letra == "A" or letra == "e" or letra == "E" or letra == "i" or letra == "I" or letra == "o" or letra == "O" or letra == "u" or letra == "U"
if vogal:
    print("A letra digitada é uma vogal.")
else:
    print("A letra digitada é uma consoante.")