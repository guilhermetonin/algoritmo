nome = input("Nome do produto: ")
valor = float(input("Valor: "))
qtde = int(input("Quantidade: "))
metodo = int(input("1. A vista ou 2. A prazo: "))

total = valor * qtde
parcelas = 1
acrescimo = 0
desconto = 0
pagar = 0

if (metodo == 1):
  desconto = total * 0.10 # 10%

else:
  parcelas = int(input("Número de parcelas: "))

  if (parcelas <= 5):
    acrescimo = total * 0.15 # 15%
  else:
    acrescimo = total * 0.20 # 20%

pagar = total + acrescimo - desconto
totalParcela = pagar / parcelas

print("\nTotal da compra:", total)

if (metodo == 1):
  print("Desconto: ", desconto)

else:
  print("Valor de cada parcela: ", totalParcela)
  print("Acréscimo: ", acrescimo)

print("Líquido a pagar: ", pagar)