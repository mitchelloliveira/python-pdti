# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 05/08/2020
# --------------------------------------------------------------
# Faça um programa que leia e valide as seguintes informações:
#   Nome: maior que 3 caracteres;
#   Idade: entre 0 e 150;
#   Salário: maior que zero;
#   Sexo: 'f' ou 'm';
#   Estado Civil: 's', 'c', 'v', 'd';

iterador = True

while iterador:
    nome = input("Nome: ")
    if len(nome) > 3:
        break
    else:
        print("Nome deve ter mais de 3 letras")

while iterador:
    idade = int(input("Idade: "))
    if idade >= 0 and idade <= 150:
        break
    else:
        print("Idade deve ser entre >= 0 e <= 150")

while iterador:
    salario = float(input("Salário: "))
    if salario > 0:
        break
    else:
        print("O salário deve ser maior que zero.")

while iterador:
    sexo = input("Sexo (F-Feminino|M-Masculino): ")
    if "fm".find(sexo.lower()) >= 0:
        break
    else:
        print("Digite (F) para Feminino ou (M) para Masculino.")

while iterador:
    estado_civil = input("Estado civil (S-solteiro|C-Casado|V-Viúvo|D-Divorciado): ")
    if "scvd".find(estado_civil.lower()) >= 0:
        break
    else:
        print("Digite (S) p/ Solteiro | (C) p/ Casado")

print("\n", "Cadastro realizado com sucesso!")