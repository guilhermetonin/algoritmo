# --- criação de funções (def) ---

def imprimirCompras():
  # 'compras' é uma variável local, só existe dentro desta função
  compras = ['Miojo', 'Ovo', 'Leite', 'Pão']
  print(f'lista de compras: {compras}')

  for item in compras:
    print(f'produto: {item}')
# fim da função

print('antes da função')
imprimirCompras() # chama a função

print('depois da função')
imprimirCompras()


# --- parâmetros ---
# parâmetro 'juros' tem um valor padrão de 0.25
def reajuste(salario,juros=0.25):

  # 'return' retorna o resultado
  return salario + salario * juros

# usa o valor padrão para juros
print(f'reajuste 1: {reajuste(1518)}')

# valor 0.10 substitui o valor padrão
print(f'reajuste 2: {reajuste(1518, 0.10)}')


# --- return ---
def maior(x, y):
  if x > y:
    return x
  else:
    return y
    # 'return' encerra imediatamente a função.
    print('não será impressa.') 


x = int(input('valor de x: '))
y = int(input('valor de y: '))

maiorValor = maior(x, y)
print(f'maior valor: {maiorValor}')


# --- variável global e local ---
nome = 'gui'
def valor():
  # pode acessar a variável global
  print(f'nome: {nome}')
  
  # 'sobrenome' é uma variável local
  sobrenome = 'junior'
  # desaparece ao fim da função