# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 05/08/2020
# --------------------------------------------------------------
# Altere o programa anterior permitindo ao usuário informar as populações e as
# taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

pais_a = int(input("Informe a população do país A: "))
taxa_a = float(input("Informe a taxa de crescimento do país A: "))

pais_b = int(input("Informe a população do país B: "))
taxa_b = float(input("Informe a taxa de crescimento do país B: "))

anos = 0

while pais_a < pais_b:
    pais_a = pais_a + pais_a * taxa_a
    pais_b = pais_b + pais_b * taxa_b
    anos += 1

print("\n")
print("O país A tem população de {} com taxa de crescimento de {}%".format(int(pais_a), taxa_a*100))
print("O país B tem população de {} com taxa de crescimento de {}".format(int(pais_b), taxa_b*100))
print("Serão necessários {} anos para que o país A alcence o país B.".format(anos))
