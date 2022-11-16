num1 = float(input('Informe o primeiro numero'))
num2 = float(input('Informe o segundo numero'))

if num1 > num2:
  print(f"O maior número é {num1}")
elif num2 > num1:
  print(f"O maior número é {num2}")
else:
  print("Os números são iguais!")