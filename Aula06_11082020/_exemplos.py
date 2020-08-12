# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 11/08/2020
# --------------------------------------------------------------
# Exemplos diversos

# Função strip
a = " Hello, world "
print(a.strip())

# Função minúscula
a = "HELLO, WORLD"
print(a.lower())

# Função maiúscula
a = "hello, world"
print(a.upper())

# Função separar por delimitador
a = "Ana Maria;17;Feminino"
lista = a.split(";")
lista.append("Brasileira")
print(lista)

texto = "Bem vindo ao mundo dos programadores"
lista_palavras = texto.split(" ")
print(lista_palavras)

# Função contém retorna um valor lógico
texto = "Foi fácil fazer ficar fiado fico freguês"
x = "fiado" in  texto
print(x)

# Função Format(){}
qtd = 3
item = 567
preco = 49.95

ordem = "Eu quero pagar {} reais para {} quantidades do item {}.".format(preco, qtd, item)
print(ordem)
# ou
ordem = f"Eu quero pagar {preco} reais para {qtd} quantidades do item {item}."
print(ordem)

# função min e max
minimo = min()

# função abs()
a = abs(-125)

#função exponencial pow()
a = pow(4 ,3)

#Algumas funções precisam ser importadas

import math

x = math.ceil(1.4)
y = math.floor(1.4)

# Exemplo função Random
import random

for i in range(1, 13):
    numero = int(random.random() * 35) # multiplicar por 35 para gerar numeros inteiros de 0 até o numero multiplicado.
    # ou
    numero = int(random.randint(1, 12))  # multiplicar por 35 para gerar numeros inteiros de 0 até o numero multiplicado.
    print(numero)


