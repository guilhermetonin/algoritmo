

def contarVogais(texto):
  vogais = 'aeiou'
  cont = 0

  for c in texto:
    if c in vogais:
        cont = cont + 1
  return cont      

texto = input('Informe um texto: ')
print(contarVogais(texto))