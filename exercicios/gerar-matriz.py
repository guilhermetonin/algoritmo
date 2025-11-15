'''
1. gere uma matriz de 5x5 e calcule na função:
  a) soma escalar dos elementos
  b) função que multiplica por *3 os valores pares da matriz
  c) funcao que recebe maior valor da matriz
'''
def somar(matriz):
  soma = 0
  for l in matriz:
    for n in l:
      soma += n
  return soma

def multiplicar(matriz):
  for l in range(len(matriz)):
    for c in range(len(matriz[l])):
      if matriz[l][c] % 2 == 0:
        matriz[l][c] = matriz[l][c] * 3

def maiorValor(matriz):
  maior = 0
  for l in matriz:
    for n in l:
      if n > maior:
        maior = n
  return maior

matriz = [[2,3,4],
          [5,6,7],
          [8,9,10]
]

total = somar(matriz)
print(f'Soma Total: {total}')
multiplicar(matriz)
numeroMaior = maiorValor(matriz)
print(f'Número maior: {numeroMaior}')