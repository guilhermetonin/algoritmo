# condicionais

x = int(input("Digite um número: "))

# if
if (x > 0):
  print("positivo")
print("fim do prog1")

# 
a = int(input("Digite um número inteiro: "))
if (x % 2 == 0):
  print(f"O valor de A é {a} e é par")
print("fim do prog")

# if e else
nota = int(input("Digite a nota do aluno: "))
if (nota >= 30 and nota < 60):
  print("O aluno deverá fazer sub")

else: 
  print("O aluno não precisa fazer sub")
print("fim.")

# impar ou par
num = int(input("Digite um valor: "))

if (num % 2 == 0): 
  print(f"O valor {num} é par")

else:
  print(f"O valor {num} é ímpar")
print("fim")

# alinhamento de if
n = int(input("Digite um valor inteiro: "))
if (n == 0):
  print(f"O valor de {n} é igual a 0")
else:
  if (x > 0): 
    print(f"O valor de {n} é positivo")
  else:
    print(f"O valor de {n} é negativo")
print("fim")

# elif
n = int(input("Digite um valor inteiro: "))
if (n == 0):
  print(f"O valor de {n} é igual a 0")

elif (n > 0): # else if
  print(f"O valor de {n} é positivo")
  
else:
  print(f"O valor de {n} é negativo")
print("fim")