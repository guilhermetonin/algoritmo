# --- chave ---
# chave (ex: 'nome') é o identificador
# valor (ex: 'Guilherme') é o conteúdo
dicionario = {'nome': 'Guilherme', 'codigo': '25941', 'curso': 'S.I'}
print(dicionario) # exibe o dicionário inteiro


# --- pop() ---
# remove um item pela chave e retorna o valor removido
# sem especificar ele remove e retorna o último elemento
nome = dicionario.pop('nome')
print(f'valor removido: `{nome}`') # Guilherme
print(f'após pop: {dicionario}') # sem a chave 'nome'


# --- popitem() ---
# remove e retorna o último chave-valor inserido no dicionário
removido = dicionario.popitem()
print(f'chave, valor removido: {removido}')
print(f'após popitem: {dicionario}')


# --- dicionário ---
carro = {'Marca': 'Volkswagen',
         'Motor': 1.0,
         'País': 'Alemanha'}
print(carro)

# acesso direto a um valor
print(carro['País'])

# --- adiciona chave e valor ao dicionário ---
carro['Estado'] = 'Novo'
print(f'adição: {carro}')


# --- métodos de manipulação ---
aluno = {'nome': 'Ana', 'Idade': '28'}


# --- clear() ---
# remove todos os elementos, deixando vázio ---
aluno.clear()
print(aluno) # []


# --- referência simples ---
# aponta para o mesmo objeto na memória que 'aluno' 
# não é uma cópia
aluno_2 = aluno
print(aluno_2)

# adiciona uma chave e valor
aluno_2['Curso'] = 'Sistemas'
print(f'aluno original: {aluno}') # foi modificado
print(f'aluno2: {aluno_2}') # mesmo contéudo

# --- copy() ---
# cria uma cópia real
copia = aluno.copy()
print(f'cópia: {copia}')


# --- get() ---
# retorna o valor de um chave ou valor padrão
a = copia.get('Curso')
print(f'get(): {a}')


# --- keys() ---
print(copia.keys()) # exibe as chaves


# --- values() ---
print(copia.values()) # exibe os valores das chaves