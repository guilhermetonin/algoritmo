''''
Moda em um vetor é o número que é repetido com maior frequência
Se tiver mais de um número com frequência máxima igual, não terá uma moda

Faça um programa que:
  1. Leia números positivos (validar a entrada de dados) 
  2. Imprima a moda do vetor ou uma mensagem que a moda não existe
  3. Crie uma função para a moda
'''

# --- encontra a moda ---
def calcularModa(vetor):
  # dicionário com a contagem de cada número
  frequencias = {}

  for numero in vetor:
    # já tem
    if numero in frequencias:
      frequencias[numero] += 1
    else:
      # começa com 1
      frequencias[numero] = 1

  # maior frequência
  frequenciaMaxima = 0
  
  # --- encontra o valor da frequência máxima ---
  for numero in frequencias:
    # 'freq' é o valor da frequência que apareceu
    freq = frequencias[numero]

    if freq > frequenciaMaxima:
      frequenciaMaxima = freq
      
  # --- nenhum se repete ---
  if frequenciaMaxima == 1:
    return 'Não existe, todos são únicos.'


  # números que tem a frequência máxima do vetor
  modas = []
  
  # --- encontrar a moda ---
  for numero in frequencias:
    freq = frequencias[numero]
    
    if freq == frequenciaMaxima:
      # adiciona se a sua frequência for igual a máxima
      modas.append(numero)
      
  # existe
  if len(modas) == 1:
    return modas[0]
  
  # não existe
  else:
    return 'Não existe, aconteceu um empate.'


# --- adiciona números ao vetor ---
def adicionarNumeros():
  while True:
      try:
        numero = float(input('\n| Digite um número positivo: '))
        if numero <= 0:
          print('\n* ERRO. Número deve ser positivo.')
        else:
          vetor.append(numero)
          break
      except ValueError:
        print('\n* ERRO. Número digitado incorretamente.')


vetor = []
encerrador = 1 # valor padrão

# --- opções do programa ---
while(encerrador == 1):
  print('\n--- OPÇÕES ---')
  print('0. Parar execução')
  print('1. Adicionar números')
  print('2. Mostrar vetor atual')
  print('3. Encontrar a moda')
  opcao = int(input('Opção escolhida: '))

  if opcao == 0:
    encerrador = 0
  elif opcao == 1:
    adicionarNumeros()
  elif opcao == 2:
    print(f'\n| VETOR: {vetor}')
  elif opcao == 3:
    print(f'\n| MODA: {calcularModa(vetor)}')
    encerrador = 0
  else:
    print('\n* ERRO. Opção incorreta.')
    break