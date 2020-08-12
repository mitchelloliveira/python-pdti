# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 10/08/2020
# --------------------------------------------------------------
# Faça um programa com uma função chamada soma_imposto.
# A função possui dois parâmetros formais: taxa_imposto,
# que é a quantia de imposto sobre vendas expressa em porcentagem e custo,
# que é o custo de um item antes do imposto.
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

def soma_imposto(taxa_imposto, custo):
    valor_final = custo + (taxa_imposto * custo)
    return valor_final

taxa = float(input("Informe o valor da Taxa: "))
custo_inicial = float(input("Informe o valor do custo inicial: "))

print("O valor final do produto é ", soma_imposto(taxa, custo_inicial))