'''
CDB 14,5% AA
LCA 11,5% AA
P. 6% AA
prazos fixos, com 5 ou 10 ou 20 anos
calcular a rentabilidade ano a ano e total
cbd tem imposto de renda sobre o rendimento de 15%
'''

prazo = 5
capital = 1000
taxa = 14.5
rendimentos = []

for i in range(5):
  rendimento = capital * (taxa / 100)
  capital = capital + rendimento

  rendimentos.append({'ano': i+1,
                     'rendimento': rendimento,
                     'total': capital,
                     'rendimento_liquido': rendimento * 0.85})
  
print(rendimentos)