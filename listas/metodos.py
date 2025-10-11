# --- busca de elementos ---
lista = [10, 20, 30, 40, 50]

if 30 in lista:
  print("Encontrado.")
else:
  print("Não encontrado :(")


# --- inverte ---
lista = [1, 2, 3, 5, 4]
lista.reverse()
print(lista)


# --- ordena crescente ---
lista.sort() 
print(lista)


# --- remove um elemento específico ---
nome = ["guilherme", "tonin", "teste"]
nome.remove("teste")
print(nome)


# --- remove e retorna ---
# último elemento
nomes = ["carlos", "miguel", "gaules", "fabio"]

ultimo = nomes.pop()

print(nomes) # ["carlos", "miguel", "gaules"]
print(ultimo) # "fabio"


# primeiro elemento
nomes = ["raphael", "vitor", "flaco"]

primeiro = nomes.pop(0) # índice 0

print(nomes) # ["vitor", "flaco"]
print(primeiro) # "raphael"

