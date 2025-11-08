lista = [9.5, 7.4, 8.9, 10]
pesos = [2, 1, 4, 2]

def calcularMediaAritmetica(lista):
  # sum() soma todos os elementos da lista
  # len() qtde de elementos na lista
  return sum(lista) / len(lista)

def calcularMediaPonderada(numero, peso):
  totalNumeros = 0
  totalPesos = 0
  for i in range(len(lista)):
    totalNumeros += numero[i] * peso[i]
    totalPesos += peso[i]
  mediaPonderada = totalNumeros / totalPesos
  return mediaPonderada

def calcularRazao(mediaAritmetica, mediaPonderada):
  return mediaAritmetica / mediaPonderada

mediaAritmetica = calcularMediaAritmetica(lista)
mediaPonderada = calcularMediaPonderada(lista,pesos)
razao = calcularRazao(mediaAritmetica, mediaPonderada)

print(f'Média aritmética: {mediaAritmetica}')
print(f'Média ponderada: {mediaPonderada}')
print(f'Razão entre as médias: {razao}')