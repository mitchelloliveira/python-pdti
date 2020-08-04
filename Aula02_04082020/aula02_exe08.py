# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

preco1 = float(input("Informe o preço do produto1: "))
preco2 = float(input("Informe o preço do produto2: "))
preco3 = float(input("Informe o preço do produto3: "))

menor = 99999

if preco1 < menor:
    menor = preco1

if preco2 < menor:
    menor = preco2

if preco3 < menor:
    menor = preco3

print("Você deve comprar o produto com valor ", menor)