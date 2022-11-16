num1 = float(input('Informe o primeiro numero'))
num2 = float(input('Informe o segundo numero'))
num3 = float(input('Informe o terceiro numero'))

maior = float()
menor = float()
if num1 > num2 and num1 > num3:
  maior = num1
  if num2 < num3:
    menor = num2
  else:
    menor = num3
  print(f"O maior número é {maior} e o menor é {menor}")

elif num2 > num1 and num2 > num3:
  maior = num2
  if num1 < num3:
    menor = num1
  else:
    menor = num3
  print(f"O maior número é {maior} e o menor é {menor}")

elif num3 > num2 and num3 > num1:
  maior = num3
  if num2 < num1:
    menor = num2
  else:
    menor = num1
  print(f"O maior número é {maior} e o menor é {menor}")
  
else:
  print("Os números são iguais!")