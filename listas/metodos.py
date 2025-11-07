lista = [10, 20, 30, 40, 50]

# --- if ... in ... ---
# verifica se um valor está presente na lista
if 30 in lista:
    print('encontrado.') 
else:
    print('não encontrado ')


# --- reverse() ---
# modifica a lista invertendo ela
lista.reverse()
print(lista) # [50, 40, 30, 20, 10]


# --- sort() ---
# ordena a lista em ordem crescente
lista.sort() 
print(lista) # [10, 20, 30, 40, 50]


# --- remove() ---
# busca o primeiro valor correspondente e o remove
nome = ['guilherme', 'tonin', 'teste']

nome.remove('teste')
print(nome) # ['guilherme', 'tonin']