n = 5
notas = []

# preencher vetor
for i in range(1,n+1):
  x = int(input(f"Nota do aluno {i}: "))
  notas.append(x) # adiciona o elemento ao final do array

# calcular média
media = 0
for n1 in notas:
  media = media + n1
media = media / n

# verificar aprovados
for n1 in notas:
  if n1 > media:
    print(f"Aprovado: {n1}")
