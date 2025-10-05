# --- tipos de dados ---
x = 10 + 5 
print(type(x)) # <class 'int'>
print("x vale:", x) 

y = 33.33
print(type(y)) # <class 'float'>

a = "facef"
print(type(a)) # <class 'str'>


# --- exibir ---
idade = 18
altura = 1.75

# tradicional
print("A altura é", altura, "e a idade é", idade) 

# f-string
print(f"A altura é {altura} e a idade é {idade}") 


# --- entrada de dados ---
nome = input("digite seu nome: ") # input retorna uma string
print(f"seu nome é {nome}") 

# exemplo de um 'número'
numero = input("Digite um número: ")
print(f"O número é {numero}")
print(type(numero)) # <class 'str'>

# --- converter o tipo ---

n = int(input("Digite um valor inteiro: ")) # converte para inteiro

k = float(input("Digite um valor decimal: ")) # converte para reais


# --- arrendondar número ---
t = 7 / 3

print(f"Número arredondado é {round(t, 2)}") # com 2 casas decimais
print(f"Número original é {t}")


# --- módulo de matemática ---
import math

print(math.e) # const euler
print(math.pi) # const pi

print(math.sqrt(4)) # raiz quadrada

# lista as funções
print(dir(math))