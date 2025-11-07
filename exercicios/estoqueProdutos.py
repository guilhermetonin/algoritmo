qtdes = []
valores = []

# preenche o vetor
for i in range(3):
  v = float(input(f'Valor do produto {i+1}: R$ '))
  valores.append(v)

  q = int(input(f'Quantidade do produto {i+1}: '))
  qtdes.append(q)

# calcula os totais
totais = []
for i in range(3):
  totais.append(qtdes[i] * valores[i])
  print(f'Valor: R$ {valores[i]} | Qtde: {qtdes[i]} | Total: R$ {totais[i]}')

# quantidade do produto com maior valor
maiorQtde = 0
maiorValor = valores[0]
for i in range(len(qtdes)):
  if (valores[i] > maiorValor):
    maiorQtde = qtdes[i]
    maiorValor = valores[i]

print(f'Qtde do produto com maior valor: {maiorQtde}')

# soma geral de todos os produtos
totalGeral = 0
for i in range(len(qtdes)):
  totalGeral += (qtdes[i] * valores[i])

print(f'Soma Geral: R$ {totalGeral}')