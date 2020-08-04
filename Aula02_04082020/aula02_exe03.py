#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

genero = input("Digite F ou M para informa o seu gênero: ")

if genero == "F":
    print("O seu gênero é Feminino.")
elif genero == "M":
    print("O seu gênero é Masculino.")
else:
    print("Sexo inválido.")