# permite diferentes tipos de elementos
compras = ["miojo", "carne", "ovo", "arroz", 12.2]
print(compras)

# --- atribuição ---
# índice começa no 0
compras[0] = 99.9
print(compras[0])


# --- adição ---
# adiciona um elemento ao fim da lista
n = [5, 10, 15]
n.append(20)
print(n)


# --- gera uma lista ---
# começando em 0
x = list(range(5))
print(f"x = {x}")

# --- unpacking ---
x = [5, 7, 8]
[a, b, c] = x
print(f"a={a} b={b} c={c}")

# matrizes aninhadas
matriz = [[1, 2], [3, 4]]
matriz[0][1] = "oi"
print(matriz)