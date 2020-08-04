nota1 = float(input("Informe a prmeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1+nota2)/2

aprovado_distinicao = media == 10
reprovado = media < 7
if reprovado:
    print("Reprovado")
elif aprovado_distinicao:
    print("Aprovado com distinção")
else:
    print("Aprovado")