# --- tradicional ---
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sublista = [] 

for n in numeros:
  if n < 7:
    sublista.append(n)
print(sublista) # [1, 2, 3, 4, 5, 6]

# --- maneira compacta ---
# o primeiro 'n' é o elemento que será inserido na lista
# ele é o resultado, como se fosse o .append(n)

# 'for n in numeros' percorre a lista original
# ele define a variável temporária 'n' a cada interação

# 'if n < 4' é a condição
lista = [n for n in numeros if n < 4] 
print(lista) # [1, 2, 3]