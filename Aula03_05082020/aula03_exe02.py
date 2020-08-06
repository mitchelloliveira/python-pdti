# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 05/08/2020
# --------------------------------------------------------------
# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

iterador = True

while iterador:
    nome = input("Informe o usuário: ")
    senha = input("Informe a senha: ")
    if nome != senha:
        break
    else:
        print("Acesso negado!")

print("Login efetuado com sucesso!")