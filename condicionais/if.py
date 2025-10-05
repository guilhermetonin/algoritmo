# IF - ELSE

# impar ou par
num = int(input("Digite um valor: "))

if (num % 2 == 0): 
  print(f"O valor {num} é par")

else:
  print(f"O valor {num} é ímpar")

print("fim")


# alinhamento
n = int(input("Digite um valor inteiro: "))

if (n == 0):
  print(f"O valor de {n} é igual a 0")
else:
  if (n > 0): 
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

# 