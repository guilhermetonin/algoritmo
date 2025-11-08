def calcular(a,b,operacao):
  resultado = 0
  if operacao == 1:
    resultado = a + b
    print(f'{a} + {b} = {resultado}')
  elif operacao == 2:
    resultado = a - b
    print(f'{a} - {b} = {resultado}')
  elif operacao == 3:
    resultado = a * b
    print(f'{a} * {b} = {resultado}')
  elif operacao == 4:
    resultado = a / b
    print(f'{a} / {b} = {resultado}')
  else:
    print('Operação inválida, digite a opção corretamente.')

print('Informe a operação desejada:')
print('1. Somar \t 3. Subtrair')
print('3. Multiplicar \t 4. Dividir')

operacao = int(input('Digite: '))
a = float(input('Número A: '))
b = float(input('Número B: '))

calcular(a,b,operacao)




