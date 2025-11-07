'''
Uma loja online oferece descontos especiais baseados em dois critérios:

Idade do cliente:
  Estudante: < 25 anos
  Sênior: ≥ 60 anos

Valor total da compra:
  Compras acima de R$ 200,00 têm desconto base de 10%
  Compras acima de R$ 500,00 têm desconto base de 15%
  Clientes estudantes ou sênior recebem desconto adicional

Descontos adicionais:
  Estudantes: +5% de desconto adicional
  Sênior: +7% de desconto adicional

Retorne:
  1. Solicite a idade do cliente e o valor total da compra
  2. Calcule o valor final com os descontos
  3. Informe:
    Valor do desconto base
    Valor do desconto adicional
    Valor final a ser pago
'''

# preenche os dados do cliente
def cadastroInicial():
  idade = int(input('Informe sua idade: '))
  valor = float(input('Informe o valor da compra: '))
  return (idade,valor)

# calcula o desconto base e o adicional
def calcularDescontos(idade,valor):
  valorInicial = valor
  descontoBase = 0 
  descontoAdicional = 0

  if valor > 500.00:
    descontoBase = 15
  elif valor > 200.00:
    descontoBase = 10
  if idade >= 60: # senior
    descontoAdicional = 7
  elif idade < 25: # estudante
    descontoAdicional = 5
  
  descontoBase = valorInicial * (descontoBase / 100)
  descontoAdicional = valorInicial * (descontoAdicional / 100)
  descontoTotal = descontoBase + descontoAdicional
  valorFinal = valorInicial - descontoTotal

  return descontoBase, descontoAdicional, valorFinal

# exibe todas as informações na tela
def exibirNaTela(idade,valorInicial,valorFinal,descontoBase,DescontoAdicional):
  print('\n~~~ RESUMO DA COMPRA ~~~\n')
  print(f'IDADE: {idade}')
  print(f'VALOR INICIAL: R$ {valorInicial:.2f}')
  print(f'DESCONTO BASE: -R$ {descontoBase:.2f}')
  print(f'DESCONTO ADICIONAL: -R$ {descontoAdicional:.2f}')
  print(f'VALOR FINAL A PAGAR: R$ {valorFinal:.2f}')

# execução
idade, valor = cadastroInicial()
descontoBase, descontoAdicional, valorFinal = calcularDescontos(idade,valor)
exibirNaTela(idade,valor,valorFinal,descontoBase,descontoAdicional)