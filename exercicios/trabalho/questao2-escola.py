'''
Uma escola precisa de um sistema para cadastrar notas dos alunos e gerar relatórios estatísticos.

1. Cadastrar múltiplos alunos (nome e nota)
2. Calcular estatísticas das notas
3. Permitir que o usuário cadastre quantos alunos desejar
4. Validar notas (apenas entre 0 e 10)
5. Gerar relatório final

Faça um programa que:
  1. Use um loop para cadastrar alunos até que o usuário decida parar
  2. Para cada aluno, solicite nome e nota (validando a entrada)
  3. Ao final, exiba:
    Quantidade de alunos cadastrados
    Média geral das notas
    Maior e menor nota
    Porcentagem de alunos aprovados (nota ≥ 7)
    Lista de alunos com suas situações (Aprovado/Reprovado)
'''

# --- registra um um novo aluno ---
def cadastrarAlunos(alunos):
  while True:
    try: 
      nome = input('Nome do aluno: ').strip() # remove espaços
      if nome:
        break
      else:
        print('ERRO. Nome incorreto.')
    except ValueError:
      print('ERRO. Tente novamente.')

  while True:
    try:
      nota = float(input(f'Nota do {nome}: '))
      if 0 <= nota <= 10:
        break
      else:
        print('ERRO. Nota incorreta.')
    except ValueError:
      print('ERRO. Tente novamente.')

  aluno = {
    'Nome': nome,
    'Nota': nota
  }
  alunos.append(aluno)
  return (alunos)


# --- calcula a média geral dos alunos cadastrados ---
def calcularMediaGeral(alunos):
  media = 0
  for i in range(len(alunos)):
    media += alunos[i]['Nota']
  return media / len(alunos)
  

# --- encontra a menor e maior nota entre os alunos ---
def calcularMaiorMenor(alunos):
  # maior nota
  maiorNota = alunos[1]['Nota'] 
  nomeMaior = alunos[1]['Nota']

  # menor nota
  menorNota = alunos[1]['Nota']
  nomeMenor = alunos[1]['Nota']

  for i in range(len(alunos)):
    
    if alunos[i]['Nota'] > maiorNota:
      nomeMaior = alunos[i]['Nome']
      maiorNota = alunos[i]['Nota']
    
    if menorNota > alunos[i]['Nota']:
      nomeMenor = alunos[i]['Nome']
      menorNota = alunos[i]['Nota']

  # exibe as informações na tela
  print('\n--- MAIOR e MENOR NOTA ---')
  print(f'| MAIOR NOTA: {maiorNota} \t| ALUNO: {nomeMaior}')
  print(f'| MENOR NOTA: {menorNota} \t| ALUNO: {nomeMenor}')


# --- calcula a taxa de aprovação ---
def porcentagemAprovados(alunos):
  qtdeAlunos = 0 # quantidade de alunos aprovados

  for i in range(len(alunos)):
    if alunos[i]['Nota'] >= 7:
      qtdeAlunos += 1
    
  # exibe as informações na tela
  qtdeAlunos = (qtdeAlunos * 100) / len(alunos)
  print(f'| PORCENTAGEM APROVAÇÃO: {qtdeAlunos:.2f}%')


# --- verifica a situação de cada aluno ---
def relatorioEscolar(alunos):
  aprovados = []
  reprovados = []

  for i in range(len(alunos)):
    if alunos[i]['Nota'] >= 7:
      aprovados.append(alunos[i])
    else: 
      reprovados.append(alunos[i])
  
  # exibe as informações na tela
  print('\n--- ALUNOS APROVADOS ---')
  for i in range(len(aprovados)):
    print(f'| Nota: {aprovados[i]['Nota']} \t| Nome: {aprovados[i]['Nome']}')

  # exibe a taxa de aprovação
  porcentagemAprovados(alunos)

  print('\n--- ALUNOS REPROVADOS ---')
  for i in range(len(reprovados)):
    print(f'| Nota: {reprovados[i]['Nota']} \t| Nome: {reprovados[i]['Nome']}')


# --- mostra todas as informações dos alunos ---
def mostrarInformacoes():
  print('\n\n--- RELATÓRIO DA ESCOLA ---')
  print(f'| QUANTIDADE DE ALUNOS: {len(alunos)}')

  calcularMediaGeral(alunos)
  calcularMaiorMenor(alunos)
  relatorioEscolar(alunos)


# --- ínicio do programa ---
encerrarPrograma = 0 # valor padrão
alunos = [
    {'Nome': 'João', 'Nota': 9.5},
    {'Nome': 'Maria', 'Nota': 7.0},
    {'Nome': 'Pedro', 'Nota': 5.5},
    {'Nome': 'Ana', 'Nota': 8.2},
    {'Nome': 'Lucas', 'Nota': 6.8},
    {'Nome': 'Sofia', 'Nota': 4.2},
    {'Nome': 'Guilherme', 'Nota': 10}
]

# funcionalidades do programa
while (encerrarPrograma == 0):
  print('\n--- ESCOLHA UMA OPÇÃO ABAIXO ---')

  print('0 - Encerrar programa.')
  print('1 - Cadastrar novo aluno')
  print('2 - Gerar relatório final')
  escolha = int(input('Digite o número: '))

  # verificação do número escolhido
  if (escolha == 0):
    print('Encerrando programa...')
    encerrarPrograma = 1
  elif (escolha == 1):
    cadastrarAlunos(alunos)
  elif (escolha == 2):
    mostrarInformacoes()
  else: 
    print('ERRO. Número escolhido incorreto.')