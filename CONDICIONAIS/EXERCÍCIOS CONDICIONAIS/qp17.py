num1 = float(input('Informe o primeiro numero'))
num2 = float(input('Informe o segundo numero'))
num3 = float(input('Informe o terceiro numero'))

if num1 > num2 and num1 > num3:
  print(f"O maior número é {num1}")
elif num2 > num1 and num2 > num3:
  print(f"O maior número é {num2}")
elif num3 > num1 and num3 > num2:
  print(f"O maior número é {num3}")
else:
  print("Os números são iguais!")