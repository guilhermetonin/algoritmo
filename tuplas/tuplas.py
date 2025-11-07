# --- tuplas ---
# são imutáveis e usa parênteses ( ) para criar
aluno = ('Ricardo', 1.74, 33)

# permite acesso a elementos por posição.
print('acesso posicional da Tupla')
print(f'posição 0: {aluno[0]}') 
print(f'posição 1: {aluno[1]}')
print(f'posição 2: {aluno[2]}') 


# --- adição de tuplas ---
# o operador + concatena duas tuplas
sala1 = ('Maria', 18)
sala2 = ('Matheus', 14)
escola = sala1 + sala2
print(escola) # ('Maria', 18, 'Matheus', 14)


# --- criação e tipagem de tuplas ---
tupla_vazia = ()
print(type(tupla_vazia)) # tuple


# 1 elemento
nao_tupla = (1)
print(type(nao_tupla)) # int

# para criar uma tupla com um 1 elemento
tupla_sim = (1,)
print(type(tupla_sim)) # tuple

# --- porque utilizar? ---
# normalmente tem elementos de diferentes tipos
# guarda elementos que não podem ser alterados
# são mais rápidas de processar que listas