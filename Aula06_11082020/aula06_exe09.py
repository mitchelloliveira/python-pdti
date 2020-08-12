# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 11/08/2020
# --------------------------------------------------------------
# Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF
# no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação
# dos dígitos verificadores edos caracteres de formatação.

def valida_cpf(cpf):
    # 999.999.999-99
    if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        return False
    so_numeros = cpf.replace('.','').replace('-','')
    contador = 10
    soma = 0
    for digito in so_numeros:
        if contador > 1:
            soma += int(digito) * contador
            contador -= 1

    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0

    if digito1 != int(so_numeros[9]):
        return False

    contador = 11
    soma = 0
    for digito in so_numeros:
        if contador > 1:
            soma += int(digito) * contador
            contador -= 1

    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0

    if digito2 == int(so_numeros):
        return False

    return True

cpf = input("Informe seu CPF: ")


if valida_cpf(cpf):
    print("válido.")
else:
    print("inválido.")