# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Informe o turno em que você estuda (M-Matutino | V-Vespertino | N-Noturno): ")

if turno.lower() == "m":
    mensagem = "Bom dia!"
elif turno.lower() == "v":
    mensagem = "Bom Tarde!"
elif turno.lower() == "n":
    mensagem = "Boa Noite!"
else:
    mensagem = "Opção Inválida!"

print(mensagem)