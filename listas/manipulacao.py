# --- tamanho da lista ---
lista = [1, 2, 3]
print(f"lista: {lista} | tamanho: {len(lista)}")


# --- concatenação ---
a = [1, 2, 3]
b = [4, 5, 6]
concatenada = a + b
print(concatenada)


# --- multiplica a lista ---
lista_m = concatenada * 2
print(lista_m)


# --- remoção de elementos ---
lista = [1, 2, 3]
del lista[2] # pelo índice
print(lista)


# --- referência ---
a = [1, 3, 5]

# aponta para a mesma referência [ a = b ]
b = a[:] # faz uma cópia
a.append(10)

print(f"a: {a} | b: {b}")