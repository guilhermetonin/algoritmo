lista = [5.5, 6.6, 7.7, 8.8, 9.9, 10.0]
soma = 0

# --- for ... in ... ---
# não precisa especificar o inicio ou fim
for numero in lista:
  soma += numero

print(f"Soma geral: {soma}")


# --- forma posicional ---
alunos = ["guilherme", "fabio", "julia"]

for n in alunos:
  print(n)

for n in range(len(alunos)):
  print(f"Posição {n} - {alunos[n]}")


# exemplo
alunos = ["A", "B", "C"]
len(alunos) # 3

# sequência de índices de 0 até 3
range(len(alunos)) # range(0, 3)

# converte para uma lista de índices
list(range(len(alunos))) # [0, 1, 2]
