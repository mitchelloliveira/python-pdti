# Curso de Python - PDTI-SENAC/RN
# Profº Weskley Bezerra
# Mitchell Oliveira
# 10/08/2020
# --------------------------------------------------------------
# Exemplo de Função

def minha_funcao():
    print("Olá, eu sou uma função.")

minha_funcao()

# -----------------------------------------
def bem_vindo(nome):
    print("Bem vindo", nome)

bem_vindo("Mitchell")

# -----------------------------------------
def nome_completo(primeiro, ultimo):
    print(primeiro, ultimo)

nome_completo("Mitchell", "Oliveira")

# -----------------------------------------
# Argumentos arbitrários -> são argumentos
# que não se sabe a quantidade

def nomes(*nome):
    print(nome) # Nesse caso o resultado seria uma túpla e não pode ser modificado
    lista = list(nome) # Converteu para lista
    print(lista)

nomes("Ana", "Joana", "Maria", "Carla")

# -----------------------------------------
# Função com valor padrão
def pais(pais = 'Brasil'):
    print("Eu vivo no", pais)

pais()

# -----------------------------------------
# Função com retorno
def somar(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero

    return resultado

teste = somar(2,2,2,2,2)

print("A soma é", teste)

# -----------------------------------------
# Função de filtro em uma lista
nomes = ["jose", "pedro", "joão", "maria", "sara", "lucas"]

def minha_funcao(caractere, lista):
    result_lista = []
    for item in lista:
        if item.startswith(caractere):
            result_lista.append(item)

    return result_lista

filtro = minha_funcao("j", nomes)

print(filtro)

# -----------------------------------------
# Criar um algoritmo que informe se um
# número é primo ou não.

def e_primo(numero):
    limite = numero+1
    contador = 0
    for i in range(1,limite):
        if numero % i == 0:
            contador += 1
        if contador > 2:
            break
    return contador == 2

# testando a função e_primo
numero = int(input("Informe um número: "))

if e_primo(numero):
    print("É primo!")
else:
    print("Não é primo!")
