# --- criação ---
# permite diferentes tipos de elementos
compras = ['miojo', 'carne', 'ovo', 'arroz', 12.2]
print(compras)

# listas podem ser alteradas e seu índice começa em 0
compras[0] = 99.9


# --- append() ---
#  adiciona um novo elemento no final da lista
numeros = [5, 10, 15]
numeros.append(20)
print(numeros) # [5, 10, 15, 20]


# --- range() ---
# gera um objeto range
obj_range = range(5) # range(0, 5)

# --- list() ---
# converte essa sequência para uma lista
lista_range = list(obj_range) # [0, 1, 2, 3, 4]


# --- unpacking ---
# desempacota os elementos da lista em variáveis individuais
x = [5, 7, 8]
[a, b, c] = x 
print(f'a={a} b={b} c={c}')


# --- matrizes ---
# uma lista que contém outras listas
matriz = [[1, 2], [3, 4]]

# acessa a primeira lista 
print(matriz[0]) # [1, 2]

# na lista [0] acessa o elemento do índice [1]
matriz[0][1] = 'modificado'
print(matriz) # [[1, 'modificado'], [3, 4]]