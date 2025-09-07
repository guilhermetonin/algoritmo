x = 10 + 5

print(type(x)) # tipo da variavel
print("x vale:", x) # console.log

y = 33.33

print(type(y))

a = "facef"
print(type(a))

idade = 18
altura = 1.75

print("A altura é", altura, "e a idade é", idade)
print(f"A altura é {altura} e a idade é {idade}")


# input
nome = input("digite seu nome: ") #prompt
print(f"seu nome é {nome}")


# input de um 'número'
numero = input("Digite um número: ")
print(f"O número é {numero}")
print(type(numero)) # string


# arrendondando numero
t = 7 / 3
print(f"Número arrendondado é {round(t, 2)}")
print(f"Número original é {t}")


# inteiro no input
n = int(input("Digite um valor inteiro: "))
n = n * 2
print(f"O valor dobrado de n é: {n}")

"""
documentacao
"""

import math # importar um modulo

print(math.e)

print(math.pi)

print(math.sqrt(4)) # raíz quadrada

print(dir(math)) # mostra as funcionalidades de um modulo