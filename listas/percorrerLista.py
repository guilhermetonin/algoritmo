lista = [5.5, 6.6, 7.7, 8.8, 9.9, 10.0]
soma = 0

# --- for ... in ... ---
# acessa diretamente cada elemento da lista a cada iteração
for numero in lista:
  soma += numero
print(f'soma geral: {soma}')


# --- forma posicional ---
alunos = ['guilherme', 'fabio', 'julia']
for n in alunos:
  print(n) # imprime o nome de cada aluno


# --- len(alunos) --- 
# retorna o tamanho da lista
letras = ['A', 'B', 'C']
len(letras) # 3

# --- range(len(alunos)) ---
# gera uma sequência de índices de 0 até 3 (excluso).
range(len(alunos)) # cria um range(0, 3)

# exemplo no for
for n in range(len(alunos)):
  print(f'índice: {n} | valor: {alunos[n]}')


# converte o range para uma lista
list(range(len(alunos))) # [0, 1, 2].